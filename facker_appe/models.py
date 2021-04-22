from django.db import models

# Create your models here.


class student(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    salary=models.IntegerField()
    job=models.CharField(max_length=30)
    location=models.CharField(max_length=50)


