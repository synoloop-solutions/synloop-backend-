from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    project_lead = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="project_lead",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ['-created_at']


class ProjectMemberInvite(models.Model):
    project = models.ForeignKey(Project, related_name='invites', on_delete=models.CASCADE)
    email = models.EmailField()
    invited_by = models.ForeignKey(User, related_name='project_invites', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"Invite to {self.project.name} for {self.email}"

    class Meta:
        verbose_name = "Project Member Invite"
        verbose_name_plural = "Project Member Invites"
        ordering = ['-created_at']


class ProjectMember(models.Model):
    project = models.ForeignKey(Project, related_name='members', on_delete=models.CASCADE)
    member = models.ForeignKey(
        User, 
        related_name='project_memberships', on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    role = models.CharField(max_length=50, choices=[('admin', 'Admin'), ('member', 'Member')], default='member')
    joined_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.member.username} - {self.project.name}"

    class Meta:
        verbose_name = "Project Member"
        verbose_name_plural = "Project Members"
        unique_together = ('project', 'member')
        ordering = ['-joined_at']


class Task(models.Model):
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    assigned_to = models.ForeignKey(
        User,
        related_name='tasks',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=20,
        choices=[('todo', 'To Do'), ('in_progress', 'In Progress'), ('done', 'Done')],
        default='todo'
    )
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ['-created_at']