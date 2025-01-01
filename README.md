# Async FastAPI MySQL API

![FastAPI](https://img.shields.io/badge/FastAPI-0078D7?style=for-the-badge&logo=fastapi&logoColor=white)  ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)  ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-BA2B00?style=for-the-badge&logo=sqlalchemy&logoColor=white)  ![Async Icon](https://img.shields.io/badge/Asyncmy-0078D7?style=for-the-badge&logo=asyncapi&logoColor=white)

## Description

An **asynchronous REST API** built with **FastAPI** and **MySQL** as the database backend. This API provides CRUD operations for users and ensures high-performance, asynchronous database interactions.

---

### Features

- ⚡ Fully asynchronous API using FastAPI
- 🔗 Integration with MySQL using SQLAlchemy
- 🌐 RESTful API for User CRUD operations

---

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/rahulkumar-fullstack/async-fastapi-mysql-api.git
   cd async-fastapi-mysql-api

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Unix
   .\venv\Scripts\activate  # Windows

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

---

### Usage

1. **Start the FastAPI application**:

   ```bash
   uvicorn app.main:app --reload
   ```

2. **Access the API** at `http://127.0.0.1:8000`

---

### Endpoints

- **Create User**: `POST /api/v1/users/`
- **Get User**: `GET /api/v1/users/{user_id}`
- **Update User**: `PUT /api/v1/users/{user_id}`
- **Delete User**: `DELETE /api/v1/users/{user_id}`
- **List Users**: `GET /api/v1/users/`

---

### Technologies

- 🐍 **Python**: The programming language used.
- 🔧 **FastAPI**: A modern web framework for building APIs.
- 🌱 **MySQL**: Database system used for storage.
- 🏗️ **SQLAlchemy**: ORM tool for managing the database interactions.
- 🚘 **Asyncmy**: Async MySQL driver
---
