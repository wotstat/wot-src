from collections import namedtuple
from datetime import datetime
from helpers import time_utils
from account_helpers.AccountSettings import HINTS_LEFT, NUM_BATTLES, LAST_DISPLAY_DAY
from gui.shared.utils.plugins import IPlugin
_HINT_DISPLAY_COUNT_AFTER_RESET = 1
HINT_TIMEOUT = 6

class HintPriority(object):
    DYN_SQUAD = 1
    TRAJECTORY = 2
    HELP = 3
    MAPBOX = 4
    DEV_MAPS = 4
    BATTLE_COMMUNICATION = 5
    QUESTS = 6
    RESERVES = 7
    RADAR = 8
    SIEGE = 9


class HelpHintContext(object):
    MECHANICS = b'mechanics'
    ROLE_HELP = b'roleHelp'
    MAPS_TRAINING = b'mapsTraining'
    MAPBOX = b'mapbox'
    DEV_MAPS = b'devMaps'
    BATTLE_ROYALE = b'battleRoyale'
    COMMANDER_CAMERA = b'commanderCamera'


HintData = namedtuple(b'HintData', (b'vKey', b'key', b'messageLeft', b'messageRight', b'offsetX', b'offsetY', b'priority', b'reducedPanning', b'hintCtx', b'centeredMessage'))
HintData.__new__.__defaults__ = (
 b'', b'', b'', b'', 0, 0, HintPriority.HELP, False, None, False)

class HintPanelPlugin(IPlugin):
    __slots__ = ()

    @classmethod
    def isSuitable(cls):
        raise NotImplementedError
        return

    def setPeriod(self, period):
        return

    def updateMapping(self):
        return

    def _getHint(self):
        raise NotImplementedError
        return

    @staticmethod
    def _updateCounterOnUsed(settings):
        if settings:
            settings[LAST_DISPLAY_DAY] = datetime.now().timetuple().tm_yday
            settings[NUM_BATTLES] = 0
            settings[HINTS_LEFT] = max(0, settings[HINTS_LEFT] - 1)
        return settings

    @staticmethod
    def _updateBattleCounterOnUsed(settings):
        if settings:
            settings[HINTS_LEFT] = max(0, settings[HINTS_LEFT] - 1)
        return settings

    @staticmethod
    def _updateCounterOnStart(setting, dayCoolDown, battleCoolDown):
        if not setting:
            return
        hintsLeft = setting[HINTS_LEFT]
        numBattles = setting[NUM_BATTLES]
        lastDayOfYear = setting[LAST_DISPLAY_DAY]
        dayOfYear = datetime.now().timetuple().tm_yday
        daysLeft = (dayOfYear - lastDayOfYear + time_utils.DAYS_IN_YEAR) % time_utils.DAYS_IN_YEAR
        if hintsLeft == 0 and (daysLeft >= dayCoolDown or numBattles >= battleCoolDown):
            setting[HINTS_LEFT] = _HINT_DISPLAY_COUNT_AFTER_RESET
        return

    @classmethod
    def _updateCounterOnBattle(cls, setting):
        if setting and not cls._haveHintsLeft(setting):
            setting[NUM_BATTLES] = setting[NUM_BATTLES] + 1
        return

    @staticmethod
    def _haveHintsLeft(setting):
        if not setting:
            return False
        return setting[HINTS_LEFT] > 0
