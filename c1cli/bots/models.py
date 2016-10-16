# -*- coding: utf-8 -*-


class Bot:
    def __init__(self, data=None):
        if data is None:
            data = dict()
        self.name = data['name'] if 'name' in data.keys() else None
        self.language = data['language'] if 'language' in data.keys() else None
        self.fancy_name = data['fancy_name'] if 'fancy_name' in data.keys() else None
        self.scenario = data['scenario'] if 'scenario' in data.keys() else None

    def to_json(self):
        data = dict()
        data['name'] = self.name
        data['language'] = self.language
        data['fancy_name'] = self.fancy_name
        data['scenario'] = self.scenario
        return data

    def __eq__(self, other):
        if not self.name == other.name:
            return False
        if not self.language == other.language:
            return False
        if not self.fancy_name == other.fancy_name:
            return False
        if not self.scenario == other.scenario:
            return False
        return True