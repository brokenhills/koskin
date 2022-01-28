from django.urls import include, path
from rest_framework import routers
from api.v1.viewsets import WritingsViewSet, BiographyViewSet, ContactViewSet, GalleryViewSet, MainViewSet, \
    NewsViewSet

api_router = routers.SimpleRouter()
api_router.register('biography', BiographyViewSet)
api_router.register('contact', ContactViewSet)
api_router.register('gallery', GalleryViewSet)
api_router.register('news', NewsViewSet)
api_router.register('writings', WritingsViewSet)
api_router.register('main', MainViewSet)

url_patterns = [
    path('', include(api_router.urls)),
]
