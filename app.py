from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware
import yaml
import os

# ---------------------------------------------------
# Load OpenAPI YAML (exported from our previous step)
# ---------------------------------------------------
base_dir = os.path.dirname(__file__)
yaml_path = os.path.join(base_dir, "openapi.yaml")

with open(yaml_path, "r", encoding="utf-8") as f:
    openapi_spec = yaml.safe_load(f)

# ---------------------------------------------------
# Initialize FastAPI app
# ---------------------------------------------------
app = FastAPI(
    title=openapi_spec["info"]["title"],
    description=openapi_spec["info"]["description"],
    version=openapi_spec["info"]["version"],
    docs_url="/docs",         # Swagger UI
    redoc_url="/redoc"        # Optional Redoc UI
)

# Allow local frontend testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------
# Serve the OpenAPI YAML directly
# ---------------------------------------------------
@app.get("/openapi.yaml", include_in_schema=False)
async def get_openapi_yaml():
    return FileResponse("openapi.yaml", media_type="text/yaml")

# ---------------------------------------------------
# Custom OpenAPI schema (from the YAML file)
# ---------------------------------------------------
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    app.openapi_schema = openapi_spec
    return app.openapi_schema

app.openapi = custom_openapi

# ---------------------------------------------------
# Simple root route
# ---------------------------------------------------
@app.get("/", include_in_schema=False)
def root():
    return {
        "message": "Wehbe Stock Broker API",
        "docs": "/docs",
        "redoc": "/redoc",
        "openapi_yaml": "/openapi.yaml"
    }

# ---------------------------------------------------
# Run with: uvicorn app:app --reload
# ---------------------------------------------------
