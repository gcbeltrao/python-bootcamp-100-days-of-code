import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

app = Flask(__name__)


class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


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
        return {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def random_cafe():
    cached_cafes = db.session.execute(db.select(Cafe)).scalars()

    coffee_shop_list = [cafe.to_dict() for cafe in cached_cafes]
    random_cafe = random.choice(coffee_shop_list)
    return jsonify(random_cafe)


@app.route("/all")
def all_cafe():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name)).scalars()
    return jsonify(cafes=[cafe.to_dict() for cafe in result])


@app.route("/search")
def search():
    query_location = request.args.get("loc")
    result = db.session.execute(
        db.select(Cafe).where(Cafe.location == query_location)
    ).scalars()
    cafes = list(result)

    if cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes])

    return (
        jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}),
        404,
    )


@app.route("/add", methods=["POST"])
def add():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        seats=request.form.get("seats"),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        has_sockets=bool(request.form.get("sockets")),
        can_take_calls=bool(request.form.get("calls")),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe_to_update = db.session.execute(
        db.select(Cafe).where(Cafe.id == cafe_id)
    ).scalar()
    if cafe_to_update:
        cafe_to_update.coffee_price = new_price
        db.session.commit()
        return jsonify({"succes": "Successfully updated the price."})
    return jsonify(
        error={"Not found": "Sorry, a cafe with that id was not found in the database."}
    )


@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api_key")
    cafe_to_delete = db.session.execute(
        db.select(Cafe).where(Cafe.id == cafe_id)
    ).scalar()
    if cafe_to_delete:
        if api_key == "TopSecretAPIKey":
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify({"succes": "Successfully deleted the cafe."})
        return jsonify(
            {
                "error": "Sorry, that's not allowed. Make sure you have the correct api_key."
            }
        )
    return jsonify(
        error={"Not found": "Sorry, a cafe with that id was not found in the database."}
    )


if __name__ == "__main__":
    app.run(debug=True)
