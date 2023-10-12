from app import db  # Import the database instance from your Flask app

class RestaurantPizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    pizza = db.relationship('Pizza', backref='restaurant_pizzas')
    restaurant = db.relationship('Restaurant', backref='pizza_restaurants')

    __table_args__ = (
        db.CheckConstraint(price.between(1, 30), name='check_price_range'),
    )