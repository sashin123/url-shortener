# URL Shortener - Project one of getting to know Python.

A Python REST API service that converts long URLs into short, memorable links.

## Features

- Convert long URLs to short codes
- Track click statistics
- Simple REST API

## Tech Stack

- **Framework**: Flask
- **Database**: SQLite
- **Language**: 3.12.10

## Setup

### Prerequisites
- Python 3.12.10 (based off my testing, there are a lot of issues if using 3.13)
- pip

### Installation

1. Clone the repository:
git clone https://github.com/sashin123/url-shortener.git
cd url-shortener

2. Create and activate virtual environment:
python3 -m venv venv
source venv/bin/activate // On Windows: venv\Scripts\activate // gitbash: venv/Scripts/activate

3. Install backend dependencies:
pip install -r requirements.txt

4. Install Frontend Dependencies:
npm install

5. Run each app
    -frontend: npm run dev
    -backend: python -m flask run --app urlshortener.app --port 5000
    both apps are connected using cors

6. Tests
    -backend: python -m pytest -v, implicitly call tests from root

## Development Status

- [x] Project setup
- [X] Database models
- [X] Core shortening logic
- [X] API endpoints
- [X] Testing

## License

MIT License