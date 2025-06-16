# server/app.py

from server.config import app, db

# Import blueprints from controllers
from server.controllers.restaurant_controller import restaurant_bp
from server.controllers.pizza_controller import pizza_bp
from server.controllers.restaurant_pizza_controller import restaurant_pizza_bp

# Register blueprints
app.register_blueprint(restaurant_bp)
app.register_blueprint(pizza_bp)
app.register_blueprint(restaurant_pizza_bp)

# A simple root route for health check
@app.route('/')
def index():
    return '<h1>Pizza Restaurant API</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)