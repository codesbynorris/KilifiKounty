from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.mail import send_mail
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from Karibu_Kilifi.models import carHire, destination, accommodation, attraction, Guide, TravelPackages


# Create your views here.
class hireForm(ModelForm):
    class Meta:
        model = carHire
        fields = ['make', 'model', 'plate', 'seater', 'price', 'image', 'description']


def addnew(request):
    if request.method == "POST":
        formset = hireForm(request.POST, request.FILES)

        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect('carsforhirelist/')
    else:
        formset = hireForm()

    return render(request, 'Car Hire/Admin/newcar.html', {'formset': formset})


class newDestination(ModelForm):
    class Meta:
        model = destination
        fields = ['name', 'description', 'image', 'link']


def addDestination(request):
    if request.method == "POST":
        destinationform = newDestination(request.POST)

        if destinationform.is_valid():
            destinationform.save()
            return HttpResponseRedirect('destinationlist/')
    else:
        destinationform = newDestination()

    return render(request, 'Destinations/Admin/new_destination.html', {'destination': destinationform})


class newAccommodation(ModelForm):
    class Meta:
        model = accommodation
        fields = ['name', 'location', 'price', 'description', 'type', 'rooms', 'image', 'phone', 'email_address']


def addAccommodation(request):
    accommodationform = newAccommodation()
    if request.method == "POST":
        accommodationform = newAccommodation(request.POST, request.FILES)

        if accommodationform.is_valid():
            accommodationform.save()
            return HttpResponseRedirect('accommodationlist/')
        else:
            accommodationform = newAccommodation()
    return render(request, 'Accommodations/Admin/new_accommodation.html', {'accommodation': accommodationform})


class newAttraction(ModelForm):
    class Meta:
        model = attraction
        fields = ['name', 'location', 'fee', 'description', 'image']


def addAttraction(request):
    if request.method == "POST":
        attractionform = newAttraction(request.POST)

        if attractionform.is_valid():
            attractionform.save()
            return HttpResponseRedirect('attractionlist/')
    else:
        attractionform = newAttraction()
    return render(request, 'Attractions/Admin/new_attraction.html', {'attraction': attractionform})


def cars(request, id):
    carhire_class = carHire.objects.get(pk=id)
    return render(request, "", {"chire": carhire_class})


def carHire_list(request):
    carhireList = carHire.objects.all()
    return render(request, 'Car Hire/Admin/carhire_list.html', {"hire": carhireList})


def carCheckOut(request):
    CheckOut = carHire.objects.all()
    return render(request, 'Car Hire/User/car_hire.html', {"hire": CheckOut})

def CarInfo(request):
    return render(request, 'Car Hire/User/carhire_login.html')


def SampleHome(request):
    return render(request, 'homesample.html')

def homepage(request):
    return render(request, 'home2.html')


def accommodations(request, id):
    accommodation_class = accommodation.objects.all()
    return render(request, '', {"accommodate": accommodation_class})


def accommodation_List(request):
    accommodationList = accommodation.objects.all()
    return render(request, 'Accommodations/Admin/accommodationlist.html', {"accommodation": accommodationList})


def accommodate(request):
    CheckIn = accommodation.objects.all()
    return render(request, 'Accommodations/User/accommodation_users.html', {"accommodateme": CheckIn})


def attractions(request, id):
    attraction_class = attraction.objects.all()
    return render(request, '', {"attract": attraction_class})


def attraction_List(request):
    attractionList = attraction.objects.all()
    return render(request, 'Attractions/Admin/attractionslist.html', {"attract": attractionList})


def attract(request):
    Visit = attraction.objects.all()
    return render(request, 'Attractions/User/attraction_users.html', {"attractme": Visit})


def destinations(request, id):
    destination_class = destination.objects.all()
    return render(request, '', {"destine": destination_class})


def destination_List(request):
    destinationList = destination.objects.all()
    return render(request, 'Destinations/Admin/destinationslist.html', {"destiny": destinationList})


def destine(request):
    Destine = destination.objects.all()
    return render(request, 'Destinations/User/destination_users.html', {"destinationme": Destine})


class NewGuideForm(ModelForm):
    class Meta:
        model = Guide
        fields = ['firstname', 'middle_name', 'surname', 'image', 'email', 'dob', 'age', 'description']


def hireguide(request):
    if request.method == "POST":
        GuideForm = NewGuideForm(request.POST, request.FILES)

        if GuideForm.is_valid():
            GuideForm.save()
            return HttpResponseRedirect('applicationsuccess/')
    else:
        GuideForm = NewGuideForm()

    return render(request, 'Guides/admin/newguide.html', {'hireguide': GuideForm})


def successfulapplication(request):
    return render(request, 'Guides/admin/application/successfulapplication.html')


def guides(request, id):
    guides_class = Guide.objects.all()
    return render(request, '', {"guide": guides_class})


def guide_List(request):
    guideList = Guide.objects.all()
    return render(request, 'Guides/admin/guidelist.html', {"guidance": guideList})


def guide(request):
    TakeMe = Guide.objects.all()
    return render(request, 'Guides/User/guides.html', {"guideme": TakeMe})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {"form": form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {"form": form})


def handle_form_submission(request):
    if request.method == 'POST':
        email_address = request.POST['email_address']

        # Send email to the user using their provided email address
        send_mail(
            'Thank you for your interest in becoming a tour guide!',
            'We have received your application and will review it shortly.',
            'codesbynorris@gmail.com',
            [email_address],
            fail_silently=False
        )

    return render(request, '')


def travel_packages(request):
    travel_packages = TravelPackages.objects.all()
    return render(request, 'home2.html', {'travel_packages': travel_packages})



