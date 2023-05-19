from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .forms import ImageForm
from .models import Image

def home(request):
    return render(request, 'home.html')

def upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("File uploaded successfully!")
    else:
        form = ImageForm()
    
    image_urls = ["messi.jpg", "airport.jpg"]

    context = {
        "form": form,
        "image_urls": image_urls
    }

    return render(request, 'upload.html', context)

