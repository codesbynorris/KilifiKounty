from django.contrib.auth.models import AbstractUser, User
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


class destination(models.Model):
    name = models.CharField(max_length=25, verbose_name='Location')
    image = models.ImageField(verbose_name='Image', blank=True)
    description = models.TextField(max_length=500, verbose_name='Description')
    link = models.URLField(verbose_name='Google Maps Link')

    def __str__(self):
        return f"{self.name}"


class accommodation(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    location = models.CharField(max_length=20, verbose_name='Location')
    price = models.IntegerField(verbose_name='Price')
    image = models.ImageField(verbose_name='Image', blank=True)
    description = models.TextField(max_length=100, verbose_name='Description')
    type = models.CharField(max_length=20, verbose_name='Type')
    rooms = models.IntegerField(verbose_name='No. of rooms')
    phone = models.CharField(verbose_name='Contact Phone', blank=True, max_length=15)
    email_address = models.EmailField(verbose_name='Email Address', blank=True)

    def __str__(self):
        return f"{self.name} located in {self.location}"


class attraction(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    location = models.CharField(max_length=20, verbose_name='Location')
    fee = models.CharField(max_length=4, verbose_name='Entrance Fee', help_text='Input fee if there is any')
    description = models.TextField(max_length=1000, verbose_name='Description')
    image = models.ImageField(verbose_name='Image', blank=True)

    def __str__(self):
        return f"{self.name} in {self.location}"


class Guide(models.Model):
    firstname = models.CharField(max_length=15, verbose_name='First Name')
    middle_name = models.CharField(max_length=15, verbose_name='Middle Name')
    surname = models.CharField(max_length=15, verbose_name='Surname')
    image = models.ImageField(blank=True, verbose_name='Photo')
    email = models.EmailField(verbose_name='Email Address')
    dob = models.DateField(verbose_name='Date of Birth')
    age = models.IntegerField(verbose_name='Age')
    description = models.CharField(max_length=100, verbose_name='Describe yourself', blank=True)

    def __str__(self):
        return f"{self.middle_name} of {self.age} years old"


class TravelPackages(models.Model):
    attraction = models.ForeignKey(attraction, on_delete=models.CASCADE)
    accommodation = models.ForeignKey(accommodation, on_delete=models.CASCADE)
    package_name = models.CharField(max_length=40, verbose_name='Package Name')
    package_description = models.TextField()
    package_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Price')
    was = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Former Price', blank=True, null=True)

    def __str__(self):
        return f"{self.package_name} is {self.package_price}"
