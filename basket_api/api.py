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

def calculate_amount(items: dict):
    prices = {'pen': 5.00, 'tshirt': 20.00, 'mug': 7.50}
    basket_items = dict()
    amount = 0.0

    for k,v in items.items():
        item_lower = k.lower()
        if item_lower == 'pen' and v>=2:
            if v%2 is 0:
                amount += v*(prices[item_lower]/2)
            else:
                amount += int(v/2)*(prices[item_lower])
                amount += prices[item_lower]
        elif item_lower == 'tshirt' and v >= 3:
            amount += v*(prices[item_lower]*0.75)
        else:
            amount += v*prices[item_lower]
        
        basket_items[item_lower] = v
    
    basket = {'items': basket_items, 'total_amount': amount}
    return basket

"""
Items is a dict, the keys are the item code and the values are the quantity
"""
@app.route('/basket/<basket_id>/add', methods=['PUT'])
def add_to_basket(basket_id):
    basket = basket_controler.get_basket(basket_id)
    if basket:
        items = request.get_json()['items']
        if validate_items(items):
            basket = calculate_amount(items)
            basket_controler.add_to_basket(basket_id, basket)
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