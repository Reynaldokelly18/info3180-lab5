from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from . import db


class Movie(db.Model):
    __tablename__ = 'movie'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    poster = db.Column(db.String(100), nullable=False)  # Assuming poster path/name will be stored
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, title, description, poster, created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")):
        self.title=title
        self.description=description
        self.poster=poster
        self.created_at=created_at
    
def __repr__(self):
    return f"Movie('{self.title}', '{self.created_at}')"