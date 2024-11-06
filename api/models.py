from sqlalchemy import Column, Integer, String, Date
from .database import Base

class Pet(Base):
    __tablename__ = "pets_table"
    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String)
    age = Column(Integer)
    description = Column(String)
    image_url = Column(String)
    time_at_shelter = Column(Integer)
    arrival_date = Column(Date)

class IntakeRequest(Base):
    __tablename__ = "intake_requests"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    phone = Column(String)
    cat_type = Column(String)
    reason = Column(String)
