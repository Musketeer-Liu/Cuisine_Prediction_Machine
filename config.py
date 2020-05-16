import os


class Config(object):
    # Developing Mode, Mutually Exclusive with Production
    FLASK_ENV='development'
    # # Production Mode, Mutually Exclusive with Development
    # FLASK_ENV='production'

    # Flask-WTF use SECRET_KEY for Encryption Token to aviod Cross-Site Request Forgery (CSRF)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    CORS_HEADERS = 'Content-Type'
