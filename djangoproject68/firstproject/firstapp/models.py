from django.db import models


class Employee(models.Model):
    name=models.CharField(max_length=30)
    number=models.IntegerField()
    sal=models.FloatField()
