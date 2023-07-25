from django.shortcuts import get_list_or_404
from rest_framework import viewsets, status
from .models import Testimonial
from .serializers import *
import random
from rest_framework.response import Response

class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

    def get_queryset(self):

        if 'home' in self.request.path:
            testimonials = list(Testimonial.objects.all())
            random_testimonials = random.sample(testimonials, min(len(testimonials), 3))

            return random_testimonials

        return super().get_queryset()

class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    
    def get_queryset(self):
        queryset = Destination.objects.all()
        name = self.request.query_params.get('name', None)

        if name is not None:
            queryset = queryset.filter(name__icontains=name)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        if not queryset:
            return Response({"message": "No destination was found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
