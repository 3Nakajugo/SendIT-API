from flask import Flask
from config import app_config

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'
