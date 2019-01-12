from behave import when, then


@when(u'I fetch customer {id}')
def fetch_customer(context, id):
    response = context.web_client.get('/customers/{0}'.format(id))
    context.response = response.get_json()


@then(u'I should see customer "{expected_name}"')
def assert_customer(context, expected_name):
    response = context.response
    full_name = f"{response['firstName']} {response['surname']}"
    assert full_name == expected_name
