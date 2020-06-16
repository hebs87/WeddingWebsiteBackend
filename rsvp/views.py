from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import RSVP
from .serializers import RSVPSerializer


# Create your views here.
class RSVPViewSet(viewsets.ModelViewSet):
    queryset = RSVP.objects.all()
    serializer_class = RSVPSerializer
