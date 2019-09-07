from courtfinderapi.app import app
from .courts import courts


app.register_blueprint(courts)
