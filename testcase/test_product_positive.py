from tools.basic_auth import BasicAuth
from tools.db_connect import DBConnect
import json

req = BasicAuth()


def test_insert_product():
    title = 'TEST4 TITLE'
    price = '6.99'

    input_data = {
        'product': {
            'title': title,
            'type': 'simple',
            'regular_price': price}}

    print("Making the 'product' API call")
    info = req.post_method('products', input_data)
    response_code = info[0]
    response_body = info[1]
    print("Verifying the response status code")
    assert response_code == 201, \
        "The status code returned creating product is not as expected. Expected: 201, Actual: {}".format(response_code)

    rs_title = response_body["product"]["title"]
    rs_price = response_body["product"]["regular_price"]
    product_id = response_body["product"]["id"]

    print('id is: {}'.format(product_id))

    print("verifying the title in the response")
    assert rs_title == title, \
        "The title in response is not same as in request.The response title is: {}".format(rs_title)
    print("verifying the price in the response")
    assert rs_price == price, \
        "The price in response did not match Expected: {}, Actual, {}".format(price, rs_price)

    print('The create_product test PASS')


test_insert_product()
