from courtfinderapi.app import app
from .main import main
from .courts import courts
from .users import users

app.register_blueprint(main)
app.register_blueprint(courts)
app.register_blueprint(users)
