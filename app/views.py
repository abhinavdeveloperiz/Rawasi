from django.shortcuts import render
from .models import BannerImages, Clients, Services, Courses, Students, Gallery

# Create your views here.

def home(request):
    banner_images = BannerImages.objects.last()
    Services_list = Services.objects.all()[:6]
    clients_list = Clients.objects.all()

    context = {
        'banner': banner_images,
        'Services': Services_list,
        'clients': clients_list,
    }

    return render(request, 'home.html',context)


def about(request):
    return render(request, 'about.html')

def courses(request):
    return render(request, 'courses.html')

def blog(request):
    return render(request, 'blog.html')

def gallery(request):
    return render(request, 'gallery.html')

def ourstudents(request):
    return render(request, 'ourstudents.html')

def contact(request):
    return render(request, 'contact.html')






