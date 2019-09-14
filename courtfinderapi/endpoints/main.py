from flask import Blueprint
from flask_cors import CORS

main = Blueprint("main", __name__)

CORS(main) # enable CORS on the main blue print

@main.route("/", methods=["GET", "POST"])
def index():
    return {"Success": "You've hit the courtfinder api"}

@main.app_errorhandler(403)
@main.app_errorhandler(404)
@main.app_errorhandler(405)
@main.app_errorhandler(500)
def error_404(error):
    return {"error": "resource not found"}
