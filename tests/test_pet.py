import requests
import pytest

@pytest.fixture
def pet_url():
    return "https://petstore.swagger.io/v2"

#uploads an image
def test_post_image(pet_url):
    petId = 1
    files = {'file': ('dog.jpg', open('dog.jpg', 'rb'), 'image/jpeg')}
    response = requests.post(f"{pet_url}/pet/{petId}/uploadImage", files=files) 
    assert response.status_code == 200
#тест загрузки без фото
def test_post_without_image(pet_url):
    petId = 1
    response = requests.post(f"{pet_url}/pet/{petId}/uploadImage") 
    assert response.status_code == 415


#add a new pet to the store
def test_post_new_pet(pet_url):
    payload = {
        "id": 1,
        "name": "Doggie",
        "photoUrls": ["string"],
        "tags": [],
        "status": "available"
    }
    response = requests.post(f"{pet_url}/pet", json=payload)
    assert response.status_code == 200

#update an existing pet
def test_put_update(pet_url):
    payload = {
        "id": 1,
        "name": "DoggieUpdated",
        "photoUrls": ["string"],
        "tags": [],
        "status": "available"
    }
    response = requests.put(f"{pet_url}/pet", json=payload)
    assert response.status_code == 200
#проверка с несуществующим ID
def test_put_update_not_found(pet_url):
    petId = 78906
    response = requests.get(f"{pet_url}/pet/{petId}") 
    assert response.status_code == 404
    payload = {
        "id": petId,
        "name": "DoggieUpdated",
        "photoUrls": ["string"],
        "tags": [],
        "status": "available"
    }
    response = requests.put(f"{pet_url}/pet", json=payload)
    assert response.status_code == 404

#find pet by status
def test_get_status(pet_url):
    params = {"status": "available"}
    response = requests.get(f"{pet_url}/pet/findByStatus", params=params) 
    assert response.status_code == 200

#find pet by ID
def test_get_id(pet_url):
    petId = 1
    response = requests.get(f"{pet_url}/pet/{petId}") 
    assert response.status_code == 200

#updates a pet in the store with form data
def test_post_update_with_form(pet_url):
    petId = 1
    data = {
        "name": "Doggie",
        "status": "sold"
    }
    response = requests.post(f"{pet_url}/pet/{petId}", data=data)
    assert response.status_code == 200
#проверка с несуществующим ID
def test_post_update_with_form_not_found(pet_url):
    petId = 7890
    data = {
        "name": "Doggie",
        "status": "sold"
    }
    response = requests.post(f"{pet_url}/pet/{petId}", data=data)
    assert response.status_code == 404

#deletes a pet
def test_delete(pet_url):
    #удаление
    petId = 1
    response = requests.delete(f"{pet_url}/pet/{petId}")
    assert response.status_code == 200
    #проверка
    response = requests.get(f"{pet_url}/pet/{petId}")
    assert response.status_code == 404
#проверка с несуществующим ID
def test_delete_not_found(pet_url):
    petId = 7890
    response = requests.delete(f"{pet_url}/pet/{petId}")
    assert response.status_code == 404