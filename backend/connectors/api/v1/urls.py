from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors134522ViewSet

router = DefaultRouter()
router.register(
    "testconnectors134522", Testconnectors134522ViewSet, basename="testconnectors134522"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
