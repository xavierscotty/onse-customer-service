import os

from flask import Flask, jsonify


def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)

    if config is None:
        app.config.from_object(os.environ['APP_SETTINGS'])
    else:
        app.config.from_mapping(config)

    @app.route('/health')
    def hello_world():
        return jsonify({"message": "OK"})

    return app
