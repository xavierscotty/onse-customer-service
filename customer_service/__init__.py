import os

from flask import Flask, jsonify, Response

import json


def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)

    if config is None:
        app.config.from_object(os.environ['APP_SETTINGS'])
    else:
        app.config.from_mapping(config)

    @app.route('/health')
    def hello_world():
        return jsonify({"message": "OK"})

    @app.route('/customers/<int:customer_id>', methods=['GET'])
    def get_customers(customer_id):

        if customer_id == 12345:
            return jsonify({
                'id': str(customer_id),
                'name': 'Joe',
                'surname': 'Blogg'
            })
        else:
            return jsonify({
                'message': 'Not found'
            }), 404

    return app
