from pprint import pprint
from urllib import response
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash, re
import requests

DATABASE = 'my_v_binder'

class Card:
    def __init__(self):
        pass

    @classmethod
    def get_all(cls, name):
        response = requests.get(f"https://api.pokemontcg.io/v2/cards?q=name:{name}")
        return response.json()

    @classmethod
    def get_one(cls, id):
        response = requests.get(f"https://api.pokemontcg.io/v2/cards/{id}")
        pprint(response)
        return response.json()