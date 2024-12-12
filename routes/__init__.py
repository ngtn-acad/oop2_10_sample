from .restaurant import restaurant_bp
from .food import food_bp
from .user import user_bp
from .api import api_bp



# Blueprintをリストとしてまとめる
blueprints = [
    restaurant_bp,
    food_bp,
    user_bp,
    api_bp,
]
