from woocommerce import API


class BasicAuth:

    def __init__(self):
        admin_consumer_key = "ck_4c5db02305903c89717481b801f510a50c769cf0"
        admin_consumer_secret = "cs_be0444f22ccc2358bb98193aa39279ce33b78aa8"

        self.wcapi = API(
            url="http://127.0.0.1/sreenu_store",
            consumer_key=admin_consumer_key,
            consumer_secret=admin_consumer_secret,
            version="v3")

    def test_api(self):
        print(self.wcapi.get("").json())

    def post_method(self, endpoint, data):
        result = self.wcapi.post(endpoint, data)
        rs_response = result.status_code
        rs_body = result.json()
        rs_url = result.url
        return rs_response, rs_body, rs_url

    def get_method(self, endpoint):
        result = self.wcapi.get(endpoint)
        rs_response = result.status_code
        rs_body = result.json()
        rs_url = result.url
        return rs_response, rs_body, rs_url


#test = BasicAuth()
#test.test_api()
