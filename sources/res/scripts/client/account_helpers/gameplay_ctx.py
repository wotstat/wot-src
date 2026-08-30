import ArenaType, constants
from constants import RANDOM_FLAGS
from debug_utils import LOG_DEBUG, LOG_ERROR, LOG_WARNING
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore
_ASSAULT2_GP_NAME = constants.ARENA_GAMEPLAY_NAMES[6]
ENABLED_ARENA_GAMEPLAY_NAMES = constants.ARENA_GAMEPLAY_NAMES[:3] + (_ASSAULT2_GP_NAME,)
ENABLED_ARENA_EPIC_NAMES = (
 constants.ARENA_GAMEPLAY_NAMES[15],)

def getDefaultMask():
    return ArenaType.getGameplaysMask(ENABLED_ARENA_GAMEPLAY_NAMES)


def getMask():
    from account_helpers.settings_core.ServerSettingsManager import SETTINGS_SECTIONS
    settingsCore = dependency.instance(ISettingsCore)
    settingsMask = userMask = settingsCore.serverSettings.getSectionSettings(SETTINGS_SECTIONS.GAMEPLAY, b'gameplayMask', getDefaultMask())
    ctfMask = ArenaType.getGameplaysMask((b'ctf',))
    nationsMask = ArenaType.getGameplaysMask((b'nations',))
    if not userMask:
        LOG_WARNING(b'Gameplay is not defined', userMask)
    elif userMask & ctfMask == 0:
        LOG_WARNING(b'Gameplay "ctf" is not defined', userMask)
    if userMask & nationsMask:
        userMask ^= nationsMask
        LOG_DEBUG(b'Nations battle mode currently unavailable')
    userMask |= ctfMask
    if settingsMask != userMask:
        _setMask(userMask)
    return userMask


def setMaskByNames(names):
    gameplayNames = {
     b'ctf'}
    for name in names:
        if name in ArenaType.g_gameplayNames:
            gameplayNames.add(name)
        else:
            LOG_ERROR(b'Gameplay is not available', name)

    gameplayMask = ArenaType.getGameplaysMask(gameplayNames)
    LOG_DEBUG(b'Set gameplay (names, mask)', gameplayNames, gameplayMask)
    _setMask(gameplayMask)
    return


def isCreationEnabled(gameplayName, isEpic):
    if isEpic:
        return gameplayName in ENABLED_ARENA_EPIC_NAMES
    return gameplayName in ENABLED_ARENA_GAMEPLAY_NAMES


def _setMask(gameplayMask):
    from account_helpers.settings_core.ServerSettingsManager import SETTINGS_SECTIONS
    settingsCore = dependency.instance(ISettingsCore)
    settingsCore.serverSettings.setSectionSettings(SETTINGS_SECTIONS.GAMEPLAY, {b'gameplayMask': gameplayMask})
    return


def isMapsInDevelopmentEnabled():
    from account_helpers.settings_core.settings_constants import GAME
    settingsCore = dependency.instance(ISettingsCore)
    return settingsCore.getSetting(GAME.GAMEPLAY_DEV_MAPS)


def getRandomFlags():
    flags = 0
    if isMapsInDevelopmentEnabled():
        flags |= RANDOM_FLAGS.IS_MAPS_IN_DEVELOPMENT_ENABLED
    return flags


def getWinbackFlags():
    flags = 0
    if isMapsInDevelopmentEnabled():
        flags |= RANDOM_FLAGS.IS_MAPS_IN_DEVELOPMENT_ENABLED
    return flags
