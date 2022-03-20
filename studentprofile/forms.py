from cProfile import label
from dataclasses import fields
from pyexpat import model
from random import choices
from sqlite3 import Date
from tkinter import Widget
from turtle import title
from unittest.util import _MAX_LENGTH
from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from datetime import datetime,date
from studentprofile.models import Homework, Notes, Todo
import django.forms
import django.forms.utils
import django.forms.widgets
import arrow










class DashboardForm(forms.Form):
    text=forms.CharField(max_length=225,label="Enter your Search:")


class UserRegisterForm(UserCreationForm):
    class Meta:
        model= User
        fields =['username',
        'password1','password2'

        ]


class NotesForm(forms.ModelForm):
    class Meta:
        model= Notes
        fields =['title','description']



class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields=['title','is_finished']




class DateTimeInput(forms.DateInput):
    input_type = "datetime-local"
    format=arrow.get('2022-02-09 19:26:33','YYYY-MM-DD HH:mm:ss')


    


class HomeWorkForm(forms.ModelForm):

    
    class Meta:
        model=Homework
        widgets={'due':DateTimeInput()}
        fields=['subject','title','description','due','is_finished']





class ConversionForm(forms.Form):
    CHOICES = [('length', 'Length'),
               ('mass', 'Mass')]

    measurement = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)


class ConversionLengthForm(forms.Form):
    CHOICES = [('yard', 'Yard'),
               ('foot', 'Foot')]
    input = forms.CharField(required=False,
                            label=False, widget=forms.TextInput(attrs={'type': 'number', 'placeholder': 'Enter the number'}))
    measure1 = forms.CharField(
        label='', widget=forms.Select(choices=CHOICES))
    measure2 = forms.CharField(
        label='', widget=forms.Select(choices=CHOICES))


class ConversionMassForm(forms.Form):
    CHOICES = [('pound', 'Pound'),
               ('kilogram', 'Kilogram')]
    input = forms.CharField(required=False,
                            label=False, widget=forms.TextInput(attrs={'type': 'number', 'placeholder': 'Enter the number'}))

    measure1 = forms.CharField(
        label='', widget=forms.Select(choices=CHOICES))
    measure2 = forms.CharField(
        label='', widget=forms.Select(choices=CHOICES))
             