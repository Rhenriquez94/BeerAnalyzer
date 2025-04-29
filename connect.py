
from sqlalchemy import create_engine

def connect():
    """
    Conecta a la base de datos PostgreSQL y devuelve el engine.
    """
    engine = create_engine("postgresql+psycopg2://postgres:123@localhost:5432/beer_analyzer")
    return engine
