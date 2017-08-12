from django.shortcuts import render
from django.http import HttpResponse

from .models import House

# Create your views here.
def index(request):
    houses = House.objects.all()

    context = {'houses':houses}
    return render(request, 'house_main.html', context)
    #return render(request, 'house_detail.html')

def detail(request, id):
    house = House.objects.filter(id=id)
    context = {'house':house}
    return render(request, 'house_detail.html', context)