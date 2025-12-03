from fastapi import APIRouter
from fastapi_auth.db.schema.user import UserInLogin, UserInCreate
authRouter = APIRouter()

@authRouter.post("/register")
def register(signupDetails: UserInCreate):
    return {"message": "User registered successfully"}

@authRouter.post("/login")
def login(loginDetails: UserInLogin):
    return {"message": "User logged in successfully"}

