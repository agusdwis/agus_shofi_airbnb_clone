from django.db import models
from django.urls import reverse

# Create your models here.


class Categories(models.Model):  # done
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=4000)
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    status = models.SmallIntegerField(default=1)

    def __str__(self):
        return f'{self.name}'


class Cities(models.Model):  # done
    name = models.CharField(max_length=300)
    status = models.SmallIntegerField(default=1)

    def __str__(self):
        return f'{self.name}'


class PropertyTypes(models.Model):
    name = models.CharField(max_length=100)
    status = models.SmallIntegerField(default=1)

    def __str__(self):
        return f"{self.name}"


class Dwelling(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=4000)
    address = models.TextField(max_length=4000)
    category_id = models.ForeignKey(
        Categories, on_delete=models.CASCADE, related_name='category')
    city_id = models.ForeignKey(
        Cities, on_delete=models.CASCADE, related_name='city')
    property_type = models.ForeignKey(
        PropertyTypes, default=1, on_delete=models.CASCADE, related_name='property_type')
    rating = models.IntegerField(default=5)
    person_capacity = models.IntegerField(default=1)
    bedroom_count = models.IntegerField(default=1)
    bed_count = models.IntegerField(default=1)
    bath_count = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    status = models.SmallIntegerField(default=1)

    def __str__(self):
        return f'{self.name}'

    def get_absolut_url(self):
        return reverse("rooms:detail_room", kwargs={'id': self.id})


def upload_location(instance, filename):
    return "%s/%s" % (instance.property_id, filename)


class DwellingImages(models.Model):
    property_id = models.ForeignKey(
        Dwelling, on_delete=models.CASCADE, related_name='property_images')
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    status = models.SmallIntegerField(default=1)

    def __str__(self):
        return f'{self.property_id}'


class Amenities(models.Model):
    name = models.CharField(max_length=100)
    property_id = models.ForeignKey(
        Dwelling, default=1, on_delete=models.CASCADE, related_name='property_amenities')
    status = models.SmallIntegerField(default=1)

    def __str__(self):
        return f"{self.name}"


class Reviews(models.Model):
    property_id = models.ForeignKey(
        Dwelling, on_delete=models.CASCADE, related_name="property_reviews", default=1)
    name = models.CharField(max_length=80)
    comment = models.TextField(max_length=4000)
    rating = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'Review by {self.name}'
