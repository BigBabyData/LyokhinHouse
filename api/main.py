import os
from typing import Any, Dict

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import Config
from waitress import serve
from functools import wraps

# Инициализация приложения
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
CORS(app, resources={
    r"/*": {"origins": "https://lyokhinhouse.up.railway.app"}
})

# Получение токена администратора из переменных окружения
ADMIN_TOKEN = os.environ.get("ADMIN_TOKEN")
if not ADMIN_TOKEN:
    raise ValueError("Не задан переменная окружения ADMIN_TOKEN")


# ---------------------------
# Модели БД
# ---------------------------
class CatsInShelter(db.Model):
    """
    Модель для котов, находящихся в приюте.
    """
    __tablename__ = "cats_in_shelter"

    id = db.Column(db.Integer, primary_key=True)
    cat_name = db.Column(db.String, nullable=True)
    cat_age = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String, nullable=True)
    image_url = db.Column(db.String, nullable=True)
    time_at_shelter = db.Column(db.Integer, nullable=True)
    arrival_date = db.Column(db.Date, nullable=True)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "cat_name": self.cat_name,
            "cat_age": self.cat_age,
            "description": self.description,
            "image_url": self.image_url,
            "time_at_shelter": self.time_at_shelter,
            "arrival_date": self.arrival_date.isoformat() if self.arrival_date else None
        }


class NewCatsApplications(db.Model):
    """
    Модель для заявок на добавление нового кота.
    """
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

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "owner_name": self.owner_name,
            "phone_number": self.phone_number,
            "cat_type": self.cat_type,
            "where_found": self.where_found,
            "reason_to_give_to_shelter": self.reason_to_give_to_shelter,
            "breed": self.breed,
            "gender": self.gender,
            "cat_name": self.cat_name
        }


class TakeCatApplication(db.Model):
    """
    Модель для заявок на забор кота из приюта.
    """
    __tablename__ = "take_cat_applications"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String, nullable=True)
    phone_number = db.Column(db.String, nullable=True)
    when_pick_up = db.Column(db.String, nullable=True)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "full_name": self.full_name,
            "phone_number": self.phone_number,
            "when_pick_up": self.when_pick_up
        }


# ---------------------------
# Декораторы
# ---------------------------
def admin_required(f):
    """
    Декоратор для маршрутов, требующих проверки токена администратора.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        admin_token = request.headers.get("Token")
        if admin_token != ADMIN_TOKEN:
            return jsonify({"error": "Access denied"}), 403
        return f(*args, **kwargs)
    return decorated_function


# ---------------------------
# Вспомогательные функции
# ---------------------------
def safe_commit(instance) -> Any:
    """
    Безопасное сохранение изменений в базу данных.
    Возвращает кортеж (успех: bool, ошибка: str или None).
    """
    try:
        db.session.add(instance)
        db.session.commit()
        return True, None
    except Exception as e:
        db.session.rollback()
        return False, str(e)


def safe_delete(instance) -> Any:
    """
    Безопасное удаление записи из базы данных.
    Возвращает кортеж (успех: bool, ошибка: str или None).
    """
    try:
        db.session.delete(instance)
        db.session.commit()
        return True, None
    except Exception as e:
        db.session.rollback()
        return False, str(e)


# ---------------------------
# Маршруты
# ---------------------------

@app.route("/", methods=["GET"])
def index():
    """
    Корневой маршрут для проверки состояния API.
    """
    return jsonify({"status": "LyokhinHouse API is now running!"}), 200


@app.route("/get_cats_in_shelter", methods=["GET"])
def get_cats():
    """
    Получить список всех котов в приюте.
    """
    cats = CatsInShelter.query.all()
    return jsonify({"cats_in_shelter": [cat.to_dict() for cat in cats]}), 200


@app.route("/get_cat_in_shelter/<int:cat_id>", methods=["GET"])
def get_cat_by_id(cat_id: int):
    """
    Получить информацию о конкретном коте по его ID.
    """
    cat = CatsInShelter.query.get(cat_id)
    if not cat:
        return jsonify({"error": "Cat not found"}), 404
    return jsonify(cat.to_dict()), 200


@app.route("/get_new_cats_applications", methods=["GET"])
@admin_required
def get_new_cats_applications():
    """
    Получить список всех заявок на новых котов (требует админ-токен).
    """
    cats = NewCatsApplications.query.all()
    return jsonify({"new_cats": [cat.to_dict() for cat in cats]}), 200


@app.route("/submit_application", methods=["POST"])
def submit_application():
    """
    Отправить заявку на добавление нового кота.
    Ожидается JSON с ключами: owner_name, phone_number, cat_type, where_found,
    reason_to_give_to_shelter, breed, gender, cat_name.
    """
    data = request.get_json() or {}
    if not data.get("owner_name") or not data.get("phone_number"):
        return jsonify({"error": "owner_name and phone_number are required"}), 400

    new_cat_application = NewCatsApplications(
        owner_name=data.get("owner_name"),
        phone_number=data.get("phone_number"),
        cat_type=data.get("cat_type"),
        where_found=data.get("where_found"),
        reason_to_give_to_shelter=data.get("reason_to_give_to_shelter"),
        breed=data.get("breed"),
        gender=data.get("gender"),
        cat_name=data.get("cat_name"),
    )

    success, error = safe_commit(new_cat_application)
    if not success:
        return jsonify({"error": error}), 500

    return jsonify({
        "message": "Application added successfully!",
        "id": new_cat_application.id
    }), 201


@app.route("/submit_take_cat", methods=["POST"])
def take_cat():
    """
    Отправить заявку на забор кота из приюта.
    Ожидается JSON с ключами: full_name, phone_number, when_pick_up.
    """
    data = request.get_json() or {}
    if not data.get("full_name") or not data.get("phone_number"):
        return jsonify({"error": "full_name and phone_number are required"}), 400

    take_cat_application = TakeCatApplication(
        full_name=data.get("full_name"),
        phone_number=data.get("phone_number"),
        when_pick_up=data.get("when_pick_up")
    )

    success, error = safe_commit(take_cat_application)
    if not success:
        return jsonify({"error": error}), 500

    return jsonify({
        "message": "Application added successfully!",
        "id": take_cat_application.id
    }), 201


@app.route("/get_take_cats_applications", methods=["GET"])
@admin_required
def get_take_cats_applications():
    """
    Получить список всех заявок на забор кота (требует админ-токен).
    """
    applications = TakeCatApplication.query.all()
    return jsonify({"take_cats_applications": [app.to_dict() for app in applications]}), 200


@app.route("/delete_new_cat_application/<int:app_id>", methods=["DELETE"])
@admin_required
def delete_new_cat(app_id: int):
    """
    Удалить заявку на нового кота по ID (требует админ-токен).
    """
    cat_application = NewCatsApplications.query.get(app_id)
    if cat_application is None:
        return jsonify({"error": "Application not found"}), 404

    success, error = safe_delete(cat_application)
    if not success:
        return jsonify({"error": error}), 500

    return jsonify({"message": "Application deleted successfully"}), 200


@app.route("/delete_take_cat_application/<int:app_id>", methods=["DELETE"])
@admin_required
def delete_take_cat(app_id: int):
    """
    Удалить заявку на забор кота по ID (требует админ-токен).
    """
    application = TakeCatApplication.query.get(app_id)
    if application is None:
        return jsonify({"error": "Application not found"}), 404

    success, error = safe_delete(application)
    if not success:
        return jsonify({"error": error}), 500

    return jsonify({"message": "Application deleted successfully"}), 200


# ---------------------------
# Точка входа
# ---------------------------
if __name__ == "__main__":
    # Предполагается, что база данных и таблицы уже инициализированы где-то ещё,
    # либо используются миграции. При необходимости можно добавить db.create_all().
    serve(app, host="0.0.0.0", port=5000)