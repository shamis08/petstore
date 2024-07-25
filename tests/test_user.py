import requests
import pytest

@pytest.fixture
def pet_url():
    return "https://petstore.swagger.io/v2"

#creates list of users with given input array
def test_post_createWithList(pet_url):
    payload = [
        {
            "id": 1,
            "username": "user99",
            "firstName": "FirstName",
            "lastName": "LastName",
            "email": "user1@example.com",
            "password": "password",
            "phone": "1234567890",
            "userStatus": 1
        }
    ]
    response = requests.post(f"{pet_url}/user/createWithList", json=payload)
    assert response.status_code == 200

#get user by username
def test_get_username(pet_url):
    username = "user99"
    response = requests.get(f"{pet_url}/user/{username}")
    assert response.status_code == 200

#updated user
def test_put_update(pet_url):
    username = "user99"
    payload = {
        "id": 1,
        "username": "user1",
        "firstName": "FirstNameUpdated",
        "lastName": "LastNameUpdated",
        "email": "user1@example.com",
        "password": "password",
        "phone": "1234567890",
        "userStatus": 1
    }
    response = requests.put(f"{pet_url}/user/{username}", json=payload)
    assert response.status_code == 200

#logs user into the system
def test_get_login(pet_url):
    params = {
        "username": "user99",
        "password": "password"
    }
    response = requests.get(f"{pet_url}/user/login", params=params)
    assert response.status_code == 200

#logs out current logged in user session
def test_get_logout(pet_url):
    response = requests.get(f"{pet_url}/user/logout")
    assert response.status_code == 200

#creates list of users with given input array
def test_post_createWithArray(pet_url):
    payload = [
        {
            "id": 1,
            "username": "user99",
            "firstName": "FirstName",
            "lastName": "LastName",
            "email": "user1@example.com",
            "password": "password",
            "phone": "1234567890",
            "userStatus": 1
        }
    ]
    response = requests.post(f"{pet_url}/user/createWithArray", json=payload)
    assert response.status_code == 200

#create user
def test_post_create(pet_url):
    payload = {
        "id": 1,
        "username": "user99",
        "firstName": "FirstName",
        "lastName": "LastName",
        "email": "user1@example.com",
        "password": "password",
        "phone": "1234567890",
        "userStatus": 1
    }
    response = requests.post(f"{pet_url}/user", json=payload)
    assert response.status_code == 200

#delete user
def test_delete_user(pet_url):
    username = "user99"
    response = requests.delete(f"{pet_url}/user/{username}")
    assert response.status_code == 200
    #проверка
    response = requests.get(f"{pet_url}/user/{username}")
    assert response.status_code == 404