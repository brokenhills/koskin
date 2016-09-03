from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from writings.models import Writings

# Create your views here.

def writings(request):
    writing = Writings.objects.all()
    context = {
        'writings': writing
    }
    return render(request, 'writings/writings.html', context)

def show_writing(request, idwr):
    text = get_object_or_404(Writings, idwr=idwr)
    return render(request, 'writings/text.html', {'text': text})