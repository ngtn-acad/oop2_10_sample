from .user import user_bp
from .goods import product_bp
from .order import order_bp

# Blueprintをリストとしてまとめる
blueprints = [
  user_bp,
  product_bp,
  order_bp
]
