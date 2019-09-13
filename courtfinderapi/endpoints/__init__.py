from courtfinderapi.app import app
from .courts import courts
from .main import main

app.register_blueprint(courts)
app.register_blueprint(main)
