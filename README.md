
# PythonAssignment-CN

A Django REST Framework project for managing events, RSVPs, and reviews.  
This repository demonstrates API design, JWT authentication, and modular app structure.

---

## Features
- Event Management: Create, update, list, and delete events
- RSVP System: Users can RSVP to events with statuses like Going, Interested, or Not Going
- Reviews: Add ratings and comments for events
- JWT Authentication: Secure endpoints using JSON Web Tokens
- Browsable API: Explore endpoints via Django REST Framework’s built-in UI

---

## Installation

1. Clone the repository:
   bash
   git clone https://github.com/MayurThakkar-178/PythonAssignment-CN.git
   cd PythonAssignment-CN
   

2. Create and activate a virtual environment:
   bash
   python -m venv .venv
   source .venv/bin/activate


3. Install dependencies:
   bash
   pip install -r requirements.txt

4. Apply migrations:
   bash
   python manage.py makemigrations
   python manage.py migrate

6. Create a superuser:
   bash
   python manage.py createsuperuser
   

7. Run the server:
   bash
   python manage.py runserver


---

## Authentication

This project uses JWT authentication.

Obtain a token:
bash
curl -X POST http://127.0.0.1:8000/api/token/ \
-H "Content-Type: application/json" \
-d '{"username":"your_username","password":"your_password"}'


Use the token in requests:
bash
curl -X GET http://127.0.0.1:8000/api/events/ \
-H "Authorization: Bearer <your_token>"



## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| /api/events/ | GET | List all events |
| /api/events/ | POST | Create a new event |
| /api/events/{id}/ | GET | Retrieve event details |
| /api/events/{id}/ | PUT/PATCH | Update event |
| /api/events/{id}/ | DELETE | Delete event |
| /api/events/{id}/rsvp/ | POST | RSVP to an event |
| /api/events/{id}/rsvp/{user_id}/ | PATCH | Update RSVP |
| /api/events/{id}/reviews/ | POST | Add a review |
| /api/events/{id}/reviews_list/ | GET | List reviews for an event |


## Tech Stack
- Python 3.12
- Django 5.x
- Django REST Framework
- SimpleJWT for authentication
- SQLite (default, can be swapped for PostgreSQL/MySQL)
