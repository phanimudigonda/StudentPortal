

from collections import deque
from email.utils import format_datetime
from pyexpat import model
from re import S
from this import s
from tkinter import CASCADE
from turtle import title
from arrow import Arrow
import arrow
from django.db import models
from datetime import datetime

from django.contrib.auth.models import User
from django.forms import DateTimeInput



class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=300)
    description=models.TextField()

    def __str__(self):
        return self.title

class Todo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    is_finished=models.BooleanField(default=False)



    def __str__(self):
        return self.title

class Homework(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    subject=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    description=models.TextField()

    due=models.DateTimeField()
    is_finished=models.BooleanField(default=False)


    def __str__(self):
        return self.title



