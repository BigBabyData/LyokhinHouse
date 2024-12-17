from flask import Flask, request, jsonify
from flask_cors import CORS
from config import Config
from flask_sqlalchemy import SQLAlchemy
import os

ADMIN_TOKEN = os.environ.get("ADMIN_TOKEN")

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

CORS(app)

# Модель для котов в приюте
class CatsInShelter(db.Model):
    __tablename__ = "cats_in_shelter"
    id = db.Column(db.Integer, primary_key=True)
    cat_name = db.Column(db.String, nullable=True)
    cat_age = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String, nullable=True)
    image_url = db.Column(db.String, nullable=True)
    time_at_shelter = db.Column(db.Integer, nullable=True)
    arrival_date = db.Column(db.Date, nullable=True)

# Модель для новых заявок
class NewCatsApplications(db.Model):
    __tablename__ = "new_cats_applications"
    id = db.Column(db.Integer, primary_key=True)
    owner_name = db.Column(db.String, nullable=True)
    phone_number = db.Column(db.String, nullable=True)
    cat_type = db.Column(db.String, nullable=True)
    where_found = db.Column(db.String, nullable=True)
    reason_to_give_to_shelter = db.Column(db.String, nullable=True)
    breed = db.Column(db.String, nullable=True)
    gender = db.Column(db.String, nullable=True)
    cat_name = db.Column(db.String, nullable=True)

class TakeCatApplication(db.Model):
    __tablename__ = "take_cat_applications"
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String, nullable=True)
    phone_number = db.Column(db.String, nullable=True)
    when_pick_up = db.Column(db.String, nullable=True)

@app.route('/')
def index():
    return {"status": "LyokhinHouse API is now running!"}

@app.route("/get-cats-in-shelter")
def get_cats():
    cats = CatsInShelter.query.all()
    return {"cats_in_shelter": [
        {"id": cat.id,
         "cat_name": cat.cat_name,
         "cat_age": cat.cat_age,
         "description": cat.description,
         "image_url": cat.image_url,
         "time_at_shelter": cat.time_at_shelter,
         "arrival_date": cat.arrival_date
        }
        for cat in cats]
    }

@app.route("/get-cat-in-shelter/<int:cat_id>", methods=["GET"])
def get_cat_by_id(cat_id):
    # Получение кота по ID
    cat = CatsInShelter.query.get(cat_id)
    
    if not cat:
        return jsonify({'error': 'Cat not found'}), 404

    return {
        "id": cat.id,
        "cat_name": cat.cat_name,
        "cat_age": cat.cat_age,
        "description": cat.description,
        "image_url": cat.image_url,
        "time_at_shelter": cat.time_at_shelter,
        "arrival_date": cat.arrival_date,
    }

# @app.route("/get-cat-in-shelter-html-page/<int:cat_id>")
# def get_cat_html_page_by_id(cat_id):
#     cat = CatsInShelter.query.get(cat_id)
    
#     if not cat:
#         return jsonify({'error': 'Cat not found'}), 404
    
#     return 

@app.route("/get-new-cats", methods=["GET"])
def get_new_cats():
    admin_token = request.headers.get('Token')

    if admin_token != ADMIN_TOKEN:
        return {"Acces denied"}

    cats = NewCatsApplications.query.all()
    
    return {"new_cats": [
        {"id": cat.id,
         "owner_name": cat.owner_name,
         "phone_number": cat.phone_number,
         "cat_type": cat.cat_type,
         "where_found": cat.where_found,
         "reason_to_give_to_shelter": cat.reason_to_give_to_shelter,
         "breed": cat.breed,
         "gender": cat.gender,
         "cat_name": cat.cat_name
        }
        for cat in cats]
    }

@app.route("/submit-application", methods=["POST"])
def submit_application():
    # Получение данных из тела запроса
    data = request.get_json()

    owner_name = data.get("owner_name")
    phone_number = data.get("phone_number")
    cat_type = data.get("cat_type")
    where_found = data.get("where_found")
    reason_to_give_to_shelter = data.get("reason_to_give_to_shelter")
    breed = data.get("breed")
    gender = data.get("gender")
    cat_name = data.get("cat_name")

    # Создание новой записи
    new_cat_application = NewCatsApplications(
        owner_name=owner_name,
        phone_number=phone_number,
        cat_type=cat_type,
        where_found=where_found,
        reason_to_give_to_shelter=reason_to_give_to_shelter,
        breed=breed,
        gender=gender,
        cat_name=cat_name,
    )
    
    try:
        db.session.add(new_cat_application)
        db.session.commit()
        return jsonify({'message': 'Application added successfully!', 'id': new_cat_application.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# curl -X POST https://lyokhinhouse-api.up.railway.app/submit-application \
# -H "Content-Type: application/json" \
# -d '{
#     "owner_name": "Ваше имя",
#     "phone_number": "Ваш номер телефона",
#     "cat_type": "Тип кошки",
#     "where_found": "Место нахождения",
#     "reason_to_give_to_shelter": "Причина передачи в приют",
#     "breed": "Порода",
#     "gender": "Пол",
#     "cat_name": "Имя кошки"
# }'

@app.route("/submit-take-cat", methods=["POST"])
def take_cat():
    data = request.get_json()

    id = data.get("id")
    full_name = data.get("full_name")
    phone_number = data.get("phone_number")
    when_pick_up = data.get("when_pick_up")

    take_cat_application = TakeCatApplication(
        id=id,
        full_name=full_name,
        phone_number=phone_number,
        when_pick_up=when_pick_up
    )

    try:
        db.session.add(take_cat_application)
        db.session.commit()
        return jsonify({'message': 'Application added successfully!', 'id': take_cat_application.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route("/get-take-cats-applications", methods=["GET"])
def get_take_cats_applications():
    admin_token = request.headers.get('Token')

    if admin_token != ADMIN_TOKEN:
        return {"Acces denied"}
    
    applications = TakeCatApplication.query.all()
    
    return {"take-cats-applications": [
        {"id": application.id,
         "full_name": application.full_name,
         "phone_number": application.phone_number,
         "when_pick_up": application.when_pick_up
        }
    for application in applications]}

# curl -X POST https://lyokhinhouse-api.up.railway.app/submit-take-cat \
# -H "Content-Type: application/json" \
# -d '{
#     "full_name": "Иван Иванов",
#     "phone_number": "+1234567890",
#     "when_pick_up": "2023-10-01"
# }'


if __name__ == '__main__':
    # Запуск приложения с Waitress
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)