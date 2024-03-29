# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: enum.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


class AuthenticationState(betterproto.Enum):
    AUTH_STATE_UNSPECIFIED = 0
    AUTH_STATE_MFA_NEEDED = 1
    AUTH_STATE_PASSWORD_CHANGE_REQUIRED = 2
    AUTH_STATE_SUCCESS = 3
    AUTH_STATE_FAILED = 4


class ChangeUsernameState(betterproto.Enum):
    CHANGE_USERNAME_UNSPECIFIED = 0
    CHANGE_USERNAME_SUCCESS = 1
    CHANGE_USERNAME_USERNAME_ALREADY_IN_USE = 2


class ChangeEmailState(betterproto.Enum):
    CHANGE_EMAIL_UNSPECIFIED = 0
    CHANGE_EMAIL_SUCCESS = 1
    CHANGE_EMAIL_EMAIL_ALREADY_IN_USE = 2


class ChangePasswordState(betterproto.Enum):
    CHANGE_PASSWORD_UNSPECIFIED = 0
    CHANGE_PASSWORD_SUCCESS = 1
    CHANGE_PASSWORD_CURRENT_PASSWORD_INCORRECT = 2
    CHANGE_PASSWORD_NEW_PASSWORD_INSECURE = 3


class TwoFactorType(betterproto.Enum):
    TWO_FACTOR_UNSPECIFIED = 0
    TWO_FACTOR_TOTP = 1
    TWO_FACTOR_SMS = 2
    TWO_FACTOR_EMAIL = 3


class TwoFactorSaveState(betterproto.Enum):
    TWO_FACTOR_SAVE_UNSPECIFIED = 0
    TWO_FACTOR_SAVE_SUCCESS = 1
    TWO_FACTOR_SAVE_SMS_NOT_ENABLED = 2
    TWO_FACTOR_SAVE_CODE_INCORRECT = 3
    TWO_FACTOR_SAVE_CANNOT_UPDATE = 4


class DeleteTwoFactorState(betterproto.Enum):
    DELETE_TWO_FACTOR_UNSPECIFIED = 0
    DELETE_TWO_FACTOR_SUCCESS = 1
    DELETE_TWO_FACTOR_FAILED = 2


class ProtectionType(betterproto.Enum):
    PROTECTION_TYPE_UNSPECIFIED = 0
    PROTECTION_TYPE_NONE = 1
    PROTECTION_TYPE_HCAPTCHA = 2
    PROTECTION_TYPE_RECAPTCHA = 3


class NotificationType(betterproto.Enum):
    NOTIFICATION_TYPE_UNSPECIFIED = 0
    NOTIFICATION_TYPE_NONE = 1
    NOTIFICATION_TYPE_IMMEDIATE = 2
    NOTIFICATION_TYPE_DIGEST = 3


class DayPart(betterproto.Enum):
    DAY_PART_UNSPECIFIED = 0
    DAY_PART_AM = 1
    DAY_PART_PM = 2
