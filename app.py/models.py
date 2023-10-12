from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from app import db
from app import app


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza_restaurants.db'
db = SQLAlchemy(app)

# Define your models here

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name
class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    pizzas = db.relationship('Pizza', secondary='restaurant_pizza', back_populates='restaurants')

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    ingredients = db.Column(db.String(255), nullable=False)
    restaurants = db.relationship('Restaurant', secondary='restaurant_pizza', back_populates='pizzas')

class RestaurantPizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False, check_constraint='price >= 1 and price <= 30')
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    pizza = db.relationship('Pizza', backref='restaurant_pizzas')
    restaurant = db.relationship('Restaurant', backref='pizza_restaurants')