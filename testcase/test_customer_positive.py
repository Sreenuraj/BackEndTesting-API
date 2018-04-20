from tools.basic_auth import BasicAuth
from tools.db_connect import DBConnect
from utilities.generate_random_info_cust import generate_random_info

req = BasicAuth()
sql = DBConnect()


def test_create_customer():
    global customer_id
    global email
    global user_name
    global first_name
    global last_name

    gen = generate_random_info()
    email = gen['email']
    user_name = gen['user_name']
    first_name = gen['first_name']
    last_name = gen['last_name']

    input_data = {
        "customer": {
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "username": user_name,
            "password": "test123",
            "billing": {
                "first_name": first_name,
                "last_name": last_name,
                "company": "",
                "address_1": "969 Market",
                "address_2": "",
                "city": "San Francisco",
                "state": "CA",
                "postcode": "94103",
                "country": "US",
                "email": email,
                "phone": "(555) 555-5555"
                },
            "shipping": {
                "first_name": first_name,
                "last_name": last_name,
                "company": "",
                "address_1": "969 Market",
                "address_2": "",
                "city": "San Francisco",
                "state": "CA",
                "postcode": "94103",
                "country": "US"
                }
            }
        }

    result = req.post_method('customers', input_data)
    print("TC1 test_create_customer start")

    response_code = result[0]
    assert response_code == 201, "Response code received is not 201, it is {}".format(response_code)

    response_body = result[1]['customer']
    customer_id = response_body['id']

    assert response_body['email'] == email, "Email don't match"
    assert response_body['first_name'] == first_name, "first_name don't match"

    print("TC1 test_create_customer End - Pass")


def test_created_cust_exist_in_db():
    query = "select * from wp825.wpjm_users where id={};".format(customer_id)
    result = sql.select_method('wp825', query)
    print(result)
    print('TC2 test_created_cust_exist_in_db start')
    # print(customer_id, result[0][0])
    assert str(result[0][0]) == str(customer_id), 'Customer_id dont match'
    assert result[0][1] == user_name, 'User name dont match'

    print('TC2 test_created_cust_exist_in_db ends - pass')


test_create_customer()
test_created_cust_exist_in_db()
