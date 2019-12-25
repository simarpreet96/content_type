from django.contrib import admin
from django.urls import path
from django.conf.urls import url
#from django.contrib.auth import views as auth_views
from . import views 
#from food.views import *

urlpatterns = [
	path('', views.view1, name='view1'),


]