from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=100)


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    name = models.CharField(max_length=100)
