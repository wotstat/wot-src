from gui.Scaleform.genConsts.BATTLE_ROYAL_CONSTS import BATTLE_ROYAL_CONSTS
from gui.impl import backport
from gui.impl.gen import R

def formatRespawnActivatedMessage(time, delay=0):
    return {b'time': time, 
       b'delay': delay, 
       b'quickHide': False, 
       b'title': (backport.text(R.strings.battle_royale.battle.respawnMessagePanel.respawnActivated.title())), 
       b'description': (backport.text(R.strings.battle_royale.battle.respawnMessagePanel.respawnActivated.description())), 
       b'messageLinkage': (BATTLE_ROYAL_CONSTS.MESSAGE_TIMER_LINKAGE)}


def formatRespawnFinishedMessage(time, delay=0):
    return {b'time': time, 
       b'delay': delay, 
       b'quickHide': False, 
       b'title': (backport.text(R.strings.battle_royale.battle.respawnMessagePanel.respawned.title())), 
       b'description': (backport.text(R.strings.battle_royale.battle.respawnMessagePanel.respawned.description())), 
       b'messageLinkage': (BATTLE_ROYAL_CONSTS.MESSAGE_RESPAWN_NO_ICON_LINKAGE)}


def formatRespawnNotAvailableMessage(time, delay=0):
    return {b'time': time, 
       b'delay': delay, 
       b'quickHide': False, 
       b'title': (backport.text(R.strings.battle_royale.battle.respawnMessagePanel.respawnNotAvailable.title())), 
       b'description': (backport.text(R.strings.battle_royale.battle.respawnMessagePanel.respawnNotAvailable.description())), 
       b'messageLinkage': (BATTLE_ROYAL_CONSTS.MESSAGE_RESPAWN_NOT_AVAILABLE_LINKAGE)}


def formatRespawnNotAvailableSoonMessage(time, delay=0):
    return {b'time': time, 
       b'delay': delay, 
       b'quickHide': False, 
       b'title': (backport.text(R.strings.battle_royale.battle.respawnMessagePanel.respawnNotAvailableSoon.title())), 
       b'messageLinkage': (BATTLE_ROYAL_CONSTS.MESSAGE_RESPAWN_NO_ICON_LINKAGE)}


def formatRespawnActivatedSquadMessage(time, delay=0):
    return {b'time': time, 
       b'delay': delay, 
       b'quickHide': False, 
       b'title': (backport.text(R.strings.battle_royale.battle.respawnMessagePanel.respawnActivatedSquad.title())), 
       b'messageLinkage': (BATTLE_ROYAL_CONSTS.MESSAGE_TIMER_LINKAGE)}


def formatAllyInBattleMessage(time, delay=0):
    return {b'time': time, 
       b'delay': delay, 
       b'quickHide': False, 
       b'title': (backport.text(R.strings.battle_royale.battle.respawnMessagePanel.squad.inBattle.title())), 
       b'description': (backport.text(R.strings.battle_royale.battle.respawnMessagePanel.squad.inBattle.description())), 
       b'messageLinkage': (BATTLE_ROYAL_CONSTS.MESSAGE_RESPAWN_AVAILABLE_LINKAGE)}


def formatPickUpSphereMessage(time, delay=0):
    return {b'time': time, 
       b'delay': delay, 
       b'quickHide': False, 
       b'title': (backport.text(R.strings.battle_royale.battle.respawnMessagePanel.squad.pickUp.title())), 
       b'description': (backport.text(R.strings.battle_royale.battle.respawnMessagePanel.squad.pickUp.description())), 
       b'messageLinkage': (BATTLE_ROYAL_CONSTS.MESSAGE_RESPAWN_NO_ICON_LINKAGE)}


def formatStayInCoverMessage(time, delay=0):
    return {b'time': time, 
       b'delay': delay, 
       b'quickHide': False, 
       b'title': (backport.text(R.strings.battle_royale.battle.respawnMessagePanel.squad.stayInCover.title())), 
       b'description': (backport.text(R.strings.battle_royale.battle.respawnMessagePanel.squad.stayInCover.description())), 
       b'messageLinkage': (BATTLE_ROYAL_CONSTS.MESSAGE_TIMER_LINKAGE)}


def formatAllyRespawnedMessage(time, delay=0):
    return {b'time': time, 
       b'delay': delay, 
       b'quickHide': False, 
       b'title': (backport.text(R.strings.battle_royale.battle.respawnMessagePanel.squad.squadmanRespawned.title())), 
       b'description': (backport.text(R.strings.battle_royale.battle.respawnMessagePanel.squad.squadmanRespawned.description())), 
       b'messageLinkage': (BATTLE_ROYAL_CONSTS.MESSAGE_RESPAWN_NO_ICON_LINKAGE)}


def formatAllyRespawnInProgressMessage(time, delay=0):
    return {b'time': time, 
       b'delay': delay, 
       b'quickHide': False, 
       b'title': (backport.text(R.strings.battle_royale.battle.respawnMessagePanel.squad.respawning.title())), 
       b'messageLinkage': (BATTLE_ROYAL_CONSTS.MESSAGE_TIMER_LINKAGE)}
