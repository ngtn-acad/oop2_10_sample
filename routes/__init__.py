from .user import user_bp
from .subject import subject_bp
from .regist import regist_bp

# Blueprintをリストとしてまとめる
blueprints = [
  user_bp,
  subject_bp,
  regist_bp
]
