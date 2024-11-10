from fastapi import FastAPI
from api.routers import pets, intake
from api.database import engine, Base

# Создаем все таблицы
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(pets.router)
app.include_router(intake.router)
