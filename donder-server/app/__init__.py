import os

from flask import Flask
from .db_setup import init_db 

def create_app():
    app = Flask(__name__)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    with app.app_context():
        init_db()
        print("DB Initialized")

    return app