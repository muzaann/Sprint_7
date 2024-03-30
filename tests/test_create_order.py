import pytest
import requests
import allure
from data import Data


class TestOrderCreate:

    @allure.title('Параметирозованная проверка заказа с разными вариантами цвета самоката')
    @allure.description('Создаем заказ, передавая в качестве параметра color возможные цвета по отдельности, \
    оба цвета сразу, не выбираем ни одного цвета  проверяем, что код ответа: 201, текст ответа содержит track')
    @pytest.mark.parametrize("color", Data.color_data)
    def test_order_any_color_success(self, generate_required_order_data, color):
        generate_required_order_data['color'] = color
        response = requests.post(f'{Data.main_url}{Data.api_order}', data=generate_required_order_data, timeout=7)
        assert 201 == response.status_code and 'track' in response.text, \
            (f'Ожидаемый код: 201, полученный код: {response.status_code}, \
             ожидаемый текст содержит: "track", полученный текст: {response.text}')
#Тест падает при передаче одного цвета самоката - код ответа 500 вместо ожидаемого 201,
# при передаче сразу двух цветов или ни одного - тест проходит


