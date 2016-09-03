from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from biography.models import Biography

# Create your views here.

def biography(request):
    bio = Biography.objects.all()
    context = {
        'biography': bio
    }
    return render(request, 'biography/biography.html', context)