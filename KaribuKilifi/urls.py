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

from Karibu_Kilifi.views import addnew, addDestination, addAccommodation, addAttraction, carHire_list, cars, carCheckOut

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('addnew/', addnew),
                  path('newdestination/', addDestination),
                  path('newaccommodation/', addAccommodation),
                  path('newattraction/', addAttraction),
                  path('car/<int:id>', cars),
                  path('addnew/carsforhirelist/', carHire_list),
                  path('lolo/', carHire_list),
                  path('carhire/', carCheckOut)
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Admin Titles
admin.site.site_header = "Car Hire"
