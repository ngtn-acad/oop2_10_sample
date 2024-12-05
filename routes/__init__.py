from .user import user_bp
from .product import product_bp
from .order import order_bp
from .review import review_b

# Blueprintをリストとしてまとめる
blueprints = [
  user_bp,
  product_bp,
  order_bp,
  review_bp
]
