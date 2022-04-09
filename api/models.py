from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
#from imagekit import *
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, blank=False)
    category = models.CharField(max_length=100, blank=False)
    price = models.DecimalField(max_digits=50, decimal_places=2)
    description = models.TextField()
    stars = models.TextField()
    header_image = models.ImageField(null= True, blank=True, upload_to = "images/" )

    thumbnail = ImageSpecField(
        source = 'image', processors=[ResizeToFill(140,140)],format='PNG',
        options = {'quality':60}
    )


    def __str__(self):
        return self.name



#username : krish
#password : 12345