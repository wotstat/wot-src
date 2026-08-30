from helpers import aop
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Dict, Sequence

class _FlashDisableSettingsAspect(aop.Aspect):

    def __init__(self, settings):
        super(_FlashDisableSettingsAspect, self).__init__()
        self.__disabledSettings = settings
        return

    def atCall(self, cd):
        for itemId, guiPath in self.__disabledSettings.iteritems():
            self.__disableControl(cd, itemId, guiPath)

        return

    def __disableControl(self, cd, itemId, guiPath):
        page = b''
        subpage = b''
        pathLen = len(guiPath)
        if pathLen == 1:
            page = guiPath[0]
        elif pathLen == 2:
            page, subpage = guiPath
        cd.self.as_disableControlS(page, itemId, subpage)
        return


class DisableCameraSettingsFlashPointcut(aop.Pointcut):

    def __init__(self, settings):
        aop.Pointcut.__init__(self, b'gui.Scaleform.daapi.view.common.settings.SettingsWindow', b'SettingsWindow', b'as_setDataS')
        self.addAspect(_FlashDisableSettingsAspect, settings=settings)
        return


class DisableAltModeTogglePointcut(aop.Pointcut):

    def __init__(self):
        super(DisableAltModeTogglePointcut, self).__init__(b'AvatarInputHandler.control_modes', b'ArcadeControlMode', b'^__activateAlternateMode$')
        return
