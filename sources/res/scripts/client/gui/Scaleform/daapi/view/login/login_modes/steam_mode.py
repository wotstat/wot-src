import LGC
from gui import DialogsInterface
from base_lgc_mode import BaseLgcMode
from helpers import dependency
from skeletons.gameplay import IGameplayLogic

class SteamMode(BaseLgcMode):
    __gameplay = dependency.descriptor(IGameplayLogic)

    def __init__(self, view):
        super(SteamMode, self).__init__(view, None)
        return

    def onPopulate(self):
        if self.__checkLgcAvailable():
            super(SteamMode, self).onPopulate()
        return

    def updateForm(self):
        if self._loginManager.lgcAvailable:
            self._view.as_showSteamLoginFormS({b'userName': (LGC.getUserName())})
        else:
            self._view.as_showSteamLoginFormS({})
        return

    def _onLgcError(self):
        self._loginManager.tryPrepareLGCLogin()
        self.__checkLgcAvailable()
        return

    def __checkLgcAvailable(self):
        if not self._loginManager.lgcAvailable:
            DialogsInterface.showI18nInfoDialog(b'steamStartNeeded', self.__onDialogCallback)
            return False
        return True

    def __onDialogCallback(self, _):
        self.__gameplay.quitFromGame()
        return
