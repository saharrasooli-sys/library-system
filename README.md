# 📚 Library Management System

A web-based library management system built with Flask,
allowing librarians and members to manage books, users, and checkouts.

---

## 👥 Team Members
- **Member 1** – Database & Models
- **Member 2** – Routes & API
- **Member 3** – Frontend (UI/UX)
- **Member 4** – Testing, Documentation & DevOps

---

## ✅ Features
- View and search books by title
- Add and delete books
- Register and login users
- Check out and return books
- View checkout history
- User profile page

---

## 🛠️ Requirements
- Python 3.10 or higher
- pip (comes with Python)

---

## 🚀 How to Run the Project

### 1. Clone the repository
```
git clone https://github.com/yasamannabizada-lgtm/library-system.git
cd library-system
```

### 2. Create a virtual environment
```
python -m venv venv
```

### 3. Activate the virtual environment
Windows:
```
venv\Scripts\activate
```
Mac/Linux:
```
source venv/bin/activate
```

### 4. Install dependencies
```
pip install -r requirements.txt
```

### 5. Run the app
```
python app.py
```

### 6. Open in your browser
```
http://127.0.0.1:5000
```

---

## 🧪 How to Run Tests
```
pytest tests/ -v
```

---

## 📁 Project Structure
```
library-system/
├── app.py                  ← Main Flask application
├── models.py               ← Database models (User, Book, Checkout)
├── routes.py               ← All routes and API endpoints
├── static/
│   ├── css/
│   │   └── style.css       ← Stylesheet
│   └── books/              ← PDF book files
├── templates/              ← HTML pages
│   ├── base.html
│   ├── index.html
│   ├── books.html
│   ├── search.html
│   ├── login.html
│   ├── register.html
│   ├── profile.html
│   ├── history.html
│   └── book_details.html
├── tests/
│   ├── test_models.py      ← Unit tests
│   └── test_routes.py      ← Integration tests
├── docs/
│   ├── api.md              ← API documentation
│   └── schema.md           ← Database schema
└── README.md
```

---

## 📖 Documentation
- API Endpoints → see `/docs/api.md`
- Database Schema → see `/docs/schema.md`
