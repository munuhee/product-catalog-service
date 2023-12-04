"""Product database model."""

from datetime import datetime
from app import db

class Product(db.Model):
    """Product class representing items in the database."""

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    dimension = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        """Representation of Product object."""
        return f"<product:{self.id}, name:'{self.name}'>"
