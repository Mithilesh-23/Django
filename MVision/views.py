from django.shortcuts import render

# Create your views here.
def all_vision(request):
    return render(request, 'MVision/all_vision.html')