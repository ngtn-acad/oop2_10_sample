from .customer import customer_bp
from .product import product_bp
from .goods import product_bp
from .order import order_bp

# Blueprintをリストとしてまとめる
blueprints = [
  customer_bp,
  product_bp,
  order_bp
]
