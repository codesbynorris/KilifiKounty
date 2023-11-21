from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from Karibu_Kilifi.models import carHire, destinations, accommodation, attractions


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

    return render(request, 'addnew.html', {'formset': formset})




class newDestination(ModelForm):
    class Meta:
        model = destinations
        fields = ['name', 'description']


def addDestination(request):
    # if request.method == "POST":
    # destinationform = newDestination(request.POST)

    # if destinationform.is_valid():
    # destinationform.save()
    # return HttpResponseRedirect()
    # else:
    destinationform = newDestination()
    return render(request, 'new_destination.html', {'destination': destinationform})


class newAccommodation(ModelForm):
    class Meta:
        model = accommodation
        fields = ['name', 'location', 'price', 'description', 'type', 'rooms']


def addAccommodation(request):
    # if request.method == "POST":
    # accommodationform = newAccommodation(request.POST)

    # if accommodationform.is_valid():
    # accommodationform.save()
    # return HttpResponseRedirect()
    # else:
    accommodationform = newAccommodation()
    return render(request, 'new_accommodation.html', {'accommodation': accommodationform})


class newAttraction(ModelForm):
    class Meta:
        model = attractions
        fields = ['name', 'location', 'fee', 'description']


def addAttraction(request):
    # if request.method == "POST":
    # attractionform = newAttraction(request.POST)

    # if attractionform.is_valid():
    # attractionform.save()
    # return HttpResponseRedirect()
    # else:
    attractionform = newAttraction()
    return render(request, 'new_attraction.html', {'attraction': attractionform})


def cars(request, id):
    carhire_class = carHire.objects.get(pk=id)
    return render(request, "carsforhire.html", {"chire": carhire_class})


def carHire_list(request):
    carhireList = carHire.objects.all()
    return render(request, 'carhire_list.html', {"hire": carhireList})

def carCheckOut(request):
    CheckOut = carHire.objects.all()
    return render(request, 'car_hire.html', {"hire": CheckOut})
