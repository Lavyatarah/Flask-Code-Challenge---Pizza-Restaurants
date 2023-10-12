from flask import Flask
from app import app
from flask import jsonify

# Route to get all restaurants
@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([{'id': restaurant.id, 'name': restaurant.name, 'address': restaurant.address} for restaurant in restaurants])

# Route to get a specific restaurant by ID
@app.route('/restaurants/<int:restaurant_id>', methods=['GET'])
def get_restaurant(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    if restaurant:
        pizzas = [{'id': pizza.id, 'name': pizza.name, 'ingredients': pizza.ingredients} for pizza in restaurant.pizzas]
        return jsonify({'id': restaurant.id, 'name': restaurant.name, 'address': restaurant.address, 'pizzas': pizzas})
    else:
        return jsonify({'error': 'Restaurant not found'}), 404

# Route to delete a restaurant by ID
@app.route('/restaurants/<int:restaurant_id>', methods=['DELETE'])
def delete_restaurant(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    if restaurant:
        RestaurantPizza.query.filter_by(restaurant_id=restaurant_id).delete()
        db.session.delete(restaurant)
        db.session.commit()
        return '', 204
    else:
        return jsonify({'error': 'Restaurant not found'}), 404

# Route to get all pizzas
@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([{'id': pizza.id, 'name': pizza.name, 'ingredients': pizza.ingredients} for pizza in pizzas])

# Route to create a new RestaurantPizza
@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')
    
    restaurant_pizza = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
    db.session.add(restaurant_pizza)
    
    try:
        db.session.commit()
        pizza = Pizza.query.get(pizza_id)
        return jsonify({'id': pizza.id, 'name': pizza.name, 'ingredients': pizza.ingredients}), 201
    except:
        db.session.rollback()
        return jsonify({'errors': ['validation errors']}), 400

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)