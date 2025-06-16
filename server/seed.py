# server/seed.py

from server.config import app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

def seed_data():
    with app.app_context():
        # Clear existing data
        print("Clearing database...")
        RestaurantPizza.query.delete()
        Restaurant.query.delete()
        Pizza.query.delete()

        # Seed Restaurants
        print("Seeding restaurants...")
        restaurants_data = [
            {"name": "Sottocasa NYC", "address": "298 Atlantic Ave, Brooklyn, NY 11201"},
            {"name": "Pizzana", "address": "11712 San Vicente Blvd, Los Angeles, CA 90049"},
            {"name": "Kiki's Pizza", "address": "123 Main St, Anytown, USA"}
        ]
        restaurants = [Restaurant(**data) for data in restaurants_data]
        db.session.add_all(restaurants)
        db.session.commit()

        # Seed Pizzas
        print("Seeding pizzas...")
        pizzas_data = [
            {"name": "Cheese", "ingredients": "Dough, Tomato Sauce, Cheese"},
            {"name": "Pepperoni", "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"},
            {"name": "Margherita", "ingredients": "Dough, Tomato Sauce, Mozzarella, Basil"}
        ]
        pizzas = [Pizza(**data) for data in pizzas_data]
        db.session.add_all(pizzas)
        db.session.commit()

        # Seed RestaurantPizzas (associations)
        print("Seeding restaurant-pizza associations...")
        restaurant_pizzas_data = [
            {"price": 15, "restaurant_id": restaurants[0].id, "pizza_id": pizzas[0].id},
            {"price": 18, "restaurant_id": restaurants[0].id, "pizza_id": pizzas[1].id},
            {"price": 20, "restaurant_id": restaurants[1].id, "pizza_id": pizzas[2].id},
            {"price": 10, "restaurant_id": restaurants[2].id, "pizza_id": pizzas[0].id},
        ]
        restaurant_pizzas = [RestaurantPizza(**data) for data in restaurant_pizzas_data]
        db.session.add_all(restaurant_pizzas)
        db.session.commit()

        print("Seeding complete!")

if __name__ == '__main__':
    seed_data()