from rest_framework import serializers
from .models import Project, ProjectMember, ProjectMemberInvite


class ProjectMemberInviteSerializers:
    class ProjectMemberInviteRetrieveSerializer(serializers.ModelSerializer):
        class Meta:
            model = ProjectMemberInvite
            fields = [
                # "project",
                "email",
                "invite_by",
                "created_at",
                "updated_at",
            ]


class ProjectMemberSerializer:
    class ProjectMemberRetrieveSerializer(serializers.ModelSerializer):
        class Meta:
            model = ProjectMember
            fields = [
                'project',
                'member',
                'role',
                'joined_at',
            ]


class ProjectSerializers:

    class ProjectCreateSerializer(serializers.ModelSerializer):
        class Meta:
            model = Project
            fields = [
                'name', 
                'description',
                'project_lead'
            ]

    class ProjectUpdateSerializer(serializers.ModelSerializer):
        class Meta:
            model = Project
            fields = [
                'name', 
                'description','project_lead'
            ]

    class ProjectDetailSerializer(serializers.ModelSerializer):
        members = serializers.SerializerMethodField()

        class Meta:
            model = Project
            fields = [
                'name',
                'description',
                'created_at',
                'updated_at',
                'project_lead',
                'members'
            ]
        def get_members(self, obj):
            members = obj.members.all()
            return ProjectMemberSerializer.ProjectMemberRetrieveSerializer(members, many=True).data

    class InviteMemberSerializer(serializers.ModelSerializer):
        class Meta:
            model = ProjectMemberInvite
            fields = [
                'email',
            ]
