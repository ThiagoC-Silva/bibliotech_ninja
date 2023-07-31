from ninja import Router
from .schema import UserSchema, UserCreateSchema, UserUpdateSchema
from .models import User
from typing import List
from django.shortcuts import get_object_or_404

router = Router()


@router.get('user/', response = List[UserSchema])
def list_user(request):
    return User.objects.all()


@router.post('user/')
def create_user(request, payload: UserCreateSchema ):
    User.objects.create(**payload.dict())
    return {'Sucess': True}


@router.put('user/{user_id}/')
def update_user(request, user_id: int, payload: UserUpdateSchema):
    user = get_object_or_404(User, id = user_id)
    for attr, value in payload.dict().items():
        setattr(user, attr, value)
    user.save()
    return {'Sucess': True}


@router.delete('user/{user_id}/')
def delete_user(request, user_id: int):
    user = get_object_or_404(User, id = user_id)
    user.delete()
    return {'Sucess': True}
    
