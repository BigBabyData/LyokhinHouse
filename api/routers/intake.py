from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from api.database import SessionLocal
from api.models import Intake

router = APIRouter()

class IntakeRequest(BaseModel):
    full_name: str
    phone: str
    cat_type: str
    reason: str

@router.post("/intake")
def add_intake(intake: IntakeRequest, db: Session = Depends(get_db)):
    new_intake = Intake(**intake.dict())
    db.add(new_intake)
    db.commit()
    return {"status": "success"}
