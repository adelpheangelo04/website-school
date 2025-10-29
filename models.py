from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    # Structure de base : id, username, email, password_hash, role
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), default='user')

class News(db.Model):
    # Structure : id, title_fr, title_en, content_fr, content_en, image_path, created_at
    id = db.Column(db.Integer, primary_key=True)
    title_fr = db.Column(db.String(200), nullable=False)
    title_en = db.Column(db.String(200))
    content_fr = db.Column(db.Text, nullable=False)
    content_en = db.Column(db.Text)
    image_path = db.Column(db.String(300))
    created_at = db.Column(db.DateTime, default=db.func.now())

class Result(db.Model):
    # Structure : id, year, success_rate, description_fr, description_en
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    success_rate = db.Column(db.Float)
    description_fr = db.Column(db.Text)
    description_en = db.Column(db.Text)

class GalleryImage(db.Model):
    # Structure : id, title_fr, title_en, image_path, category
    id = db.Column(db.Integer, primary_key=True)
    title_fr = db.Column(db.String(200))
    title_en = db.Column(db.String(200))
    image_path = db.Column(db.String(300), nullable=False)
    category = db.Column(db.String(50))

class ContactMessage(db.Model):
    # Structure : id, name, email, message, is_read, created_at
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)
    is_read = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=db.func.now())

class ThemeSettings(db.Model):
    # Structure : id, primary_color, secondary_color, accent_color
    id = db.Column(db.Integer, primary_key=True)
    primary_color = db.Column(db.String(7), default='#007bff')  # Hex color
    secondary_color = db.Column(db.String(7), default='#6c757d')
    accent_color = db.Column(db.String(7), default='#28a745')
