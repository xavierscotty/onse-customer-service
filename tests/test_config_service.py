def test_get_health(web_client):
    response = web_client.get('/health')

    assert response.status_code == 200
    assert response.is_json
    assert response.get_json() == {'message': 'OK'}


def test_get_customers(web_client):
    response = web_client.get('/customers/12345')
    assert response.is_json
    assert response.get_json() == {
        'id': '12345',
        'name': 'Joe',
        'surname': 'Blogg'
    }

def test_get_customers_not_found(web_client):
    response = web_client.get('/customers/000000')
    assert response.is_json
    assert response.status_code == 404
    assert response.get_json() == {
        'message': 'Not found'
    }
