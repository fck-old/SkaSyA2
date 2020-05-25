import datetime

from django.db import models
from django.utils import timezone

class ToDo(models.Model):
    due_date = models.DateTimeField()
    description = models.CharField(max_length=160)
    percent = models.FloatField()
    
    def __str__(self):
        return self.description
