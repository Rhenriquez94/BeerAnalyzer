
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()

def connect():
    """
    Conecta a la base de datos PostgreSQL usando variables de entorno.
    """
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    database = os.getenv("DB_NAME")

    url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
    engine = create_engine(url)
    return engine