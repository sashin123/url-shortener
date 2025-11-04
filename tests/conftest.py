import sys
import os
import pytest

# Add parent directory to path so we can import url_shortener
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'url-shortener'))

from urlshortener.app import app
from urlshortener.models import db


@pytest.fixture
def client():
    """Create test client with test database"""
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()
