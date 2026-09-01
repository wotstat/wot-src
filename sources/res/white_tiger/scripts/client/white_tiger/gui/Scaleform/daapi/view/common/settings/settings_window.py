from __future__ import absolute_import
from white_tiger.gui.Scaleform.daapi.view.meta.WhiteTigerSettingsWindowMeta import WhiteTigerSettingsWindowMeta
from helpers import dependency
from white_tiger.skeletons.white_tiger_controller import IWhiteTigerController

class WhiteTigerSettingsWindow(WhiteTigerSettingsWindowMeta):
    __wtController = dependency.descriptor(IWhiteTigerController)

    def __init__(self, **kwargs):
        super(WhiteTigerSettingsWindow, self).__init__(ctx={b'redefinedKeyMode': True, 
           b'isBattleSettings': True, 
           b'tabIndex': 0})
        return

    def _update(self):
        super(WhiteTigerSettingsWindow, self)._update()
        self.__setEventSettingVisibility()
        return

    def __setEventSettingVisibility(self):
        self.as_setIsEventS(self.__wtController.isInWhiteTigerMode())
        return
