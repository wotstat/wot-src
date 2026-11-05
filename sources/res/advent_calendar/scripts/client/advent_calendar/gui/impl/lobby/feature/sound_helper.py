from __future__ import absolute_import
from sound_gui_manager import CommonSoundSpaceSettings
from shared_utils import CONST_CONTAINER

class AdventCalendarSounds(CONST_CONTAINER):
    ADVENT_CALENDAR_NAME = b'advent_calendar_sound'
    OVERLAY_HANGAR_GENERAL = b'STATE_overlay_hangar_general'
    OVERLAY_HANGAR_GENERAL_ON = b'STATE_overlay_hangar_general_on'
    OVERLAY_HANGAR_GENERAL_OFF = b'STATE_overlay_hangar_general_off'
    ADVENT_CALENDAR_ENTER = b'adv_enter'
    ADVENT_CALENDAR_CLOSE = b'adv_exit'


ADVENT_CALENDAR_MAIN_WINDOW_SOUND = CommonSoundSpaceSettings(name=AdventCalendarSounds.ADVENT_CALENDAR_NAME, entranceStates={(AdventCalendarSounds.OVERLAY_HANGAR_GENERAL): (AdventCalendarSounds.OVERLAY_HANGAR_GENERAL_ON)}, exitStates={(AdventCalendarSounds.OVERLAY_HANGAR_GENERAL): (AdventCalendarSounds.OVERLAY_HANGAR_GENERAL_OFF)}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=AdventCalendarSounds.ADVENT_CALENDAR_ENTER, exitEvent=AdventCalendarSounds.ADVENT_CALENDAR_CLOSE)
