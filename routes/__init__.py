from .user import user_bp
from .product import product_bp
from .push import order_bp

# Blueprintをリストとしてまとめる
blueprints = [
  user_bp,
  product_bp,
  order_bp
]
