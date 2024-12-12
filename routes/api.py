from flask import Blueprint, jsonify
from models import Restaurant
from playhouse.shortcuts import model_to_dict

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.get('/restaurants')
def restaurants():
    restaurants = [model_to_dict(restaurant) for restaurant in Restaurant.select()]
    return jsonify(restaurants)
