from pprint import pprint
from urllib import response
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash, re
import requests

DATABASE = 'my_v_binder'

class Card:
    def __init__(self, data):
        self.id = data['id'],
        self.name = data['name'],
        self.api_id = data['api_id']
        self.binder_id = data['binder_id']

    @classmethod
    def save(cls, data:dict ) -> int:
        query = "INSERT INTO cards (name, api_id, binder_id) VALUES ( %(name)s, %(api_id)s, %(binder_id)s);"
        return connectToMySQL(DATABASE).query_db( query, data )

    @classmethod
    def get_my_cards(cls, data):
        query = "SELECT * FROM cards WHERE binder_id = %(binder_id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        cards = []
        for row in results:
            cards.append( cls(row) )
        return cards

    @classmethod
    def get_all(cls, name):
        response = requests.get(f"https://api.pokemontcg.io/v2/cards?q=name:{name}")
        return response.json()

    @classmethod
    def get_one(cls, id):
        response = requests.get(f"https://api.pokemontcg.io/v2/cards/{id}")
        pprint(response)
        return response.json()