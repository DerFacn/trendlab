from flask import Flask, render_template
from app.config import Config
from app.core.database import Database

db = Database()


def create_app(config_obj=Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_obj)

    db.init_app(app)
    db.init_db()

    @app.route('/')
    def index():
        return render_template('index.html')
    
    return app
