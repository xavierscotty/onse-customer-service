from unittest.mock import patch

from customer_service.model.customer import Customer
from customer_service.model.errors import CustomerNotFound


def test_get_health(web_client):
    response = web_client.get('/health')

    assert response.status_code == 200
    assert response.is_json
    assert response.get_json() == {'message': 'OK'}


@patch('customer_service.model.commands.get_customer')
def test_get_customers(get_customer, web_client, customer_repository):
    get_customer.return_value = Customer(customer_id=12345,
                                         first_name='Joe',
                                         surname='Bloggs')

    response = web_client.get('/customers/12345')

    get_customer.assert_called_with(
        customer_id=12345,
        customer_repository=customer_repository)
    assert response.is_json
    assert response.get_json() == {
        'customerId': '12345',
        'firstName': 'Joe',
        'surname': 'Bloggs'
    }


@patch('customer_service.model.commands.get_customer')
def test_get_customers_not_found(get_customer, web_client):
    get_customer.side_effect = CustomerNotFound()

    response = web_client.get('/customers/000000')

    assert response.is_json
    assert response.status_code == 404
    assert response.get_json() == {
        'message': 'Not found'
    }
