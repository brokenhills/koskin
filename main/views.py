from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from writings.models import Writings

# Create your views here.

def main(request):
    return render(request, 'main/index.html')
