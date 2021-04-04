import os

from orator import DatabaseManager, Schema, Model
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

DATABASES = {
    "postgres": {
        "driver": "postgres",
        "host": os.getenv("DB_HOST"),
        "database": os.getenv("DB_NAME"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "prefix": "",
        "port": 5432
    }
}

db = DatabaseManager(DATABASES)
schema = Schema(db)
Model.set_connection_resolver(db)
