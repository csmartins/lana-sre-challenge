import json
from flask import Flask
from flask import abort
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

@app.route('/basket/<basket_id>/add', methods=['PUT'])
def add_to_basket(basket_id):
    return 'added to basket {}'.format(basket_id)

@app.route('/basket/<basket_id>', methods=['DELETE'])
def delete_basket(basket_id):
    return 'deleted basket {}'.format(basket_id)