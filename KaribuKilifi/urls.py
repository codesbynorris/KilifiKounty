"""
URL configuration for KaribuKilifi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Karibu_Kilifi import views
from Karibu_Kilifi.views import addnew, addDestination, addAccommodation, addAttraction, carHire_list, cars, \
    carCheckOut, SampleHome, accommodation_List, accommodate, attraction_List, attract, destination_List, destine, \
    successfulapplication, hireguide, guide_List, guider, signup_view, login_view, travel_packages, homepage, CarInfo, \
    login_status, logout_view, search_cars, carcheckout, attractioncheckout, accommodationreservation, \
    Package_Reservation, car_count, update_guide, save_guide_changes, delete_guide, stk_push_callback

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('admin_site/', login_status,  name='admin'),

                  # SignUp & Login
                  # path('Karibu_Kilifi/', include(Karibu_Kilifi.urls)),
                  path('signup/', signup_view, name='signup'),
                  path('login/', login_view, name='login'),
                  path('logout/', logout_view, name='logout'),
                  path('accounts/', include('django.contrib.auth.urls')),

                  # Car Hire admin
                  path('addnew/', addnew, name='Hire'),
                  path('addnew/carsforhirelist/', carHire_list),
                  # Car Hire User
                  path('carinfo/', CarInfo,),
                  path('carhire/', carCheckOut, name='CarHire'),
                  path('carhire_checkout', carcheckout, name='CarCheckOut'),

                  # accommodation admin
                  path('newaccommodation/', addAccommodation, name='Accommodate'),
                  path('newaccommodation/accommodationlist/', accommodation_List),
                  # accommodation users
                  path('accommodate/', accommodate, name='Accommodation'),
                  path('accommodationreservation/', accommodationreservation, name='AccommodationReservation'),

                  # attraction sites admin
                  path('newattraction/', addAttraction, name='NewAttraction'),
                  path('newattraction/attractionlist/', attraction_List),
                  # attraction users
                  path('attraction/', attract, name='Attraction'),
                  path('attractionreservation/', attractioncheckout, name='AttractionReservation'),

                  # Destination admin
                  path('newdestination/', addDestination, name='NewDestination'),
                  path('newdestination/destinationlist/', destination_List),
                  # destination users
                  path('destination/', destine, name='Destination'),

                  # guide
                  path('hiring_guides/', hireguide),
                  path('hiring_guides/applicationsuccess/', successfulapplication),
                  # guide admin use
                  path('guidelist/', guide_List, name='Guide_List'),
                  # guides users
                  path('guides/', guider),

                  path('home/', SampleHome, name='normal'),
                  # path('home2/', homepage, name='homepage'),
                  # Broken Links
                  path('car/<int:id>', cars),
                  path('test/', travel_packages, name='home'),
                  path('packagereservation/', Package_Reservation, name='PackageReservation'),

                  # path('search/', search_cars, name='search'),
                  path('admin_site/car_count/', car_count, name='Total_Cars'),
                  path('update_guide/<int:guide_id>/', update_guide, name='update_guide'),
                  path('save_guide_changes/<int:guide_id>/', save_guide_changes, name='save_guide_changes'),
                  path('delete_guide/<int:guide_id>/', delete_guide, name='delete_guide'),
                  path('daraja/stk-push', stk_push_callback, name='mpesa_stk_push_callback'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Admin Titles
admin.site.site_header = "Car Hire"
