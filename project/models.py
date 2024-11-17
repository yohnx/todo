import uuid
from django.db import models
from account.models import User

# Create your models here.
class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='project', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class ProjectFile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    #attachment = models.FileField(upload_to='projectfiles', blank=True, null=True, default='')

    def __str__(self):
        return self.name

