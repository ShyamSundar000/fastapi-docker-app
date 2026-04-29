from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
#DATABASE_URL = "postgresql://postgres:postgrelearning123@localhost:5432/contacts_db"
print("DATABASE_URL =", DATABASE_URL)
engine=create_engine(DATABASE_URL)

SessionLocal=sessionmaker(bind=engine)

Base = declarative_base()

#try:
#   engine.connect()
#    print("Database connected successfully!")
#except:
#    print("Connection failed!")