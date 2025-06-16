# server/controllers/pizza_controller.py

from flask import Blueprint, make_response, jsonify
from server.models.pizza import Pizza

pizza_bp = Blueprint('pizza_bp', __name__, url_prefix='/pizzas')

@pizza_bp.route('/')
def get_pizzas():
    pizzas = Pizza.query.all()
    pizzas_data = []
    for pizza in pizzas:
        pizzas_data.append({
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients
        })
    return make_response(jsonify(pizzas_data), 200)