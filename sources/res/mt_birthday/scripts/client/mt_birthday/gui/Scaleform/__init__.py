from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.system_factory import registerLobbyTooltipsBuilders, registerScaleformLobbyPackages

def registerBirthdayScaleform():
    registerScaleformLobbyPackages((b'mt_birthday.gui.Scaleform.daapi.view.lobby',))
    return


def registerGiftSystemTooltipsBuilders():
    registerLobbyTooltipsBuilders([
     (
      b'mt_birthday.gui.Scaleform.daapi.view.tooltips.lobby_builders',
      TOOLTIPS_CONSTANTS.BIRTHDAY_SET)])
    return
