from ast import Return
from asyncio.base_futures import _FINISHED


from doctest import Example
from email import message
from email.mime import audio
from gettext import install
import json
from modulefinder import IMPORT_NAME
from os import link
from pickle import REDUCE
from pyexpat.errors import messages
from re import U, search
import re
from tkinter.tix import Form
from turtle import title
from unicodedata import name
from unittest import result
from webbrowser import get
from winreg import REG_RESOURCE_REQUIREMENTS_LIST
from django import urls
from django.db import DEFAULT_DB_ALIAS
from django.forms import forms
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import context
import pip
from studentprofile.forms import ConversionForm, ConversionLengthForm, ConversionMassForm, DashboardForm, HomeWorkForm, NotesForm, TodoForm, UserRegisterForm

import wikipedia
import warnings
import sys 
import copy
import os

from studentprofile.models import Homework, Notes, Todo
from django.contrib import messages



from . import forms
from youtubesearchpython import VideosSearch
import requests

import studentprofile

from django.contrib.auth.decorators import login_required
from django.views import generic





def home(request):
    return render(request,'studentprofile/home.html')



def base(request):
    return render(request,'studentprofile/base.html')

def wiki(request):
    if request.method == "POST":
        text=request.POST['text']
        form=DashboardForm(request.POST)
        search=wikipedia.page(text)
        context={
            'form':form,
            'title':search.title,
            'link':search.url,
            'details':search.summary,
        }
        return render(request,'studentprofile/wiki.html',context)
    else:
        form=DashboardForm()
        return render(request,'studentprofile/wiki.html',{'form':form})
def youtube(request):
    if request.method == "POST":
        form=DashboardForm(request.POST)
        text=request.POST['text']
        videos=VideosSearch(text,limit=5)
        result_list=[]
        for i in videos.result()['result']:
            result_dict={
                'input':text,
                'title':i['title'],
                'duration':i['duration'],
                'thumbnail':i['thumbnails'][0]['url'],
                'channel':i['channel']['name'],
                'link':i['link'],
                'views':i['viewCount']['short'],
                'published':i['publishedTime'],


            }
            desc=''

            for j in i['descriptionSnippet']:
                desc +=j['text']
            result_dict['description']=desc
            result_list.append(result_dict)


        
        return render(request,'studentprofile/youtube.html',{'form':form,'results':result_list})
    else:
        form=DashboardForm()
        return render(request,'studentprofile/youtube.html',{'form':form})


def dictionary(request):
    if request.method == "POST":
        text = request.POST['text']
        form = DashboardForm(request.POST)
        url = "https://api.dictionaryapi.dev/api/v2/entries/en_US/"+text
        r = requests.get(url)
        answer = r.json
        
       
      

                                           

        try:
            phonetics=answer[0]['phonetics'][0]['text']
            audio = answer[0]['phonetics'][0]['audio']
            defination =answer[0]['meanings'][0]['definations'][0]['defination']
            example =answer[0]['meanings'][0]['definations'][0]['example']
            synonyms =answer[0]['meanings'][0]['definations'][0]['synonyms']

            context={
                'form': form,
                'input': text,
                'phonetics': phonetics,
                'audio': audio,
                'defination': defination,
                'example': example,
                'synonyms': synonyms,


            }
        except:

            context={
                'form':form,
                input:'',
            }




        return render(request,'studentprofile/dictionary.html',context)
    
    else:
        form=DashboardForm()
    return render(request,'studentprofile/dictionary.html',{'form':form})


def base(request):
    return render(request,'studentprofile/base.html')





def books(request):
    if request.method == 'POST':
        text=request.POST['text']
        form = DashboardForm(request.POST)
        url ="https://www.googleapis.com/books/v1/volumes?q="+text
        r = requests.get(url)
        answer= r.json()
        result_list=[]
        for i in range(10):

            result_dict={
                'title':answer['items'][i]['volumeInfo']['title'],
                'subtitle':answer['items'][i]['volumeInfo'].get('subtitle'),
                'description':answer['items'][i]['volumeInfo'].get('description'),
                'count':answer['items'][i]['volumeInfo'].get('pageCount'),
                'categories':answer['items'][i]['volumeInfo'].get('categories'),
                'thumbnail':answer['items'][i]['volumeInfo']['imageLinks']['thumbnail'],
                'preview':answer['items'][i]['volumeInfo'].get('previewLink')
            }
                
                

            

            result_list.append(result_dict)

        context={
            'form':form,
            'results':result_list,
        }
        

        return render(request,'studentprofile/books.html',context)
    else:
        form =DashboardForm()
        return render(request,'studentprofile/books.html',{'form':form})


def register(request):
    if request.method == 'POST':
        u_form = UserRegisterForm(request.POST)
        if u_form.is_valid():
            u_form.save()
            username=u_form.cleaned_data.get('username')
            messages.success(request,f'Acoount Created For {username}')
            return redirect('login')

    else:
        u_form=UserRegisterForm()
    return render(request,'studentprofile/register.html',{'u_form':u_form})


@login_required
def profile(request):
    homeworks = Homework.objects.filter(is_finished=False,user=request.user)
    todos= Todo.objects.filter(is_finished=False,user=request.user)
    if len(homeworks)==0:
        homeworks_done = True
    else:
        homeworks_done= False
    if len(todos)==0:
        todos_done=True
    else:
        todos_done=False
    context={
        'homeworks':zip(homeworks, range(1,len(homeworks)+1)),
        'todos':zip(todos,range(1,len(todos)+1)),
        'homeworks_done':homeworks_done,
        'todos_done':todos_done,
    }
    return render(request,'studentprofile/profile.html',context)


@login_required
def notes(request):
    if request.method== 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            notes = Notes(user=request.user,title=request.POST['title'],description=request.POST['description'])
            notes.save()
            messages.success(
                request, f'Notes Added From{request.user.username}')
        
    else:
        form =NotesForm()
    notes= Notes.objects.filter(user=request.user)

    context={'form':form,'notes':notes}


    return render(request,'studentprofile/notes.html',context)


class NotesDetailView(generic.DetailView):
    model=Notes



def delete_note(request,pk=None):
    Notes.objects.get(id=pk).delete()
    return redirect('notes')

    
@login_required
def todo(request):
    if request.method=='POST':
        form= TodoForm(request.POST)
        if form.is_valid():

            try:

                finished = request.POST['is_finished']
                if finished == 'on':
                    finished=True
                else:
                    finished=False

            except:
                finished=False
            todos=Todo(
                user=request.user,title=request.POST['title'],is_finished=finished)
            todos.save()
            messages.success(
                request,f'Todo Added from{request.user.username}!')
    else:
        form=TodoForm()
    todos=Todo.objects.filter(user=request.user)


    if len(todos)==0:
        todos_done=True

    else:
        todos_done=False
    todos=zip(todos,range(1,len(todos)+1))
    context={'form':form,'todos':todos,'todos_done':todos_done}
    return render(request,'studentprofile/todo.html',context)

def update_todo(request,pk=None):
    todo=Todo.objects.get(id=pk)
    if todo.is_finished==True:
        todo.is_finished=False

    else:
        todo.is_finished=True
    todo.save()
    if 'profile' in request.META['HTTP_REFERER']:
        return redirect('profile')

    return redirect('todo')


def delete_todo(request,pk=None):
    Todo.objects.get(id=pk).delete()
    if 'profile' in request.META['HTTP_REFERER']:
        return redirect('profile')

    return redirect('todo')
@login_required
def homework(request):
    if request.method =='POST':
        form=HomeWorkForm(request.POST)
        if form.is_valid():
            try:
                finished=request.POST['is_finished']
                if finished=='on':
                    finished=True
                else:
                    finished=False

                
            except:
                finished=False

            homeworks=Homework(user=request.user,subject=request.POST['subject'],title=request.POST['title'],description=request.POST['description'],due=request.POST['due'],is_finished=finished)
            homeworks.save()
            messages.success(request,f'Homework Added from {request.user.username}!')

    else:
        form=HomeWorkForm()
    homeworks=Homework.objects.filter(user=request.user)
    if len(homeworks)==0:
        homeworks_done=True


    else:
        homeworks_done=False

    homeworks=zip(homeworks,range(1,len(homeworks)+1))
    context={'form':form,'homeworks':homeworks,'homeworks_done':homeworks_done}
    return render(request,'studentprofile/homework.html',context)


def update_homework(request,pk=None):
    homework=Homework.objects.get(id=pk)
    if homework.is_finished==True:
        homework.is_finished=False

    else:
        homework.is_finished=True
    homework.save()
    if profile in request.META['HTTP_REFERER']:
        return redirect('profile')
    else:
        return redirect('homework')


def delete_homework(request,pk=None):
    Homework.objects.get(id=pk).delete()
    return redirect('homework')
        

def conversion(request):
    if request.method=='POST':
        form=ConversionForm(request.POST)
        if request.POST['measurement']=='length':
            measurement_form=ConversionLengthForm()
            context={'form':form,'m_form':measurement_form,'input':True}
            if 'input' in request.POST:
                first=request.POST['measure1']
                second=request.POST['measure2']
                input=request.POST['input']
                answer=''
                if input and int(input)>=0:
                    if first=='yard' and second=='foot':
                        answer=f'{input} yard={int(input)*3} foot'
                    if first=='foot' and second=='yard':
                        answer=f'{input} foot={int(input)/3} yard'
                context={'form':form,'m_form':measurement_form,'input':True,'answer':answer}

        if request.POST['measurement'] =='mass':
            measurement_form=ConversionMassForm()
            context={'form':form,'m_form':measurement_form,'input':True}
            if 'input' in request.POST:
                first=request.POST['measure1']
                second=request.POST['measure2']
                input=request.POST['input']
                answer=''
                if input and int(input)>=0:
                    if first=='pound' and second=='kilogram':
                        answer=f'{input} pound={int(input)*0.453592} kilogram'
                    if first=='kilogram' and second=='pound':
                        answer=f'{input} kilogram={int(input)*2.20462} pound'
                context={'form':form,'m_form':measurement_form,'input':True,'answer':answer}


    else:
        form=ConversionForm()
        context={'form':form,'input':False}
    return render(request,'studentprofile/conversion.html',context)











        


 











    


        









