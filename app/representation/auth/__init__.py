from flask import Blueprint
from .routes import signup, login, logout

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

auth_bp.add_url_rule('/signup', 'signup', signup, methods=['GET', 'POST'])
auth_bp.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])
auth_bp.add_url_rule('/logout', 'logout', logout, methods=['GET'])
