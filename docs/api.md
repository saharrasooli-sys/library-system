# 📡 API Documentation

## Base URL
```
http://127.0.0.1:5000
```

---

## 📚 Books

| Method | Endpoint                  | Description              | Success Code |
|--------|---------------------------|--------------------------|--------------|
| GET    | /api/books                | Get all books            | 200          |
| POST   | /books/add                | Add a new book           | 201          |
| DELETE | /books/delete/\<id\>      | Delete a book by ID      | 200          |
| GET    | /books/search?title=      | Search books by title    | 200          |

### Example: Add a Book
**Request:**
```
POST /books/add
Content-Type: application/json

{
  "title": "Harry Potter",
  "author": "J.K. Rowling"
}
```
**Response:**
```
{
  "message": "Book added successfully"
}
```

### Example: Search Books
**Request:**
```
GET /books/search?title=Harry
```
**Response:**
```
[
  {
    "id": 1,
    "title": "Harry Potter and the Shadow of Time",
    "author": "J.K Rowling",
    "is_available": true
  }
]
```

---

## 👤 Users

| Method | Endpoint       | Description           | Success Code |
|--------|----------------|-----------------------|--------------|
| POST   | /api/register  | Register a new user   | 201          |
| POST   | /api/login     | Login a user          | 200          |
| POST   | /api/logout    | Logout current user   | 200          |

### Example: Register
**Request:**
```
POST /api/register
Content-Type: application/json

{
  "full_name": "Ali Hassan",
  "email": "ali@email.com"
}
```
**Response:**
```
{
  "message": "User registered successfully"
}
```

### Example: Login
**Request:**
```
POST /api/login
Content-Type: application/json

{
  "email": "ali@email.com"
}
```
**Response:**
```
{
  "message": "Welcome Ali Hassan!"
}
```

---

## 📋 History

| Method | Endpoint      | Description            | Success Code |
|--------|---------------|------------------------|--------------|
| GET    | /api/history  | Get all checkout records | 200        |

### Example: Get History
**Response:**
```
[
  {
    "user": "Ali",
    "book": "Harry Potter",
    "checkout_date": "2026-05-10"
  }
]
```

---

## ❌ Error Responses

| Code | Meaning                        |
|------|--------------------------------|
| 400  | Bad request (e.g. duplicate email) |
| 404  | Resource not found             |
| 200  | Success                        |
| 201  | Created successfully           |
