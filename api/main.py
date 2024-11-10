from flask import Flask
import config as Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile(Config)
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

@app.route('/')
def index():
    return "LyokhinHouse API is now running!"

@app.route('/get-cats')
def get_cats():
    cats = CatsInShelter.query.all()
    return {'cats_in_shelter': [cat.cat_name for cat in cats]}

if __name__ == '__main__':
    # app.run()

    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)