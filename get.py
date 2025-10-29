def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

response = get_docs()
print(response.status_code)

def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH, params={"count":20})

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

response = get_users_table()
print(response.status_code)
print(response.headers)

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

response = post_new_user(data.user_body)
print(response.status_code)

def post_products_kits (products_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH, json=products_ids, headers=data.headers)
response = post_products_kits(data.product_ids)
print(response.status_code)
print (response.json())

#pruebas ejercicio
# primera prueba El número permitido de caracteres (2) firstname
def get_user_body(first_name):

    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body

def test_create_user_2_letter_in_first_name_get_success_response():
    user_body = get_user_body("Aa")
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""
    users_table_response = sender_stand_request.get_users_table()
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]
    assert users_table_response.text.count(str_user) == 1

# 2 prueba  El número permitido de caracteres (15) firstname

def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body

def test_create_user_15_letter_in_first_name_get_success_response():
    user_body = get_user_body("Aaaaaaaaaaaaaaa")
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""
    users_table_response = sender_stand_request.get_users_table()
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]
    assert users_table_response.text.count(str_user) == 1

  # 3 prueba con un(1) caracter en first name
    def get_user_body(first_name):
        current_body = data.user_body.copy()
        current_body["firstName"] = first_name
        return current_body

    def test_create_user_15_letter_in_first_name_get_success_response():
        user_body = get_user_body("A")
        user_response = sender_stand_request.post_new_user(user_body)
        assert user_response.status_code == 400
        assert user_response.json()["authToken"] != ""
        users_table_response = sender_stand_request.get_users_table()
        str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
                   + user_body["address"] + ",,," + user_response.json()["authToken"]
        assert users_table_response.text.count(str_user) == 1
 # 4 prueba con 16 caracteres en first name
        def get_user_body(first_name):
            current_body = data.user_body.copy()
            current_body["firstName"] = first_name
            return current_body

        def test_create_user_15_letter_in_first_name_get_success_response():
            user_body = get_user_body("Аааааааааааааааа")
            user_response = sender_stand_request.post_new_user(user_body)
            assert user_response.status_code == 400
            assert user_response.json()["authToken"] != ""
            users_table_response = sender_stand_request.get_users_table()
            str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
                       + user_body["address"] + ",,," + user_response.json()["authToken"]
            assert users_table_response.text.count(str_user) == 1