from battle_royale.gui.battle_control.controllers.notification_manager import RespawnMessage, MessageType
from gui.Scaleform.genConsts.BATTLE_ROYAL_CONSTS import BATTLE_ROYAL_CONSTS
from gui.impl import backport
from gui.impl.gen import R

def formatRespawnedMessage(time, delay=0, postDelay=1):
    message = RespawnMessage()
    message.time = time
    message.delay = delay
    message.postDelay = postDelay
    return message


def formatRespawnActivatedMessage(*args, **kwargs):
    message = formatRespawnedMessage(*args, **kwargs)
    message.msgType = MessageType.respActivatedMsg
    message.messageVO = {b'time': 0, 
       b'quickHide': False, 
       b'title': (backport.text(R.strings.battle_royale.battle.respawnMessagePanel.respawnActivated.title())), 
       b'description': (backport.text(R.strings.battle_royale.battle.respawnMessagePanel.respawnActivated.description())), 
       b'messageLinkage': (BATTLE_ROYAL_CONSTS.MESSAGE_TIMER_LINKAGE)}
    return message


def formatRespawnFinishedMessage(*args, **kwargs):
    message = formatRespawnedMessage(*args, **kwargs)
    message.msgType = MessageType.respFinishedMsg
    message.messageVO = {b'time': 0, 
       b'quickHide': False, 
       b'title': (backport.text(R.strings.battle_royale.battle.respawnMessagePanel.respawned.title())), 
       b'description': (backport.text(R.strings.battle_royale.battle.respawnMessagePanel.respawned.description())), 
       b'messageLinkage': (BATTLE_ROYAL_CONSTS.MESSAGE_RESPAWN_NO_ICON_LINKAGE)}
    return message


def formatRespawnNotAvailableMessage(*args, **kwargs):
    message = formatRespawnedMessage(*args, **kwargs)
    message.msgType = MessageType.respNotAvailableMsg
    message.messageVO = {b'time': 0, 
       b'quickHide': False, 
       b'title': (backport.text(R.strings.battle_royale.battle.respawnMessagePanel.respawnNotAvailable.title())), 
       b'description': (backport.text(R.strings.battle_royale.battle.respawnMessagePanel.respawnNotAvailable.description())), 
       b'messageLinkage': (BATTLE_ROYAL_CONSTS.MESSAGE_RESPAWN_NOT_AVAILABLE_LINKAGE)}
    return message


def formatRespawnNotAvailableSoonMessage(*args, **kwargs):
    message = formatRespawnedMessage(*args, **kwargs)
    message.msgType = MessageType.respNotAvailableSoonMsg
    message.messageVO = {b'time': 0, 
       b'quickHide': False, 
       b'title': (backport.text(R.strings.battle_royale.battle.respawnMessagePanel.respawnNotAvailableSoon.title())), 
       b'messageLinkage': (BATTLE_ROYAL_CONSTS.MESSAGE_RESPAWN_NO_ICON_LINKAGE)}
    return message


def formatRespawnActivatedSquadMessage(*args, **kwargs):
    message = formatRespawnedMessage(*args, **kwargs)
    message.msgType = MessageType.respActivatedMsg
    message.messageVO = {b'time': 0, 
       b'quickHide': False, 
       b'title': (backport.text(R.strings.battle_royale.battle.respawnMessagePanel.respawnActivatedSquad.title())), 
       b'messageLinkage': (BATTLE_ROYAL_CONSTS.MESSAGE_TIMER_LINKAGE)}
    return message


def formatAllyInBattleMessage(*args, **kwargs):
    message = formatRespawnedMessage(*args, **kwargs)
    message.msgType = MessageType.allyInBattleMsg
    message.messageVO = {b'time': 0, 
       b'quickHide': False, 
       b'title': (backport.text(R.strings.battle_royale.battle.respawnMessagePanel.squad.inBattle.title())), 
       b'description': (backport.text(R.strings.battle_royale.battle.respawnMessagePanel.squad.inBattle.description())), 
       b'messageLinkage': (BATTLE_ROYAL_CONSTS.MESSAGE_RESPAWN_AVAILABLE_LINKAGE)}
    return message


def formatPickUpSphereMessage(*args, **kwargs):
    message = formatRespawnedMessage(*args, **kwargs)
    message.msgType = MessageType.pickUpSphereMsg
    message.messageVO = {b'time': 0, 
       b'quickHide': False, 
       b'title': (backport.text(R.strings.battle_royale.battle.respawnMessagePanel.squad.pickUp.title())), 
       b'description': (backport.text(R.strings.battle_royale.battle.respawnMessagePanel.squad.pickUp.description())), 
       b'messageLinkage': (BATTLE_ROYAL_CONSTS.MESSAGE_RESPAWN_NO_ICON_LINKAGE)}
    return message


def formatStayInCoverMessage(*args, **kwargs):
    message = formatRespawnedMessage(*args, **kwargs)
    message.msgType = MessageType.stayInCoverMsg
    message.messageVO = {b'time': 0, 
       b'quickHide': False, 
       b'title': (backport.text(R.strings.battle_royale.battle.respawnMessagePanel.squad.stayInCover.title())), 
       b'description': (backport.text(R.strings.battle_royale.battle.respawnMessagePanel.squad.stayInCover.description())), 
       b'messageLinkage': (BATTLE_ROYAL_CONSTS.MESSAGE_TIMER_LINKAGE)}
    return message


def formatAllyRespawnedMessage(*args, **kwargs):
    message = formatRespawnedMessage(*args, **kwargs)
    message.msgType = MessageType.allyRespawnedMessage
    message.messageVO = {b'time': 0, 
       b'quickHide': False, 
       b'title': (backport.text(R.strings.battle_royale.battle.respawnMessagePanel.squad.squadmanRespawned.title())), 
       b'description': (backport.text(R.strings.battle_royale.battle.respawnMessagePanel.squad.squadmanRespawned.description())), 
       b'messageLinkage': (BATTLE_ROYAL_CONSTS.MESSAGE_RESPAWN_NO_ICON_LINKAGE)}
    return message


def formatAllyRespawnInProgressMessage(*args, **kwargs):
    message = formatRespawnedMessage(*args, **kwargs)
    message.messageVO = {b'time': 0, 
       b'quickHide': False, 
       b'title': (backport.text(R.strings.battle_royale.battle.respawnMessagePanel.squad.respawning.title())), 
       b'messageLinkage': (BATTLE_ROYAL_CONSTS.MESSAGE_TIMER_LINKAGE)}
    return message
