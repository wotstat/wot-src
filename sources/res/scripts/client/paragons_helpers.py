from gui.impl import backport
from gui.impl.gen import R
from gui.paragons.paragons_constants import ParagonsSystemMessages
from messenger import MessengerEntry
from messenger.m_constants import SCH_CLIENT_MSG_TYPE

def _pushParagonsClientMessage(messageType, parameters=None):
    return MessengerEntry.g_instance.protos.BW.serviceChannel.pushClientMessage({b'type': messageType, 
       b'parameters': parameters}, SCH_CLIENT_MSG_TYPE.PARAGONS_SM_TYPE)


def pushParagonsEnableMessage():
    _pushParagonsClientMessage(ParagonsSystemMessages.PROJECT_IS_AVAILABLE)
    return


def pushParagonsBranchResetAvailableMessage():
    _pushParagonsClientMessage(ParagonsSystemMessages.BRANCH_RESET_IS_AVAILABLE)
    return


def pushParagonsContinuingMessage():
    _pushParagonsClientMessage(ParagonsSystemMessages.PROJECT_IS_CONTINUING)
    return


def pushParagonsNewStageAvailableMessage():
    _pushParagonsClientMessage(ParagonsSystemMessages.NEW_CHAPTER_IS_AVAILABLE)
    return


def pushParagonsDisableMessage():
    _pushParagonsClientMessage(ParagonsSystemMessages.PROJECT_IS_UNAVAILABLE)
    return


def pushParagonsBranchResetErrorNotification():
    _pushParagonsClientMessage(ParagonsSystemMessages.BRANCH_RESET_ERROR)
    return


def pushParagonsBattleRewardMessage(coins, sourceID):
    _pushParagonsClientMessage(ParagonsSystemMessages.BATTLE_REWARD, parameters={b'coins': coins, 
       b'source': (backport.text(R.strings.paragons.notifications.source.dyn(sourceID)()))})
    return


def pushParagonsLevelRewardMessage(chapter, level, coins, showSelector, rewards):
    if showSelector:
        messageType = ParagonsSystemMessages.LEVEL_SELECTABLE_REWARDS
    else:
        messageType = ParagonsSystemMessages.LEVEL_REWARDS
    _pushParagonsClientMessage(messageType, parameters={b'coins': coins, 
       b'rewards': rewards, 
       b'chapter': chapter, 
       b'level': level})
    return


def pushParagonsBranchResetedNotification(credits, equipments, instructions, ammunitions, appearances, kits, crews):
    _pushParagonsClientMessage(ParagonsSystemMessages.BRANCH_RESETED, parameters={b'credits': credits, 
       b'equipments': equipments, 
       b'instructions': instructions, 
       b'ammunitions': ammunitions, 
       b'appearances': appearances, 
       b'kits': kits, 
       b'crews': crews})
    return


def pushParagonsBranchIsUnavalableMessage():
    _pushParagonsClientMessage(ParagonsSystemMessages.BRANCH_IS_UNAVAILABLE)
    return


def pushParagonsBranchIsAvalableMessage():
    _pushParagonsClientMessage(ParagonsSystemMessages.BRANCH_IS_AVAILABLE)
    return
