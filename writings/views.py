from django.shortcuts import render, get_object_or_404
from writings.models import Writings

# Create your views here.


def writings(request):
    writing = Writings.objects.all().order_by('-datead')
    return render(request, 'writings/writings.html', {'writings': writing})


def show_writing(request, idwr):
    text = get_object_or_404(Writings, idwr=idwr)
    return render(request, 'writings/text.html', {'text': text})
