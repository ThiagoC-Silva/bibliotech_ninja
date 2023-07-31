from ninja import Router
from .schema import UserSchema
from .models import User
from typing import List
from django.shortcuts import get_object_or_404

router = Router()


@router.get('user/', response = List[UserSchema])
def list_user(request):
    user = User.objects.all()
    return user


@router.post('create/')
def create_user(request, payload: UserSchema ):
    User.objects.create(**payload.dict())
    return {'Sucess': True}


@router.put('update/{user_id}/')
def update_user(request, user_id: int, payload: UserSchema):
    user = get_object_or_404(User, id = user_id)
    for attr, value in payload.dict().items():
        setattr(user, attr, value)
    user.save()
    return {'Sucess': True}


@router.delete('{user_id}/')
def delete_user(request, user_id: int):
    user = get_object_or_404(User, id = user_id)
    user.delete()
    return {'Sucess': True}
    
