from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="userinfo.name")
    phone = serializers.CharField(source="userinfo.phone")
    birthdate = serializers.DateField(source="userinfo.birthdate")
    organization = serializers.IntegerField(source="userinfo.organization.pk")

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'phone', 'birthdate', 'organization']