# app/__init__.py
import flask
from flask import Flask
from config import Config
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config.from_object(Config)


# 最后才导入防止循环导入
from application import routes
