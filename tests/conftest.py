import pytest

from App import create_app
from App.models.userModels import User
from App.models import db

# ----------
# Fixtures
# -----------


@pytest.fixture(scope='module')
def new_user():
    user = User(user_name='bob', email='bob@gmail.com', birthdate='2000-12-22')
    user.set_password('password_to_hash')
    return user


@pytest.fixture(scope='module')
def test_client():
    # Create a Flask app for testing
    flask_app = create_app()

    #create a test client
    with flask_app.test_client() as test_client:
        # establish application context
        with flask_app.app_context():
            yield test_client


@pytest.fixture(scope='module')
def create_test_user(test_client):
    user = User(user_name='bob', email='bob@gmail.com', birthdate='2000-12-22')
    user.set_password('password_to_hash')

    db.session.add(user)
    db.session.commit()
    
    yield

    db.delete(user)


@pytest.fixture(scope='function')
def login_user(test_client):
    test_client.post('/login', 
                    data=dict(email='bob@gmail.com', password='password_to_hash'),
                    follow_redirects=True)
    
    yield

    test_client.get('/logout', follow_redirects=True)