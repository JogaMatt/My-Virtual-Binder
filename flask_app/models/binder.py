from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash, re

DATABASE = 'my_v_binder'

class Binder:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.trade = data['trade']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data:dict ) -> int:
        query = "INSERT INTO binders (name, trade, user_id) VALUES ( %(name)s, %(trade)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db( query, data )

    @classmethod
    def update(cls,data):
        query = "UPDATE binders SET card_id=%(card_id)s, updated_at=NOW() WHERE user_id = %(user_id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_all_binders(cls):
        query = "SELECT * FROM binders;"
        results = connectToMySQL(DATABASE).query_db(query)
        binders = []
        for row in results:
            binders.append( cls(row) )
        return binders