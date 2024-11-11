from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

class CatsInShelter(db.Model):
    __tablename__ = "cats_in_shelter"
    id = db.Column(db.Integer, primary_key=True)
    cat_name = db.Column(db.String, nullable=True)
    cat_age = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String, nullable=True)
    image_url = db.Column(db.String, nullable=True)
    time_at_shelter = db.Column(db.Integer, nullable=True)
    arrival_date = db.Column(db.Date, nullable=True)

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
    return "LyokhinHouse API is now running!"

@app.route("/get-cats-in-shelter")
def get_cats():
    cats = CatsInShelter.query.all()
    return {'cats_in_shelter': [(cat.cat_name, cat.id) for cat in cats]}

@app.route("/get-new-cats")
def get_new_cats():
    return "test"

if __name__ == '__main__':
    # app.run()

    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)