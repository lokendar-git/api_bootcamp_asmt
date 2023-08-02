from fastapi import APIRouter, HTTPException, Depends
from database import create_user, update_user, delete_user, get_user_by_email
from schemas import User
import re

router = APIRouter()

@router.post("/create_user/", status_code=201)
async def create_user_profile(user: User):
    # Check age to be greater than 18
    if user.age <= 18:
        raise HTTPException(status_code=400, detail="Age must be greater than 18")
    
    # Check phone number to have only digits
    if not len(str(user.mobile_number)) == 10:
        raise HTTPException(status_code=400, detail="Phone number must contain 10 digits")
    
    # Check birthday format (should be 'yyyy-mm-dd')
    if not re.match(r'^\d{2}-\d{2}-\d{4}$', user.birthday):
        raise HTTPException(status_code=400, detail="Invalid birthday format. Should be 'dd-mm-yyyy'")
    
    if create_user(user):
        return {"message": "User created successfully"}
    else:
        raise HTTPException(status_code=409, detail="User with this email already exists")

@router.put("/update_user/{email}/", status_code=200)
async def update_user_profile(email: str, user: User):
    # Check age to be greater than 18
    if user.age <= 18:
        raise HTTPException(status_code=400, detail="Age must be greater than 18")
    
    # Check phone number to have only digits
    if not str(user.mobile_number).isdigit():
        raise HTTPException(status_code=400, detail="Phone number must contain only digits")
    
    # Check birthday format (should be 'yyyy-mm-dd')
    if not re.match(r'^\d{2}-\d{2}-\d{4}$', user.birthday):
        raise HTTPException(status_code=400, detail="Invalid birthday format. Should be 'dd-mm-yyyy'")

    if update_user(email, user):
        return {"message": "User updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="User not found")

@router.delete("/delete_user/{email}/", status_code=200)
async def delete_user_profile(email: str):
    if delete_user(email):
        return {"message": "User deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="User not found")

@router.get("/get_user/{email}/", response_model=User)
async def get_user_profile(email: str):
    user = get_user_by_email(email)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
