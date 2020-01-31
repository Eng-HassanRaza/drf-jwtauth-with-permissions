Django REST Api which use JWT authentication with admin and user permissions

Steps to follow to run this API

Clone Repo:
Clone Repo: https://github.com/Eng-HassanRaza/drf-jwtauth-with-permissions.git

Create Virtual Envirnment for this project
Activate Virtual Envirnment

Install Requirements:
pip install -r requierments

Run server
python manage.py runserver

Usage example
Create User
    Endpoint: /api/users/
    Method POST
    Json Body example
    {
        "email": "test@test.com",
        "first_name": "test_first",
        "last_name": "test_last",
        "password" : "Testpass123",
        "profile": {
            "company_name": "test comp",
            "role": "admin"
        }
    }

Login User
    Endpoint: /api/auth/login/
    Method POST
    Json Body Example
    {
        "email": "test@test.com",
        "password" : "Testpass123"
    }
    Return
    JWT_Token
    userObj

All Users
    Endpoint: /api/users/
    Method GET
    Add JWT Token in header
    Note: To view all user you have to the rights of admin/superuser

User Profile
    Endpoint: /api/users/2/
    Method Get
    Add JWT Token in header

UpDate User
    Endpoint: /api/users/2/
    Method PUT
    Add JWT Token in header
    Json Body:
    {
        "email": "test@test.com",
        "password" : "Testpass123"
      "profile": {
        "company_name": "test comp updated",
        "role": "admin"
      }
    }

Delete User:
    Endpoint: /api/users/3/
    Method DELETE
    Add JWT Token in header
