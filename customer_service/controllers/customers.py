from flask import jsonify, Blueprint

from customer_service.model import commands
from customer_service.model.errors import CustomerNotFound

customers = Blueprint('customers', __name__, url_prefix='/customers/')


@customers.route('/<string:customer_id>', methods=['GET'])
def get_customer(customer_id):
    try:
        customer = commands.get_customer(int(customer_id))

        return jsonify(customerId=str(customer.id),
                       firstName=customer.first_name,
                       surname=customer.surname)
    except CustomerNotFound:
        return jsonify({
            'message': 'Not found'
        }), 404
