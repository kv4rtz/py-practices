from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ForeignKey('Course', on_delete=models.CASCADE)