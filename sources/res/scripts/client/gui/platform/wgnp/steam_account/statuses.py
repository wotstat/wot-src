import typing
from gui.platform.base.response import Codes
from gui.platform.base.statuses.constants import StatusTypes
from gui.platform.base.statuses.status import Status
if typing.TYPE_CHECKING:
    from gui.platform.wgnp.steam_account.request import EmailStatusParams

class SteamAccEmailStatus(Status):
    __slots__ = ()

    @property
    def email(self):
        return self.data.get(b'email', b'')


def createEmailStatusFromResponse(response):
    statusType, data = StatusTypes.UNDEFINED, None
    if response.isSuccess():
        state = response.getData().get(b'state')
        if state in (b'no_active_request', b'spa_email_already_taken', b'confirmation_code_expired'):
            statusType = StatusTypes.ADD_NEEDED
        elif state == b'email_sent':
            statusType, data = StatusTypes.ADDED, {b'email': (response.getData().get(b'email', b''))}
        elif state == b'spa_generic_conflict':
            data = {b'error': b'spa_generic_conflict'}
        else:
            statusType = StatusTypes.CONFIRMED
    else:
        data = {b'error': (Codes(response.code))}
    return SteamAccEmailStatus(statusType=statusType, data=data)
