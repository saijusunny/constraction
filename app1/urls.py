from django import views
from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),

    
    
]