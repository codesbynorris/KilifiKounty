from django.contrib import admin

from Karibu_Kilifi.models import carHire, destination, accommodation, attraction, Guide, TravelPackages

# Register your models here.
admin.site.register(carHire)
admin.site.register(destination)
admin.site.register(accommodation)
admin.site.register(attraction)
admin.site.register(Guide)
admin.site.register(TravelPackages)
