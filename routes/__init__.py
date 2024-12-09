from .user import user_bp
from .appointment import appointment_bp
from .jibyou import jibyou_bp

# Blueprintをリストとしてまとめる
blueprints = [
  user_bp,
  appointment_bp,
  jibyou_bp
]
