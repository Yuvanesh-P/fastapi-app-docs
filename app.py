from fastapi import FastAPI

app = FastAPI(
    title="My FastAPI Application",
    description="Simple Python backend application",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "FastAPI application is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }