from .customer import customer_bp
from .goods import goods_bp
from .order import order_bp

# Blueprintをリストとしてまとめる
blueprints = [customer_bp, goods_bp, order_bp]
