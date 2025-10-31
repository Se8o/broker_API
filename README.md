# Wehbe Stock Broker API

A REST API documentation server for a **Stock Broker** platform.  
The application serves an **OpenAPI 3.0 specification** (`openapi.yaml`) and provides interactive documentation through **Swagger UI** and **ReDoc**.

---

## Features

- Full **OpenAPI 3.0** specification  
- Endpoint **`/api`** → redirects to Swagger UI  
- **Swagger UI** (`/docs`) and **ReDoc** (`/redoc`) documentation interfaces  
- Serves the OpenAPI YAML file at `/openapi.yaml`  
- Built with **FastAPI + Uvicorn + PyYAML**  
- Ready to deploy or extend with backend logic  

---

## Requirements

To run the application locally, you need:

| Software | Minimum Version | Notes |
|-----------|-----------------|-------|
| Python | 3.10+ | Tested on 3.13 |
| pip | latest | For installing dependencies |
| Git | optional | For cloning the repository |

---

## Installation & Running (Local Setup)

###  Clone the repository
```bash
https://github.com/Se8o/broker_API.git
2️⃣ Create a virtual environment
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
# or
.venv\Scripts\activate      # Windows
3️⃣ Install dependencies
pip install fastapi uvicorn pyyaml
4️⃣ Run the FastAPI server
uvicorn app:app --reload
🌐 Access the documentation
Endpoint	Description
/api	Redirects to Swagger UI
/docs	Swagger UI interactive documentation
/redoc	ReDoc documentation
/openapi.yaml	Raw OpenAPI YAML specification
/	Root endpoint with API info
