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
