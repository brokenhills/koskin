from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from news.models import News

# Create your views here.

def news(request):
    new = News.objects.all()
    context = {
        'news': new
    }
    return render(request, 'news/news.html', context)