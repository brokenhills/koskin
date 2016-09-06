from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from main.models import Main
from writings.models import Writings


# Create your views here.


def main(request):
    m = Main.objects.all()
    w = Writings.objects.filter(is_liked=True)
    return render(request, 'main/index.html', {'main': m, 'writ': w})


def show_liked(request, idwr):
    text = get_object_or_404(Writings, idwr=idwr)
    return render(request, 'main/liked.html', {'text': text})
