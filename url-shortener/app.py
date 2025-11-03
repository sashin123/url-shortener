"""
URL Shortener - Flask App
Main Entry Point of app
"""

from flask import Flask, request, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

from models import db, URLMapping
from utils import generate_short_code, is_valid_url
from config import config


# Load env variables
load_dotenv()

#initialize flask app
app = Flask(__name__)

#getting config based on environment
env = os.getenv('FLASK_ENV', 'development')
app.config.from_object(config[env]) 

#initialize database with app
db.init_app(app)

#create tables 
with app.app_context():
    db.create_all()


#api routes
#checks app health, basically ensures the app is up and running
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200


#Creates a shortened URL from a given original URL(long URL)
@app.route('/shorten', methods=['POST'])
def shorten_url():
    try:
        data = request.get_json()

        if not data or 'url' not in data:
            return jsonify({'error': 'Missing required field: url'}), 400
        
        original_url = data['url']

        if not is_valid_url(original_url):
            return jsonify({'error': 'Invalid URL format'}), 400

        #Checks if URL is already shortened
        existing = URLMapping.query.filter_by(original_url=original_url).first()

        # Ensure uniqueness, if short code already exists, generate a new one with 8 random bytes appended
        while URLMapping.query.filter_by(short_code=short_code).first():
            short_code = generate_short_code(original_url + str(os.urandom(8)))

        #Create and save the new URL mapping
        mapping = URLMapping(original_url=original_url, short_code=short_code)
        db.session.add(mapping)
        db.session.commit()

        return jsonify({
            'message': 'URL Shortened Successfully,',
            'short_code': short_code,
            'short_url': f'https://localhost:5000/{short_code}',
            original_url: original_url
        }), 201
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    

@app.route('/<short_code>', methods=['GET'])
def redirect_url(short_code):
    try:
        mapping = URLMapping.query.filter_by(short_code=short_code).first()
        
        if not mapping:
            return jsonify({'error': 'Short URL not found'}), 404

        
        #increment click counter
        mapping.increment_clicks()


        #redirect to original URL
        return redirect(mapping.original_url), 301
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    


#get statistics for a given short url
@app.route('/stats/<short_code>', methods=['GET'])
def get_stats(short_code):
    try:
        mapping = URLMapping.query.filter_by(short_code=short_code).first()

        if not mapping:
            return jsonify({'error:', 'Short URL not found'}), 404
        
        return jsonify(mapping.to_dict()), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)