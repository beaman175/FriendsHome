from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #candidates = Candidate.objects.all()
    return render(request, 'index.html')