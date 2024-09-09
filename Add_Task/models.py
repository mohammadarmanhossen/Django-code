from django.db import models
from Add_Category.models import CategoryModel

class TaskModel(models.Model):
    title=models.CharField(max_length=100)
    taskDescription=models.TextField()
    date=models.DateField()
    is_completed = models.BooleanField(default=False)
    category=models.ManyToManyField(CategoryModel)
    
    def __str__(self):
        return self.title