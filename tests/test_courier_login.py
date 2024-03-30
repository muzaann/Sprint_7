import pytest
import requests
import allure
from data import Data


class TestCourierLogin:

    @allure.title('Проверка успешной авторизации')
    @allure.description('Создаем курьера, авторизауемся по логину/паролю, проверяем, что код ответа: 201,\
                        текст ответа содержит id курьера')
    def test_authorization_succsess(self, generate_courier_data_and_delete_after_test):
        requests.post(f'{Data.main_url}{Data.api_create_courier}', data=generate_courier_data_and_delete_after_test)
        del generate_courier_data_and_delete_after_test['firstName']
        response = requests.post(f'{Data.main_url}{Data.api_login_courier}',
                                 data=generate_courier_data_and_delete_after_test)
        assert 200 == response.status_code and 'id' in response.text, \
            (f'Ожидаемый код: 201, полученный код: {response.status_code}, \
             ожидаемый текст содержит: "id", полученный текст: {response.text}')

    @allure.title('Параметризованная проверка невозможности авторизации курьера без передачи логина или пароля')
    @allure.description('Создаем курьера, пытаемся авторизоваться без логина или пароля,проверяем что \
            код ответа: 400, текст ответа: "Недостаточно данных для входа"')
    @pytest.mark.parametrize('missing_argument', (('login'), ('password')))
    def test_login_courier_without_login_or_password_fail(self, generate_courier_data, missing_argument):
        requests.post(f'{Data.main_url}{Data.api_create_courier}', data=generate_courier_data)
        del generate_courier_data[missing_argument]
        response = requests.post(f'{Data.main_url}{Data.api_login_courier}', data=generate_courier_data)
        assert 400 == response.status_code and Data.text_login_400 in response.text, \
        f'Ожидаемый код: 400, полученный код: {response.status_code}, ожидаемый текст содержит: \
        {Data.text_login_400}, полученный текст: {response.text}'
#Тест падает при передаче неверного пароля из-за неверного кода ответа от сервера - 504 вместо ожидаемого 400

    @allure.title('Параметризованная проверка невозможности авторизации при передаче неверного логина или пароля')
    @allure.description('Создаем курьера, пытаемся авторизоваться передавая неверный логин или пароль, \
                        проверяем что код ответа: 404, текст ответа: "Учетная запись не найдена"')
    @pytest.mark.parametrize('incorrect_argument', (('login'), ('password')))
    def test_login_courier_with_incorrect_login_or_password_fail(self, generate_courier_data, incorrect_argument):
        requests.post(f'{Data.main_url}{Data.api_create_courier}', data=generate_courier_data)
        generate_courier_data[incorrect_argument] = 'error'
        response = requests.post(f'{Data.main_url}{Data.api_login_courier}', data=generate_courier_data)
        r = response.json()
        assert 404 == r['code'] and Data.text_login_404 == r['message'], (f'Ожидаемый код: 404, \
        полученный код: {r['code']}, ожидаемый текст: {Data.text_login_404}, полученный текст: {r['message']}')



