import json
from flask import Flask
from flask import abort
from flask import request
from basket_api.basket import BasketControler

app = Flask(__name__)

basket_controler = BasketControler()

@app.route('/basket/new')
def new_basket():
    basket_id = basket_controler.new_basket()
    return json.dumps({'basket_id': basket_id})

@app.route('/basket/<basket_id>')
def get_basket(basket_id):
    basket = basket_controler.get_basket(basket_id)
    if basket:
        return json.dumps(basket)
    else:
        abort(404)

@app.route('/basket/<basket_id>/total')
def get_basket_total(basket_id):
    basket_total = basket_controler.get_basket_total(basket_id)
    if basket_total:
        return json.dumps(basket_total)
    else:
        abort(404)

@app.route('/basket/<basket_id>/items')
def get_basket_items(basket_id):
    get_basket_items = basket_controler.get_basket_items(basket_id)
    if get_basket_items:
        return json.dumps(get_basket_items)
    else:
        abort(404)

def validate_items(items: dict):
    valid_codes = ['pen', 'tshirt', 'mug']
    for key in items.keys():
        if key.lower() not in valid_codes:
            return False
        if not isinstance(items[key], int):
            return False
    
    return True

"""
Items is a dict, the keys are the item code and the values are the quantity
"""
@app.route('/basket/<basket_id>/add', methods=['PUT'])
def add_to_basket(basket_id):
    basket = basket_controler.get_basket(basket_id)
    if basket:
        items = request.get_json()['items']
        if validate_items(items):
            
            basket_controler.add_to_basket(basket_id, items)
            basket = basket_controler.get_basket(basket_id)
            return json.dumps(basket)
        else:
            abort(400)
    else:
        abort(404)

@app.route('/basket/<basket_id>', methods=['DELETE'])
def delete_basket(basket_id):
    status = basket_controler.delete_basket(basket_id)
    return json.dumps({'deletion_status': bool(status)})