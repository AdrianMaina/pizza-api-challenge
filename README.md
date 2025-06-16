# Pizza Restaurant API

This is a RESTful API for a Pizza Restaurant built with Flask and SQLAlchemy. It allows users to view restaurants, pizzas, and associate pizzas with restaurants at specific prices.

## Project Structure

This project follows the MVC (Model-View-Controller) pattern:
- **`models/`**: Contains the SQLAlchemy data models (`Restaurant`, `Pizza`, `RestaurantPizza`).
- **`controllers/`**: Contains the Flask Blueprints that handle the API routing logic.
- **`app.py`**: The main application file that initializes the Flask app and registers the blueprints.
- **`config.py`**: Handles configuration, including database setup.
- **`seed.py`**: A script to seed the database with initial data.

## Setup and Installation

Follow these steps to get the application running locally.

1.  **Clone the Repository**
    ```sh
    git clone <your-repo-url>
    cd pizza-api-challenge
    ```

2.  **Create a Virtual Environment and Install Packages**
    This project uses `pipenv` to manage dependencies.
    ```sh
    pipenv install flask flask_sqlalchemy flask_migrate
    pipenv shell
    ```

3.  **Set Up the Database**
    You need to set the `FLASK_APP` environment variable and then run the database migration commands.
    ```sh
    export FLASK_APP=server/app.py
    flask db init  # Run this only once to initialize the migrations folder
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```

4.  **Seed the Database**
    Run the seed script to populate the database with sample data.
    ```sh
    python server/seed.py
    ```

5.  **Run the Application**
    ```sh
    python server/app.py
    ```
    The API will be available at `http://127.0.0.1:5555`.

## API Endpoints

### Restaurant Routes

#### `GET /restaurants`
- **Description**: Get a list of all restaurants.
- **Success Response (200 OK)**:
  ```json
  [
    {
      "id": 1,
      "name": "Sottocasa NYC",
      "address": "298 Atlantic Ave, Brooklyn, NY 11201"
    },
    {
      "id": 2,
      "name": "Pizzana",
      "address": "11712 San Vicente Blvd, Los Angeles, CA 90049"
    }
  ]