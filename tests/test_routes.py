"""
Integration Tests for Library Management System - Routes
Member 4: Testing & Documentation
"""

import pytest
import sys
import os
import json

# Help Python find the app files
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app as flask_app
from models import db, User, Book, Checkout


# =========================================================
# SETUP - Runs before every test
# =========================================================

@pytest.fixture
def client():
    """Create a test client with a clean database."""
    flask_app.config['TESTING'] = True
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with flask_app.app_context():
        db.create_all()
        with flask_app.test_client() as client:
            yield client
        db.session.remove()
        db.drop_all()


# =========================================================
# PAGE LOAD TESTS
# =========================================================

def test_home_page_loads(client):
    """Home page / should return 200."""
    response = client.get('/')
    assert response.status_code == 200

def test_books_page_loads(client):
    """Books page /books should return 200."""
    response = client.get('/books')
    assert response.status_code == 200

def test_login_page_loads(client):
    """Login page /login should return 200."""
    response = client.get('/login')
    assert response.status_code == 200

def test_register_page_loads(client):
    """Register page /register should return 200."""
    response = client.get('/register')
    assert response.status_code == 200

def test_history_page_loads(client):
    """History page /history should return 200."""
    response = client.get('/history')
    assert response.status_code == 200

def test_search_page_loads(client):
    """Search page /search should return 200."""
    response = client.get('/search')
    assert response.status_code == 200

def test_profile_page_loads(client):
    """Profile page /profile should return 200."""
    response = client.get('/profile')
    assert response.status_code == 200


# =========================================================
# BOOKS API TESTS
# =========================================================

def test_get_all_books(client):
    """GET /api/books should return 200 and a list."""
    response = client.get('/api/books')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)

def test_add_book(client):
    """POST /books/add should create a new book."""
    response = client.post('/books/add',
        data=json.dumps({"title": "Test Book", "author": "Test Author"}),
        content_type='application/json'
    )
    assert response.status_code == 201
    data = json.loads(response.data)
    assert 'message' in data

def test_search_books_by_title(client):
    """GET /books/search?title= should return matching books."""
    # First add a book
    client.post('/books/add',
        data=json.dumps({"title": "Harry Potter", "author": "J.K. Rowling"}),
        content_type='application/json'
    )
    # Now search for it
    response = client.get('/books/search?title=Harry')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)

def test_search_returns_empty_for_no_match(client):
    """Search with no matching title should return empty list."""
    response = client.get('/books/search?title=XYZNOTFOUND')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data == []

def test_delete_book(client):
    """DELETE /books/delete/<id> should remove a book."""
    # Add a book first
    client.post('/books/add',
        data=json.dumps({"title": "Delete Me", "author": "Nobody"}),
        content_type='application/json'
    )
    # Delete book with id 1
    response = client.delete('/books/delete/1')
    assert response.status_code == 200

def test_delete_nonexistent_book(client):
    """DELETE on a book that doesn't exist should return 404."""
    response = client.delete('/books/delete/999')
    assert response.status_code == 404


# =========================================================
# USER API TESTS
# =========================================================

def test_register_new_user(client):
    """POST /api/register should create a new user."""
    response = client.post('/api/register',
        data=json.dumps({
            "full_name": "Ali Hassan",
            "email": "ali@test.com"
        }),
        content_type='application/json'
    )
    assert response.status_code == 201
    data = json.loads(response.data)
    assert 'message' in data

def test_register_duplicate_email(client):
    """Registering with same email twice should return 400."""
    user_data = json.dumps({
        "full_name": "Ali Hassan",
        "email": "ali@test.com"
    })
    client.post('/api/register',
        data=user_data,
        content_type='application/json'
    )
    response = client.post('/api/register',
        data=user_data,
        content_type='application/json'
    )
    assert response.status_code == 400

def test_login_existing_user(client):
    """POST /api/login with valid email should return 200."""
    # Register first
    client.post('/api/register',
        data=json.dumps({"full_name": "Ali Hassan", "email": "ali@test.com"}),
        content_type='application/json'
    )
    # Then login
    response = client.post('/api/login',
        data=json.dumps({"email": "ali@test.com"}),
        content_type='application/json'
    )
    assert response.status_code == 200

def test_login_nonexistent_user(client):
    """POST /api/login with unknown email should return 404."""
    response = client.post('/api/login',
        data=json.dumps({"email": "nobody@test.com"}),
        content_type='application/json'
    )
    assert response.status_code == 404

def test_logout(client):
    """POST /api/logout should return 200."""
    response = client.post('/api/logout')
    assert response.status_code == 200


# =========================================================
# HISTORY API TESTS
# =========================================================

def test_get_history(client):
    """GET /api/history should return 200 and a list."""
    response = client.get('/api/history')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
