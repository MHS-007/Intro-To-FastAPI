## FastAPI – Basic CRUD Demo

### What is FastAPI?

FastAPI is a modern Python web framework that makes it super easy to build APIs (Application Programming Interfaces). Think of it as a tool that helps your Python applications communicate with other programs or websites. It's fast, reliable, and automatically generates documentation for your API, which means you can see and test your API through a web browser without writing extra code.

### About This Project

This repository contains:
- A minimal "hello" app (`file.py`) - a simple introduction to FastAPI
- A complete Student CRUD API (`Basic_CRUD.py`) - demonstrates Create, Read, Update, and Delete operations

### Requirements
- Python 3.8 or higher

### Installation & Setup

1. **Create a virtual environment** (recommended):
```bash
python -m venv venv
```

2. **Activate the virtual environment**:
   - On Windows (PowerShell):
   ```bash
   .\venv\Scripts\Activate.ps1
   ```
   - On Windows (Command Prompt):
   ```bash
   venv\Scripts\activate
   ```
   - On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

### Run the apps
You can run either of the two apps with Uvicorn.

- Run the CRUD API (recommended):
```bash
uvicorn Basic_CRUD:app --reload
```

- Run the minimal hello app:
```bash
uvicorn file:app --reload
```

By default, the server starts at `http://127.0.0.1:8000`.

### API Overview (Basic_CRUD.py)
Base URL: `http://127.0.0.1:8000`

- GET `/` – Default message
- GET `/students` – List all students
- POST `/students` – Create a student
- GET `/students/{id}` – Retrieve a student by ID
- PUT `/students/{id}` – Update a student by ID
- DELETE `/students/{id}` – Delete a student by ID

Student model:
```json
{
  "ID": 1,
  "Name": "Alice",
  "Age": 20
}
```

### Example requests
Using Python `requests` library:

```python
import requests

# List students
requests.get("http://127.0.0.1:8000/students")

# Create a student
requests.post(
    "http://127.0.0.1:8000/students",
    json={"ID": 1, "Name": "Alice", "Age": 20}
)

# Get by ID
requests.get("http://127.0.0.1:8000/students/1")

# Update by ID
requests.put(
    "http://127.0.0.1:8000/students/1",
    json={"ID": 1, "Name": "Alice Smith", "Age": 21}
)

# Delete by ID
requests.delete("http://127.0.0.1:8000/students/1")
```

Or using curl:
```bash
# List students
curl -X GET http://127.0.0.1:8000/students

# Create a student
curl -X POST http://127.0.0.1:8000/students \
  -H "Content-Type: application/json" \
  -d '{"ID":1, "Name":"Alice", "Age":20}'

# Get by ID
curl -X GET http://127.0.0.1:8000/students/1

# Update by ID
curl -X PUT http://127.0.0.1:8000/students/1 \
  -H "Content-Type: application/json" \
  -d '{"ID":1, "Name":"Alice Smith", "Age":21}'

# Delete by ID
curl -X DELETE http://127.0.0.1:8000/students/1
```

### Interactive docs
FastAPI provides interactive documentation:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

### Notes
- The CRUD API uses an in-memory list; data resets on server restart.