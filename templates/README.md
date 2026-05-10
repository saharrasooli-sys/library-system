# Library Management System

A professional Library Management System built using Flask, SQLite, HTML, CSS, Bootstrap, and JavaScript.

---

## Features

- User Registration
- User Login
- Add Books
- Delete Books
- Edit Books
- Search Books
- Checkout History
- Responsive Design
- Modern User Interface

---

## Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS
- Bootstrap 5
- JavaScript

---

## Project Structure

library-final/
│
├── app.py
├── models.py
├── routes.py
├── templates/
├── static/
├── library.db
└── README.md

---

## How To Run The Project

### 1. Create Virtual Environment

python -m venv venv

### 2. Activate Virtual Environment

Windows:

venv\Scripts\activate

### 3. Install Dependencies

pip install flask flask-sqlalchemy

### 4. Run The Application

python app.py

### 5. Open In Browser

http://127.0.0.1:5000

---

## Pages

- Home Page
- Books Page
- Search Page
- Login Page
- Register Page
- History Page

---

## Team Contributions

### Member 1
- Database Design
- SQLite Integration
- Flask SQLAlchemy Models

### Member 2
- API Routes
- Authentication
- Backend Logic

### Member 3
- Frontend Development
- Bootstrap UI
- HTML Templates
- API Integration
- Responsive Design

## API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| /api/books | GET | Get all books |
| /api/register | POST | Register user |
| /api/login | POST | Login user |
| /books/add | POST | Add book |
| /books/delete/<id> | DELETE | Delete book |
| /books/search | GET | Search books |
| /api/history | GET | Get checkout history |

---

## Author

Library Management System Team