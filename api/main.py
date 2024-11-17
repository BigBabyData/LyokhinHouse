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
    data = request.get_json()

    owner_name = data.get_json("owner_name")
    phone_number = data.get_json("phone_number")
    cat_type = data.get_json("cat_type")
    where_found = data.get_json("where_found")
    reason_to_give_to_shelter = data.get_json("reason_to_give_to_shelter")
    breed = data.get_json("breed")
    gender = data.get_json("gender")
    cat_name = data.get_json("cat_name")

    new_cat_application = NewCats(owner_name=owner_name,
                                  phone_number=phone_number,
                                  cat_type=cat_type,
                                  where_found=where_found,
                                  reason_to_give_to_shelter=reason_to_give_to_shelter,
                                  breed=breed,
                                  gender=gender,
                                  cat_name=cat_name
                                  )
    
    try:
        db.session.add(new_cat_application)
        db.session.commit()
        return jsonify({'message': 'Application added successfully!', 'id': new_application.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # app.run()

    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)