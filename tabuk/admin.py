from django.contrib import admin
from .models import Booking, Checkout, Package

# Register your models here.

admin.site.register(Package) 
admin.site.register(Booking)
admin.site.register(Checkout) 



