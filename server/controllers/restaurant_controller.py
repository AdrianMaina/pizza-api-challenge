# server/controllers/restaurant_controller.py

from flask import Blueprint, make_response, jsonify
from server.config import db
from server.models.restaurant import Restaurant

restaurant_bp = Blueprint('restaurant_bp', __name__, url_prefix='/restaurants')

@restaurant_bp.route('/')
def get_restaurants():
    restaurants = Restaurant.query.all()
    restaurants_data = []
    for restaurant in restaurants:
        restaurants_data.append({
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address
        })
    return make_response(jsonify(restaurants_data), 200)

@restaurant_bp.route('/<int:id>')
def get_restaurant_by_id(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return make_response(jsonify({"error": "Restaurant not found"}), 404)
    
    pizzas_data = []
    for rp in restaurant.pizzas:
        pizzas_data.append({
            "id": rp.pizza.id,
            "name": rp.pizza.name,
            "ingredients": rp.pizza.ingredients
        })

    restaurant_data = {
        "id": restaurant.id,
        "name": restaurant.name,
        "address": restaurant.address,
        "pizzas": pizzas_data
    }
    return make_response(jsonify(restaurant_data), 200)

@restaurant_bp.route('/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return make_response(jsonify({"error": "Restaurant not found"}), 404)
    
    db.session.delete(restaurant)
    db.session.commit()

    return make_response('', 204)