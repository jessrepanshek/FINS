from flask import Flask, render_template, session, redirect, request, url_for, g
from flask_session import Session
import secrets
import string

SESSION_TYPE = 'filesystem'


# UI class to organize all Flask code in an object-oriented framework
# - Jack, 10/18/2023
class UI:
    app = Flask(__name__)

    @staticmethod
    @app.route('/')
    def dashboard():
        return render_template('dashboard.html')

    @staticmethod
    @app.route('/login')
    def login():
        return render_template('login.html')

    @classmethod
    def run(cls):
        cls.app.secret_key = cls.gen_session_key()
        cls.app.config.from_object(__name__)
        Session(cls.app)
        cls.app.run()

    @staticmethod
    def gen_session_key():
        alphabet = string.ascii_letters + string.digits + string.punctuation
        key = ''.join(secrets.choice(alphabet) for i in range(16))
        return key


if __name__ == '__main__':
    UI.run()
