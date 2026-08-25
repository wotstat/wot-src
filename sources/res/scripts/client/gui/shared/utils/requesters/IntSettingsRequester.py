from __future__ import absolute_import
import logging
from copy import copy
from future.utils import viewitems
from functools import wraps
from account_helpers.AccountSettings import MAPBOX_CAROUSEL_FILTER_1, MAPBOX_CAROUSEL_FILTER_2, FUN_RANDOM_CAROUSEL_FILTER_1, FUN_RANDOM_CAROUSEL_FILTER_2, COMP7_CAROUSEL_FILTER_1, COMP7_CAROUSEL_FILTER_2, CAROUSEL_FILTER_3, RANKED_CAROUSEL_FILTER_3, EPICBATTLE_CAROUSEL_FILTER_3, MAPBOX_CAROUSEL_FILTER_3, COMP7_CAROUSEL_FILTER_3, FUN_RANDOM_CAROUSEL_FILTER_3, COMP7_LIGHT_CAROUSEL_FILTER_1, COMP7_LIGHT_CAROUSEL_FILTER_2, COMP7_LIGHT_CAROUSEL_FILTER_3
import BigWorld, constants
from account_helpers.settings_core.ServerSettingsManager import SETTINGS_SECTIONS
from adisp import adisp_async, adisp_process
from debug_utils import LOG_WARNING
from gui.shared.utils import code2str
_logger = logging.getLogger(__name__)

def requireSync(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        instance = args[0]
        if not instance.isSynced():
            LOG_WARNING(b'Calling %s require for IntSettingsRequester to be synced.' % func.__name__, stack=bool(constants.IS_DEVELOPMENT))
        return func(*args, **kwargs)

    return wrapper


class IntSettingsRequester(object):
    __SETTINGS = {b'VERSION': 0, 
       b'GAME': 1, 
       b'GRAPHICS': 2, 
       b'SOUND': 3, 
       b'CONTROLS': 4, 
       b'AIM_ARCADE_1': 43, 
       b'AIM_ARCADE_2': 44, 
       b'AIM_ARCADE_3': 45, 
       b'AIM_SNIPER_1': 46, 
       b'AIM_SNIPER_2': 47, 
       b'AIM_SNIPER_3': 48, 
       b'MARKERS_ENEMY': 49, 
       b'MARKERS_DEAD': 50, 
       b'MARKERS_ALLY': 51, 
       b'GUI_START_BEHAVIOR': 52, 
       b'FEEDBACK': 53, 
       b'EULA_VERSION': (constants.USER_SERVER_SETTINGS.EULA_VERSION), 
       b'GAMEPLAY': 55, 
       b'FORT': 56, 
       b'USERS_STORAGE_REV': 57, 
       b'CONTACTS': 58, 
       b'GAME_EXTENDED': (constants.USER_SERVER_SETTINGS.GAME_EXTENDED), 
       b'FALLOUT': 60, 
       b'LIMITED_UI_1': 61, 
       b'LIMITED_UI_2': 62, 
       b'AIM_ARCADE_4': 63, 
       b'AIM_SNIPER_4': 64, 
       b'MARKS_ON_GUN': (constants.USER_SERVER_SETTINGS.HIDE_MARKS_ON_GUN), 
       b'BATTLE_COMM': (constants.USER_SERVER_SETTINGS.BATTLE_COMM), 
       b'DOG_TAGS': (constants.USER_SERVER_SETTINGS.DOG_TAGS), 
       b'ONCE_ONLY_HINTS': 70, 
       b'BATTLE_HUD': (constants.USER_SERVER_SETTINGS.BATTLE_HUD), 
       b'CAROUSEL_FILTER_1': 73, 
       b'CAROUSEL_FILTER_2': 74, 
       b'UNIT_FILTER': 77, 
       b'LIMITED_UI_PERMANENT_1': 78, 
       b'LIMITED_UI_PERMANENT_2': 79, 
       b'RANKED_CAROUSEL_FILTER_1': 80, 
       b'RANKED_CAROUSEL_FILTER_2': 81, 
       b'FEEDBACK_DAMAGE_INDICATOR': 82, 
       b'FEEDBACK_DAMAGE_LOG': 83, 
       b'FEEDBACK_BATTLE_EVENTS': 84, 
       b'FEEDBACK_BORDER_MAP': 85, 
       b'UI_STORAGE': 86, 
       b'EPICBATTLE_CAROUSEL_FILTER_1': 87, 
       b'EPICBATTLE_CAROUSEL_FILTER_2': 88, 
       b'BATTLE_MATTERS_QUESTS': (constants.USER_SERVER_SETTINGS.BATTLE_MATTERS_QUESTS), 
       b'QUESTS_PROGRESS': (constants.USER_SERVER_SETTINGS.QUESTS_PROGRESS), 
       b'SESSION_STATS': (constants.USER_SERVER_SETTINGS.SESSION_STATS), 
       b'BATTLEPASS_CAROUSEL_FILTER_1': 97, 
       b'BATTLE_PASS_STORAGE': 98, 
       b'ONCE_ONLY_HINTS_2': 99, 
       b'ROYALE_CAROUSEL_FILTER_1': 100, 
       b'ROYALE_CAROUSEL_FILTER_2': 101, 
       b'GAME_EXTENDED_2': (constants.USER_SERVER_SETTINGS.GAME_EXTENDED_2), 
       b'SPG_AIM': (constants.USER_SERVER_SETTINGS.SPG_AIM), 
       MAPBOX_CAROUSEL_FILTER_1: 103, 
       MAPBOX_CAROUSEL_FILTER_2: 104, 
       b'CONTOUR': (constants.USER_SERVER_SETTINGS.CONTOUR), 
       FUN_RANDOM_CAROUSEL_FILTER_1: 107, 
       FUN_RANDOM_CAROUSEL_FILTER_2: 108, 
       b'UI_STORAGE_2': (constants.USER_SERVER_SETTINGS.UI_STORAGE_2), 
       COMP7_CAROUSEL_FILTER_1: 110, 
       COMP7_CAROUSEL_FILTER_2: 111, 
       b'SENIORITY_AWARDS_STORAGE': (constants.USER_SERVER_SETTINGS.SENIORITY_AWARDS), 
       b'REFERRAL_PROGRAM': (constants.USER_SERVER_SETTINGS.REFERRAL_PROGRAM), 
       b'ADVANCED_ACHIEVEMENTS_STORAGE': (constants.USER_SERVER_SETTINGS.ADVANCED_ACHIEVEMENTS_STORAGE), 
       b'ONCE_ONLY_HINTS_3': 116, 
       RANKED_CAROUSEL_FILTER_3: 118, 
       EPICBATTLE_CAROUSEL_FILTER_3: 119, 
       MAPBOX_CAROUSEL_FILTER_3: 120, 
       COMP7_CAROUSEL_FILTER_3: 121, 
       FUN_RANDOM_CAROUSEL_FILTER_3: 122, 
       CAROUSEL_FILTER_3: 123, 
       b'PERSONAL_MISSION_3': (constants.USER_SERVER_SETTINGS.PERSONAL_MISSION_3), 
       COMP7_LIGHT_CAROUSEL_FILTER_1: 125, 
       COMP7_LIGHT_CAROUSEL_FILTER_2: 126, 
       COMP7_LIGHT_CAROUSEL_FILTER_3: 127, 
       (SETTINGS_SECTIONS.SITUATIONAL_PERKS): 128}

    def __init__(self):
        self.__isSynced = False
        self.__cache = {}
        return

    def isSynced(self):
        return self.__isSynced

    def clear(self):
        self.__isSynced = False
        self.__cache = {}
        return

    @adisp_async
    @adisp_process
    def request(self, callback=None):
        self.__cache = yield self._requestCache()
        callback(self)
        return

    def getCacheValue(self, key, defaultValue=None):
        return self.__cache.get(key, defaultValue)

    @requireSync
    @adisp_process
    def setSetting(self, key, value):
        yield self._addIntSettings({(self.__SETTINGS[key]): (int(value))})
        return

    @requireSync
    @adisp_process
    def setSettings(self, settings):
        intSettings = {self.__SETTINGS[k]: int(v) for k, v in viewitems(settings)}
        yield self._addIntSettings(intSettings)
        return

    @requireSync
    def getSetting(self, key, defaultValue=None):
        return self.getCacheValue(self.__SETTINGS[key], defaultValue)

    @requireSync
    @adisp_process
    def delSettings(self, settings):
        yield self._delIntSettings(settings)
        return

    def _response(self, resID, value, callback):
        if resID < 0:
            _logger.error(b'[class %s] There is error while getting data from cache: %s[%d]', self.__class__.__name__, code2str(resID), resID)
            return callback({})
        self.__isSynced = True
        callback(copy(value))
        return

    @adisp_async
    def _requestCache(self, callback=None):
        player = BigWorld.player()
        if player is not None and player.intUserSettings is not None:
            self.__isSynced = False
            player.intUserSettings.getCache((lambda resID, value: self._response(resID, value, callback)))
        else:
            _logger.warning(b'Player or intUserSettings is not defined: %r, %r', player, player.intUserSettings if player is not None else None)
        return

    @adisp_async
    def _addIntSettings(self, settings, callback=None):
        import BattleReplay
        if not BattleReplay.g_replayCtrl.isPlaying:
            player = BigWorld.player()
            if player is not None:
                self.__cache.update(settings)
                player.intUserSettings.addIntSettings(settings, callback)
            else:
                _logger.warning(b'Player is not defined, int setting can not be added: %r', settings)
        return

    @adisp_async
    def _delIntSettings(self, settings, callback=None):
        import BattleReplay
        if not BattleReplay.g_replayCtrl.isPlaying:
            player = BigWorld.player()
            if player is not None:
                player.intUserSettings.delIntSettings(settings, callback)
            else:
                _logger.warning(b'Player is not defined, int setting can not be removed: %r', settings)
        return
