"""
URL Shortener - Unit Tests
Test suite for all API endpoints
"""

import pytest
from urlshortener.app import app
from urlshortener.models import db, URLMapping


@pytest.fixture
def test_health(client):
    """Test health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'healthy'


def test_shorten_valid_url(client):
    """Test shortening a valid URL"""
    response = client.post('/shorten', json={
        'url': 'https://www.example.com'
    })
    assert response.status_code == 201
    assert 'short_code' in response.json
    assert 'short_url' in response.json
    assert len(response.json['short_code']) == 7


def test_shorten_missing_url(client):
    """Test shortening without URL parameter"""
    response = client.post('/shorten', json={})
    assert response.status_code == 400
    assert 'error' in response.json


def test_shorten_invalid_url(client):
    """Test shortening an invalid URL"""
    response = client.post('/shorten', json={
        'url': 'not-a-valid-url'
    })
    assert response.status_code == 400
    assert 'error' in response.json


def test_shorten_duplicate_url(client):
    """Test shortening the same URL twice"""
    url = 'https://www.example.com'
    
    response1 = client.post('/shorten', json={'url': url})
    short_code1 = response1.json['short_code']
    
    response2 = client.post('/shorten', json={'url': url})
    short_code2 = response2.json['short_code']
    
    assert response2.status_code == 200
    assert short_code1 == short_code2


def test_redirect_valid_short_code(client):
    """Test redirecting with valid short code"""
    response = client.post('/shorten', json={
        'url': 'https://www.example.com'
    })
    short_code = response.json['short_code']
    
    response = client.get(f'/{short_code}', follow_redirects=False)
    assert response.status_code == 302
    assert response.location == 'https://www.example.com'


def test_redirect_invalid_short_code(client):
    """Test redirecting with invalid short code"""
    response = client.get('/invalid123', follow_redirects=False)
    assert response.status_code == 404


def test_stats_valid_short_code(client):
    """Test getting stats for valid short code"""
    response = client.post('/shorten', json={
        'url': 'https://www.example.com'
    })
    short_code = response.json['short_code']
    
    response = client.get(f'/stats/{short_code}')
    assert response.status_code == 200
    assert response.json['short_code'] == short_code
    assert response.json['original_url'] == 'https://www.example.com'
    assert 'clicks' in response.json


def test_stats_invalid_short_code(client):
    """Test getting stats for invalid short code"""
    response = client.get('/stats/invalid123')
    assert response.status_code == 404