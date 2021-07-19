from django.contrib.auth.models import User
from rest_framework import serializers
import socket

from .models import UserInfo
from .models import Organization


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="userinfo.name")
    phone = serializers.CharField(source="userinfo.phone")
    birthdate = serializers.DateField(source="userinfo.birthdate")
    organization_id = serializers.IntegerField(source="userinfo.organization.pk", read_only=True)
    organization_name = serializers.CharField(source="userinfo.organization.name", read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'email', 'phone', 'birthdate', 'organization_id', 'organization_name']


    def create(self, validated_data):
        current_user = getattr(self.context.get("request"), "user")
        user = User.objects.create_user(username=validated_data.get("username"), password=validated_data.get("password"), email=validated_data.get("email"))
        UserInfo.objects.create(user=user, organization=current_user.userinfo.organization, name=validated_data.get("name"), phone=validated_data.get("phone"), birthdate=validated_data.get("birthdate"))

        return user


class MinUserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="userinfo.name", read_only=True)

    class Meta:
        model = User
        fields = ['id', 'name']


class UserInfoSerializer(serializers.ModelSerializer):
    organization_name = serializers.CharField(source="userinfo.organization.name", read_only=True)
    public_ip = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', 'organization_name', 'public_ip']

    def get_public_ip(self, obj):
        return socket.gethostbyname(socket.gethostname())


class OrgSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Organization
        fields = ['id', 'address', 'name', 'phone']
