from fastapi import FastAPI
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import yaml
import os

base_dir = os.path.dirname(__file__)
yaml_path = os.path.join(base_dir, "openapi.yaml")

with open(yaml_path, "r", encoding="utf-8") as f:
    openapi_spec = yaml.safe_load(f)

app = FastAPI(
    title=openapi_spec["info"]["title"],
    description=openapi_spec["info"]["description"],
    version=openapi_spec["info"]["version"],
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/openapi.yaml", include_in_schema=False)
async def get_openapi_yaml():
    """Return the raw OpenAPI YAML file."""
    return FileResponse(yaml_path, media_type="text/yaml")


def custom_openapi():
    """Load OpenAPI schema from external YAML."""
    if app.openapi_schema:
        return app.openapi_schema
    app.openapi_schema = openapi_spec
    return app.openapi_schema

app.openapi = custom_openapi

@app.get("/api", include_in_schema=False)
def api_docs_redirect():
    """Redirect /api to the Swagger UI."""
    return RedirectResponse(url="/docs")

@app.get("/", include_in_schema=False)
def root():
    return {
        "message": "Stock Broker API",
        "api_docs": "/api",
        "swagger_docs": "/docs",
        "redoc_docs": "/redoc",
        "openapi_yaml": "/openapi.yaml"
    }