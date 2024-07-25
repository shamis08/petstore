import requests
import pytest

@pytest.fixture
def pet_url():
    return "https://petstore.swagger.io/v2"

#returns pet inventories by status
def test_get_inventory(pet_url):
    response = requests.get(f"{pet_url}/store/inventory")
    assert response.status_code == 200

#place an order for a pet
def test_post_order(pet_url):
    payload = {
        "id": 1,
        "petId": 1,
        "quantity": 1,
        "shipDate": "2022-07-20T00:00:00.000Z",
        "status": "placed",
        "complete": True
    }
    response = requests.post(f"{pet_url}/store/order", json=payload)
    assert response.status_code == 200

#find purchase order by ID
def test_get_order_id(pet_url):
    orderId = 1
    response = requests.get(f"{pet_url}/store/order/{orderId}")
    assert response.status_code == 200

#delete purchase order by ID
def test_delete_order(pet_url):
    orderId = 1
    response = requests.delete(f"{pet_url}/store/order/{orderId}")
    assert response.status_code == 200
    #проверка
    response = requests.get(f"{pet_url}/store/order/{orderId}")
    assert response.status_code == 404