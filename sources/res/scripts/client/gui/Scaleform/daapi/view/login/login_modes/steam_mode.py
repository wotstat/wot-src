from __future__ import absolute_import
import WGC
from gui import DialogsInterface
from gui.Scaleform.daapi.view.login.login_modes.base_wgc_mode import BaseWgcMode
from helpers import dependency
from skeletons.gameplay import IGameplayLogic

class SteamMode(BaseWgcMode):
    __gameplay = dependency.descriptor(IGameplayLogic)

    def __init__(self, view):
        super(SteamMode, self).__init__(view, None)
        return

    def onPopulate(self):
        if self.__checkWgcAvailable():
            super(SteamMode, self).onPopulate()
        return

    def updateForm(self):
        if self._loginManager.wgcAvailable:
            self._view.as_showSteamLoginFormS({b'userName': (WGC.getUserName())})
        else:
            self._view.as_showSteamLoginFormS({})
        return

    def _onWgcError(self):
        self._loginManager.tryPrepareWGCLogin()
        self.__checkWgcAvailable()
        return

    def __checkWgcAvailable(self):
        if not self._loginManager.wgcAvailable:
            DialogsInterface.showI18nInfoDialog(b'steamStartNeeded', self.__onDialogCallback)
            return False
        return True

    def __onDialogCallback(self, _):
        self.__gameplay.quitFromGame()
        return
