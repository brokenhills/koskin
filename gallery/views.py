from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from gallery.models import Gallery


# Create your views here.

def gallery(request):
    gal = Gallery.objects.all()
    context = {
        'gallery': gal
    }
    return render(request, 'gallery/gallery.html', context)

def show_image(request, idim):
    image = get_object_or_404(Gallery, idim=idim)
    return render(request, 'gallery/image.html', {'image': image})

def get_next(request):
    r = Gallery.objects.first
    return render(request, 'gallery/image.html', {'image': r.get_next_by_created()})
def get_prev(request):
    r = Gallery.objects.first
    return render(request, 'gallery/image.html', {'image': r.get_previous_by_created()})
