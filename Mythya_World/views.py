from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello World, Welcome to Mythya World")
    return render(request, 'website/index.html')


def about(request):
    # return HttpResponse("Hello World, About")
    return render(request, 'website/about.html')

def contact(request):
    # return HttpResponse("Hello World, Contact")
    return render(request, 'website/contact.html')

def gallery(request):
    # return HttpResponse("Hello World, Gallery")
    return render(request, 'website/gallery.html')





