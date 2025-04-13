# 🚀 Django To-Do App with MySQL

![Django](https://img.shields.io/badge/Django-4.2-brightgreen)
![MySQL](https://img.shields.io/badge/MySQL-8.0-blue)
![Python](https://img.shields.io/badge/Python-3.10+-yellow)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.2-purple)

A full-featured task management application built with Django and MySQL, featuring secure authentication and real-time updates.

## ✨ Key Features

- ✅ **Task Management**
  - Add/edit/delete tasks with descriptions
  - Mark tasks as complete/incomplete
  - Prevent duplicate task entries
- 🔒 **User Authentication**
  - Secure login/logout
  - User-specific task lists
- 🛡️ **Database Security**
  - MySQL encrypted connections
  - Environment variable configuration
- 📱 **Responsive Design**
  - Works on all device sizes
  - Dark/light mode support

## 🗃️ MySQL Database Setup

### Prerequisites
- MySQL Server 8.0+
- MySQL client tools

### Configuration Steps

1. **Create MySQL Database**:
   ```sql
   CREATE DATABASE todo_app_db;
   CREATE USER 'todo_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'your_strong_password_here';
   GRANT ALL PRIVILEGES ON todo_app_db.* TO 'todo_user'@'localhost';
   FLUSH PRIVILEGES;
Install Python MySQL Client:

bash

pip install mysqlclient
Configure Environment Variables:
Create .env file:

ini
Copy
# Database
DB_NAME=todo_app_db
DB_USER=todo_user
DB_PASSWORD=your_strong_password_here
DB_HOST=localhost
DB_PORT=3306

# Django
SECRET_KEY=your_django_secret_key
DEBUG=False  # Set to True for development
Update Django Settings:

python

# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'ssl': {'ca': '/path/to/ca-cert.pem'}  # For production
        }
    }
}
🚀 Deployment Guide
Local Development
bash
Copy
# 1. Clone repository
git clone https://github.com/yourusername/django-todo-app.git
cd django-todo-app

# 2. Set up virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Start development server
python manage.py runserver
Production Deployment
bash

# Install Gunicorn and Nginx
pip install gunicorn

# Collect static files
python manage.py collectstatic

# Run with Gunicorn
gunicorn --bind 0.0.0.0:8000 todo_project.wsgi:application

📂 Project Structure

django-todo-app/
├── todo/                  # Main application
│   ├── migrations/        # Database migrations
│   ├── templates/         # HTML templates
│   ├── __init__.py
│   ├── admin.py           # Admin configuration
│   ├── apps.py
│   ├── models.py          # Database models
│   ├── tests.py
│   ├── urls.py            # App routes
│   └── views.py           # Business logic
├── todo_project/          # Project config
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main routes
│   └── wsgi.py
├── .env                   # Environment variables
├── .gitignore
├── manage.py              # Django CLI
├── requirements.txt       # Dependencies
└── README.md
