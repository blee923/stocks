from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)

    from .quote import quoter

    app.register_blueprint(quoter)

    cors = CORS(app)

    return app