from flask import Blueprint

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    pass  # À implémenter plus tard

@main_bp.route('/about')
def about():
    pass

@main_bp.route('/sections')
def sections():
    pass

@main_bp.route('/news')
def news():
    pass

@main_bp.route('/results')
def results():
    pass

@main_bp.route('/contact')
def contact():
    pass
