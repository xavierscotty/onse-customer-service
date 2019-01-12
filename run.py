import os

from customer_service.app import create
from customer_service.mock.mock_customer_repository import \
    MockCustomerRepository

if __name__ == "__main__":
    create(customer_repository=MockCustomerRepository()) \
        .run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
