"""todoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from atexit import register
from cgitb import html
from ctypes import alignment
from re import template
from unicodedata import name
from xml.etree.ElementInclude import include
import django
from django.contrib import admin
from django.urls import path,include
from django.conf import settings

from studentprofile import views 
from studentprofile import views as dash_view
from django.contrib.auth import views as auth_views
import studentprofile
from django.views.generic import TemplateView





urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('studentprofile.urls')),
    path('base',views.base,name='base'),
    path('wiki',views.wiki,name='wiki'),
    path('youtube',views.youtube,name='youtube'),
    path('dictionary',views.dictionary,name='dictionary'),
    path('books',views.books,name='books'),
    path('register',dash_view.register,name='register'),
    path('login',auth_views.LoginView.as_view(template_name='studentprofile/login.html'),name='login'),
    path('logout',auth_views.LogoutView.as_view(template_name='studentprofile/logout.html'),name='logout'),
    path('notes',views.notes,name='notes'),
    path('notes_detail/<int:pk>',views.NotesDetailView.as_view(),name='notes_detail'),
    path('delete_note/<int:pk>',views.delete_note,name='delete_note'),
    path('todo',views.todo,name='todo'),
    path('delete_todo/<int:pk>',views.delete_todo,name='delete_todo'),
    path('update_todo/<int:pk>',views.update_todo,name='update_todo'),
    path('homework',views.homework,name='homework'),
    path('update_homework/<int:pk>',views.update_homework,name='update_homework'),
    path('delete_homework/<int:pk>',views.delete_homework,name='delete_homework'),
    path('conversion',views.conversion,name='conversion'),
    path('profile',views.profile,name='profile')

]
