from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import django.middleware.csrf
from django.views.decorators.csrf import csrf_exempt

from .models import House, Comment

# Create your views here.
def index(request):
    houses = House.objects.all()
    context = {'houses':houses}

    return render(request, 'house_main.html', context)
    #return render(request, 'house_detail.html')



def detail(request, id):
    house = House.objects.filter(id=id)
    comment = Comment.objects.filter(ref=id)

    context = {'house':house,'comment':comment}

    return render(request, 'house_detail.html', context)

def write(request):
    return render(request, 'house_write.html')

@csrf_exempt

def register(request):
    print(request.POST['title'])
    house = House(title = request.POST['title'],
                  name = request.POST['name'],
                  phone = request.POST['phone'],
                  price = request.POST['price'],
                  content = request.POST['content'],
                  address = request.POST['address'])
                  #photo = request.POST['photo'])
    print(house)
    house.save()

    url='/house/detail/1/'
    return HttpResponseRedirect(url)
#    return render(request, 'house_main.html')


