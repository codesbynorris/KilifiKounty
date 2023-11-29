from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.dispatch import receiver
from django.forms import ModelForm
from django.http import HttpResponseRedirect, HttpResponse
from django_daraja.mpesa.core import MpesaClient


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout, user_logged_in
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

from Karibu_Kilifi.models import carHire, destination, accommodation, attraction, Guide, TravelPackages, LoginForm, \
    SignupForm, Notification, SubscriptionForm, Subscriber


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


def guider(request):
    TakeMe = Guide.objects.all()
    return render(request, 'Guides/User/guides.html', {"guideme": TakeMe})


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            is_admin = form.cleaned_data['is_admin']

            if User.objects.filter(username=username).exists():
                # Handle case when the username is already taken
                error_message = 'Username already exists. Please choose a different username.'
                return render(request, 'signup.html', {'form': form, 'error_message': error_message})

            # Create a new user account
            user = User.objects.create_user(username=username, password=password)

            # Set user as admin based on checkbox value
            if is_admin:
                user.is_staff = False
                user.is_superuser = True
                user.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


@csrf_protect
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            is_admin = form.cleaned_data['is_admin']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                if is_admin:
                    return redirect('admin')
                else:
                    return redirect('homepage')
            else:
                form.add_error(None, "Invalid username or password.")  # Add form-level error

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def travel_packages(request):
    travel_packages = TravelPackages.objects.all()
    return render(request, 'home2.html', {'travel_packages': travel_packages})


def login_status(request):
    if request.user.is_authenticated:
        logged_in_user = request.user
    else:
        logged_in_user = None

    return render(request, 'Admin.html', {'logged_in_user': logged_in_user})


def logout_view(request):
    logout(request)
    return redirect('normal')


def search_cars(request):
    search_query = request.GET.get('search_query')
    results = None

    if search_query:
        results = (carHire.objects.filter(make__icontains=search_query) |
                   carHire.objects.filter(model__icontains=search_query))
        # You can add more filters or refine the search query based on your needs

    hire = carHire.objects.all()  # Retrieve all cars for initial display

    return render(request, 'Car Hire/User/car_hire.html', {'results': results, 'hire': hire})


def reservation_form(request):
    tour_guides = Guide.objects.all()

    context = {
        'tour_guides': tour_guides
    }
    return render(request, 'Attractions/User/reservation.html', context)


def create_notification(user, message):
    Notification.objects.create(user=user, message=message)


@receiver(user_logged_in)
def user_logged_in_handler(sender, user, request, **kwargs):
    message = "Welcome back! You've logged in."
    create_notification(user, message)


def get_notifications(request):
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(user=request.user, is_read=False)
        return render(request, 'notifications.html', {'notifications': notifications})
    else:
        return render(request, 'notifications.html', {'notifications': []})


def carcheckout(request):
    return render(request, 'Car Hire/User/checkout.html')


def attractioncheckout(request):
    return render(request, 'Attractions/User/reservation.html')


def accommodationreservation(request):
    return render(request, 'Accommodations/User/reservation.html')


def Package_Reservation(request):
    return render(request, 'packagereservation.html')


def car_count(request):
    total_cars = carHire.objects.count()
    print("Total Cars Count:", total_cars)
    return render(request, 'Admin.html', {'total_cars': total_cars})


def ad_site_view(request):
    total_cars = carHire.objects.count()
    return render(request, 'Admin.html', {'total_cars': total_cars})


def update_guide(request, guide_id):
    guide = get_object_or_404(Guide, id=guide_id)
    return render(request, 'update_guide.html', {'guide': guide})


def save_guide_changes(request, guide_id):
    guide = get_object_or_404(Guide, id=guide_id)

    if request.method == 'POST':
        guide.firstname = request.POST.get('firstname')
        guide.middle_name = request.POST.get('middle_name')
        guide.surname = request.POST.get('surname')
        guide.age = request.POST.get('age')
        guide.dob = request.POST.get('dob')

        if 'image' in request.FILES:
            guide.image = request.FILES['image']

        # Save the updated guide data
        guide.save()

        # Redirect to guide list or any other appropriate page after saving changes
        return HttpResponseRedirect('/guidelist/')  # Replace '/guide_list/' with your actual URL

    return render(request, 'update_guide.html', {'guide': guide})  # Render the same page if not POST request


def delete_guide(request, guide_id):
    guide = get_object_or_404(Guide, id=guide_id)
    if request.method == 'POST':
        guide.delete()
        messages.success(request, 'Guide deleted successfully')
    return redirect('guidelist/')


def index(request):
    cl = MpesaClient()
    # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
    phone_number = '0723452067'
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = 'https://darajambili.herokuapp.com/express-payment';
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)


def stk_push_callback(request):
    data = request.body

    return HttpResponse("STK Push in Django👋")