# -*- coding: utf-8 -*-
import requests
import json
from base64 import b64encode

from c1cli.entities.CoreResponse import ActionResponse


def push(token, botname, userid, obj, channel):
    """
    Sends push message
    :param token: ChatFirst User Token
    :param botname: ChatFirst Bot name
    :param userid: unique user id
    :param obj: c1cli.entities.ActionResponse
    :param channel: telegram
    :return: True/False success status
    """
    if channel == 'telegram':
        headers = dict()
        headers['Authorization'] = "Basic {token}".format(token=b64encode(token + ":"))
        headers["Content-Type"] = "application/json"
        data = obj.to_dict()
        params = dict()
        params["id"] = userid
        params["channel"] = channel

        res = requests.post("https://ch-message-processor-test.azurewebsites.net/v1/push/{botname}".format(botname=botname),
                        headers=headers, data=json.dumps(data), params=params)
        print res.text
        return res.status_code == 200

    if channel == 'facebook':
        headers = dict()
        headers['Authorization'] = "Basic {token}".format(token=b64encode(token + ":"))
        headers["Content-Type"] = "application/json"
        data = obj.to_dict()
        params = dict()
        params["id"] = userid
        params["channel"] = channel

        res = requests.post("https://ch-message-processor-test.azurewebsites.net/v1/push/{botname}".format(botname=botname),
                        headers=headers, data=json.dumps(data), params=params)
        print res.text
        return res.status_code == 200

    if channel == 'sms':
        url = 'http://ch-utility.azurewebsites.net/api/v1/send/sms'
        headers = {"Content-Type": "application/json"}

        # Loop over all messages
        for item in obj.messages:
            data = {
                    "Phones": userid,
                    "Text": item
                }
            res = requests.post(url, headers=headers, data=json.dumps(data))

            # Return if failed
            if res.status_code != 200:
                return False
        return True

    return False


def push_old(token, botname, userid, text, channel):
    """
    Sends oldstyle push message
    :param token: ChatFirst Bot Token
    :param botname: ChatFirst Bot name
    :param userid: unique user id
    :param obj: c1cli.entities.ActionResponse
    :param channel: telegram
    :return: True/False success status
    """
    if channel == 'telegram':
        url = 'http://ch-utility.azurewebsites.net/api/v1/send/telegram'
        headers = {"Content-Type": "application/json"}
        data = {
            "BotToken": token,
            "ChatId": userid,
            "Text": text
        }
        res = requests.post(url, headers=headers, json=data)
        print res.text
        return res.status_code == 200
    return False


def sms(phone, text):
    """
    Sends sms
    :param phone: users phone number
    :param text: sms message text
    :return: True/False success status
    """
    obj = ActionResponse()
    obj.count = 1
    obj.messages = [text]
    return push(None, None, phone, obj, 'sms')
