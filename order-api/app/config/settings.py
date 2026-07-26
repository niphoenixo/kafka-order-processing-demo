from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Kafka Order Processing Demo"

    KAFKA_BOOTSTRAP_SERVERS: str = "localhost:9092"

    ORDER_TOPIC: str = "orders"

    class Config:
        env_file = ".env"


settings = Settings()