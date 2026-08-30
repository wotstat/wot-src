import types, os, enum, BigWorld, ResMgr, i18n, constants
from aih_constants import CTRL_MODE_NAME, CTRL_MODES
from debug_utils import LOG_CURRENT_EXCEPTION
from soft_exception import SoftException
from external_strings_utils import unicode_from_utf8
VERSION_FILE_PATH = b'../version.xml'
_CLIENT_VERSION = None
LOC_VERSION_FILE_PATH = b'../loc_version.xml'

def gEffectsDisabled():
    return False


def isPlayerAccount():
    return hasattr(BigWorld.player(), b'databaseID')


def isPlayerAvatar():
    return hasattr(BigWorld.player(), b'arena')


def isPlayerExist():
    return hasattr(BigWorld, b'player')


def getLanguageCode():
    if i18n.doesTextExist(b'#settings:LANGUAGE_CODE'):
        return i18n.makeString(b'#settings:LANGUAGE_CODE')
    else:
        return


def getClientLanguage():
    lng = constants.DEFAULT_LANGUAGE
    try:
        lng = getLanguageCode()
        if lng is None:
            lng = constants.DEFAULT_LANGUAGE
    except Exception:
        LOG_CURRENT_EXCEPTION()

    return lng


def getClientOverride():
    if constants.IS_CHINA:
        return b'CN'
    else:
        if getClientLanguage() == b'ko':
            return b'KR'
        return


def getLocalizedData(dataDict, key, defVal=b''):
    resVal = defVal
    if dataDict:
        lng = getClientLanguage()
        localesDict = dataDict.get(key, {})
        if localesDict:
            if lng in localesDict:
                resVal = localesDict[lng]
            elif constants.DEFAULT_LANGUAGE in localesDict:
                resVal = localesDict[constants.DEFAULT_LANGUAGE]
            else:
                resVal = localesDict.items()[0][1]
    return resVal


def int2roman(number):
    numerals = {1: b'I', 4: b'IV', 5: b'V', 9: b'IX', 10: b'X', 40: b'XL', 50: b'L', 
       90: b'XC', 100: b'C', 400: b'CD', 500: b'D', 900: b'CM', 
       1000: b'M'}
    result = b''
    for value, numeral in sorted(numerals.items(), reverse=True):
        while number >= value:
            result += numeral
            number -= value

    return result


def getClientVersion(force=True):
    global _CLIENT_VERSION
    if _CLIENT_VERSION is None or force:
        sec = ResMgr.openSection(VERSION_FILE_PATH)
        if sec is None:
            _CLIENT_VERSION = b''
        else:
            _CLIENT_VERSION = sec.readString(b'version')
    return _CLIENT_VERSION


def getShortClientVersion():
    sec = ResMgr.openSection(VERSION_FILE_PATH)
    if sec is None:
        return b''
    else:
        return sec.readString(b'version').split(b'#')[0]


def getFullClientVersion():
    sec = ResMgr.openSection(VERSION_FILE_PATH)
    if sec is None:
        return b''
    else:
        version = i18n.makeString(sec.readString(b'appname')) + b' ' + sec.readString(b'version')
        return version


def newFakeModel():
    return BigWorld.Model(b'')


_g_alphabetOrderExcept = {1105: 1077.5, 
   1025: 1045.5, 
   197: 196, 
   196: 197, 
   229: 228, 
   228: 229, 
   1030: 1048, 
   1110: 1080, 
   1028: 1045.5, 
   1108: 1077.5}

def _getSymOrderIdx(symbol):
    if not isinstance(symbol, types.UnicodeType):
        raise SoftException(b'')
    symIdx = ord(symbol)
    return _g_alphabetOrderExcept.get(symIdx, symIdx)


def strcmp(word1, word2):
    if not isinstance(word1, types.UnicodeType):
        raise SoftException(b'First argument should be unicode')
    if not isinstance(word2, types.UnicodeType):
        raise SoftException(b'Second argument should be unicode')
    for sym1, sym2 in zip(word1, word2):
        if sym1 != sym2:
            return int(round(_getSymOrderIdx(sym1) - _getSymOrderIdx(sym2)))

    return len(word1) - len(word2)


def setHangarVisibility(isVisible):
    BigWorld.worldDrawEnabled(isVisible)
    return


def getHelperServicesConfig(manager):
    from helpers.statistics import StatisticsCollector
    from helpers.platform import getPublishPlatform
    from skeletons.helpers.statistics import IStatisticsCollector
    from skeletons.helpers.platform import IPublishPlatform
    collector = StatisticsCollector()
    collector.init()
    manager.addInstance(IStatisticsCollector, collector, finalizer=b'fini')
    platform = getPublishPlatform()
    platform.init()
    manager.addInstance(IPublishPlatform, platform, finalizer=b'fini')
    return


def isShowingKillCam():
    from gui.shared.events import DeathCamEvent
    inputHandler = BigWorld.player().inputHandler
    return (inputHandler and inputHandler.ctrlModeName == CTRL_MODE_NAME.KILL_CAM and inputHandler.ctrl.killCamState in DeathCamEvent.SIMULATION_INCL_FADES) or False


def getVisibilityControllerMask(controlModes):
    visibilityMask = 0
    for index, mode in enumerate(CTRL_MODES):
        if controlModes.get(mode, True):
            visibilityMask += 1 << index

    return visibilityMask


class ReferralButtonHandler(object):

    @classmethod
    def invoke(cls, **kwargs):
        from gui.shared.event_dispatcher import showReferralProgramWindow
        from gui.Scaleform.daapi.view.lobby.referral_program.referral_program_helpers import getReferralProgramURL
        value = kwargs.get(b'value')
        url = value.get(b'action_url', None) if isinstance(value, dict) else None
        url = getReferralProgramURL() + url
        showReferralProgramWindow(url)
        return


class ClanQuestButtonHandler(object):

    @classmethod
    def invoke(cls, **kwargs):
        from gui.impl.lobby.clan_supply.clan_supply_helpers import showClanSupplyView
        showClanSupplyView(tabId=1)
        return


class ClanSupplyQuestButtonHandler(object):

    @classmethod
    def invoke(cls, **kwargs):
        from gui.impl.lobby.clan_supply.clan_supply_helpers import showClanSupplyView
        from uilogging.clan_supply.constants import ClanSupplyLogKeys
        showClanSupplyView(tabId=1, parentScreenLog=ClanSupplyLogKeys.NOTIFICATION)
        return


def unicodeToStr(data):
    if isinstance(data, unicode):
        return data.encode(b'utf-8')
    if isinstance(data, list):
        return [unicodeToStr(el) for el in data]
    if isinstance(data, dict):
        res = {}
        for k, v in data.iteritems():
            res[unicodeToStr(k)] = unicodeToStr(v)

        return res
    return data


def getPreferencesDirPath():
    _, prefsPath = unicode_from_utf8(BigWorld.wg_getPreferencesFilePath())
    return os.path.dirname(prefsPath)


class ExitCode(enum.IntEnum):
    SUCCESS = 0
    FAILED = 1
