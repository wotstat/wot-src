from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.system_factory import registerScaleformLobbyPackages, registerLobbyTooltipsBuilders

def registerArmoryYardScaleform():
    registerScaleformLobbyPackages((b'armory_yard.gui.Scaleform.daapi.view.lobby',))
    return


def registerArmoryYardTooltipsBuilders():
    registerLobbyTooltipsBuilders([
     (
      b'armory_yard.gui.Scaleform.daapi.view.tooltips.lobby_builders',
      TOOLTIPS_CONSTANTS.ARMORY_YARD_LOBBY_SET)])
    return
