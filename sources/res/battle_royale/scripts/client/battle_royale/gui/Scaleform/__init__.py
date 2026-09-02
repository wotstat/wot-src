from __future__ import absolute_import
from gui.Scaleform.genConsts.BATTLEROYALE_ALIASES import BATTLEROYALE_ALIASES
from gui.shared.system_factory import registerScaleformBattlePackages, registerScaleformLobbyPackages, registerBattleTooltipsBuilders, registerLobbyTooltipsBuilders, registerHangarDynamicGuiProvider, registerLifecycleHandledSubViews
from constants import ARENA_GUI_TYPE, QUEUE_TYPE
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as _TOOLTIPS
from gui.Scaleform.required_libraries_config import addBattleRequiredLibraries
from battle_royale.gui.hangar_preset.battle_royale_dynamic_gui_provider import BattleRoyaleHangarDynamicGuiProvider

def registerBRBattlePackages():
    registerScaleformBattlePackages(ARENA_GUI_TYPE.BATTLE_ROYALE, (b'battle_royale.gui.Scaleform.daapi.view.battle', b'battle_royale.gui.Scaleform.daapi.view.battle.shared', b'messenger.gui.Scaleform.view.battle', b'gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics'))
    return


def registerBRLobbyPackages():
    registerScaleformLobbyPackages([
     b'battle_royale.gui.Scaleform.daapi.view.lobby',
     b'battle_royale.gui.impl.lobby.views'])
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
    registerLifecycleHandledSubViews([BATTLEROYALE_ALIASES.BR_HANGAR_VIEW])
    return


def registerCustomSwf():
    addBattleRequiredLibraries([b'ub_components.swf'], ARENA_GUI_TYPE.BATTLE_ROYALE, b'BattleRoyalePersonality')
    return


def registerBRBattleQueueProvider():
    from gui.prb_control import prb_utils
    from battle_royale.gui.Scaleform.daapi.view.lobby.battle_queue_provider import BattleRoyaleQueueProvider
    prb_utils.addProviderBattleQueueCls(QUEUE_TYPE.BATTLE_ROYALE, BattleRoyaleQueueProvider, b'BattleRoyalePersonality')
    return


def registerBRHangarPresetGetter():
    registerHangarDynamicGuiProvider(QUEUE_TYPE.BATTLE_ROYALE, BattleRoyaleHangarDynamicGuiProvider)
    return
