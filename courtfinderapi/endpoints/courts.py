from flask import Blueprint, jsonify
from courtfinderapi.app import session
from courtfinderapi.models.courts import Court 

courts = Blueprint("courts", __name__)

@courts.route("/courts", methods=["GET", "POST"])
def list_courts():
    courts = session.query(Court).all()
    print(courts)
    courts = { court.id : {
        "name": court.name,
        "address": court.address,
        "total_courts": court.total_courts,
        "total_visits": court.total_visits,
        "lights": court.lights,
        "membership_required": court.membership_required,
        "description": court.description,
        "latitude": float(court.latitude),
        "longitude": float(court.longitude),
        "total_ratings": court.total_ratings,
        "average_rating": court.average_rating
    }
    for court in courts }

    return jsonify(courts)

@courts.route("/court/<id>", methods=["GET"])
def list_court(id):
    court = session.query(Court).filter_by(id=id).first()
    court = {
        "id": court.id,
        "name": court.name,
        "address": court.address,
        "total_courts": court.total_courts,
        "total_visits": court.total_visits,
        "lights": court.lights,
        "membership_required": court.membership_required,
        "description": court.description,
        "latitude": float(court.latitude),
        "longitude": float(court.longitude),
        "total_ratings": court.total_ratings,
        "average_rating": court.average_rating
    }

    return jsonify(court)
