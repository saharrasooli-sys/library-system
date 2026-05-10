# 🗄️ Database Schema

## Overview
The system uses **SQLite** as the database with **SQLAlchemy** as the ORM.
Database file: `instance/library.db`

---

## Table: users

Stores all registered library members.

| Column    | Type         | Constraints        | Description          |
|-----------|--------------|--------------------|----------------------|
| id        | Integer      | Primary Key        | Unique user ID       |
| full_name | String(100)  | Not Null           | Full name of member  |
| email     | String(120)  | Unique, Not Null   | Email address        |

---

## Table: books

Stores all books in the library.

| Column       | Type         | Constraints   | Description                    |
|--------------|--------------|---------------|--------------------------------|
| id           | Integer      | Primary Key   | Unique book ID                 |
| title        | String(200)  | Not Null      | Title of the book              |
| author       | String(100)  | Not Null      | Author of the book             |
| is_available | Boolean      | Default: True | True = available, False = out  |

---

## Table: checkouts

Tracks which user borrowed which book and when.

| Column        | Type     | Constraints              | Description              |
|---------------|----------|--------------------------|--------------------------|
| id            | Integer  | Primary Key              | Unique checkout ID       |
| user_id       | Integer  | Foreign Key → users.id   | Who borrowed the book    |
| book_id       | Integer  | Foreign Key → books.id   | Which book was borrowed  |
| checkout_date | DateTime | Default: current time    | When it was borrowed     |

---

## Relationships

```
users ──────────< checkouts >────────── books
(one user)      (many checkouts)      (one book)
```

- One **user** can have many **checkouts**
- One **book** can appear in many **checkouts** (over time)
- When a book is checked out → `is_available` is set to `False`
- When a book is returned → `is_available` is set back to `True`

---

## Entity Relationship Diagram

```
┌─────────────┐         ┌──────────────┐         ┌─────────────┐
│   users     │         │  checkouts   │         │    books    │
│─────────────│         │──────────────│         │─────────────│
│ id (PK)     │◄────────│ user_id (FK) │         │ id (PK)     │
│ full_name   │         │ book_id (FK) │────────►│ title       │
│ email       │         │ checkout_date│         │ author      │
└─────────────┘         └──────────────┘         │ is_available│
                                                  └─────────────┘
```
