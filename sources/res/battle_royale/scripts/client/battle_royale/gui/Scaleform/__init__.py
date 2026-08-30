from gui.shared.system_factory import registerScaleformBattlePackages, registerScaleformLobbyPackages, registerBattleTooltipsBuilders, registerLobbyTooltipsBuilders
from constants import ARENA_GUI_TYPE
from gui.Scaleform.daapi.settings import config as sf_config
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as _TOOLTIPS

def registerBRBattlePackages():
    registerScaleformBattlePackages(ARENA_GUI_TYPE.BATTLE_ROYALE, (b'battle_royale.gui.Scaleform.daapi.view.battle', b'battle_royale.gui.Scaleform.daapi.view.battle.shared', b'messenger.gui.Scaleform.view.battle'))
    return


def registerBRLobbyPackages():
    registerScaleformLobbyPackages([b'battle_royale.gui.Scaleform.daapi.view.lobby'])
    return


def registerBRTooltipsBuilders():
    registerBattleTooltipsBuilders([
     (
      b'battle_royale.gui.Scaleform.daapi.view.tooltips.royale_battle_builders', _TOOLTIPS.ROYALE_BATTLE_SET)])
    registerLobbyTooltipsBuilders([
     (
      b'battle_royale.gui.Scaleform.daapi.view.tooltips.royale_lobby_builders', _TOOLTIPS.ROYALE_LOBBY_SET),
     (
      b'battle_royale.gui.Scaleform.daapi.view.tooltips.royale_battle_builders', _TOOLTIPS.ROYALE_BATTLE_SET)])
    return
