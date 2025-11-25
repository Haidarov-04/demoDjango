from django.urls import path, include
from rest_framework import routers
from .views import StudentsViewSet  # точка важна!

router = routers.DefaultRouter()
router.register(r'Students', StudentsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]