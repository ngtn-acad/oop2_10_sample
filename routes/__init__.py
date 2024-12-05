from .user import user_bp
from .customer import customer_bp
from .order import order_bp
from .food import food_bp
from .drink import drink_bp
from .customer import customer_bp
from .reservation import reservation_bp

# Blueprintをリストとしてまとめる
blueprints = [
  user_bp,
  product_bp,
  order_bp,
  food_bp,
  drink_bp,
  customer_bp,
  reservation_bp,
]