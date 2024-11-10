from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.database import SessionLocal
from api.models import Pet

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/pets")
def read_pets(db: Session = Depends(get_db)):
    pets = db.query(Pet).all()
    return pets


