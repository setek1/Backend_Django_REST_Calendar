from django.db import models
from datetime import timedelta

# Create your models here.

class calendarDate(models.Model):
    start=models.DateTimeField(auto_now=False, auto_now_add=False)
    end=models.DateTimeField(auto_now=False, auto_now_add=False)
    title=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title} {self.start} {self.end}'