from django.db import models


# Create your models here.
class carHire(models.Model):
    make = models.CharField(max_length=25, verbose_name='Car Make')
    model = models.CharField(max_length=25, verbose_name='Car Model')
    seater = models.IntegerField(verbose_name='Seater')
    image = models.ImageField(verbose_name='Car Image', upload_to='images/', blank=True, null=True)
    price = models.IntegerField(verbose_name='Hiring Price')
    plate = models.CharField(max_length=8, verbose_name='Number Plate')
    description = models.TextField(max_length=100, verbose_name='Car Description', blank=True)

    def __str__(self):
        return f"Registration Number {self.plate} is a {self.make} {self.model}"


class destinations(models.Model):
    # image = models.ImageField(verbose_name='Image')
    name = models.CharField(max_length=25, verbose_name='Location')
    description = models.TextField(max_length=500, verbose_name='Description')


class accommodation(models.Model):
    # image = models.ImageField(verbose_name='Image')
    name = models.CharField(max_length=50, verbose_name='Name')
    location = models.CharField(max_length=20, verbose_name='Location')
    price = models.IntegerField(verbose_name='Price')
    description = models.TextField(max_length=100, verbose_name='Description')
    type = models.CharField(max_length=20, verbose_name='Type')
    rooms = models.IntegerField(verbose_name='No. of rooms')
    phone = models.CharField(verbose_name='Contact Phone', blank=True, max_length=15)
    email_address = models.EmailField(verbose_name='Email Address', blank=True)


class attractions(models.Model):
    # image = models.ImageField(verbose_name='Image')
    name = models.CharField(max_length=50, verbose_name='Name')
    location = models.CharField(max_length=20, verbose_name='Location')
    fee = models.CharField(max_length=4, verbose_name='Entrance Fee', help_text='Input fee if there is any')
    description = models.TextField(max_length=1000, verbose_name='Description')
