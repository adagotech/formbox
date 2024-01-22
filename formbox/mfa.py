import pyotp

from django.contrib.auth.models import User

from formbox.mail import send_email
from formbox.models import TwoFactorOption
from formbox.settings_api import TwoFactorType
from formbox.twilio import start_verification, check_verification


def send_mfa(mfa: TwoFactorOption):
    if mfa.two_factor_type == TwoFactorType.EMAIL:
        send_email(mfa.target, 'Your MFA Code', f"Your MFA code is {mfa.secret}")
    elif mfa.two_factor_type == TwoFactorType.SMS:
        start_verification(mfa.target)


def validate_mfa(mfa: TwoFactorOption, code: str) -> bool:
    if mfa.two_factor_type == TwoFactorType.EMAIL:
        return mfa.secret == code
    elif mfa.two_factor_type == TwoFactorType.SMS:
        return check_verification(mfa.target, code)
    elif mfa.two_factor_type == TwoFactorType.TOTP:
        return pyotp.TOTP(mfa.secret).now() == code