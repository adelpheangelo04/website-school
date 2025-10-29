from flask import Blueprint

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login')
def login():
    pass  # À implémenter plus tard

@auth_bp.route('/profile')
def profile():
    pass
