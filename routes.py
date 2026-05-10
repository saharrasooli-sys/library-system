from flask import Blueprint, request, jsonify, session, render_template
from models import db, User, Book, Checkout
from datetime import datetime

routes = Blueprint('routes', __name__)

# =========================================================
# PAGE ROUTES
# =========================================================

@routes.route('/books')
def books_page():
    return render_template("books.html")


@routes.route('/login')
def login_page():
    return render_template("login.html")


@routes.route('/register')
def register_page():
    return render_template("register.html")


@routes.route('/history')
def history_page():
    return render_template("history.html")


@routes.route('/search')
def search_page():
    return render_template("search.html")


@routes.route('/profile')
def profile_page():
    return render_template("profile.html")


# =========================================================
# BOOK DETAILS PAGE
# =========================================================

@routes.route('/book/<int:book_id>')
def book_details(book_id):

    book = Book.query.get(book_id)

    if not book:
        return "Book not found"

    # YOUR REAL PDF FILE
    pdf_file = 'Harry Potter and the Shadow of Time.pdf'

    return render_template(
        'book_details.html',
        book=book,
        pdf_file=pdf_file
    )


# =========================================================
# AUTHENTICATION API
# =========================================================

@routes.route('/api/register', methods=['POST'])
def register():

    data = request.get_json()

    existing_user = User.query.filter_by(
        email=data['email']
    ).first()

    if existing_user:

        return jsonify({
            'error': 'Email already registered'
        }), 400

    new_user = User(
        full_name=data['full_name'],
        email=data['email']
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        'message': 'User registered successfully'
    }), 201


@routes.route('/api/login', methods=['POST'])
def login():

    data = request.get_json()

    user = User.query.filter_by(
        email=data['email']
    ).first()

    if not user:

        return jsonify({
            'error': 'User not found'
        }), 404

    session['user_id'] = user.id

    return jsonify({
        'message': f'Welcome {user.full_name}!'
    }), 200


@routes.route('/api/logout', methods=['POST'])
def logout():

    session.clear()

    return jsonify({
        'message': 'Logged out successfully'
    }), 200


# =========================================================
# BOOKS API
# =========================================================

@routes.route('/api/books', methods=['GET'])
def api_books():

    books = Book.query.all()

    # CREATE SAMPLE BOOKS IF DATABASE EMPTY

    if len(books) == 0:

        sample_books = [

            Book(
                title="Harry Potter and the Shadow of Time",
                author="J.K Rowling",
                is_available=True
            ),

            Book(
                title="Digital Library Guide",
                author="Library Team",
                is_available=True
            ),

            Book(
                title="Modern Flask Development",
                author="Python Community",
                is_available=True
            )

        ]

        for book in sample_books:

            db.session.add(book)

        db.session.commit()

        books = Book.query.all()

    result = []

    for book in books:

        result.append({

            'id': book.id,
            'title': book.title,
            'author': book.author,
            'is_available': book.is_available

        })

    return jsonify(result), 200


# =========================================================
# ADD BOOK
# =========================================================

@routes.route('/books/add', methods=['POST'])
def add_book():

    data = request.get_json()

    new_book = Book(
        title=data['title'],
        author=data['author'],
        is_available=True
    )

    db.session.add(new_book)
    db.session.commit()

    return jsonify({
        'message': 'Book added successfully'
    }), 201


# =========================================================
# DELETE BOOK
# =========================================================

@routes.route('/books/delete/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):

    book = Book.query.get(book_id)

    if not book:

        return jsonify({
            'error': 'Book not found'
        }), 404

    db.session.delete(book)
    db.session.commit()

    return jsonify({
        'message': 'Book deleted successfully'
    }), 200


# =========================================================
# SEARCH BOOKS
# =========================================================

@routes.route('/books/search', methods=['GET'])
def search_books():

    title = request.args.get('title', '')

    query = Book.query

    if title:

        query = query.filter(
            Book.title.ilike(f'%{title}%')
        )

    books = query.all()

    result = []

    for book in books:

        result.append({

            'id': book.id,
            'title': book.title,
            'author': book.author,
            'is_available': book.is_available

        })

    return jsonify(result), 200


# =========================================================
# HISTORY API
# =========================================================

@routes.route('/api/history', methods=['GET'])
def api_history():

    result = [

        {
            'user': 'Ali',
            'book': 'Harry Potter',
            'checkout_date': '2026-05-10'
        },

        {
            'user': 'Sara',
            'book': 'Modern Flask Development',
            'checkout_date': '2026-05-09'
        }

    ]

    return jsonify(result), 200