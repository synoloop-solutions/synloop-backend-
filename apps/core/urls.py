from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProjectViewset, TaskViewset


router = DefaultRouter()

router.register("projects", ProjectViewset, basename="projects")
router.register("tasks", TaskViewset, basename="tasks")

urlpatterns = router.urls