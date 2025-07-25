# CRM Project - Django Based

## Overview
A simple yet functional Customer Relationship Management (CRM) system built with **Django**. It allows users to register, log in, manage customers, and keep track of key information. Perfect for learning Django fundamentals and building real-world apps.

## Features
- User authentication (Sign up / Login / Logout)
- Customer list and detail pages
- Add / edit / delete customer info
- Dashboard with basic stats
- Admin panel support
- Responsive design (Bootstrap-based)

## Tech Stack
- Python 3.x  
- Django 4.x  
- SQLite (or any other DB of your choice)  
- HTML5, Bootstrap  
- Optional: Tailwind CSS / Font Awesome icons

## Installation

```bash
git clone https://github.com/yourusername/crm-django.git
cd crm-django
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
