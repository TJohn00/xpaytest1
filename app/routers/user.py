from bson import ObjectId
from fastapi import APIRouter, Form, HTTPException, UploadFile
from app.db import SessionLocal, mongo_collection
from sqlalchemy.orm import Session
from app.models import User

router = APIRouter()


@router.post("/register/")
async def register_user(
    full_name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    phone: str = Form(...),
    profile_picture: UploadFile = Form(...),
):
    try:
        with SessionLocal() as db:
            profile_picture_data = await profile_picture.read()
            new_user = create_user_db(
                db, full_name, email, phone, password, profile_picture_data)
            return {"user_id": new_user.id, "message": "User registered successfully"}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/user/{user_id}/")
def get_user(user_id: int):
    try:
        with SessionLocal() as db:
            user = db.query(User).filter(User.id == user_id).first()
            if user is None:
                raise HTTPException(status_code=404, detail="User not found")
            return user
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")


def create_user_db(db: Session, full_name: str, email: str, phone: str, password: str, profile_picture_data: bytes) -> User:
    existing_user = db.query(User).filter((User.email == email) | (User.phone == phone)).first()
    if existing_user:
        raise HTTPException(
            status_code=400, detail="Email or phone already registered")
    profile_picture_id = str(ObjectId())
    mongo_collection.insert_one(
        {"_id": profile_picture_id, "picture": profile_picture_data})
    new_user = User(
        full_name=full_name,
        email=email,
        phone=phone,
        password=password,
        profile_picture_id=profile_picture_id,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
