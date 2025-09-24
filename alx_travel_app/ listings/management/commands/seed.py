import os
import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing, Booking, Review
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Seed the database with sample data for listings, bookings, and reviews'
    
    def handle(self, *args, **options):
        self.stdout.write('Seeding database...')
        
        # Create sample users if they don't exist
        hosts = []
        guests = []
        
        host_data = [
            {'username': 'john_host', 'email': 'john@example.com', 'first_name': 'John', 'last_name': 'Smith'},
            {'username': 'sarah_host', 'email': 'sarah@example.com', 'first_name': 'Sarah', 'last_name': 'Johnson'},
            {'username': 'mike_host', 'email': 'mike@example.com', 'first_name': 'Mike', 'last_name': 'Brown'},
        ]
        
        guest_data = [
            {'username': 'alice_traveler', 'email': 'alice@example.com', 'first_name': 'Alice', 'last_name': 'Williams'},
            {'username': 'bob_traveler', 'email': 'bob@example.com', 'first_name': 'Bob', 'last_name': 'Davis'},
            {'username': 'carol_traveler', 'email': 'carol@example.com', 'first_name': 'Carol', 'last_name': 'Miller'},
        ]
        
        for user_info in host_data:
            user, created = User.objects.get_or_create(
                username=user_info['username'],
                defaults=user_info
            )
            if created:
                user.set_password('password123')
                user.save()
            hosts.append(user)
            self.stdout.write(f'Created host: {user.username}')
        
        for user_info in guest_data:
            user, created = User.objects.get_or_create(
                username=user_info['username'],
                defaults=user_info
            )
            if created:
                user.set_password('password123')
                user.save()
            guests.append(user)
            self.stdout.write(f'Created guest: {user.username}')
        
        # Create sample listings
        listings_data = [
            {
                'title': 'Cozy Apartment in Downtown',
                'description': 'A beautiful apartment in the heart of the city with amazing views.',
                'address': '123 Main Street',
                'city': 'New York',
                'country': 'USA',
                'price_per_night': 120.00,
                'property_type': 'apartment',
                'num_bedrooms': 2,
                'num_bathrooms': 1,
                'max_guests': 4,
                'amenities': 'WiFi, Kitchen, Air Conditioning, TV, Heating',
                'host': hosts[0],
            },
            {
                'title': 'Luxury Villa with Pool',
                'description': 'Stunning villa with private pool and garden. Perfect for families.',
                'address': '456 Beach Road',
                'city': 'Miami',
                'country': 'USA',
                'price_per_night': 350.00,
                'property_type': 'villa',
                'num_bedrooms': 4,
                'num_bathrooms': 3,
                'max_guests': 8,
                'amenities': 'Pool, WiFi, Kitchen, Air Conditioning, TV, Garden, Parking',
                'host': hosts[1],
            },
            {
                'title': 'Mountain Cabin Retreat',
                'description': 'Peaceful cabin surrounded by nature. Ideal for hiking enthusiasts.',
                'address': '789 Mountain View',
                'city': 'Denver',
                'country': 'USA',
                'price_per_night': 95.00,
                'property_type': 'cabin',
                'num_bedrooms': 1,
                'num_bathrooms': 1,
                'max_guests': 2,
                'amenities': 'Fireplace, WiFi, Kitchen, Heating, Mountain View',
                'host': hosts[2],
            },
            {
                'title': 'Modern Studio near City Center',
                'description': 'Compact and modern studio apartment with all necessary amenities.',
                'address': '321 Urban Avenue',
                'city': 'San Francisco',
                'country': 'USA',
                'price_per_night': 85.00,
                'property_type': 'studio',
                'num_bedrooms': 1,
                'num_bathrooms': 1,
                'max_guests': 2,
                'amenities': 'WiFi, Kitchenette, Air Conditioning, TV, Laundry',
                'host': hosts[0],
            },
            {
                'title': 'Spacious Family House',
                'description': 'Large family house with backyard and play area for children.',
                'address': '654 Suburban Lane',
                'city': 'Chicago',
                'country': 'USA',
                'price_per_night': 200.00,
                'property_type': 'house',
                'num_bedrooms': 3,
                'num_bathrooms': 2,
                'max_guests': 6,
                'amenities': 'Garden, WiFi, Kitchen, Air Conditioning, TV, Parking, Play Area',
                'host': hosts[1],
            }
        ]
        
        listings = []
        for listing_data in listings_data:
            listing, created = Listing.objects.get_or_create(
                title=listing_data['title'],
                city=listing_data['city'],
                defaults=listing_data
            )
            listings.append(listing)
            self.stdout.write(f'Created listing: {listing.title}')
        
        # Create sample bookings
        bookings = []
        status_choices = ['confirmed', 'completed', 'pending']
        
        for i in range(10):
            listing = random.choice(listings)
            guest = random.choice(guests)
            
            # Generate random dates
            days_in_future = random.randint(1, 60)
            check_in = datetime.now().date() + timedelta(days=days_in_future)
            stay_duration = random.randint(2, 7)
            check_out = check_in + timedelta(days=stay_duration)
            
            total_price = listing.price_per_night * stay_duration
            
            booking = Booking.objects.create(
                listing=listing,
                guest=guest,
                check_in_date=check_in,
                check_out_date=check_out,
                total_price=total_price,
                status=random.choice(status_choices),
                num_guests=random.randint(1, listing.max_guests),
                special_requests=random.choice([
                    '', 
                    'Early check-in requested', 
                    'Traveling with a pet', 
                    'Special occasion celebration'
                ])
            )
            bookings.append(booking)
            self.stdout.write(f'Created booking for {listing.title} by {guest.username}')
        
        # Create sample reviews for completed bookings
        for booking in bookings:
            if booking.status == 'completed' and random.choice([True, False]):
                review = Review.objects.create(
                    listing=booking.listing,
                    guest=booking.guest,
                    booking=booking,
                    rating=random.randint(3, 5),
                    comment=random.choice([
                        'Great stay! Would definitely recommend.',
                        'Nice place, exactly as described.',
                        'Wonderful experience, host was very helpful.',
                        'Comfortable and clean, had everything we needed.',
                        'Perfect location and great amenities.'
                    ])
                )
                self.stdout.write(f'Created review for booking #{booking.id}')
        
        self.stdout.write(
            self.style.SUCCESS('Successfully seeded database with sample data!')
        )
        self.stdout.write(f'Created: {len(hosts) + len(guests)} users, {len(listings)} listings, {len(bookings)} bookings')