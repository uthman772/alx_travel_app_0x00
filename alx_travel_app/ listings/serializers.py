from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Listing, Booking, Review

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class ReviewSerializer(serializers.ModelSerializer):
    guest_username = serializers.CharField(source='guest.username', read_only=True)
    
    class Meta:
        model = Review
        fields = ['id', 'guest', 'guest_username', 'booking', 'rating', 'comment', 'created_at']
        read_only_fields = ['guest', 'booking']

class ListingSerializer(serializers.ModelSerializer):
    host_info = UserSerializer(source='host', read_only=True)
    average_rating = serializers.SerializerMethodField()
    total_reviews = serializers.SerializerMethodField()
    
    class Meta:
        model = Listing
        fields = [
            'id', 'title', 'description', 'address', 'city', 'country',
            'price_per_night', 'property_type', 'num_bedrooms', 'num_bathrooms',
            'max_guests', 'amenities', 'host', 'host_info', 'is_available',
            'average_rating', 'total_reviews', 'created_at', 'updated_at'
        ]
        read_only_fields = ['host', 'created_at', 'updated_at']
    
    def get_average_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews:
            return sum(review.rating for review in reviews) / len(reviews)
        return 0
    
    def get_total_reviews(self, obj):
        return obj.reviews.count()

class BookingSerializer(serializers.ModelSerializer):
    listing_title = serializers.CharField(source='listing.title', read_only=True)
    guest_info = UserSerializer(source='guest', read_only=True)
    
    class Meta:
        model = Booking
        fields = [
            'id', 'listing', 'listing_title', 'guest', 'guest_info', 
            'check_in_date', 'check_out_date', 'total_price', 'status',
            'num_guests', 'special_requests', 'created_at', 'updated_at'
        ]
        read_only_fields = ['guest', 'total_price', 'created_at', 'updated_at']
    
    def validate(self, data):
        if data['check_in_date'] >= data['check_out_date']:
            raise serializers.ValidationError("Check-out date must be after check-in date")
        return data