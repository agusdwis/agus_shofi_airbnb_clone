from django import forms

from .models import Dwelling, Reviews, DwellingImages


class DwellingForm(forms.ModelForm):
    class Meta:
        model = Dwelling
        fields = [
            "name",
            "description",
            "address",
            "category_id",
            "city_id",
            "property_type",
            "person_capacity",
            "bedroom_count",
            "bed_count",
            "bath_count",
            "price",
            "publish",
        ]


class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['property_id', 'name', 'comment', 'rating']


class ImagesForm(forms.ModelForm):
    class Meta:
        model = DwellingImages
        fields = ["property_id", "image"]


class NewReview(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['name', 'comment', 'rating']
