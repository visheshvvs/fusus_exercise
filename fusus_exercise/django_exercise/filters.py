import django_filters as filters
from django.contrib.auth.models import User


class PhoneFilter(filters.FilterSet):
    phone = filters.CharFilter(field_name="userinfo__phone", lookup_expr="icontains")

    class Meta:
        model = User
        fields = ["phone"]
