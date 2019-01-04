import pytest

from customer_service import create_app


@pytest.fixture
def app():
    return create_app()


@pytest.fixture
def web_client(app):
    return app.test_client()
