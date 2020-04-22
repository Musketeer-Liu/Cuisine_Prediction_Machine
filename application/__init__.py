# app/__init__.py
from flask import Flask

app = Flask(__name__)

# 最后才导入防止循环导入
from application import routes
