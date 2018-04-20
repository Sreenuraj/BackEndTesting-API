from tools.basic_auth import BasicAuth

req = BasicAuth()


def test_empty_payload():

    input_data = {}
    result = req.post_method('products', input_data)

    rs_response_code = result[0]
    print("TC1 test_empty_payload starts")
    assert rs_response_code == 400, "Expected 400 as response code but received ()".format(rs_response_code)

    response_body = result[1]
    assert 'errors' in response_body.keys(), "Expected 'errors' in the response but not received"

    response_exp_err_msg = "No product data specified to create product"
    response_act_err_msg = response_body['errors'][0]['message']
    assert response_exp_err_msg == response_act_err_msg, "Actual error message differs"

    response_exp_err_code = "woocommerce_api_missing_product_data"
    response_act_err_code = response_body['errors'][0]['code']
    assert response_exp_err_code == response_act_err_code, "Error code differs"

    print("TC1 test_empty_payload and result is Pass")


def test_empty_title():

    input_data = {}
    product = {}
    product['regular_price'] = '8.99'
    product['type'] = 'simple'
    # product['title'] = 'simple'
    input_data['product'] = product

    result = req.post_method("products", input_data)
    print("TC2 test_empty_title starts")

    rs_response_code = result[0]
    assert rs_response_code == 400, "Response code received is not 400"

    rs_body = result[1]
    assert 'errors' in rs_body.keys(), "Keyword errors not found in the response"

    rs_exp_err_msg = 'Missing parameter title'
    rs_act_err_msg = rs_body['errors'][0]['message']
    assert rs_act_err_msg == rs_exp_err_msg, "Error msg in response not matching"

    rs_exp_err_code = 'woocommerce_api_missing_product_title'
    rs_act_err_code = rs_body['errors'][0]['code']
    assert rs_exp_err_code == rs_act_err_code, "Error code in response not matching"

    print("TC2 test_empty_title Ends and result is PASS")


def test_get_product_not_exists():
    id_of_product = 222
    result = req.get_method('products/{}'.format(id_of_product))
    print("TC3 test_get_product_not_exists starts")
    response_code = result[0]
    assert response_code == 404, "Expected 404 received {}".format(response_code)

    response_body = result[1]
    assert 'errors' in response_body.keys(), "Expected error in the body but not found"

    rs_exp_err_msg = "No product found with the ID equal to {}".format(id_of_product)
    rs_act_err_msg = response_body['errors'][0]['message']
    assert rs_exp_err_msg == rs_act_err_msg, "Message received differs"

    print("TC3 test_get_product_not_exists Ends and result is Pass")


test_empty_payload()
test_empty_title()
test_get_product_not_exists()

