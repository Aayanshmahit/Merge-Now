from sqlmodel import create_engine, SQLModel, Session
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("Database Url is missing from .env!")

database_engine = create_engine(DATABASE_URL , echo = True)

def create_db_and_tables():
    SQLModel.metadata.create_all(database_engine)

def get_database_session():
    with Session(database_engine) as session:
        yield session

create_db_and_tables()