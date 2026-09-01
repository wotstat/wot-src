from __future__ import absolute_import

def getStateMachineRegistrators():
    from white_tiger.gui.impl.lobby.states import registerStates, registerTransitions
    return (
     registerStates, registerTransitions)


def getViewSettings():
    return ()


def getBusinessHandlers():
    return ()


def getContextMenuHandlers():
    return ()


def registerModeToPOMapping():
    from gui.Scaleform.daapi.view.lobby.formatters.tooltips import _MODENAME_TO_PO_FILE
    from white_tiger.gui.white_tiger_gui_constants import SELECTOR_BATTLE_TYPES
    _MODENAME_TO_PO_FILE.update({(SELECTOR_BATTLE_TYPES.WHITE_TIGER): b'white_tiger_lobby'})
    return


def registerWhiteTigerTokenBonus():
    from gui.server_events.bonuses import _BONUSES
    from constants import EVENT_TYPE
    from white_tiger.gui.server_events.bonuses import whiteTigerTokensFactory
    _BONUSES[b'tokens'].update({b'default': whiteTigerTokensFactory, 
       (EVENT_TYPE.BATTLE_QUEST): whiteTigerTokensFactory, 
       (EVENT_TYPE.TOKEN_QUEST): whiteTigerTokensFactory, 
       (EVENT_TYPE.PERSONAL_QUEST): whiteTigerTokensFactory, 
       (EVENT_TYPE.ELEN_QUEST): whiteTigerTokensFactory})
    _BONUSES[b'ticket'] = whiteTigerTokensFactory
    _BONUSES[b'lootBox'] = whiteTigerTokensFactory
    return


def registerWhiteTigerBonusPackers():
    from gui.shared.system_factory import registerBonusPackers
    from white_tiger.gui.wt_bonus_packers import WTTokenBonusPacker
    registerBonusPackers(b'ticket', WTTokenBonusPacker())
    return
