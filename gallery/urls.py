
from django.conf.urls import include, url
from django.contrib import admin
from gallery import views
from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()

urlpatterns = [
    url(r'^gallery/', views.gallery, name='gallery'),
    url(r'^image/(?P<idim>[0-9]+)/$', views.show_image, name='image')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)