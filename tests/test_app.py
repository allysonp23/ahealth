import pytest
from app import create_app, db

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"
    })

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_add_owner(client):
    response = client.post('/owners', json={"name": "John Doe"})
    assert response.status_code == 201
    assert response.json['message'] == "Owner added"
