import json
import uuid

from redis import Redis
from os import environ 

class BasketControler:
    def __init__(self):
        self.REDIS_CONN_STRING = environ.get('REDIS_CONN_STRING')
        self.redis_connection = self.redis_setup(self.REDIS_CONN_STRING)

    def redis_setup(self, redis_conn_string):
        (host, port, password) = redis_conn_string.split(',')
        rconn = Redis(
                    host=host,
                    port=port)
                    # password=password)
        return rconn

    def new_basket(self):
        basket_id = str(uuid.uuid4())
        clean_basket = {'items':[],'total_amount':0}
        self.redis_connection.set(basket_id, json.dumps(clean_basket))
        return basket_id

    def get_basket(self, basket_id):
        pass

    def get_basket_total(self, basket_id):
        pass

    def get_basket_items(self, basket_id):
        pass

    def add_to_basket(self, basket_id, items):
        pass

    def delete_basket(self, basket_id):
        pass