from flask import jsonify, Blueprint

customers = Blueprint('customers', __name__, url_prefix='/customers/')


@customers.route('/<string:customer_id>', methods=['GET'])
def get_customers(customer_id):
    if customer_id == '12345':
        return jsonify({
            'customerId': customer_id,
            'firstName': 'Joe',
            'surname': 'Bloggs'
        })
    else:
        return jsonify({
            'message': 'Not found'
        }), 404
