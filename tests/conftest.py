import pytest

from customer_service import create_app


@pytest.fixture
def app():
    return create_app({'HOSTNAME': 'example-host-name',
                       'TESTING': True})


@pytest.fixture
def client(app):
    return app.test_client()
