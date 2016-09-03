
from django.conf.urls import include, url
from django.contrib import admin
from news import views
admin.autodiscover()

urlpatterns = [
    url(r'^news/', views.news, name='news')
]