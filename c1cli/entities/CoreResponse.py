import json


class ActionResponse(object):
    def __init__(self):
        self.count = 0
        self.messages = []
        self.forced = None
        self.keyboard = None
        self.entities = []

    def to_dict(self):
        res = dict()
        res['Count'] = self.count
        res['Messages'] = self.messages
        res['ForcedState'] = self.forced
        res['ForcedKeyboard'] = self.keyboard
        res['Entities'] = list()
        for item in self.entities:
            res['Entities'].append(item.to_dict())
        return res


class ErrorResponse(ActionResponse):
    def __init__(self, message):
        ActionResponse.__init__(self)
        self.messages = [message]


class LinkedEntity:
    def __init__(self):
        self.name = None
        self.desc = None
        self.url = None
        self.options = list()

    def __str__(self):
        return json.dumps(self.to_dict())

    def to_dict(self):
        res = dict()
        res['Handle'] = ''
        res['Name'] = self.name
        res['ImageUrl'] = self.url
        res['Description'] = self.desc
        res["EntityOptions"] = self.options
        return res
