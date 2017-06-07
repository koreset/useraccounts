import json
from base64 import b64encode

import requests

from api.services.constants import UAA_TOKEN_ENDPOINT, CLIENT_TOKEN, UAA_USERS_ENDPOINT


class UserService():
    def __init__(self):
        self.access_token = CLIENT_TOKEN

    def create_user(self, user_data):
        firstname = user_data["firstname"]
        lastname = user_data["lastname"]
        fullname = (firstname + " " + lastname)
        username = fullname.replace(" ", ".").lower()
        user_data["fullname"] = fullname
        user_data["username"] = username
        access_token = self.get_token()
        print access_token

        # Time to load the user into UAA
        payload = dict()
        payload["userName"] = user_data["username"]
        payload["password"] = user_data["password"]
        payload["name"] = dict()
        payload["name"]["formatted"] = user_data["fullname"]
        payload["name"]["givenName"] = user_data["firstname"]
        payload["name"]["familyName"] = user_data["lastname"]
        payload["phoneNumbers"] = list()
        payload["phoneNumbers"].append({"value": user_data["cellphone"]})
        payload["emails"] = list()
        payload["emails"].append({"primary": True, "value": user_data["email"]})
        payload["verified"] = True

        headers = dict()
        headers["Authorization"] = "Bearer " + self.access_token
        headers["Content-Type"] = "application/json"
        print "Headers: ", headers
        response = requests.post(UAA_USERS_ENDPOINT, json=payload, headers=headers)
        print response.content

        return payload

    def get_token(self):
        base64string = b64encode("uas:wordpass15")
        headers = {"Authorization": "Basic " + base64string}
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        payload = dict()
        payload["grant_type"] = "client_credentials"
        payload["response_type"] = "token"

        response = requests.post(UAA_TOKEN_ENDPOINT, data=payload, headers=headers)
        print "Status code: ", response.status_code
        if response.status_code == 200:
            access_token = json.loads(response.content)["access_token"]
            self.access_token = access_token



user_service = UserService()
