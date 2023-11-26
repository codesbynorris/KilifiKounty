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

import Karibu_Kilifi
from Karibu_Kilifi import urls
from Karibu_Kilifi.views import addnew, addDestination, addAccommodation, addAttraction, carHire_list, cars, \
    carCheckOut, SampleHome, accommodation_List, accommodate, attraction_List, attract, destination_List, destine, \
    successfulapplication, hireguide, guide_List, guide, signup, login_view, travel_packages, homepage, CarInfo

urlpatterns = [
                  path('admin/', admin.site.urls),

                  # SignUp & Login
                  # path('Karibu_Kilifi/', include(Karibu_Kilifi.urls)),
                  path('signup/', signup, name='signup'),
                  path('login/', login_view, name='login'),

                  # Car Hire admin
                  path('addnew/', addnew),
                  path('addnew/carsforhirelist/', carHire_list),
                  # Car Hire User
                  path('carinfo/', CarInfo,),
                  path('carhire/', carCheckOut, name='CarHire'),
                  # duplication path('lolo/', carHire_list),

                  # accommodation admin
                  path('newaccommodation/', addAccommodation),
                  path('newaccommodation/accommodationlist/', accommodation_List),
                  # accommodation users
                  path('accommodate/', accommodate, name='Accommodation'),

                  # attraction sites admin
                  path('newattraction/', addAttraction),
                  path('newattraction/attractionlist/', attraction_List),
                  # attraction users
                  path('attraction/', attract, name='Attraction'),

                  # Destination admin
                  path('newdestination/', addDestination),
                  path('newdestination/destinationlist/', destination_List),
                  # destination users
                  path('destination/', destine, name='Destination'),

                  # guide
                  path('hiring_guides/', hireguide),
                  path('hiring_guides/applicationsuccess/', successfulapplication),
                  # guide admin use
                  path('guidelist/', guide_List),
                  # guides users
                  path('guides/', guide),

                  path('home/', SampleHome),
                  # path('home2/', homepage, name='homepage'),
                  # Broken Links
                  path('car/<int:id>', cars),
                  path('test/', travel_packages, name='homepage'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Admin Titles
admin.site.site_header = "Car Hire"
