"""Blueprint for API module of the parent application

Responsible for initializing the modules and routes
within the core api.
"""
from flask import Blueprint

api = Blueprint('api', __name__)

from . import classifier
