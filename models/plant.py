from datetime import date

from flask import json

class Plant(object):
    id=None
    name = None
    opt_Humidity = None

    def __init__(self, dict):
        self.name = dict['name']
        self.opt_Humidity = dict['opt_Humidity']

    def set_id(self, id):
        self.id = id
