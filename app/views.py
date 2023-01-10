from flask import Blueprint, render_template, request, jsonify
from .models import db, Cafe
from random import choice


views = Blueprint('views', __name__)


@views.route("/")
def home():
    return render_template("index.html")


@views.route("/random")
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = choice(cafes)
    return jsonify(cafe=random_cafe.to_dict())


@views.route("/all")
def get_all_cafes():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafe=[cafe.to_dict() for cafe in cafes])


@views.route("/search")
def search_cafe_by_location():
    location = request.args.get("loc")
    cafe = db.session.query(Cafe).filter_by(location=location).first()
    if cafe:
        return jsonify(cafe=cafe.to_dict())
    else:
        return jsonify(error={"Not Found": "Sorry, no cafe listed at that location."})


@views.route("/add", methods=["POST"])
def add_new_cafes():
    new_cafe = Cafe(name=request.form.get("name"),
                    map_url=request.form.get("map_url"),
                    img_url=request.form.get("img_url"),
                    location=request.form.get("location"),
                    seats=request.form.get("seats"),
                    has_sockets=bool(request.form.get("has_sockets")),
                    has_toilet=bool(request.form.get("has_toilet")),
                    has_wifi=bool(request.form.get("has_wifi")),
                    can_take_calls=bool(request.form.get("can_take_calls")),
                    coffee_price=request.form.get("coffee_price"))
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})
