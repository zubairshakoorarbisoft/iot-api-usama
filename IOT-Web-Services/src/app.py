from fastapi import FastAPI
import uvicorn
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

from src.routers import sensor

def create_app() -> FastAPI:
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    ]
    app = FastAPI(
        title="IOT Sensor Web Service",
        description="A simple wrapper API around IOT devices.",
        openapi_url="/swagger.json",
        middleware=middleware)
    app.include_router(sensor.router)

    return app


app = create_app()

@app.get("/healthcheck")
def healthcheck():
    return "200 OK"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, )