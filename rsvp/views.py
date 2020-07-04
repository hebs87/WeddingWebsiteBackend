from django.shortcuts import render
from rest_framework import viewsets
from .models import RSVP, HomeCarousel, VillaCarousel
from .serializers import RSVPSerializer, HomeCarouselSerializer, VillaCarouselSerializer


# Create your views here.
class RSVPViewSet(viewsets.ModelViewSet):
    queryset = RSVP.objects.all()
    serializer_class = RSVPSerializer


class HomeCarouselViewSet(viewsets.ModelViewSet):
    queryset = HomeCarousel.objects.all()
    serializer_class = HomeCarouselSerializer


class VillaCarouselViewSet(viewsets.ModelViewSet):
    queryset = VillaCarousel.objects.all()
    serializer_class = VillaCarouselSerializer


def home(request):
    """
    Renders home page
    """
    details = RSVP.objects.all()

    context = {
        'details': details
    }

    return render(request, 'index.html', context)
