from flask import Flask
from flask_restful import Api
from src.routes.endpoints import initialize_endpoints
from src.entities.Base import db
import os

def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:jogadornumero01@localhost:5432/f1db",
    )

    db.init_app(app)

    api = Api(app, prefix="/api")
    initialize_endpoints(api)

    return app
