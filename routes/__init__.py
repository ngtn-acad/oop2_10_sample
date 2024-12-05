from .user import user_bp
from .product import product_bp
from .order import role_bp

# Blueprintをリストとしてまとめる
blueprints = [
  user_bp,
  product_bp,
  role_bp
]
