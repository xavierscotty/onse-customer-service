import os

from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
from yaml import Loader, load

SWAGGER_URL = '/docs'

def create_app():
    app = Flask(__name__)

    @app.route('/health', methods=['GET'])
    def get_health():
        return jsonify({"message": "OK"})

    @app.route('/customers/<string:customerId>', methods=['GET'])
    def get_customers(customerId):

        if customerId == '12345':
            return jsonify({
                'customerId': customerId,
                'firstName': 'Joe',
                'surname': 'Bloggs'
            })
        else:
            return jsonify({
                'message': 'Not found'
            }), 404
        
    
    app.register_blueprint(setup_swagger(), url_prefix=SWAGGER_URL)

    return app

def setup_swagger():

    swagger_yml = load(open(get_app_base_path() + '/../swagger.yml', 'r'), Loader=Loader)

    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
        '',
        config={  # Swagger UI config overrides
            'app_name': "Customer Service API",
            'spec': swagger_yml
        },
    )

    return swaggerui_blueprint

def get_app_base_path():
   return os.path.dirname(os.path.realpath(__file__))


