import json
import requests
import urls
import pytest
from data import Data
from helper import Generator
from selenium import webdriver

@pytest.fixture(params=["chrome", "firefox"])
def driver_unauthorized_user(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()

    driver.get(urls.BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def create_and_delete_user(request):
    email = Generator.fake_email()
    password = Generator.fake_password()
    name = Generator.fake_name()

    payload = {"email": email, "password": password, "name": name}
    response_create_user = requests.post(urls.BASE_URL + urls.REGISTRATION_ENDPOINT, json=payload)
    if response_create_user.status_code != 200 or response_create_user.json()["success"] is not True:
        pytest.fail(f"Ошибка при создании пользователя: {response_create_user.status_code}, {response_create_user.text}")

    access_token = {"Authorization": response_create_user.json()["accessToken"]}
    refresh_token = response_create_user.json().get("refreshToken")

    yield {"access_token": access_token, "refresh_token": refresh_token}

    response_delete_user = requests.delete(urls.BASE_URL + urls.USER_ENDPOINT, headers=access_token)
    if response_delete_user.status_code != 202 or response_delete_user.json()["success"] is not True:
        pytest.fail(f"Ошибка при удалении пользователя: {response_delete_user.status_code}, {response_delete_user.text}")

@pytest.fixture(params=["chrome", "firefox"])
def driver_authorized_user(request, create_and_delete_user):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()

    driver.get(urls.BASE_URL)

    access_token = create_and_delete_user["access_token"]["Authorization"]
    refresh_token = create_and_delete_user["refresh_token"]
    driver.execute_script(f"window.localStorage.setItem('accessToken', {json.dumps(access_token)});")
    driver.execute_script(f"window.localStorage.setItem('refreshToken', {json.dumps(refresh_token)});")

    driver.refresh()

    yield driver
    driver.quit()

@pytest.fixture
def create_order(create_and_delete_user):
    access_token = create_and_delete_user["access_token"]

    payload = {"ingredients": [Data.ingredient_1_id, Data.ingredient_2_id]}
    response_create_order = requests.post(urls.BASE_URL + urls.ORDER_ENDPOINT, json=payload, headers=access_token)
    if response_create_order.status_code != 200 or response_create_order.json()["success"] is not True:
        pytest.fail(f"Ошибка при создании заказа: {response_create_order.status_code}, {response_create_order.text}")

    order_number = f"{response_create_order.json()["order"]["number"]}"
    return order_number