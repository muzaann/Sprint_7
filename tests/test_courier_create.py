import pytest
import requests
import allure
from data import Data


class TestCourierCreate:

    @allure.title('Проверка успешного создания курьера')
    @allure.description('Создаем курьера с сгенерированными данными,, проверяем, что код ответа: 201,\
                        текст ответа: "ok":true')
    def test_create_courier_success(self, generate_courier_data_and_delete_after_test):
        response = requests.post(f'{Data.main_url}/api/v1/courier', data=generate_courier_data_and_delete_after_test)
        assert 201 == response.status_code and '{"ok":true}' == response.text

    @allure.title('Проверка невозможности создания двух одинаковых курьеров')
    @allure.description('Создаем курьера, создаем еще одного курьера с теми же данными, \
                        проверяем, что код ответа: 409, текст ответа: "Этот логин уже используется"')
    def test_create_two_same_couriers_fail(self, generate_courier_data_and_delete_after_test):
        requests.post(f'{Data.main_url}/api/v1/courier', data=generate_courier_data_and_delete_after_test)
        response = requests.post(f'{Data.main_url}/api/v1/courier', data=generate_courier_data_and_delete_after_test)
        r = response.json()
        assert 409 == r['code'] and "Этот логин уже используется" == r['message'], \
            f'Ожидаемый код: 409, полученный код: {r['code']}, ожидаемый текст: "Этот логин уже используется", \
            полученный текст: {r['message']}'
# Тест падает из-за несоответсвия ожидаемого текста ответа из документации и текста по факту. Разница в приписке
# "Попробуйте другой."

    @allure.title('Параметризованная проверка невозможности создания курьера без передачи логина или пароля')
    @allure.description('Создаем курьера без логина или пароля,проверяем что код ответа: 400, \
    текст ответа: "Недостаточно данных для создания учетной записи"')
    @pytest.mark.parametrize('missing_argument', (('login'),('password')))
    def test_create__courier_faild_without_login_or_password_fail(self, generate_courier_data, missing_argument):
        del generate_courier_data[missing_argument]
        response = requests.post(f'{Data.main_url}/api/v1/courier', data=generate_courier_data)
        r = response.json()
        assert 400 == r['code'] and "Недостаточно данных для создания учетной записи" == r['message'], \
            f'Ожидаемый код: 400, полученный код: {r['code']}, ожидаемый текст: \
             "Недостаточно данных для создания учетной записи", полученный текст: {r["message"]}'

    @allure.title('Проверка успешного создания курьера без передачи имени')
    @allure.description('Создаем курьера непередавая имя, проверяем, что код ответа: 201,\
                        текст ответа: "ok":true')
    def test_create__courier_faild_without_first_name_succsess(self, generate_courier_data):
        del generate_courier_data['firstName']
        response = requests.post(f'{Data.main_url}/api/v1/courier', data=generate_courier_data)
        assert 201 == response.status_code and '{"ok":true}' == response.text, f'Ожидаемый код: 201, \
        полученный код: {response.status_code}, ожидаемый текст: "ok":true", полученный текст: {response.text}'



