from flask import Blueprint, jsonify
from flask_cors import CORS

from courtfinderapi.app import session, client
from courtfinderapi.models.courts import Court

courts = Blueprint("courts", __name__)

CORS(courts) # enable CORS on the courts blue print

@courts.route("/courts", methods=["GET", "POST"])
def list_courts():
    courts = session.query(Court).all()
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
    if court:
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
            "average_rating": court.average_rating,
            "reviews": { review.id : {
                    "username": review.username,
                    "rating": review.rating,
                    "review": review.review,
                    "date": review.date
                } for review in court.reviews
            },
            "image_urls": get_images(court.id)
        }

        return jsonify(court)
    else:
        return {"error": "court not found"}


def get_URL(file_name):
    return client.generate_presigned_post(Bucket='courtfinder', Key=file_name)

def get_images(court):
    try:
        prefix = 'courts/' + str(court) + '/'
        result = client.list_objects(Bucket='courtfinder', Prefix=prefix, Delimiter='/')

        image_urls = []
        skipthedir = 0  # becuase the directory itself is also retrived we want to skip it
        for object in result.get('Contents'):
            if skipthedir > 0:
                url = get_URL(object.get('Key'))
                image_urls.append(url.get('url') + '/' + url.get('fields')['key'])
            else:
                skipthedir += 1

        return image_urls

    except Exception as e:
        print(e)
        return jsonify({"error": "There was a problem with the data you provided."})
