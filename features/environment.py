from customer_service.app import create


def before_all(context):
    context.web_client = create().test_client()
