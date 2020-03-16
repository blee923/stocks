from flask import Flask

def create_app():
    app = Flask(__name__)

    from .quote import quoter

    app.register_blueprint(quoter)

    return app