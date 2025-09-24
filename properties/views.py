from django.shortcuts import render, get_object_or_404, redirect
from .models import Property


def browse(request):
    properties = Property.objects.filter(is_published=True)
    return render(request, 'properties/browse.html', {'properties': properties})


def property_detail(request, pk: int):
    prop = get_object_or_404(Property, pk=pk, is_published=True)
    return render(request, 'properties/detail.html', {'property': prop})


def sell_property(request):
    return render(request, 'properties/sell.html')


