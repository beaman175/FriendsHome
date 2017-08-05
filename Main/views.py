from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'house_main.html')
    #return render(request, 'house_detail.html')

def detail(request, id):
   return render(request, 'house_detail.html')