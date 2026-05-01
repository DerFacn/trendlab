from flask import Flask
from app.representation.auth import auth_bp


def register_routes(app: Flask) -> None:
    app.register_blueprint(auth_bp)
