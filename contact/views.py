from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from writings.models import Writings

# Create your views here.

def contact(request):
    return render(request, 'contact/contact.html')