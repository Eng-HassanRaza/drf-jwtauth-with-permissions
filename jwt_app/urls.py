from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet
from django.urls import include, path
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    path('auth/', include('rest_auth.urls')),
]