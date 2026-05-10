"""
Unit Tests for Library Management System - Models
Member 4: Testing & Documentation
"""

import pytest
import sys
import os

# Help Python find the app files
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app as flask_app
from models import db, User, Book, Checkout


# =========================================================
# SETUP - Runs before every test
# =========================================================

@pytest.fixture
def app():
    """Create a clean test app with empty database."""
    flask_app.config['TESTING'] = True
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with flask_app.app_context():
        db.create_all()
        yield flask_app
        db.session.remove()
        db.drop_all()


# =========================================================
# BOOK TESTS
# =========================================================

def test_create_book(app):
    """Test that a book can be added to the database."""
    with app.app_context():
        book = Book(title="Harry Potter", author="J.K. Rowling", is_available=True)
        db.session.add(book)
        db.session.commit()
        assert Book.query.count() == 1

def test_book_title_saved_correctly(app):
    """Test that the book title is saved correctly."""
    with app.app_context():
        book = Book(title="1984", author="George Orwell", is_available=True)
        db.session.add(book)
        db.session.commit()
        saved = Book.query.first()
        assert saved.title == "1984"

def test_book_author_saved_correctly(app):
    """Test that the book author is saved correctly."""
    with app.app_context():
        book = Book(title="1984", author="George Orwell", is_available=True)
        db.session.add(book)
        db.session.commit()
        saved = Book.query.first()
        assert saved.author == "George Orwell"

def test_book_is_available_by_default(app):
    """Test that a new book starts as available."""
    with app.app_context():
        book = Book(title="The Alchemist", author="Paulo Coelho", is_available=True)
        db.session.add(book)
        db.session.commit()
        saved = Book.query.first()
        assert saved.is_available == True

def test_book_can_be_marked_unavailable(app):
    """Test that a book can be marked as unavailable (checked out)."""
    with app.app_context():
        book = Book(title="Harry Potter", author="J.K. Rowling", is_available=True)
        db.session.add(book)
        db.session.commit()
        book.is_available = False
        db.session.commit()
        saved = Book.query.first()
        assert saved.is_available == False

def test_multiple_books_can_be_added(app):
    """Test that multiple books can be stored."""
    with app.app_context():
        book1 = Book(title="Book One", author="Author One", is_available=True)
        book2 = Book(title="Book Two", author="Author Two", is_available=True)
        book3 = Book(title="Book Three", author="Author Three", is_available=True)
        db.session.add_all([book1, book2, book3])
        db.session.commit()
        assert Book.query.count() == 3

def test_book_can_be_deleted(app):
    """Test that a book can be removed from the database."""
    with app.app_context():
        book = Book(title="Delete Me", author="Nobody", is_available=True)
        db.session.add(book)
        db.session.commit()
        db.session.delete(book)
        db.session.commit()
        assert Book.query.count() == 0


# =========================================================
# USER TESTS
# =========================================================

def test_create_user(app):
    """Test that a user can be registered."""
    with app.app_context():
        user = User(full_name="Ali Hassan", email="ali@test.com")
        db.session.add(user)
        db.session.commit()
        assert User.query.count() == 1

def test_user_full_name_saved(app):
    """Test that the user full name is saved correctly."""
    with app.app_context():
        user = User(full_name="Sara Ahmed", email="sara@test.com")
        db.session.add(user)
        db.session.commit()
        saved = User.query.first()
        assert saved.full_name == "Sara Ahmed"

def test_user_email_saved(app):
    """Test that the user email is saved correctly."""
    with app.app_context():
        user = User(full_name="Sara Ahmed", email="sara@test.com")
        db.session.add(user)
        db.session.commit()
        saved = User.query.first()
        assert saved.email == "sara@test.com"

def test_duplicate_email_not_allowed(app):
    """Test that two users cannot have the same email."""
    with app.app_context():
        user1 = User(full_name="Ali Hassan", email="same@test.com")
        user2 = User(full_name="Sara Ahmed", email="same@test.com")
        db.session.add(user1)
        db.session.commit()
        db.session.add(user2)
        try:
            db.session.commit()
            assert False, "Should have raised an error"
        except Exception:
            db.session.rollback()
            assert User.query.count() == 1


# =========================================================
# CHECKOUT TESTS
# =========================================================

def test_create_checkout(app):
    """Test that a checkout record can be created."""
    with app.app_context():
        user = User(full_name="Ali Hassan", email="ali@test.com")
        book = Book(title="Harry Potter", author="J.K. Rowling", is_available=True)
        db.session.add_all([user, book])
        db.session.commit()

        checkout = Checkout(user_id=user.id, book_id=book.id)
        db.session.add(checkout)
        db.session.commit()
        assert Checkout.query.count() == 1

def test_checkout_links_user_and_book(app):
    """Test that checkout correctly links a user to a book."""
    with app.app_context():
        user = User(full_name="Ali Hassan", email="ali@test.com")
        book = Book(title="Harry Potter", author="J.K. Rowling", is_available=True)
        db.session.add_all([user, book])
        db.session.commit()

        checkout = Checkout(user_id=user.id, book_id=book.id)
        db.session.add(checkout)
        db.session.commit()

        saved = Checkout.query.first()
        assert saved.user_id == user.id
        assert saved.book_id == book.id
