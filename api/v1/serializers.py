from rest_framework.serializers import ModelSerializer
from biography.models import Biography
from contact.models import Contact
from gallery.models import Gallery
from main.models import Main
from writings.models import Writings
from news.models import News


class BiographySerializer(ModelSerializer):
    class Meta:
        model = Biography
        fields = '__all__'


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class MainSerializer(ModelSerializer):
    class Meta:
        model = Main
        fields = '__all__'


class GallerySerializer(ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'


class WritingSerializer(ModelSerializer):
    class Meta:
        model = Writings
        fields = '__all__'


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
