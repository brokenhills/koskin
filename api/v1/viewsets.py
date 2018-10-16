from rest_framework import viewsets
from biography.models import Biography
from contact.models import Contact
from gallery.models import Gallery
from main.models import Main
from writings.models import Writings
from news.models import News
from api.v1.serializers import WritingSerializer, BiographySerializer, ContactSerializer, GallerySerializer, \
    MainSerializer, NewsSerializer


class BiographyViewSet(viewsets.ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographySerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


class MainViewSet(viewsets.ModelViewSet):
    queryset = Main.objects.all()
    serializer_class = MainSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class WritingsViewSet(viewsets.ModelViewSet):
    queryset = Writings.objects.all()
    serializer_class = WritingSerializer
