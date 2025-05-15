from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy
from app.models import post, tag, tags
from app import app


@app.route('/')
def home():
  return 'test this app '
