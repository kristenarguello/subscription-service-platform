from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Configurações do banco de dados
    RABBITMQ: str = "amqp://guest:guest@localhost/"
    MONGO_DB_URI: str = "mongodb://localhost:27017"
    ASSINATURAS_URL: str = "http://localhost:8000/assinaturas/ATIVAS"
