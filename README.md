# Buggy Server

This is a deliberately buggy FastAPI server that randomly throws exceptions. It's designed to simulate unreliable server behavior for testing purposes.

## Features

- Random HTTP exceptions (400, 404, 500, 503, 504)
- Random Python exceptions (ValueError, TimeoutError, KeyError, MemoryError)
- Random delays and timeouts
- Intermittent successful responses

## Installation

1. Make sure you have Python 3.7+ installed
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On Unix/MacOS
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Starting the Server

Run the following command to start the server:
```bash
python buggy_server.py
```

The server will start on `http://localhost:8000`

## API Endpoints

### 1. Root Endpoint
- **URL:** `/`
- **Method:** GET
- **Behavior:** Always works
- **Example:**
  ```bash
  curl http://localhost:8000/
  ```

### 2. Get User
- **URL:** `/users/{user_id}`
- **Method:** GET
- **Failure Rate:** 30%
- **Possible Errors:**
  - 404 Not Found
  - 500 Internal Server Error
  - Custom Server Error
  - Value Error
  - Timeout Error
- **Example:**
  ```bash
  curl http://localhost:8000/users/123
  ```

### 3. Create Item
- **URL:** `/items/`
- **Method:** POST
- **Failure Rate:** 40%
- **Possible Errors:**
  - 504 Gateway Timeout
  - 400 Bad Request
- **Example:**
  ```bash
  curl -X POST http://localhost:8000/items/ \
       -H "Content-Type: application/json" \
       -d '{"name": "test item", "description": "test description"}'
  ```

### 4. List Products
- **URL:** `/products`
- **Method:** GET
- **Failure Rate:** 35%
- **Possible Errors:**
  - Key Error
  - Memory Error
  - 503 Service Unavailable
- **Example:**
  ```bash
  curl http://localhost:8000/products
  ```

### 5. Update Item
- **URL:** `/update/{item_id}`
- **Method:** PUT
- **Failure Rate:** 45%
- **Possible Errors:**
  - Connection Error
  - 409 Conflict
  - 422 Unprocessable Entity
- **Example:**
  ```bash
  curl -X PUT http://localhost:8000/update/456 \
       -H "Content-Type: application/json" \
       -d '{"name": "updated item", "status": "modified"}'
  ```

## Error Simulation

Each endpoint (except the root endpoint) has a predefined failure rate:
- `/users/{user_id}` - 30% chance of failure
- `/items/` - 40% chance of failure
- `/products` - 35% chance of failure
- `/update/{item_id}` - 45% chance of failure

When an endpoint fails, it will randomly select from its possible error types and throw that error.

## Interactive API Documentation

FastAPI provides automatic interactive API documentation:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc