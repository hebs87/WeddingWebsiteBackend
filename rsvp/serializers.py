from rest_framework import serializers
from .models import RSVP, HomeCarousel


class RSVPSerializer(serializers.ModelSerializer):
    """
    Serializes the Detail model data and returns as JSON
    """
    class Meta:
        model = RSVP
        fields = ('id', 'guest_name', 'attending', 'not_attending', 'favourite_song',
                  'favourite_drink', 'dietary_requirements', 'additional_info')


class HomeCarouselSerializer(serializers.ModelSerializer):
    """
    Serializes the HomeCarousel image url and returns as JSON
    """
    class Meta:
        model = HomeCarousel
        fields = ('id', 'image_url')
