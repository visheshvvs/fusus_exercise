from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.filters import SearchFilter
from django_filters import rest_framework as filters

from .serializers import UserSerializer
from .filters import PhoneFilter


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = PhoneFilter
    search_fields = ["=id", "userinfo__name", "email"]