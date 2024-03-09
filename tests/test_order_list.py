import requests
import allure
from data import Data

class TestOrderList:
    @allure.title('Проверка отображения в теле ответа списка заказов')
    @allure.description('Отправляем запрос на список заказов с лимитом 5 и около станции "Кадужская"\
                        проверяем, что вывелось 5 заказов, станция "Калужская"')
    def test_order_list(self):
        response = requests.get(f'{Data.main_url}/api/v1/orders?limit=5&page=0&nearestStation=["110"]')
        r = response.json()
        assert len(r['orders']) == 5 and r['availableStations'][0]['name'] == 'Калужская',\
            f'ожидавлось 5 заказов получили {len(r['orders'])}, ожидалось "Калужская", \
            получили {r['availableStations'][0]['name']}'


