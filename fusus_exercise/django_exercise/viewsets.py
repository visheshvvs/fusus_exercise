from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Organization
from .filters import PhoneFilter
from .serializers import OrgSerializer, MinUserSerializer, UserSerializer, UserInfoSerializer



class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = User.objects.select_related("userinfo__organization")
    serializer_class = UserSerializer
    filterset_class = PhoneFilter
    search_fields = ["=id", "userinfo__name", "email"]

    def get_queryset(self):
        return super().get_queryset().filter(userinfo__organization=self.request.user.userinfo.organization)


class OrgViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser, ]
    queryset = Organization.objects.all()
    serializer_class = OrgSerializer


class OrgUsersViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser, ]
    serializer_class = MinUserSerializer

    def get_queryset(self):
        return User.objects.filter(userinfo__organization_id=self.kwargs["organization_pk"]).select_related("userinfo")


class IPInfoViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = UserInfoSerializer
    queryset = User.objects.select_related("userinfo__organization")

    def get_object(self):
        return self.request.user
