# ALX Travel App - Milestone 3

This project implements CRUD API endpoints for managing property listings and bookings using Django REST Framework.

## Features

- **Listings API**: Full CRUD operations for property listings
- **Bookings API**: Full CRUD operations for bookings
- **Swagger Documentation**: Interactive API documentation
- **Authentication**: User-based permissions and ownership

## API Endpoints

### Listings
- `GET /api/listings/` - List all listings
- `POST /api/listings/` - Create a new listing
- `GET /api/listings/{id}/` - Retrieve a specific listing
- `PUT /api/listings/{id}/` - Update a listing
- `PATCH /api/listings/{id}/` - Partial update a listing
- `DELETE /api/listings/{id}/` - Delete a listing

### Bookings
- `GET /api/bookings/` - List user's bookings (all for staff)
- `POST /api/bookings/` - Create a new booking
- `GET /api/bookings/{id}/` - Retrieve a specific booking
- `PUT /api/bookings/{id}/` - Update a booking
- `PATCH /api/bookings/{id}/` - Partial update a booking
- `DELETE /api/bookings/{id}/` - Delete a booking

## Documentation

- **Swagger UI**: `/swagger/`
- **ReDoc**: `/redoc/`

## Setup Instructions

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Create superuser: `python manage.py createsuperuser`
5. Run server: `python manage.py runserver`

## Testing with Postman

1. Start the development server
2. Import the following endpoints to Postman:

### Sample Requests:

**Create Listing (POST)**
