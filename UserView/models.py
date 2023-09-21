from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import date

# Create your models here.
class Hotels(models.Model):
    name = models.CharField(max_length=50)
    priceDay = models.FloatField()

    def __str__(self):
        return self.name

class Plane(models.Model):
    name = models.CharField(max_length=50, default='Air Plane Name')
    price = models.FloatField(default=0.0)
    Class = models.CharField(max_length=50,blank=True) 

    def __str__(self):
        return self.name + '({})'.format(self.Class)

class Packages(models.Model):
    name = models.CharField(max_length=50, default='Package Name')
    image = models.ImageField(upload_to='uploaded-images/packages')
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE, default=None, null=True)
    location = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    description = models.TextField(max_length=400)
    available_counter = models.PositiveIntegerField(default=0)
    arrivalDate = models.DateField(default=date.today)
    leaveDate = models.DateField(default=date.today)
    sale = models.FloatField(default=0.0)

    def get_duration(self):
        duration = (self.leaveDate - self.arrivalDate).days
        return duration
    
    def get_price(self):
        duration = self.get_duration()
        priceDay = self.location.priceDay
        cost = priceDay * duration + self.plane.price
        return cost
    
    def get_sale_price(self):
        duration = self.get_duration()
        priceDay = self.location.priceDay
        cost = priceDay * duration + self.plane.price - self.sale
        return cost
    
    def get_title(self):
        return self.location.name
    
    def get_plane(self):
        return self.plane.__str__()
    
    def __str__(self):
        return self.name

class Gallery(models.Model):
    image = models.ImageField(upload_to='uploaded-images/gallery')
    title = models.CharField(max_length=100, default='My Gallery Title')
    description = models.TextField(default='My gallery description', max_length=150)

    def __str__(self):
        return self.title

class Bookings(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    package = models.ForeignKey(Packages, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'package')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.package.save()
        
    def __str__(self):
        name = '{} ({}) ({}) ({})'.format(self.package.name ,self.package.location.name, self.user.username, self.package.plane.name)
        return name
