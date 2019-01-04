@when(u'I fetch customer {id}')

def step_impl(context, id):
    response = context.web_client.get('/customers/{0}'.format(id))
    context.response = response.get_json()

@then(u'I should see customer "{expected_name}"')
def step_impl(context, expected_name):
    full_name = context.response['first_name'] + " " + context.response['surname']
    assert full_name == expected_name
 