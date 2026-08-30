from gui.platform.base.response import PlatformResponse

class WGNPSteamEmailActionResponse(PlatformResponse):

    @property
    def isAccountAlreadyHasEmail(self):
        return self._isError(b'__all__', b'email_already_exists')

    @property
    def isEmailAlreadyTaken(self):
        return self._isError(b'__all__', b'spa_email_already_taken')


class WGNPSteamAccEmailAddResponse(WGNPSteamEmailActionResponse):

    @property
    def requestRestrictedUntilTime(self):
        return self.getData().get(b'extras', {}).get(b'restricted_until', 0)

    @property
    def isEmailInvalid(self):
        return self._isError(b'email', b'invalid')

    @property
    def isEmailForbidden(self):
        return self._isError(b'email', b'forbidden')

    @property
    def isEmailMinLength(self):
        return self._isError(b'email', b'min_length')

    @property
    def isEmailMaxLength(self):
        return self._isError(b'email', b'max_length')

    @property
    def isEmailBannedInCountry(self):
        return self._isError(b'email', b'restricted_by_country_policy')

    @property
    def isEmailRestrictedByCountry(self):
        return self._isError(b'__all__', b'restricted_by_country_policy')

    @property
    def isRequestLimitExceeded(self):
        return self._isError(b'__all__', b'request_limit_exceeded')


class WGNPSteamAccEmailConfirmResponse(WGNPSteamEmailActionResponse):

    @property
    def isConfirmationCodeIncorrect(self):
        return self._isError(b'__all__', b'incorrect_confirmation_code')

    @property
    def isConfirmationCodeDeactivated(self):
        return self._isError(b'__all__', b'incorrect_confirmation_code_request_deactivated')

    @property
    def isConfirmationCodeExpired(self):
        return self._isError(b'__all__', b'no_active_request', b'confirmation_code_expired')
