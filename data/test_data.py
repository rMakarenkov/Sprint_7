class CourierData:
    valid_courier = {
        "login": "BaseLogin",
        "password": "BasePassword",
        "firstName": "BaseFirstname"
    }

    valid_response = {
        "ok": True
    }
    login_taken_response = 'Этот логин уже используется'
    missing_data_create_response = 'Недостаточно данных для создания учетной записи'
    courier_not_found_response = 'Учетная запись не найдена'
    missing_data_login_response = 'Недостаточно данных для входа'


class OrderData:
    valid_order = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK"
        ]
    }
