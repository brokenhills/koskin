from django.urls import include, path
from rest_framework import routers
from api.v1.viewsets import WritingsViewSet, BiographyViewSet, ContactViewSet, GalleryViewSet, MainViewSet, \
    NewsViewSet, WritingViewSet

api_router = routers.SimpleRouter()
api_router.register('biography', BiographyViewSet)
api_router.register('contact', ContactViewSet)
api_router.register('gallery', GalleryViewSet)
api_router.register('main', MainViewSet)
api_router.register('news', NewsViewSet)
api_router.register('writings', WritingsViewSet)

url_patterns = [
    path('', include(api_router.urls)),
    path(r'writings/^(?P<pk>\w+)/$', WritingViewSet.as_view())
]
