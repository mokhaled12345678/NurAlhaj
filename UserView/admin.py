from django.contrib import admin
from .models import Packages, Gallery, Bookings, Hotels, Plane
# Register your models here.

admin.site.register(Packages)
admin.site.register(Gallery)
admin.site.register(Bookings)
admin.site.register(Hotels)
admin.site.register(Plane)