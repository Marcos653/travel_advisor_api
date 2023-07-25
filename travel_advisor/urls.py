from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import *

router = DefaultRouter()
router.register(r'testimonials', TestimonialViewSet, basename='testimonial')
router.register(r'testimonials-home', TestimonialViewSet, basename='testimonial-home')
router.register(r'destinations', DestinationViewSet, basename='destination')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
