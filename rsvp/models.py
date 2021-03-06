from django.db import models


# Create your models here.
# TODO: Add guest list model and have guest_name field in Detail model as FK?
class RSVP(models.Model):
    """
    Allows users to submit their details
    """
    guest_name = models.CharField(max_length=27, blank=False, null=True)
    attending = models.CharField(max_length=19, blank=False, null=True)
    not_attending = models.CharField(max_length=100, blank=False, null=True)
    favourite_song = models.CharField(max_length=100, blank=False, null=True)
    favourite_drink = models.CharField(max_length=100, blank=False, null=True)
    dietary_requirements = models.CharField(max_length=100, blank=False, null=True)
    additional_info = models.TextField(max_length=2000, blank=False, null=True)

    class Meta:
        verbose_name = 'RSVP'
        verbose_name_plural = 'RSVPs'

    def __str__(self):
        return "{0} - {1}, {2} can't make it".format(
            self.guest_name, self.attending, self.not_attending)


class HomeCarousel(models.Model):
    """
    Stores the image URLs for the homepage carousel
    """
    image = models.ImageField(upload_to='carousel/home/')

    class Meta:
        verbose_name = 'Home Carousel Image'
        verbose_name_plural = 'Home Carousel Images'


class VillaCarousel(models.Model):
    """
    Stores the image URLs for the homepage carousel
    """
    image = models.ImageField(upload_to='carousel/villa/')

    class Meta:
        verbose_name = 'Villa Carousel Image'
        verbose_name_plural = 'Villa Carousel Images'
