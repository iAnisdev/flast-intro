# Flaskr

Flaskr is a simple web application built with Flask that allows users to sign up, log in, and manage their to-do items. This application features JWT authentication, flash messages, and a user-friendly interface rendered with Bootstrap 5. Currently, all data is stored in JSON format.

## Features

- User authentication (Sign up, Login, Logout)
- CRUD functionality for to-do items
- JWT-based authentication for secure access
- Flash messages for user notifications
- Responsive UI with Bootstrap 5

## Requirements

To run this application, you will need:

- Python 3.x
- Flask
- Flask-JWT-Extended
- Flask-Flash
- Bootstrap 5 (included in the templates)

## Installation

1. Clone the repository:

   git clone https://github.com/iAnisdev/flast-intro
   cd flaskr

2. Create a virtual environment and activate it:

   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required packages:

   pip install Flask pyjwt

4. Run the application:

   export FLASK_APP=flaskr
   export FLASK_ENV=development
   flask run

   Navigate to `http://127.0.0.1:5000` in your web browser.

## Usage

- **Sign Up**: Create a new account to start managing your to-do items.
- **Login**: Access your account using your credentials.
- **Logout**: Log out of your account to secure your session.
- **Manage To-Dos**:
  - Add new to-do items.
  - Mark a to-do item as complete.
  - Edit existing to-do items.
  - Delete to-do items.
  - View all to-do items.

## Route Endpoints

- **POST /auth/signup**: Register a new user
- **POST /auth/login**: Log in to your account
- **GET /auth/logout**: Log out of your account
- **GET /**: Retrieve all to-do items
- **POST /todo/add**: Create a new to-do item
- **POST /todo/complete/<:id>**: Mark a to-do item as complete
- **POST /todo/edit/<:id>**: Update an existing to-do item
- **GET /todo/delete/<:id>**: Delete a to-do item

## JSON Data Storage

For now, all user and to-do data is saved in JSON files. This is suitable for development and testing but consider using a database for production use.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Feel free to submit issues and pull requests. Contributions are welcome!
