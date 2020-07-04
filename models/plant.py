from flask import json


class Plant(object):
    name = None
    opt_Humidity = None

    def __init__(self,dict):
        self.name= dict['name']
        self.opt_Humidity = dict['opt_Humidity']
