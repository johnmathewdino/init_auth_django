# Django Authentication Starter

Welcome to the Django Authentication Starter project! This project provides a solid foundation for building web applications with user authentication features, including user registration, login, logout, forgot password, password reset, and email confirmation.

## Features

- User Registration: Allow users to create new accounts by providing basic information.
- Email Confirmation: Send a confirmation email to verify user accounts.
- Login: Secure user authentication.
- Logout: Allow users to log out securely from their accounts.
- Forgot Password: Enable users to reset their passwords via email.
- Password Reset: Allow users to set a new password after forgetting the old one.

## Getting Started

Follow these steps to get the project up and running on your local development environment:

1. Clone the repository:

   ```bash
   git clone https://github.com/johnmathewdino/init_django_auth.git
   ```

2. Navigate to the project directory:

   ```bash
   cd init_django_auth
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


## Setting up Email Backend

### To get email app password
1. Go to https://myaccount.google.com/
2. Click on Security
3. Set up your 2-Step Verification
4. Click on App Passwords
5. Input an App Name and click on Create
6. Copy the generated password
7. Paste it in the EMAIL_HOST_PASSWORD field in settings.py

```bash
   # Email Host Email Address
  EMAIL_HOST_USER = ''

  # Email Host App Password
  EMAIL_HOST_PASSWORD = ''
   ```

## Usage

You can now build your web application on top of this authentication starter. Here are some important files and directories to get you started:

- `authentication`: The Django app responsible for user authentication features.
- `templates`: Store your HTML templates for registration, login, password reset, etc.
- `urls.py`: Define your URL patterns for authentication views and routes.
- `settings.py`: Configure authentication settings like email backend, authentication backends, and more.
- `views.py`: Customize authentication views or create your own views as needed.

## Contributing

Contributions to this project are welcome! Feel free to submit bug reports, feature requests, or pull requests.

