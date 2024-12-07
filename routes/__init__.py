from .order import order_bp
from .drink import drink_bp
from .food import food_bp
from .customer import customer_bp


# Blueprintをリストとしてまとめる
blueprints = [
 drink_bp,
 food_bp,
 customer_bp,
  order_bp
]
