from .user import user_bp
from .subject import subject_bp
from .order import order_bp

# Blueprintをリストとしてまとめる
blueprints = [
  user_bp,
  subject_bp,
  order_bp
]
