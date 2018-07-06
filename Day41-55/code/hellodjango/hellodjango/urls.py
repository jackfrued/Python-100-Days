"""hellodjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from demo import views

urlpatterns = [
    path('', views.login),
    path('login/', views.login),
    path('register/', views.register),
    path('check/', views.check_username),
    path('subjects/', views.show_subjects, name='sub'),
    path('subjects/<int:no>/', views.show_teachers),
    path('good/<int:no>/', views.make_comment),
    path('bad/<int:no>/', views.make_comment),
    path('admin/', admin.site.urls),
]
