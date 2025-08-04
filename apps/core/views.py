from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Project, Task
from .serializers import (
    ProjectSerializers, 
    ProjectMemberSerializer, 
    ProjectMemberInviteSerializers, 
    TaskSerializers
)


class ProjectViewset(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing project instances.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializers.ProjectDetailSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def create(self, request, *args, **kwargs):
        serialized_data = ProjectSerializers.ProjectCreateSerializer(data=request.data)
        serialized_data.is_valid(raise_exception=True)

        data = serialized_data.save()

        response_data = ProjectSerializers.ProjectDetailSerializer(data)
        return Response(data=response_data)
    

class TaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers.TaskRetrieveSerializer()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serialized_data = TaskSerializers.TaskCreateSerializer(data=request.data)
        serialized_data.is_valid(raise_exception=True)

        data = serialized_data.save()
        response_data = TaskSerializers.TaskRetrieveSerializer(data)
        return Response(data=response_data)
    
