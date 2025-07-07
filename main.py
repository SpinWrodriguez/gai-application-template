from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
# from middleware.auth import verify_token # Uncomment if you want to enable token verification middlewar
from versions.v2025R1.api.router import router as router_2025R1
from versions.v2025R2.api.router import router as router_2025R2 

app = FastAPI(title="Spinifex Copilot API")

# Middleware
## app.middleware("http")(verify_token) # Uncomment if you want to enable token verification middleware

# Versioned API
app.include_router(router_2025R1, prefix="/2025R1/api")
app.include_router(router_2025R2, prefix="/2025R2/api")

# Versioned frontend
app.mount("/2025R1", StaticFiles(directory="versions/v2025R1/frontend", html=True), name="2025R1")

@app.get("/ping")
def index():
    return {"message": "Spinifex Copilot backend running"}
