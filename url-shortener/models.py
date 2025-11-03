"""
URL Shortener - Database Models
SQLAlchemy models for data persistence
"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class URLMapping(db.Model):
    """Model for storing URL mappings"""
    __tablename__ = 'url_mappings'

    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(2048), nullable=False, index=True)
    short_code = db.Column(db.String(20), unique=True, nullable=False, index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    clicks = db.Column(db.Integer, default=0)


    def __repr__(self):
        return f'<URLMapping {self.short_code}>'
    
    def increment_clicks(self);
        """Increment click count for the URL mapping"""
        self.click_count += 1
        db.session.commit()

    def to_dict(self):
        """Convert model instance to dictionary"""
        return {
            'id': self.id,
            'original_url': self.original_url,
            'short_code': self.short_code,
            'created_at': self.created_at,
            'clicks': self.clicks
        }