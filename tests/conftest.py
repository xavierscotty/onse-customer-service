import pytest

from customer_service.app import create


@pytest.fixture
def app():
    return create()


@pytest.fixture
def web_client(app):
    return app.test_client()
