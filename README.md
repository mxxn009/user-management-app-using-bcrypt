# Flask User Management App

This project is a simple user management web application built with Flask and Flask-Bcrypt. It allows users to register and log in with secure password hashing, along with basic validation for existing users and invalid login attempts. This foundational app can be further developed with advanced UI and database integration.

## Features

- **User Registration**: Users can register with a username and password. Passwords are hashed using Flask-Bcrypt for security.
- **User Login**: Registered users can log in with their credentials. Incorrect usernames or passwords prompt an error message.
- **Password Security**: Passwords are hashed and salted with Flask-Bcrypt, meaning they're stored securely without being saved in plain text.
- **Success Pages**: After successful registration or login, users are redirected to success pages.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Flask-Bcrypt

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/mxxn009/flask-user-management-app.git
   cd flask-user-management-app
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Project Structure

- `app.py`: Main application file containing all routes and logic for user registration and login.
- `templates/`: Contains HTML templates (`index.html`, `register.html`, `login.html`, `success.html`, `reg_success.html`) for the app's user interface.

### Running the Application

To start the app, run the following command in your terminal:

```bash
python app.py
```

Visit `http://127.0.0.1:5000/` in your browser to access the app.

### Usage

1. **Register a New User**:
   - Go to the `/register` page and enter a username and password to create an account.
   - If successful, you'll be redirected to a registration success page.
   - If the username already exists, you'll receive an error message.

2. **Login**:
   - Go to the `/login` page and enter your registered credentials.
   - If successful, you'll be redirected to a login success page.
   - If the credentials are invalid, you'll receive an error message.

### Future Improvements

- **Database Integration**: Store users in a database instead of an in-memory dictionary.
- **Advanced UI**: Enhance the front end with a modern and responsive design.
- **Session Management**: Implement session handling to maintain user login states.

## License

This project is open-source and available under the MIT License.

--- 
