from django.db import models
from datetime import datetime, date
from django.utils import timezone

def user_directory_path(instance, filename):
    return 'photos/img_{}_{}.{}'.format(datetime.now().strftime('%Y%m%d%H%M%S'), filename.split('.')[0],filename.split('.')[-1])

# Create your models here.
class House(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15, null=False)
    title = models.CharField(max_length=30, null=False)
    phone = models.CharField(max_length=13, null=False)
    price = models.IntegerField(default=0, null=False)
    content = models.TextField(null=False)
    address = models.CharField(max_length=50, null=True)
    star = models.IntegerField(default=0, null=False)
    hits = models.IntegerField(default=0, null=False)

    #upload_to에 정의할 함수는 반드시 user_directory_path
    photo = models.ImageField(default=True, blank=True, upload_to = user_directory_path,null=True)
    photo2 = models.ImageField(default=True, blank=True, upload_to = user_directory_path,null=True)
    photo3 = models.ImageField(default=True, blank=True, upload_to = user_directory_path,null=True)


    #date = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.title

class Comment(models.Model):
    ref = models.ForeignKey('House',related_name='comments')
    name = models.CharField(max_length=15, null=False)
    content = models.TextField(null=False)
    star = models.IntegerField(default=0, null=False)
    date = models.DateTimeField(default=timezone.now())


    def __str__(self):
        return self.name



