from .user import user_bp
from .product import product_bp
from .order import order_bp
from.lunch import lunch_bp

# Blueprintをリストとしてまとめる
blueprints = [
  user_bp,
  product_bp,
  order_bp,
  lunch_bp,
]
