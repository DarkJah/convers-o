import pytest #ignore this import for now 
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    rv = client.get('/')
    assert rv.status_code == 200
    
def test_conversion_metro_to_km(client):
    data = {
        'selectTemp': '1',
        'valorRef': '1000'
    }
    rv = client.post('/', data=data)
    assert rv.status_code == 200
    assert b'1.0' in rv.data 