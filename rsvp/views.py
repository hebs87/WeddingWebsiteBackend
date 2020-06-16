from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import RSVP, HomeCarousel
from .serializers import RSVPSerializer, HomeCarouselSerializer


# Create your views here.
class RSVPViewSet(viewsets.ModelViewSet):
    queryset = RSVP.objects.all()
    serializer_class = RSVPSerializer


class HomeCarouselViewSet(viewsets.ModelViewSet):
    queryset = HomeCarousel.objects.all()
    serializer_class = HomeCarouselSerializer
