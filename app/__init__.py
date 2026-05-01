from flask import Flask, render_template
from app.config import Config


def create_app(config_obj=Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_obj)

    @app.route('/')
    def index():
        return render_template('index.html')
    
    return app
