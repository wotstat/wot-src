import typing
from constants import EMAIL_CONFIRMATION_TOKEN_NAME
from gui.platform.base.response import Codes
from gui.platform.base.statuses.constants import StatusTypes
from gui.platform.base.statuses.status import Status
from helpers import dependency
from skeletons.gui.shared import IItemsCache
if typing.TYPE_CHECKING:
    from gui.platform.wgnp.demo_account.request import CredentialsStatusParams

class DemoAccCredentialsStatus(Status):
    __slots__ = ()

    @property
    def isSpaWeakPassword(self):
        return self.data.get(b'error', b'') == b'spa_weak_password'

    @property
    def login(self):
        return self.data.get(b'login', b'')


class DemoAccNicknameStatus(Status):
    __slots__ = ()

    @property
    def cost(self):
        return self.data.get(b'cost', b'')


def createCredentialsConfirmationStatus():
    itemsCache = dependency.instance(IItemsCache)
    statusType = StatusTypes.CONFIRMATION_SENT
    if itemsCache.items.tokens.isTokenAvailable(EMAIL_CONFIRMATION_TOKEN_NAME):
        statusType = StatusTypes.CONFIRMED
    return DemoAccCredentialsStatus(statusType=statusType)


def createCredentialStatusFromResponse(response):
    statusType, data = StatusTypes.UNDEFINED, None
    if response.isSuccess():
        state, login = response.getData().get(b'state'), response.getData().get(b'login', b'')
        if state in (b'no_active_request', b'spa_login_already_taken'):
            statusType = StatusTypes.ADD_NEEDED
        elif state == b'email_sent':
            statusType, data = StatusTypes.ADDED, {b'login': login}
        if state == b'spa_generic_conflict':
            data = None
        elif state == b'spa_weak_password':
            statusType, data = StatusTypes.ADD_NEEDED, {b'error': b'spa_weak_password', b'login': login}
        else:
            return createCredentialsConfirmationStatus()
    else:
        data = {b'error': (Codes(response.code))}
    return DemoAccCredentialsStatus(statusType=statusType, data=data)


def createNicknameStatusFromResponse(response):
    statusType, data = StatusTypes.UNDEFINED, None
    if response.isSuccess():
        extras = response.getData().get(b'extras', {})
        errors = response.getData().get(b'errors', {}).get(b'__all__', [])
        cost = extras.get(b'free', b'')
        if extras.get(b'available', False):
            if cost == b'demo_free_first_renaming':
                statusType, data = StatusTypes.ADD_NEEDED, {b'cost': cost}
            else:
                statusType = StatusTypes.ADDED
        elif b'incomplete_state' in errors:
            statusType = StatusTypes.PROCESSING
        else:
            data = response.getData()
    else:
        data = {b'error': (Codes(response.code))}
    return DemoAccNicknameStatus(statusType=statusType, data=data)
