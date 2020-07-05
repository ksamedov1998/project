from datetime import date

from flask import json


class Plant(object):
    id = None
    name = None
    opt_humidity = None

    def __init__(self, dict):
        self.name = dict['name']
        self.opt_humidity = dict['opt_humidity']

    def __init__(self, id, name, opt_humidity):
        self.id = id
        self.name = name
        self.opt_humidity = opt_humidity

    def set_id(self, id):
        self.id = id
