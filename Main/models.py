from django.db import models

# Create your models here.
class House(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15, null=False)
    phone = models.CharField(max_length=13, null=False)
    title = models.CharField(max_length=30, null=False)
    price = models.IntegerField(default=0, null=False)
    content = models.TextField(null=False)
    star = models.IntegerField(default=0, null=False)
    hits = models.IntegerField(default=0, null=False)
    #date = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.title