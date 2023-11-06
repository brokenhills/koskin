from rest_framework import viewsets
from django_filters.rest_framework import (
    DjangoFilterBackend,
)
from rest_framework.response import Response

from api.v1.filters import DateWrRangeFilter
from core.models import (
    Writings,
    News,
    Main,
    Gallery,
    Contact,
    Biography,
)
from api.v1.serializers import (
    WritingSerializer,
    BiographySerializer,
    ContactSerializer,
    GallerySerializer,
    MainSerializer,
    NewsSerializer,
)


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
    queryset = Writings.objects.all().order_by('datewr')
    serializer_class = WritingSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = DateWrRangeFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        search = request.query_params.get('search')
        if search:
            queryset = Writings.objects.filter(
                content__search=search,
            )
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
