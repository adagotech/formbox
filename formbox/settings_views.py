from typing import List

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache
from ninja import Router
from ninja_jwt.authentication import JWTAuth

from formbox.models import TwoFactorOption
from formbox.settings_api import *

router = Router()


@never_cache
@router.get("/get-user", response=GetUserResponse, auth=JWTAuth())
def get_user(request):
    return {"username": request.user.username, "email": request.user.email}


@never_cache
@router.get("/check-username/{username}", response=CheckAvailabilityResponse, auth=JWTAuth())
def check_username(request, username: str):
    count = User.objects.filter(username=username).count()
    return {"available": count == 0}


@never_cache
@router.get("/check-email/{email}", response=CheckAvailabilityResponse, auth=JWTAuth())
def check_email(request, email: str):
    count = User.objects.filter(email=email).count()
    return {"available": count == 0}


@never_cache
@router.post("/username-change", response=ChangeUsernameResponse, auth=JWTAuth())
def username_change(request, data: ChangeUsernameRequest):
    user = User.objects.get(id=request.user.id)
    user.username = data.newUsername
    user.save()
    return {"state": ChangeUsernameState.SUCCESS}


@never_cache
@router.post("/email-change", response=ChangeEmailResponse, auth=JWTAuth())
def email_change(request, data: ChangeEmailRequest):
    user = User.objects.get(id=request.user.id)
    user.email = data.newEmail
    user.save()
    return {"state": ChangeEmailState.SUCCESS}


@never_cache
@router.post("/password-change", response=ChangePasswordResponse, auth=JWTAuth())
def password_change(request, data: ChangePasswordRequest):
    user = authenticate(username=request.user.username, password=data.currentPassword)
    if user:
        user.set_password(data.newPassword)
        user.save()
        return {"state": ChangePasswordState.SUCCESS}
    else:
        return {"state": ChangePasswordState.CURRENT_PASSWORD_INCORRECT}


@never_cache
@router.get("/mfa-options", response=List[TwoFactor], auth=JWTAuth())
def password_change(request):
    options = TwoFactorOption.objects.filter(user=request.user, active=True).all()
    return [{
        "id": option.id,
        "nickname": option.nickname,
        "twoFactorType": option.two_factor_type,
        "target": option.get_masked_target()
    } for option in options]
