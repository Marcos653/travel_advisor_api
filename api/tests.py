from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status
from .models import *
from .serializers import *

client = APIClient()

class TestimonialTest(APITestCase):

    def setUp(self):
        self.testimonial1 = Testimonial.objects.create(
            testimonial="Testimonial 1",
            person_name="Person 1"
        )
        self.testimonial2 = Testimonial.objects.create(
            testimonial="Testimonial 2",
            person_name="Person 2"
        )

    def test_get_all_testimonials(self):
        response = client.get(reverse('testimonial-list'))
        expected = Testimonial.objects.all()
        serialized = TestimonialSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_testimonial(self):
        data = {
            "testimonial": "Testimonial 3",
            "person_name": "Person 3"
        }
        response = client.post(
            reverse('testimonial-list'),
            data=data,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_testimonial(self):
        new_data = {
            "testimonial": "Testimonial 1 updated",
            "person_name": "Person 1 updated"
        }
        response = client.put(
            reverse('testimonial-detail', kwargs={'pk': self.testimonial1.pk}),
            data=new_data,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_testimonial(self):
        response = client.delete(
            reverse('testimonial-detail', kwargs={'pk': self.testimonial2.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class DestinationTest(APITestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.destination1 = Destination.objects.create(name="Destination 1", price=100)
        self.destination2 = Destination.objects.create(name="Destination 2", price=200)

    def test_get_all_destinations(self):
        response = self.client.get(reverse('destination-list'))
        destinations = Destination.objects.all()
        serializer = DestinationSerializer(destinations, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_destination(self):
        data = {"name": "Destination 3", "price": 300}
        response = self.client.post(reverse('destination-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_destination(self):
        new_data = {"name": "Updated Destination", "price": 150}
        response = self.client.put(reverse('destination-detail', kwargs={'pk': self.destination1.pk}), data=new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_destination(self):
        response = self.client.delete(reverse('destination-detail', kwargs={'pk': self.destination2.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        