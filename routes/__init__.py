from .user import user_bp
from .customer import customer_bp
from .order import order_bp

# Blueprintをリストとしてまとめる
blueprints = [
  user_bp,
  customer_bp,
  order_bp
]
