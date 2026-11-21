"""Contract tests for the public training endpoints."""
from app.app import app


def test_index():
    """The home endpoint identifies the training app."""
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.get_json() == {'service': 'devops-ci-app'}


def test_health():
    """Health must be HTTP 200 with exactly status ok."""
    response = app.test_client().get('/health')
    assert response.status_code == 200
    assert response.get_json() == {'status': 'ok'}


def test_unknown_route():
    """An unknown route must not look healthy."""
    assert app.test_client().get('/missing').status_code == 404
