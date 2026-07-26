from fastapi import FastAPI
from app.routers.order_router import router as order_router

app = FastAPI(
    title="Kafka Order Processing Demo",
    description="Event-driven order processing using Apache Kafka",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Kafka Order Processing Demo API"
    }


@app.get("/health")
def health():
    return {
        "status": "UP"
    }

app.include_router(order_router)