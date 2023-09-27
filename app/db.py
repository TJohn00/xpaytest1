from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient

POSTGRES_USER = "admin"
POSTGRES_PASSWORD = "testadmin"
POSTGRES_DB = "xpayback"
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost/{POSTGRES_DB}"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

MONGO_USER = "admin"
MONGO_PASS = "testadmin"
MONGO_DB = "xpayback"
MONGO_HOST = "localhost"
MONGO_PORT = 27017
DATABASE_URL = f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}"
mongo_client = MongoClient(DATABASE_URL)
mongo_db = mongo_client[MONGO_DB]
mongo_collection = mongo_db["user"]
