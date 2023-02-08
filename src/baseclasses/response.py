# from jsonschema import validate
from src.enums.global_enums import GlobalErrorMessage


class Response:

    def __init__(self, response):
        self.response = response
        self.response_json = response.json().get('data')
        self.response_status = response.status_code

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.parse_obj(item)
        else:
            schema.parse_obj(self.response_json)
        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, GlobalErrorMessage.WRONG_STATUS_CODE
        else:
            assert self.response_status == status_code, GlobalErrorMessage.WRONG_STATUS_CODE

        return self

    def __str__(self):
        return \
            f"\nResponse status: {self.response_status} \n \
            Response url: {self.response_url}"
