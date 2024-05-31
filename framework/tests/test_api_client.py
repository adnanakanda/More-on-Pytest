import pytest
from framework.tests.api_client import APIClient
from framework.models.user import User

@pytest.fixture
def api_client(base_url):
    return APIClient(base_url)

@pytest.fixture
def test_user():
    return User(id=0, name="Test User", email="testuser@example.com")

def test_create_user(api_client, test_user):
    created_user = api_client.create_user(test_user)
    assert created_user.id is not None
    assert created_user.name == test_user.name
    assert created_user.email == test_user.email

def test_get_user(api_client):
    user_id = 1
    user = api_client.get_user(user_id)
    assert user.id == user_id
    assert user.name is not None
    assert user.email is not None

def test_update_user(api_client, test_user):
    user_id = 1
    test_user.name = "Updated Name"
    updated_user = api_client.update_user(user_id, test_user)
    assert updated_user.id == user_id
    assert updated_user.name == "Updated Name"

def test_delete_user(api_client):
    user_id = 1
    status_code = api_client.delete_user(user_id)
    assert status_code == 200