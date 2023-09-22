"""koskin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.schemas import get_schema_view

from api.v1.routes import url_patterns
from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(url_patterns)),
    url('^openapi/', get_schema_view(
        title='Koskin API',
        description='API for Koskin Website',
        version='1.0.0',
    ), name='openapi-schema'),

] + static(prefix='media', document_root=settings.MEDIA_ROOT)
