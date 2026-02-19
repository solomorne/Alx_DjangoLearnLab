# Social Media API

## Overview
This is a Django REST Framework-based Social Media API with custom user authentication.

## Features
- Custom User Model
- Token Authentication
- User Registration
- Login Endpoint
- Profile Management
- Followers System

## Setup Instructions

1. Clone the repository
2. Install dependencies:
   pip install django djangorestframework
3. Run migrations:
   python manage.py makemigrations
   python manage.py migrate
4. Start server:
   python manage.py runserver

## API Endpoints

### Register
POST /api/accounts/register/

### Login
POST /api/accounts/login/

### Profile
GET/PUT /api/accounts/profile/

## Authentication
Uses Token Authentication.
Include header:
Authorization: Token your_token_here
