
from django.conf.urls import include, url
from django.contrib import admin
from contact import views
admin.autodiscover()

urlpatterns = [
    url(r'^contact/', views.contact, name='contact')
]