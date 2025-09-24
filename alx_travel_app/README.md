# ALX Travel App - Milestone 2

This project implements the backend components for a travel booking platform using Django and Django REST Framework.

## Features

- **Database Models**: Listing, Booking, and Review models with proper relationships
- **Serializers**: Convert model instances to JSON for API responses
- **Seed Command**: Populate database with sample data for development and testing

## Models

### Listing
- Represents properties available for booking
- Includes details like title, description, location, pricing, and amenities
- ForeignKey relationship with User (host)

### Booking
- Represents reservations made by guests
- ForeignKey relationships with Listing and User (guest)
- Includes booking dates, status, and pricing information

### Review
- Represents guest reviews for listings
- ForeignKey relationships with Listing and User (guest)
- OneToOne relationship with Booking

## Setup Instructions

1. Clone the repository and navigate to the project directory
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Seed the database: `python manage.py seed`
7. Start the development server: `python manage.py runserver`

## Seeding the Database

To populate the database with sample data:

```bash
python manage.py seed