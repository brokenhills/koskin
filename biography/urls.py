
from django.conf.urls import include, url
from django.contrib import admin
from biography import views
admin.autodiscover()

urlpatterns = [
    url(r'^biography/', views.biography, name='biography')
]