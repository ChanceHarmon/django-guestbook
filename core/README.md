# Django Guestbook

A simple guestbook web application built with Django to practice core backend and full-stack concepts, including form handling, database interactions, and request/response workflows.

## Features

- Create guestbook entries (name + message)
- Form validation with user-friendly error handling
- Delete entries with POST-based actions
- Styled UI using a warm, earth-tone design system
- Scrollable entries section for improved usability
- Basic automated test suite covering core functionality

## Tech Stack

- Python  
- Django  
- HTML (Django Templates)  
- CSS (custom styling with variables)  

## Local Setup

Clone the repository:

git clone <your-repo-url>  
cd <your-project-folder>  

Create a virtual environment:

python3 -m venv venv  
source venv/bin/activate  # macOS/Linux  
venv\Scripts\activate     # Windows  

Install dependencies:

pip install django  

Apply migrations:

python manage.py migrate  

Run the development server:

python manage.py runserver  

Open in browser:

http://127.0.0.1:8000/guestbook/

## Running Tests

python manage.py test  

## What I Practiced

- Building Django models and managing database migrations  
- Using ModelForms for input validation and data persistence  
- Implementing server-rendered templates with dynamic content  
- Handling GET/POST request flows and CSRF protection  
- Applying the POST → Redirect → GET pattern  
- Implementing basic CRUD operations (create, read, delete)  
- Writing unit tests with Django’s test framework  
- Organizing static assets and styling with CSS variables  

## Future Improvements

- Add edit functionality for entries  
- Introduce user authentication  
- Improve accessibility and mobile responsiveness  
- Deploy with a production database and environment configuration  