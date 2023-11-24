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
from django.urls import path

from Karibu_Kilifi.views import addnew, addDestination, addAccommodation, addAttraction, carHire_list, cars, \
    carCheckOut, SampleHome, accommodation_List, accommodate, attraction_List, attract, destination_List, destine, \
    successfulapplication, hireguide, guide_List, guide

urlpatterns = [
                  path('admin/', admin.site.urls),

                  # Car Hire admin
                  path('addnew/', addnew),
                  path('addnew/carsforhirelist/', carHire_list),
                  # Car Hire User
                  path('carhire/', carCheckOut),
                  # duplication path('lolo/', carHire_list),

                  # accommodation admin
                  path('newaccommodation/', addAccommodation),
                  path('newaccommodation/accommodationlist/', accommodation_List),
                  # accommodation users
                  path('accommodate/', accommodate),

                  # attraction sites admin
                  path('newattraction/', addAttraction),
                  path('newattraction/attractionlist/', attraction_List),
                  # attraction users
                  path('attraction/', attract),

                  # Destination admin
                  path('newdestination/', addDestination),
                  path('newdestination/destinationlist/', destination_List),
                  # destination users
                  path('destination/', desticane),

                  # guide
                  path('hiring_guides/', hireguide),
                  path('hiring_guides/applicationsuccess/', successfulapplication),
                  # guide admin use
                  path('guidelist/', guide_List),
                  # guides users
                  path('guides/', guide),

                  path('home/', SampleHome),
                  # Broken Links
                  path('car/<int:id>', cars),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Admin Titles
admin.site.site_header = "Car Hire"