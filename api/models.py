from django.db import models

class Testimonial(models.Model):
    image = models.ImageField(upload_to='media', blank=True)
    testimonial = models.TextField(blank=True)
    person_name = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.person_name

class Destination(models.Model):
    photo = models.ImageField(upload_to='media', blank=True)
    name = models.CharField(max_length=255, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)

    def __str__(self):
        return self.name
