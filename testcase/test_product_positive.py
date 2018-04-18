from tools.basic_auth import BasicAuth
from tools.db_connect import DBConnect
import json

req = BasicAuth()
qry = DBConnect()


def test_insert_product():
    global product_id
    global title
    global price
    title = 'TEST5 TITLE'
    price = '5.99'

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


def test_verify_product_in_db():
    sql = "select a.post_title, a.post_type, b.meta_value from wp825.wpjm_posts a " \
          "inner join wp825.wpjm_postmeta b on a.id = b.post_id " \
          "where a.id={} and b.meta_key='_regular_price'".format(product_id)
    result = qry.select_method('wp825', sql)

    assert title == result[0][0], "Title mismatch"
    assert result[0][1] == 'product', "Product type mismatch"
    assert price == result[0][2], "Price mismatch"

    print("Verify product in DB pass")


test_insert_product()
test_verify_product_in_db()
