import os


class Config(object):
    # 开发模式下使用这个参数，否则将这行Comment掉，即变为生产环境
    FLASK_ENV='development'

    # Flask-WTF use SECRET_KEY for Encryption Token to aviod Cross-Site Request Forgery (CSRF)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
