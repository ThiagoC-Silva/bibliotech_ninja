from ninja import Router
from .schema import UserSchema
from .models import User

router = Router()


@router.get('list/', response = UserSchema)
def list(request):
    return User.objects.all()