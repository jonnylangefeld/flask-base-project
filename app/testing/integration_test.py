# Test the api endpoints of the flask app

import pytest
import sys
sys.path.append('/app')  # Import the app no matter where the testsing directory is located
from app import app


@pytest.fixture(scope='module')
def test_client():
    """This fixture will have the test_client() of the flask app stored and ready to be used by the other test cases.
    scope='module' will only spin it up once for all test cases and re-use the flask test_client. This is helpful for
    sessions and other settings."""
    app.config['TESTING'] = True  # disables error catching during request handling to get better error reports
    testing_client = app.test_client()
    ctx = app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()


def test_home_page(test_client):
    """Test the root directory"""
    response = test_client.get('/')
    assert response.mimetype == 'text/html'
    assert response.status_code == 200


def test_api(test_client):
    """Test api"""
    response = test_client.get('/api')
    assert response.mimetype == 'application/json'
    assert response.status_code == 200
    assert response.json == {"Hi there": "This is a sample response"}


def test_api_variable(test_client):
    """Test api variable"""
    response = test_client.get('/api/test')
    assert response.mimetype == 'application/json'
    assert response.status_code == 200
    assert response.json == {"You entered variable:": "test"}