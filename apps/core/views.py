from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Project
from .serializers import ProjectSerializers, ProjectMemberSerializer, ProjectMemberInviteSerializers


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
        return Response(data=data)