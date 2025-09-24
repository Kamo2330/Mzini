from django.shortcuts import render
from properties.models import Property


def home(request):
    featured = Property.objects.filter(is_published=True, is_featured=True)[:6]
    return render(request, 'core/home.html', {'featured': featured})


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    return render(request, 'core/contact.html')


