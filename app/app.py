import json
from flask import Flask
from basket import BasketControler

app = Flask(__name__)

basket_controler = BasketControler()

@app.route('/basket/new')
def new_basket():
    basket_id = basket_controler.new_basket()
    return json.dumps({'basket_id': basket_id})

@app.route('/basket/<basket_id>')
def get_basket(basket_id):
    basket_controler.get_basket(basket_id)
    return 'here your basket'

@app.route('/basket/<basket_id>/total')
def get_basket_total(basket_id):
    basket_controler.get_basket_total(basket_id)
    return 'the total for basket {}: '.format(basket_id)

@app.route('/basket/<basket_id>/items')
def get_basket_items(basket_id):
    return 'the items for basket {}'.format(basket_id)

@app.route('/basket/<basket_id>/add', methods=['PUT'])
def add_to_basket(basket_id):
    return 'added to basket {}'.format(basket_id)

@app.route('/basket/<basket_id>', methods=['DELETE'])
def delete_basket(basket_id):
    return 'deleted basket {}'.format(basket_id)