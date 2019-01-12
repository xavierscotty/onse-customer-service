from customer_service.model.customer import Customer
from customer_service.model.errors import CustomerNotFound


def get_customer(customer_id):
    if customer_id != 12345:
        raise CustomerNotFound()

    return Customer(id=customer_id, first_name='Joe', surname='Bloggs')
