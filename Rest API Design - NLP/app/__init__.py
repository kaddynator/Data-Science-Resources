"""Initial module for the main application. Primary purpose is
to initialize the db variable, and to export the
create_app function. Used in app_instance.py to initialize
the application on launch.
"""
from flask import Flask, jsonify
import config
import logging


def create_app():
    """Creates the primary flask app. Responsible for

    1. Getting the configurations
    2. Initializing the database
    3. Adding an ES instance
    4. Registering sub app blueprints

    Returns
    -------
    Flask App
        The actual whole app
    """
    # Set main flask app
    logging.info('Initializing application')
    app = Flask(__name__)

    # Set up app configs
    logging.info('Initializing configurations')
    new_configs = config.generate_config()
    app.config.update(new_configs)
    app.secret_key = app.config['FLASK_SECRET']
    app.json_encoder = config.BetterEncoder

    logging.info('Registering blueprints')
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify(error=404, text=str(e)), 404

    @app.errorhandler(500)
    def server_error(e):
        return jsonify(error=500, text=str(e)), 500

    return app
