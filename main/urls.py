
from django.conf.urls import include, url
from django.contrib import admin
from main import views

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.main, name='main'),
]
