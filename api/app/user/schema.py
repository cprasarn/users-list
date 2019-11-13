from app import ma
from app.user.models import User

class UserSchema(ma.ModelSchema):
    class Meta:
        model = User