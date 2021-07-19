from rest_framework_nested import routers
from django.urls import include
from django.urls import path

from .viewsets import UserViewSet
from .viewsets import OrgViewSet
from .viewsets import OrgUsersViewSet
from .viewsets import IPInfoViewSet
from .viewsets import UserGroupViewSet


router = routers.SimpleRouter()

router.register("users", UserViewSet)
router.register("organizations", OrgViewSet)

orgs_router = routers.NestedSimpleRouter(router, r'organizations', lookup='organization')
orgs_router.register(r'users', OrgUsersViewSet, basename='org-users')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(orgs_router.urls)),
    path("auth/groups/", UserGroupViewSet.as_view({"get": "list"})),
    path("info/", IPInfoViewSet.as_view({"get": "retrieve"}))
]