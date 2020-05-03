import os


class Config(object):
    # Flask及其一些扩展使用密钥的值作为加密密钥，用于生成签名或令牌。
    # Flask-WTF插件使用它来保护网页表单免受名为Cross-Site Request Forgery或CSRF
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
