import logging
from enum import Enum
import typing
from typing import TYPE_CHECKING
import SoundGroups, WWISE
from gui.impl import backport
from gui.impl.gen import R
if TYPE_CHECKING:
    from typing import Tuple
_logger = logging.getLogger(__name__)

class _LootBoxesSounds(str, Enum):
    STATE_GROUP = b'STATE_hangar_place'
    STATE_LOOTBOXES = b'STATE_hangar_place_lootboxes'
    STATE_GARAGE = b'STATE_hangar_place_garage'
    STATE_OVERLAY_GROUP = b'STATE_overlay_hangar_general'
    STATE_REWARDS_ENTER = b'STATE_overlay_hangar_general_on'
    STATE_REWARDS_EXIT = b'STATE_overlay_hangar_general_off'
    AMBIENT_ON = b'gui_lb_amb_on'
    AMBIENT_OFF = b'gui_lb_amb_off'
    VIDEO_PAUSE = b'gui_lb_video_pause'
    VIDEO_RESUME = b'gui_lb_video_resume'
    INFOPAGE_ENTER = b'gui_lb_infopage_enter'
    INFOPAGE_EXIT = b'gui_lb_infopage_exit'


def enterLootBoxesSoundState(eventName):
    WWISE.WW_setState(_LootBoxesSounds.STATE_GROUP, _LootBoxesSounds.STATE_LOOTBOXES)
    _playAmbientOn(eventName)
    return


def exitLootBoxesSoundState(eventName):
    _playAmbientOff(eventName)
    WWISE.WW_setState(_LootBoxesSounds.STATE_GROUP, _LootBoxesSounds.STATE_GARAGE)
    return


def enterLootBoxesMultipleRewardState():
    WWISE.WW_setState(_LootBoxesSounds.STATE_OVERLAY_GROUP, _LootBoxesSounds.STATE_REWARDS_ENTER)
    return


def exitLootBoxesMultipleRewardState():
    WWISE.WW_setState(_LootBoxesSounds.STATE_OVERLAY_GROUP, _LootBoxesSounds.STATE_REWARDS_EXIT)
    return


def playInfopageEnterSound(eventName):
    _playSounds((_LootBoxesSounds.INFOPAGE_ENTER,), eventName)
    return


def playInfopageExitSound(eventName):
    _playSounds((_LootBoxesSounds.INFOPAGE_EXIT,), eventName)
    return


def playVideoPauseSound(eventName):
    _playSounds((_LootBoxesSounds.VIDEO_PAUSE,), eventName)
    return


def playVideoResumeSound(eventName):
    _playSounds((_LootBoxesSounds.VIDEO_RESUME,), eventName)
    return


def _playAmbientOn(eventName):
    _playSounds((_LootBoxesSounds.AMBIENT_ON,), eventName)
    return


def _playAmbientOff(eventName):
    _playSounds((_LootBoxesSounds.AMBIENT_OFF,), eventName)
    return


def _playSounds(soundNames, eventName):
    for soundName in soundNames:
        SoundGroups.g_instance.playSafeSound2D(_getSound(soundName, eventName))

    return


def _getSound(soundName, eventName):
    eventSoundName = (b'_').join((soundName, eventName))
    soundRes = R.sounds.dyn(eventSoundName)
    if not soundRes.exists():
        _logger.debug(b'Event sound: "%s" not found, try to use default: "%s"', eventSoundName, soundName.value)
        soundRes = R.sounds.dyn(soundName)
        if not soundRes.exists():
            _logger.error(b'Event sound: "%s" not found', soundName.value)
            return None
    return backport.sound(soundRes())
