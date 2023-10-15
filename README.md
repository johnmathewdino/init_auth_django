# Django Authentication Starter

Welcome to the Django Authentication Starter project! This project provides a solid foundation for building web applications with user authentication features, including user registration, login, logout, forgot password, password reset, and email confirmation.

You can use this as a starter project for your own Django web applications or you can copy the authentication app into your existing Django project.

## Features

- User Registration: Allow users to create new accounts by providing basic information.
- Email Confirmation: Send a confirmation email to verify user accounts.
- Login: Secure user authentication.
- Logout: Allow users to log out securely from their accounts.
- Forgot Password: Enable users to reset their passwords via email.
- Password Reset: Allow users to set a new password after forgetting the old one.

## Directory Structure

The following is a high-level overview of the project structure:

```bash
init_django_auth
├── authentication
├── core
├── templates
├── .gitignore
├── manage.py
├── README.md
└── requirements.txt

```
Important files and directories:
- `/init_django_auth/`: This is the root directory of the project.
- `/authentication/`: This directory contains the Django app responsible for user authentication features.
- `/core/`: This directory contains the project settings and URL configurations.
- `/templates/`: This directory contains the HTML templates for the authentication views.
- `requirements.txt`: This file contains a list of Python packages required to run the project.

### The Authentication App

The authentication app is the star of this project. It contains the views, forms, models, and templates for user authentication features. The following is the directory structure of the authentication app:

```bash
authentication
├── migrations
├── __init__.py
├── admin.py
├── apps.py
├── forms.py
├── models.py
├── tests.py
├── urls.py
└── views.py
```

Important files and directories in the authentication app:
- `forms.py`: This file contains the forms for UserRegistrationForm. UserRegistrationForm is a custom form that inherits from Django's built-in UserCreationForm.
- `urls.py`: This file contains the URL patterns for the authentication views.
- `views.py`: This file contains the views for user authentication features.

### The Core 

The core directory contains the project settings and URL configurations. The following is the directory structure of the core directory:

```bash
core
├── __init__.py
├── asgi.py
├── settings.py
├── urls.py
└── wsgi.py
```
Important files and directories inside the core directory:
- `settings.py`: This file contains the project settings, including authentication settings.
- `urls.py`: This file contains the URL patterns for the authentication views.


### The Templates Directory
The templates directory contains the HTML templates for the authentication views. The following is the directory structure of the templates directory:

Note: The HTML contains skeleton code for the views. You can customize the HTML to suit your needs.

```bash
templates
├── authentication
│   ├── email_activation
│   │   ├── activate_email_message.html
│   │   ├── activation_successful.html
│   │   ├── activation_unsucessful.html
│   │   └── email_sent.html
│   ├── login.html
│   ├── password_reset.html
│   ├── password_reset_complete.html
│   ├── password_reset_confirm.html
│   ├── password_reset_done.html
│   └── register.html
└── homepage.html
```

Important files and directories inside the templates directory:
- `authentication/`: This directory contains the HTML templates for the authentication views.
- `homepage.html`: This file contains the HTML template for the homepage. This is where the user will be redirected after logging in.
- `authentication/login.html`: This file contains the HTML template for the login view.
- `authentication/password_reset.html`: This file contains the HTML template for the password reset view.
- `authentication/password_reset_complete.html`: This file contains the HTML template for the password reset complete view when the password reset is successful
- `authentication/password_reset_confirm.html`: This file contains the HTML template for the password reset confirm view when the user clicks the link in the email. This containes the form for the user to enter the new password.
- `authentication/password_reset_done.html`: This file contains the HTML template for the password reset done view. This is the page that the user will be redirected to after the password reset is successful.
- `authentication/register.html`: This file contains the HTML template for the user registration view.
- `authentication/email_activation/`: This directory contains the HTML templates for the email activation views.
- `authentication/email_activation/activate_email_message.html`: This file contains the HTML template for the email message sent to users for email activation.
- `authentication/email_activation/activation_successful.html`: This file contains the HTML template for the email activation successful view.
- `authentication/email_activation/activation_unsuccessful.html`: This file contains the HTML template for the email activation unsuccessful view.
- `authentication/email_activation/email_sent.html`: This file contains the HTML template for the email sent view.


## Getting Started

You can use this project as:
1. Starter file for your own Django web applications
2. Copy the authentication app into your existing Django project 


### As a Starter Project

To use this project as a starter project for your own Django web applications, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/johnmathewdino/init_auth_django.git
   ```

2. Navigate to the project directory:

   ```bash
   cd init_auth_django
   ```

3. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Set up the email backend (see instructions below).


6. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

7. Create a superuser to access the Django admin panel:

   ```bash
   python manage.py createsuperuser
   ```

8. Start the development server:

   ```bash
   python manage.py runserver
   ```

9. Access the admin panel at `http://localhost:8000/admin/` and log in with your superuser credentials.

### Copy the Authentication App into existing Django Project

To copy the authentication app into your existing Django project, follow these steps:

1. Copy the `authentication` directory into your Django project directory.
2. Copy the `templates` directory into your Django project directory.
3. Add `authentication` to the `INSTALLED_APPS` list in your project's `settings.py` file.

```bash 
INSTALLED_APPS = [
    ...
    'authentication',
    ...
]
```

4. Add the following to your project's `settings.py` file:

```bash
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "homepage"
LOGOUT_REDIRECT_URL = "login"
```

5. Add the following to your project's `urls.py` file:

```bash
from django.urls import path, include

urlpatterns = [
    ...
    path('authentication/', include('authentication.urls')),
    ...
]
```


## Setting up Email Backend

The Email Backend will let you send emails to users for email confirmation, password reset, etc. To set up the email backend, follow these steps:

### To get email app password
1. Go to https://myaccount.google.com/
2. Click on Security
3. Set up your 2-Step Verification
4. Click on App Passwords
5. Input an App Name and click on Create
6. Copy the generated password
7. Make sure you have to following in your settings.py file

   ```bash
   EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
   EMAIL_HOST = 'smtp.gmail.com'
   EMAIL_PORT = 587
   EMAIL_USE_TLS = True
   EMAIL_USE_SSL = False
   EMAIL_HOST_USER = ''
   EMAIL_HOST_PASSWORD = ''
    ```

8. Replace EMAIL_HOST_USER with your email address
9. Replace EMAIL_HOST_PASSWORD with the app password you generated


## Contributing

Contributions to this project are welcome! Feel free to submit bug reports, feature requests, or pull requests.

