import typing, th_async
from gui.platform.base.statuses.constants import DEFAULT_CONTEXT
from skeletons.gui.platform.controller import IPlatformRequestController
if typing.TYPE_CHECKING:
    from helpers.server_settings import _Wgnp
    from gui.platform.base.statuses.events_mgr import StatusEventsManager
    from gui.platform.wgnp.steam_account.statuses import SteamAccEmailStatus
    from gui.platform.wgnp.steam_account.request import AddEmailParams, ConfirmEmailParams
    from gui.platform.wgnp.demo_account.statuses import DemoAccCredentialsStatus, DemoAccNicknameStatus
    from gui.platform.wgnp.demo_account.request import AddCredentialsParams, ConfirmCredentialsParams, ChangeNicknameParams, ValidateNicknameParams
    from gui.platform.wgnp.general.statuses import GeneralAccountCountryStatus
    from gui.platform.base.statuses.constants import StatusTypes

class IWGNPRequestController(IPlatformRequestController):

    @property
    def settings(self):
        raise NotImplementedError
        return


class IWGNPSteamAccRequestController(IWGNPRequestController):

    @th_async.th_async
    def addEmail(self, email, waitingID=None):
        raise NotImplementedError
        return

    @th_async.th_async
    def getEmailStatus(self, waitingID=None):
        raise NotImplementedError
        return

    @th_async.th_async
    def confirmEmail(self, code, waitingID=None):
        raise NotImplementedError
        return

    @property
    def emailAddedTime(self):
        raise NotImplementedError
        return

    @property
    def statusEvents(self):
        raise NotImplementedError
        return


class IWGNPDemoAccRequestController(IWGNPRequestController):

    @th_async.th_async
    def getCredentialsStatus(self, waitingID=None):
        raise NotImplementedError
        return

    @th_async.th_async
    def addCredentials(self, login, password, waitingID=None):
        raise NotImplementedError
        return

    @th_async.th_async
    def confirmCredentials(self, code, waitingID=None):
        raise NotImplementedError
        return

    @property
    def credentialsAddedTime(self):
        raise NotImplementedError
        return

    @property
    def statusEvents(self):
        raise NotImplementedError
        return

    def getCurrentStatus(self, context=DEFAULT_CONTEXT):
        raise NotImplementedError
        return

    @th_async.th_async
    def getNicknameStatus(self, waitingID=None):
        raise NotImplementedError
        return

    @th_async.th_async
    def validateNickname(self, nickname, waitingID=None):
        raise NotImplementedError
        return

    @th_async.th_async
    def changeNickname(self, nickname, cost, waitingID=None):
        raise NotImplementedError
        return


class IWGNPGeneralRequestController(IWGNPRequestController):

    @th_async.th_async
    def getAccountCountry(self, waitingID=None):
        raise NotImplementedError
        return
