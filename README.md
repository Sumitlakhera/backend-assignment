# Backend Intern Assignment

## Overview

This project is a scalable full-stack application built as part of the Backend Developer Internship assignment.

The application provides:

* User Registration and Login
* JWT Authentication
* Role-Based Access Control (RBAC)
* Product Management CRUD APIs
* Protected Frontend Dashboard
* PostgreSQL Database Integration
* Layered Backend Architecture (API → Service → Repository → Database)

The backend is built using FastAPI and PostgreSQL, while the frontend is built using React and Vite.

---

## Features

### Authentication

* User Registration
* User Login
* Password Hashing using bcrypt
* JWT Token Generation
* JWT Protected Routes
* Current User Endpoint (`/auth/me`)

### Authorization

* User and Admin Roles
* Ownership-based Product Authorization
* Protected Product Modification and Deletion

### Product Management

* Create Product
* View Products
* Update Product
* Delete Product

### Frontend

* Register Page
* Login Page
* Protected Dashboard
* Product CRUD Interface
* Success/Error Notifications
* Automatic Redirect After Registration
* Logout Functionality

---

## Tech Stack

### Backend

* FastAPI
* SQLAlchemy
* PostgreSQL
* Alembic
* Pydantic
* JWT Authentication
* Passlib (bcrypt)

### Frontend

* React
* React Router
* Axios
* Vite

---

## Project Structure

```text
backend-intern-assignment/
│
├── alembic/
│   ├── versions/
│   │   └── 8b359ada2de9_initial_schema.py
│   ├── env.py
│   ├── README
│   └── script.py.mako
│
├── app/
│   ├── api/
│   │   ├── dependencies/
│   │   │   ├── __init__.py
│   │   │   └── auth.py
│   │   │
│   │   └── v1/
│   │       ├── auth.py
│   │       └── products.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   │
│   ├── db/
│   │   ├── database.py
│   │   └── models.py
│   │
│   ├── repositories/
│   │   ├── product_repository.py
│   │   └── user_repository.py
│   │
│   ├── schemas/
│   │   ├── auth.py
│   │   └── products.py
│   │
│   └── services/
│       ├── auth_service.py
│       └── product_service.py
│
├── frontend/
│   ├── public/
│   │
│   ├── src/
│   │   ├── assets/
│   │   │   └── hero.png
│   │   │
│   │   ├── pages/
│   │   │   ├── DashboardPage.jsx
│   │   │   ├── LoginPage.jsx
│   │   │   └── RegisterPage.jsx
│   │   │
│   │   ├── routes/
│   │   │   └── ProtectedRoute.jsx
│   │   │
│   │   ├── services/
│   │   │   └── api.js
│   │   │
│   │   ├── utils/
│   │   │   └── errorHandler.js
│   │   │
│   │   ├── App.css
│   │   ├── App.jsx
│   │   ├── index.css
│   │   └── main.jsx
│   │
│   ├── package.json
│   ├── vite.config.js
│   └── README.md
│
├── .env
├── .gitignore
├── alembic.ini
├── main.py
├── requirements.txt
└── README.md
```


---

## Architecture

The backend follows a layered architecture:

```text
Client
   ↓
API Layer
   ↓
Service Layer
   ↓
Repository Layer
   ↓
Database Layer
```

### Benefits

* Separation of Concerns
* Easier Testing
* Better Maintainability
* Improved Scalability
* Cleaner Business Logic

---

## Backend Setup

### 1. Clone Repository

```bash
git clone <repository-url>
cd backend-intern-assignment
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

#### Mac/Linux

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the project root.

Example:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/backend_assignment
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 6. Run Database Migrations

```bash
alembic upgrade head
```

### 7. Start Backend Server

```bash
uvicorn main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

---

## Frontend Setup

### 1. Navigate to Frontend

```bash
cd frontend
```

### 2. Install Dependencies

```bash
npm install
```

### 3. Start Frontend

```bash
npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

---

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

## Authentication Flow

```text
Register
    ↓
Login
    ↓
JWT Token Generated
    ↓
Token Stored in Frontend
    ↓
Protected Routes
    ↓
Authorized API Access
```

---

## Database

Database Used:

```text
PostgreSQL
```

Main Entities:

### User

* id
* name
* email
* hashed_password
* role

### Product

* id
* name
* description
* price
* owner_id

---

## Scalability Considerations

This project was designed with scalability in mind:

### Layered Architecture

Business logic is separated from API and database logic, making future expansion easier.

### API Versioning

Versioned routes (`/api/v1`) allow future API evolution without breaking existing clients.

### JWT Authentication

Stateless authentication enables horizontal scaling across multiple application instances.

### Repository Pattern

Database operations are isolated from business logic, improving maintainability and testability.

### Future Enhancements

* Redis Caching
* Rate Limiting
* Docker Deployment
* CI/CD Pipeline
* Load Balancing
* Microservices Architecture
* Background Task Processing

---

## Future Improvements

* Product Search and Filtering
* Pagination
* Refresh Tokens
* User Profile Management
* Product Categories
* Redis Caching
* Docker Support
* Automated Testing

---

## Author

Backend Developer Internship Assignment Submission
