from rest_framework.serializers import ModelSerializer
from core.models import Writings, News, Main, Gallery, Contact, Biography


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
