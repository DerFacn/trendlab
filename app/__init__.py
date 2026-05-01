from app.config import Config
from app.core.database import Database
from flask import Flask, render_template, request

db = Database()


def create_app(config_obj=Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_obj)

    db.init_app(app)

    from app import models  # to create database with models

    db.init_db()

    from app.core.passwords import generate_hash

    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/hasher')
    def password_hasher():
        password = request.args.get('password')
        return {"hashed_password": generate_hash(password)}
    
    return app
