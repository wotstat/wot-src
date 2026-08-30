from httplib import REQUEST_TIMEOUT
from gui.platform.base.response import PlatformResponse

class WGNPDemoAccCredentialsActionResponse(PlatformResponse):

    @property
    def isAccountAlreadyHasLogin(self):
        return self._isError(b'__all__', b'spa_already_has_login')

    @property
    def isLoginAlreadyTaken(self):
        return self._isError(b'__all__', b'spa_login_already_taken')


class WGNPDemoAccCredentialsAddResponse(WGNPDemoAccCredentialsActionResponse):

    @property
    def requestRestrictedUntilTime(self):
        return self.getData().get(b'extras', {}).get(b'restricted_until', 0)

    @property
    def isCredentialsNotFound(self):
        return self._isError(b'__all__', b'not_found')

    @property
    def isRequestLimitExceeded(self):
        return self._isError(b'__all__', b'request_limit_exceeded')

    @property
    def isPasswordWeak(self):
        return self._isError(b'password', b'weak_password') or self._isError(b'__all__', b'weak_password')

    @property
    def isRestrictedByCountryPolicy(self):
        return self._isError(b'login', b'restricted_by_country_policy')

    @property
    def isLoginInvalid(self):
        return self._isError(b'login', b'invalid')

    @property
    def isLoginEmpty(self):
        return self._isError(b'login', b'required')

    @property
    def isLoginMinLength(self):
        return self._isError(b'login', b'min_length')

    @property
    def isLoginMaxLength(self):
        return self._isError(b'login', b'max_length')

    @property
    def isPasswordInvalid(self):
        return self._isError(b'password', b'invalid')

    @property
    def isPasswordEmpty(self):
        return self._isError(b'password', b'required')

    @property
    def isPasswordMinLength(self):
        return self._isError(b'password', b'min_length')

    @property
    def isPasswordMaxLength(self):
        return self._isError(b'password', b'max_length')


class WGNPDemoAccCredentialsConfirmResponse(WGNPDemoAccCredentialsActionResponse):

    @property
    def isConfirmationCodeIncorrect(self):
        return self._isError(b'__all__', b'incorrect_confirmation_code')

    @property
    def isConfirmationCodeDeactivated(self):
        return self._isError(b'__all__', b'incorrect_confirmation_code_request_deactivated')

    @property
    def isConfirmationCodeExpired(self):
        return self._isError(b'__all__', b'no_active_request')

    @property
    def isFormInvalid(self):
        return self._isError(b'__all__', b'invalid_form')

    @property
    def isCodeEmpty(self):
        return self._isError(b'code', b'required')

    @property
    def isSpaWeakPassword(self):
        return self._isError(b'__all__', b'spa_weak_password')

    @property
    def isSpaGenericConflict(self):
        return self._isError(b'__all__', b'spa_generic_conflict')

    @property
    def isInvalidChoice(self):
        return self._isError(b'game', b'invalid_choice')


class WGNPDemoAccChangeNicknameResponse(PlatformResponse):

    @property
    def isNameEmpty(self):
        return self._isError(b'name', b'required')

    @property
    def isNameInvalid(self):
        return self._isError(b'name', b'invalid')

    @property
    def isNameMaxLength(self):
        return self._isError(b'name', b'max_length')

    @property
    def isNameMinLength(self):
        return self._isError(b'name', b'min_length')

    @property
    def isNameForbidden(self):
        return self._isError(b'name', b'forbidden')

    @property
    def isNameExists(self):
        return self._isError(b'name', b'exists')

    @property
    def isGameEmpty(self):
        return self._isError(b'game', b'required')

    @property
    def isGameInvalid(self):
        return self._isError(b'game', b'invalid')

    @property
    def isCostEmpty(self):
        return self._isError(b'cost', b'required')

    @property
    def isCostInvalid(self):
        return self._isError(b'cost', b'invalid')

    @property
    def isViaMaxLength(self):
        return self._isError(b'via', b'max_length')

    @property
    def isTimeout(self):
        return self._isError(b'__all__', b'timeout') or self.getExtraCode() == REQUEST_TIMEOUT

    @property
    def isRequestTimeout(self):
        return self._isError(b'__all__', b'rename_request_timeout')

    @property
    def isAuthTokenExpired(self):
        return self._isError(b'__all__', b'oauth_token_expired')

    @property
    def isAuthTokenDenied(self):
        return self._isError(b'__all__', b'oauth_permission_denied')

    @property
    def isNEGold(self):
        return self._isError(b'__all__', b'ne_gold')

    @property
    def isFreeCostUnavailable(self):
        return self._isError(b'__all__', b'does_not_have_demo_free_first_renaming')

    @property
    def isCurrencyBanned(self):
        return self._isError(b'__all__', b'unknown_ban_type')

    @property
    def isNeedNicknameStatusCheck(self):
        return self._isError(b'__all__', b'rename_request_timeout', b'does_not_have_demo_free_first_renaming')


class WGNPDemoAccValidateNicknameResponse(PlatformResponse):

    @property
    def spaId(self):
        return self.getData().get(b'spa_id')

    @property
    def suggestions(self):
        return self.getData().get(b'suggestions', [])

    @property
    def isBanned(self):
        return self.getData().get(b'banned', False)

    @property
    def isOccupied(self):
        return self.spaId is not None

    @property
    def isInvalid(self):
        return b'invalid' in self.getData().get(b'__all__', [])

    @property
    def isMinLength(self):
        return b'min_length' in self.getData().get(b'__all__', [])

    @property
    def isMaxLength(self):
        return b'max_length' in self.getData().get(b'__all__', [])
