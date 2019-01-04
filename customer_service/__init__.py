import os

from flask import Flask, jsonify


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/health', methods=['GET'])
    def get_health():
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
