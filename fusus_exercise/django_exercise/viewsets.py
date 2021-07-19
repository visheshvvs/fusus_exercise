from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from .filters import PhoneFilter
from rest_framework.permissions import IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated,]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_class = PhoneFilter
    search_fields = ["=id", "userinfo__name", "email"]

