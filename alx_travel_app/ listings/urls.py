from django.urls import path, include
from rest_framework import routers
from . import views

# Create a router and register our viewsets
router = routers.DefaultRouter()
router.register(r'listings', views.ListingViewSet)
router.register(r'bookings', views.BookingViewSet)

# The API URLs are now determined automatically by the router
urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
