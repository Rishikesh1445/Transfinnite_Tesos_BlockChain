from fastapi import APIRouter, HTTPException, Depends
from models.user import UserCreate, UserLogin, UserResponse
from utils.auth_utils import create_jwt_token, hash_password, verify_password
from middleware.auth_middleware import verify_token
from database.mongodb import MongoDB
from bson import ObjectId
router = APIRouter()

@router.post("/signup", response_model=UserResponse)
async def signup(user: UserCreate):
    try:
        hashed_password = hash_password(user.password)
        user_data = {
            "email": user.email,
            "username": user.username,
            "password": hashed_password
        }
        
        await MongoDB.user_collection.insert_one(user_data)
        return {"email": user.email, "username": user.username}
    except Exception as e:
        if "duplicate key error" in str(e):
            raise HTTPException(status_code=400, detail="Email already registered")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.post("/login")
async def login(user: UserLogin):
    user_data = await MongoDB.user_collection.find_one({"email": user.email})
    
    if not user_data:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    if not verify_password(user.password, user_data["password"]):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    token = create_jwt_token(user.email)
    return {"access_token": token, "token_type": "bearer"}

@router.get("/protected", response_model=UserResponse)
async def protected_route(token_data: dict = Depends(verify_token)):
    email = token_data["email"]
    user_data = await MongoDB.user_collection.find_one({"email": email})
    
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {"email": user_data["email"], "username": user_data["username"]}
