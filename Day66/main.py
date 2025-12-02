import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean


SECRET_KEY ="TopSecretAPIKey"
app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random", methods=["GET"])
def get_random():
    cafe_db = db.session.execute(db.select(Cafe))
    random_cafe = random.choice(cafe_db.scalars().all())
    return jsonify(cafe={
        "id": random_cafe.id,
        "name": random_cafe.name,
        "map_url": random_cafe.map_url,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,
        "seats": random_cafe.seats,
        "has_toilet": random_cafe.has_toilet,
        "has_wifi": random_cafe.has_wifi,
        "has_sockets": random_cafe.has_sockets,
        "can_take_calls": random_cafe.can_take_calls,
        "coffee_price": random_cafe.coffee_price,
    })

@app.route("/all")
def all_route():
    cafe_db = db.session.execute(db.select(Cafe))
    all_cafes = cafe_db.scalars().all()
    cafe_list= []
    for cafe in all_cafes:
        cafe_json={
        "id": cafe.id,
        "name": cafe.name,
        "map_url": cafe.map_url,
        "img_url": cafe.img_url,
        "location": cafe.location,
        "seats": cafe.seats,
        "has_toilet": cafe.has_toilet,
        "has_wifi": cafe.has_wifi,
        "has_sockets": cafe.has_sockets,
        "can_take_calls": cafe.can_take_calls,
        "coffee_price": cafe.coffee_price,
        }
        cafe_list.append(cafe_json)
    return jsonify(cafes=cafe_list)

# HTTP GET - Read Record
@app.route("/search")
def search():

    try:
        loc = request.args.get("loc")
        loc_db = db.session.execute(db.select(Cafe).where(Cafe.location == loc)).scalar()
        return jsonify(cafe={
        "id": loc_db.id,
        "name": loc_db.name,
        "map_url": loc_db.map_url,
        "img_url": loc_db.img_url,
        "location": loc_db.location,
        "seats": loc_db.seats,
        "has_toilet": loc_db.has_toilet,
        "has_wifi": loc_db.has_wifi,
        "has_sockets": loc_db.has_sockets,
        "can_take_calls": loc_db.can_take_calls,
        "coffee_price": loc_db.coffee_price,
        })
    except:
        return jsonify(error={
            "Not Found": "Sorry, we don't have a cafe at that location"
        })

# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add():
    try:
        new_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("location"),
            seats=request.form.get("seats"),
            has_toilet=bool(int(request.form.get("has_toilet"))),
            has_wifi=bool(int(request.form.get("has_wifi"))),
            has_sockets=bool(int(request.form.get("has_sockets"))),
            can_take_calls=bool(int(request.form.get("can_take_calls"))),
            coffee_price=request.form.get("coffee_price"),
        )
        print("hello")
        db.session.add(new_cafe)
        db.session.commit()

        return jsonify(response={"success": "New cafe added successfully!"})
    except:
        return jsonify(error={
            "Failed": "Sorry, couldn't update"
        })


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update(cafe_id):
    try:
        price_to_update = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
        new_price = request.args.get("new_price")
        price_to_update.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price"})
    except AttributeError:
        return jsonify(error={
            "Not Found": "A cafe with that id was not found"
        })

@app.route("/report-closed/<cafe_id>")
def delete(cafe_id):
    key = request.args.get("api-key")
    if key == SECRET_KEY:
        try:
            cafe_to_delete = db.session.execute(db.select(Cafe).where(Cafe.id==cafe_id)).scalar()
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response={
                "success":"cafe deleted successfully"
            })
        except AttributeError:
            return jsonify(error={
            "Not Found": "A cafe with that id was not found"
        })
    else:
        return jsonify({"error": "Sorry, that's not allowed. Make sure you have the correct api_key"})

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
