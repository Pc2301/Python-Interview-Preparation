### 1. What is Flask? What are its main features? Also explain main components of Flask & FastAPI. 


### 2. Flask follows WSGI, while FastAPI is built on ASGI. What’s the difference?
1. WSGI (Web Server Gateway Interface): 
* Old standard for Python web servers and frameworks.
* Synchronous: handles one request per worker at a time.
* Designed in an era when web apps were mostly blocking I/O (databases, files).
* Widely adopted: Flask, Django (traditional), Bottle.

2. ASGI (Asynchronous Server Gateway Interface) 
* Supports asynchronous programming with async/await.
* Can handle concurrent requests without blocking.
* Also supports HTTP, WebSockets, and background tasks out-of-the-box.
* Used by FastAPI, Starlette, Django 3.0+ (via channels).
```python 
from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def home():
    time.sleep(5)   # Simulate blocking I/O
    return "Hello from Flask!"
# If 100 users hit this endpoint, each worker is blocked for 5s, so throughput is low.

from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/")
async def home():
    await asyncio.sleep(5)  # Non-blocking I/O
    return "Hello from FastAPI!"
# While one request is sleeping, the server can serve other requests — higher throughput and better concurrency.
```

### 3. How do you define routes in Flask vs FastAPI?

### 4. Which is synchronous by default: Flask or FastAPI?

### 5. What makes FastAPI faster than Flask?

### 6. How do you return JSON responses in Flask vs FastAPI?

### 7. How do you handle query parameters and path parameters in both frameworks?

### 8. What is the role of Blueprints in Flask? What’s the equivalent in FastAPI?

### 9. How do you handle form submissions and file uploads in Flask vs FastAPI?

### 10. How do you manage middlewares in Flask vs FastAPI?


### 11. Which framework has built-in dependency injection? How does it work?

### 12. How does FastAPI use Pydantic models? How does Flask handle request validation?

### 13. How do you integrate a database (like SQLAlchemy) with Flask and FastAPI?

### 14. How do you add authentication & authorization in both frameworks?

### 15. Explain how you would implement CORS in Flask vs FastAPI.

### 16. How do you implement background tasks in FastAPI? Can Flask do the same?

### 17. How do you handle WebSockets in Flask vs FastAPI?

### 18. If you need to build a high-performance API serving thousands of requests per second, which framework would you pick and why?

### 19. How does FastAPI leverage async/await for concurrency? Why can’t Flask do it natively?

### 20. Flask relies on extensions (Flask-RESTful, Flask-SQLAlchemy). FastAPI has built-ins like request validation. How does that affect development?

### 21. In production, which server would you use to run Flask vs FastAPI? (e.g., Gunicorn + Uvicorn workers)

### 22. How do you scale Flask and FastAPI applications in Kubernetes?

### 23. Suppose your API has to stream responses (like large files or chat tokens). How would you implement it in Flask vs FastAPI?


### 24. How do you implement API versioning in Flask vs FastAPI?

### 25. How do you benchmark performance of Flask vs FastAPI?

### 26. Which framework is better suited for GraphQL APIs? Why?

### 27. If you were designing a microservices architecture, which one would you prefer: Flask or FastAPI? Justify.

### 28. Show how to stream a file download in Flask vs FastAPI.

### 29. Implement authentication using JWT in both frameworks.

### 30. Build an endpoint to accept a POST request with JSON body and validate fields (Flask with Marshmallow / FastAPI with Pydantic).

### 31. Create an endpoint /add?a=10&b=20 that returns the sum in both frameworks.

### 32. Write a simple Hello World API in Flask and in FastAPI.
