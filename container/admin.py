from django.contrib import admin
from .models import Dwelling, DwellingImages, Categories, Reviews, Cities, Amenities, PropertyTypes

# Register your models here.
admin.site.register(Dwelling)
admin.site.register(DwellingImages)
admin.site.register(Categories)
admin.site.register(Reviews)
admin.site.register(Cities)
admin.site.register(Amenities)
admin.site.register(PropertyTypes)
