from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('rsvp', views.RSVPViewSet)
router.register('home-carousel', views.HomeCarouselViewSet)
router.register('villa-carousel', views.VillaCarouselViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
