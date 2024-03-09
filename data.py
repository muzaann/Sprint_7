from faker import Faker
from random import randint
import datetime
class Data:
    Faker.seed(randint(1, 999))
    faker = Faker()

    main_url = 'https://qa-scooter.praktikum-services.ru'
    login = faker.user_name()
    password = faker.password()
    firstName = faker.first_name()
    lastName = faker.last_name()
    address = faker.address()
    metroStation = randint(1, 257)
    phone = faker.phone_number()
    rentTime = randint(1,4)
    deliveryDate = datetime.date.today()+datetime.timedelta(days=1)
    comment = faker.text(max_nb_chars=50)
    color_data = (
        ['BLACK'], ['GREY'], ['BLACK', 'GREY'], []
    )

