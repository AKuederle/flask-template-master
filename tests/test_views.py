# Sample Test passing with nose and pytest


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200, 'Index not reachable'
