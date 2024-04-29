from django.db import models
from tasks.models import Project, Task


class BugReport(models.Model):
    
    STATUS_CHOICES = [
        ('New', 'Новая'),
        ('In_progress', 'В работе'),
        ('Completed', 'Завершена'),
    ]
    
    PRIORITY_CHOICES = [
        (0, 'Not important'),
        (1, 'Very low'),
        (2, 'Low'),
        (3, 'Normal'),
        (4, 'High'),
        (5, 'Very High'),
    ]
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )
    
    task = models.ForeignKey(
        Task,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='New',
    )
    priority = models.IntegerField(
        choices=PRIORITY_CHOICES,
        default=0,
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
   
class FeatureRequest(models.Model):
    
    STATUS_CHOICES = [
        ('Reviewed', 'Рассмотрено'),
        ('Accepted', 'Принято'),
        ('Rejected', 'Отклонено'),
    ]
    
    PRIORITY_CHOICES = [
        (0, 'Not important'),
        (1, 'Very low'),
        (2, 'Low'),
        (3, 'Normal'),
        (4, 'High'),
        (5, 'Very High'),
    ]
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )
    
    task = models.ForeignKey(
        Task,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='New',
    )
    priority = models.IntegerField(
        choices=PRIORITY_CHOICES,
        default=0,
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    