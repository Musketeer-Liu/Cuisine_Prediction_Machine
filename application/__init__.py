# app/__init__.py
from flask import Flask
from config import Config


app = Flask(__name__)
app.config.form_object(Config)


# 最后才导入防止循环导入
from application import routes
