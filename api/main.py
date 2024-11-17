from flask import Flask, request, jsonify
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

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
class NewCats(db.Model):
    __tablename__ = "new_cats"
    id = db.Column(db.Integer, primary_key=True)
    owner_name = db.Column(db.String, nullable=True)
    phone_number = db.Column(db.String, nullable=True)
    cat_type = db.Column(db.String, nullable=True)
    where_found = db.Column(db.String, nullable=True)
    reason_to_give_to_shelter = db.Column(db.String, nullable=True)
    breed = db.Column(db.String, nullable=True)
    gender = db.Column(db.String, nullable=True)
    cat_name = db.Column(db.String, nullable=True)

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

@app.route("/get-cat-in-shelter-html-page/<int:cat_id>")
def get_cat_html_page_by_id(cat_id):
    cat = CatsInShelter.query.get(cat_id)
    
    if not cat:
        return jsonify({'error': 'Cat not found'}), 404
    
    return """<!DOCTYPE html>
<html lang="ru">
    <head>
        <meta charset="utf-8">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap" rel="stylesheet">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,100..800;1,100..800&display=swap" rel="stylesheet">
        <link href="../style.css" rel="stylesheet">
        <title>Забрать из приюта</title>
    </head>
    <body>
        <div class="mobile-menu">
            <button class="close-menu">X</button>
            <a href="../giveout.html" class="menu-button">Отдать в приют</a>
            <a href="../takeFromShelter.html" class="menu-button">Взять из приюта</a>
            <a href="../index.html" class="menu-button">Связаться с нами</a>
        </div>
        <div class="takeFS">
            <header class="takeFS-header">
                <a href="../index.html" class="name">Лехин дом</a>
                <ul class="mini-nav">
                    <li class="mini-nav-item">
                        <a href="../giveout.html">Отдать в приют</a>
                    </li>
                    <li class="mini-nav-item">
                        <a href="../takeFromShelter.html">Взять из приюта</a>
                    </li>
                </ul>
                <div class="phone-circle">
                    <a href="#" class="call">
                        <img src="../img/Icon_call.svg" width="41" height="41">
                    </a>
                </div>
                <button class="menu-but">
                    <img src="../img/Icon_menu.svg" width="46" height="46">
                </button>
            </header>
            <main>
                <section class="individual-cat-page">
                    <h1>Забрать из приюта</h1>
                    <div class="cat-page-graybox">
                        <div class="individual-gallery">
                            <div class="active-image-container">
                                <img id="active-image" src="../img/image2.jpg" alt="Активное изображение">
                            </div>
                            <ul class="thumbnail-container">
                                <li><img class="thumbnail active" src="../img/image2.jpg" alt="Изображение 1"></li>
                                <li><img class="thumbnail" src="../img/image1.png" alt="Изображение 2"></li>
                                <li><img class="thumbnail" src="../img/image2.jpg" alt="Изображение 3"></li>
                            </ul>
                        </div>
                        <div class="graybox-text-block">
                            <h2 class="cat-name">Test</h2>
                            <p class="age">test</p>
                            <p class="cat-page-description">test</p>
                            <p class="additional-info">test</p>
                            <p class="graybox-tel">test</p>
                        </div>
                    </div>
                    <h2>Забрать Лёху</h2>
                    <div class="cat-ancet">
                        <div class="input">
                            <input type="text" id="fio" name="fio" placeholder="ФИО" required>
                        </div>
                        <div class="input">
                            <input type="text" id="phone" name="phone" placeholder="Телефон" required>
                        </div>
                        <div class="input">
                            <input type="text" id="time" name="time" placeholder="Когда удобно забрать" required>
                        </div>
                        <div class="cat-send">
                            <button type="submit" class="cat-send-text">Оставить заявку</button>
                        </div>
                    </div>
                </section>
                <section class="giveout-contacts">
                    <h2>Свяжитесь с нами</h2>
                    <p class="gray">по интересующим вас вопросам</p>
                    <a href="tel:+1234567890" class="tel">+7 982 672 17 58</a>
                </section>
            </main>
        </div>
    </body>
    <script src="catScript.js"></script>
</html>"""


@app.route("/get-new-cats")
def get_new_cats():
    cats = NewCats.query.all()
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
    new_cat_application = NewCats(
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

if __name__ == '__main__':
    # Запуск приложения с Waitress
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
