# server/controllers/restaurant_pizza_controller.py

from flask import Blueprint, make_response, jsonify, request
from server.config import db
from server.models.restaurant_pizza import RestaurantPizza
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant


restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__, url_prefix='/restaurant_pizzas')

@restaurant_pizza_bp.route('/', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    # Check if Pizza and Restaurant exist
    pizza = Pizza.query.get(pizza_id)
    restaurant = Restaurant.query.get(restaurant_id)

    if not pizza or not restaurant:
         return make_response(jsonify({"errors": ["Pizza or Restaurant not found."]}), 404)

    try:
        new_restaurant_pizza = RestaurantPizza(
            price=price,
            pizza_id=pizza_id,
            restaurant_id=restaurant_id
        )
        db.session.add(new_restaurant_pizza)
        db.session.commit()
        
        pizza_data = {
            "id": new_restaurant_pizza.pizza.id,
            "name": new_restaurant_pizza.pizza.name,
            "ingredients": new_restaurant_pizza.pizza.ingredients
        }
        return make_response(jsonify(pizza_data), 201)

    except ValueError as e:
        return make_response(jsonify({"errors": [str(e)]}), 400)
    except Exception:
         return make_response(jsonify({"errors": ["Validation errors"]}), 400)