from .user import user_bp
from .appointment import appointment_bp
from .medical_condition import medical_condition_bp
from .booking import booking_bp
from .jibyou import jibyou_bp

# Blueprintをリストとしてまとめる
blueprints = [
    user_bp,
    appointment_bp,
    medical_condition_bp,
    booking_bp,
    jibyou_bp
]