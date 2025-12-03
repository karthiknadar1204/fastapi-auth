from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL ="postgresql://karthiknadar1204:Fvph9DyfVm2L@ep-restless-credit-a1c7489o-pooler.ap-southeast-1.aws.neon.tech/fasapi-auth-2.0?sslmode=require&channel_binding=require"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()