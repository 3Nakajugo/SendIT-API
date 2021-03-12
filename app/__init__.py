from flask import Flask
from config import app_config

app = Flask(__name__)

from app.auth import auth_view
