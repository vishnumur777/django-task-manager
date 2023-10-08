from django.db import models

class UsersModel(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email =  models.EmailField()
    password = models.CharField(max_length=100)
    phno = models.CharField(max_length=15)
class StatusChoices(models.TextChoices):
    Complete = "Completed","C"
    InProgress = "InProgress","IP"
    pend = "Pending","P"

class TaskManage(models.Model):
    name = models.CharField(max_length=1000)
    description = models.TextField()
    status = models.CharField(max_length=100,choices=StatusChoices.choices)
    due_date =  models.DateTimeField()

