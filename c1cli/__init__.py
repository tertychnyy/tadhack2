from base64 import b64encode
from c1cli import bots
from c1cli.exceptions import ClientException
from c1cli.push.scripts import push, sms
import requests


class Client:
    def __init__(self):
        self.token = None
        self.host = "https://ch-message-processor-test.azurewebsites.net/"
        self.version = "v1"

    def init_app(self, app):
        self.token = app.config['CHATFIRST_USERTOKEN']

    def get(self, method, params=None, headers=None):
        h = dict() if headers is None else headers
        h['Authorization'] = "Basic {token}".format(token=b64encode(self.token + ":"))
        h["Content-Type"] = "application/json"

        url = self.host + self.version + method

        try:
            res = requests.get(url, params=params, headers=h)
        except:
            raise ClientException("Unable to perform Core GET request", 400)

        if res.status_code != 200:
            print res.text
            raise ClientException("{method}: Bad Core GET status code".format(method=method), res.status_code)
        return res.json()

    def post(self, method, data=None, json=None, headers=None):
        h = dict() if headers is None else headers
        h['Authorization'] = "Basic {token}".format(token=b64encode(self.token + ":"))
        h["Content-Type"] = "application/json"

        url = self.host + self.version + method
        try:
            res = requests.post(url, data=data, json=json, headers=h)
        except:
            raise ClientException("Unable to perform Core POST request", 400)

        if res.status_code not in [200, 201, 202]:
            print res.text
            raise ClientException("{method}: Bad Core POST status code".format(method=method), res.status_code)
        return res.json()

    def put(self, method, json=None, headers=None, params=None):
        h = dict() if headers is None else headers
        h['Authorization'] = "Basic {token}".format(token=b64encode(self.token + ":"))
        h["Content-Type"] = "application/json"

        url = self.host + self.version + method

        try:
            res = requests.put(url, json=json, params=params, headers=h)
        except:
            raise ClientException("Unable to perform Core PUT request", 400)

        if res.status_code not in [200, 202, 204]:
            print res.text
            raise ClientException("{method}: Bad Core PUT status code".format(method=method), res.status_code)
        return res.json()

    def delete(self, method, headers=None, params=None):
        h = dict() if headers is None else headers
        h['Authorization'] = "Basic {token}".format(token=b64encode(self.token + ":"))
        h["Content-Type"] = "application/json"

        url = self.host + self.version + method

        try:
            res = requests.delete(url, params=params, headers=h)
        except:
            raise ClientException("Unable to perform Core DELETE request", 400)

        if res.status_code not in [200, 204]:
            print res.text
            raise ClientException("{method}: Bad Core DELETE status code".format(method=method), res.status_code)
        return res.json()

    def bots_get(self):
        """
        Fetches user's bots list
        :return: List of Bot objects
        """
        return bots.get(client=self)

    def bots_get_by_name(self, bot_name):
        """
        Fetches bot by name
        :return: Fetched Bot object
        """
        return bots.get_by_name(self, bot_name)

    def bots_save(self, bot):
        """
        Saves new bot
        :return: Saves Bot object
        """
        return bots.save(self, self.token, bot)

    def bots_update(self, bot):
        """
        Updates bot
        :return: Deleted Bot object
        """
        return bots.update(self, bot)

    def bots_delete(self, bot_name):
        """
        Deletes bot
        :return: Deleted Bot object
        """
        return bots.delete(self, bot_name)

    def push_tg(self, obj, bot_name=None, user_id=None):
        """
        Pushes user in telegram
        :param bot_name: Name of bot to push from
        :param user_id: ID of user to push
        :param obj: ActionResponse object
        :return:
        """
        return push(token=self.token, botname=bot_name, userid=user_id, obj=obj, channel="telegram")

    def push_fb(self, obj, bot_name=None, user_id=None):
        """
        Pushes user in Facebook
        :param bot_name: Name of bot to push from
        :param user_id: ID of user to push
        :param obj: ActionResponse object
        :return:
        """
        return push(token=self.token, botname=bot_name, userid=user_id, obj=obj, channel="facebook")

    def push_sms(self, obj, phone=None):
        """
        Pushes user by SMS
        :param obj: ActionResponse object
        :param phone: User's phone number
        :return:
        """
        for item in obj.messages:
            try:
                sms(phone, item)
            except:
                return False
        return True



