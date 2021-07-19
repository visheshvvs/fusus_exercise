from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated

from .models import Organization
from .filters import PhoneFilter
from .serializers import OrgSerializer, MinUserSerializer, UserSerializer, UserInfoSerializer, GroupSerializer


class UserGroupViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.select_related("userinfo__organization")
    serializer_class = UserSerializer
    filterset_class = PhoneFilter
    search_fields = ["=id", "userinfo__name", "email"]

    def get_queryset(self):
        return super().get_queryset().filter(userinfo__organization=self.request.user.userinfo.organization)

class OrgViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Organization.objects.all()
    serializer_class = OrgSerializer

    def get_queryset(self):
        return super().get_queryset().filter(pk=self.request.user.userinfo.organization.pk)


class OrgUsersViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = MinUserSerializer

    def get_queryset(self):
        current_user = self.request.user
        current_user_org = current_user.userinfo.organization
        return User.objects.filter(userinfo__organization=current_user_org).select_related("userinfo")


class IPInfoViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserInfoSerializer
    queryset = User.objects.select_related("userinfo__organization")

    def get_object(self):
        return self.request.user
