from __future__ import absolute_import
import Input, BigWorld
from functools import partial
from Input import TriggerEvent
from constants import HAS_DEV_RESOURCES
_profile0 = b'BATTLE_ROYALE_DEV_INPUT_PROFILE'

def _devPredicate():
    return HAS_DEV_RESOURCES


def _pausedDeathZones():
    BigWorld.player().base.setDevelopmentFeature(0, b'paused_death_zones', 0, b'')
    return


def _pausedAirdropLoot():
    BigWorld.player().base.setDevelopmentFeature(0, b'paused_airdrop_loot', 0, b'')
    return


def _spawnBot(botName):
    BigWorld.player().vehicle.cell.brCheats.spawnBot(botName)
    return


def initBRInput():
    _actions = [
     (
      b'ACTION_PLAYER_PAUSED_DEATH_ZONE', _pausedDeathZones),
     (
      b'ACTION_PLAYER_PAUSED_AIRDROP_LOOT', _pausedAirdropLoot),
     (
      b'ACTION_PLAYER_SPAWN_BOT_WOLF', partial(_spawnBot, b'wolf')),
     (
      b'ACTION_PLAYER_SPAWN_BOT_HARE', partial(_spawnBot, b'hare')),
     (
      b'ACTION_PLAYER_SPAWN_BOT_BEAR', partial(_spawnBot, b'bear'))]
    for actionName, handler in _actions:
        action = Input.inputSystem().findAction(_profile0, actionName)
        if action:
            action.setPredicate(_devPredicate)
            action.bindEventReaction(TriggerEvent.Triggered, handler)

    Input.inputSystem().activateProfile(_profile0)
    return


def finiBRInput():
    if Input.inputSystem().hasProfile(_profile0):
        Input.inputSystem().deactivateProfile(_profile0, unbindAllReactions=True)
    return
