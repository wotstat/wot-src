import Event
from account_helpers.settings_core.settings_constants import GuiSettingsBehavior
from gui.shared.account_settings_helper import AccountSettingsHelper
from gui.shared.event_dispatcher import showCrew22Welcome
from helpers import dependency
from skeletons.gui.game_control import IHangarLoadingController, IBootcampController
from skeletons.gui.shared.utils import IHangarSpace

class HangarLoadingController(IHangarLoadingController):
    __bootcamp = dependency.descriptor(IBootcampController)
    __hangarSpace = dependency.descriptor(IHangarSpace)

    def __init__(self):
        super(HangarLoadingController, self).__init__()
        self.onHangarLoadedAfterLogin = Event.Event()
        self.__isConnectedAsAccount = False
        return

    def fini(self):
        self.__isConnectedAsAccount = False
        self.__hangarSpace.onSpaceCreate -= self.__hangarLoadedAfterLoginNotify
        return

    def onAvatarBecomePlayer(self):
        self.__isConnectedAsAccount = False
        return

    def onConnected(self):
        self.__isConnectedAsAccount = True
        return

    def onAccountBecomeNonPlayer(self):
        self.__isConnectedAsAccount = False
        self.__hangarSpace.onSpaceCreate -= self.__hangarLoadedAfterLoginNotify
        return

    def onDisconnected(self):
        self.__isConnectedAsAccount = False
        self.__hangarSpace.onSpaceCreate -= self.__hangarLoadedAfterLoginNotify
        return

    def onLobbyInited(self, event):
        if self.__isHangarLoadedAfterLogin():
            if self.__hangarSpace.spaceInited:
                self.__hangarLoadedAfterLoginNotify()
            else:
                self.__hangarSpace.onSpaceCreate += self.__hangarLoadedAfterLoginNotify
        return

    def __processCrewWelcomeScreen(self):
        if not AccountSettingsHelper.isWelcomeScreenShown(GuiSettingsBehavior.CREW_22_WELCOME_SHOWN):
            AccountSettingsHelper.welcomeScreenShown(GuiSettingsBehavior.CREW_22_WELCOME_SHOWN)
            showCrew22Welcome()
        return

    def __hangarLoadedAfterLoginNotify(self):
        self.__hangarSpace.onSpaceCreate -= self.__hangarLoadedAfterLoginNotify
        self.onHangarLoadedAfterLogin()
        return

    def __isHangarLoadedAfterLogin(self):
        return self.__isConnectedAsAccount and not self.__bootcamp.isInBootcamp() and not self.__bootcamp.isInBootcampAccount()
