from django.db import models
from django.urls import reverse 

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=100, unique=True)
    city = models.CharField(max_length=50, default="Dubai")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse ('home')

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    student_numbers = models.IntegerField(default = 0)
