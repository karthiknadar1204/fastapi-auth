from fastapi_auth.core.database import Base, engine
from fastapi_auth.db.models.user import User 

def create_tables():
    Base.metadata.create_all(bind=engine)