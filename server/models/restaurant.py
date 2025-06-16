# server/models/restaurant.py

from server.config import db

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)

    # Relationship to RestaurantPizza
    # cascade="all, delete-orphan" ensures that when a Restaurant is deleted,
    # all its associated RestaurantPizza records are also deleted.
    pizzas = db.relationship('RestaurantPizza', back_populates='restaurant', cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Restaurant {self.name}>'