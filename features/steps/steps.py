from behave import when, then, given


@given('customer "Joe Bloggs" with ID "12345" exists')
def create_customer(context):
    pass


@given('there is no customer with ID "99999"')
def do_not_create_customer(context):
    pass  # Intentionally blank


@when(u'I fetch customer "{id}"')
def fetch_customer(context, id):
    context.response = context.web_client.get('/customers/{0}'.format(id))


@then(u'I should see customer "{expected_name}"')
def assert_customer(context, expected_name):
    response = context.response

    assert response.status_code == 200, response.status_code
    assert response.is_json
    body = response.get_json()
    assert f"{body['firstName']} {body['surname']}" == expected_name


@then("I should get a not found response")
def assert_not_found_response(context):
    assert context.response.status_code == 404, context.response.status_code
