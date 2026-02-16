from django.shortcuts import render
from .models import BannerImages, Clients, Services,Projects
# Create your views here.

def home(request):
    banner_images = BannerImages.objects.last()
    Services_list = Services.objects.order_by('-id')[:6]
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

    service=Services.objects.order_by('-id')
    context = {
        'Services': service,
    }

    return render(request, 'courses.html', context)


def blog(request):
    projects = Projects.objects.order_by('-id')
    context = {
        'projects': projects,
    }
    return render(request, 'blog.html', context)


def gallery(request):
    return render(request, 'gallery.html')

def ourstudents(request):
    clients= Clients.objects.all()
    context = {
        'clients': clients,
    }
    return render(request, 'ourstudents.html', context)

def contact(request):
    return render(request, 'contact.html')






