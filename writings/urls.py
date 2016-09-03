
from django.conf.urls import include, url
from django.contrib import admin
from writings import views
admin.autodiscover()

urlpatterns = [
    url(r'^writings/', views.writings, name='writings'),
    url(r'^writing/(?P<idwr>[0-9]+)/$', views.show_writing, name='writing')
]
