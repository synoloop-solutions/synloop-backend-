from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProjectViewset


router = DefaultRouter()

router.register("projects", ProjectViewset, basename="projects")

urlpatterns = router.urls