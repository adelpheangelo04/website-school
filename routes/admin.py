from flask import Blueprint

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/dashboard')
def dashboard():
    pass  # À implémenter plus tard

@admin_bp.route('/news')
def list_news():
    pass

@admin_bp.route('/news/create')
def create_news():
    pass

@admin_bp.route('/news/<int:id>/edit')
def edit_news(id):
    pass

@admin_bp.route('/results')
def list_results():
    pass

@admin_bp.route('/results/<int:id>/edit')
def edit_result(id):
    pass

@admin_bp.route('/gallery')
def gallery():
    pass

@admin_bp.route('/messages')
def messages():
    pass

@admin_bp.route('/settings/theme')
def theme_settings():
    pass
