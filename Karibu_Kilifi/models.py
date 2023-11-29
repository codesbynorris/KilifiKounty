from datetime import date

from django import forms
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
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
    dob = models.DateField(verbose_name='Date of Birth', blank=True, null=True)
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


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    is_admin = forms.BooleanField(required=False, label='Admin')


class SignupForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    is_admin = forms.BooleanField(required=False, label='Admin')


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, name, phone_number, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            name=name,
            phone_number=phone_number,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, name, phone_number, password):
        user = self.create_user(
            email=email,
            username=username,
            name=name,
            phone_number=phone_number,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name', 'phone_number']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
