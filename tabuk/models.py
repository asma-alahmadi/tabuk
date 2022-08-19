from django.db import models
from django.utils.text import slugify


# Create your models here.

class Package (models.Model):
    destination = models.CharField(max_length=130)
    image = models.ImageField(upload_to="images")
    duration = models.IntegerField(help_text="How many days this trip will take") 
    description = models.CharField(max_length=500)
    cost = models.FloatField()
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.destination)
        super(Package, self).save(*args, **kwargs)

    
    def __str__(self):
        return f'Package to {self.destination}'


class Booking(models.Model): 
    package = models.ForeignKey (Package, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, )
    email = models.EmailField()
    adults = models.IntegerField(default=1, )
    children = models.IntegerField(default=0, blank=True, null=True) 
    start_date = models.DateField() 
    
    def __str__(self):
        return str(self.id)

    def get_total_price(self):
        return f'Total: {(self.adults * self.package.cost) + (self.children *self.package.cost)}$'


class Checkout(models.Model):
    user = models.CharField(max_length=150)
    email = models.EmailField()
    package = models.ForeignKey(Package, on_delete=models.CASCADE, null= True)
    total_price = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
