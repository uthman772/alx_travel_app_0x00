from rest_framework import serializers
from .models import Listing, Booking

class ListingSerializer(serializers.ModelSerializer):
    """Serializer for Listing model"""
    owner_username = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Listing
        fields = [
            'id', 'title', 'description', 'price_per_night', 
            'location', 'bedrooms', 'bathrooms', 'max_guests',
            'amenities', 'is_available', 'created_at', 'updated_at',
            'owner', 'owner_username'
        ]
        read_only_fields = ['owner', 'created_at', 'updated_at']

class BookingSerializer(serializers.ModelSerializer):
    """Serializer for Booking model"""
    user_username = serializers.ReadOnlyField(source='user.username')
    listing_title = serializers.ReadOnlyField(source='listing.title')
    
    class Meta:
        model = Booking
        fields = [
            'id', 'listing', 'listing_title', 'user', 'user_username',
            'check_in', 'check_out', 'total_price', 'guests',
            'status', 'created_at', 'updated_at'
        ]
        read_only_fields = ['user', 'total_price', 'created_at', 'updated_at']
    
    def validate(self, data):
        """
        Validate booking dates and availability
        """
        if data['check_in'] >= data['check_out']:
            raise serializers.ValidationError("Check-out date must be after check-in date")
        
        # Check if listing is available for the selected dates
        listing = data['listing']
        conflicting_bookings = Booking.objects.filter(
            listing=listing,
            status__in=['confirmed', 'pending'],
            check_in__lt=data['check_out'],
            check_out__gt=data['check_in']
        ).exclude(id=self.instance.id if self.instance else None)
        
        if conflicting_bookings.exists():
            raise serializers.ValidationError("Listing is not available for the selected dates")
        
        return data
    
    def create(self, validated_data):
        # Calculate total price
        listing = validated_data['listing']
        days = (validated_data['check_out'] - validated_data['check_in']).days
        validated_data['total_price'] = listing.price_per_night * days
        
        return super().create(validated_data)
