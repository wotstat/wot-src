from copy import deepcopy
import ResMgr
from BootcampConstants import HINT_TYPE, HINT_NAMES
from helpers.i18n import makeString
from debug_utils_bootcamp import LOG_CURRENT_EXCEPTION_BOOTCAMP, LOG_ERROR_BOOTCAMP
from soft_exception import SoftException

class _HintParamType(object):
    FLOAT = 0
    STRING = 1
    INT = 2


class _LessonConfiguration(object):

    def __init__(self):
        self.hints = {}
        self.prebattle = {}
        self.ribbons = []
        self.visiblePanels = []
        self.hiddenPanels = []
        self.lessonPages = []
        return


class BattleSettings(object):
    SETTINGS_XML_PATH = b'scripts/bootcamp_docs/battle_settings.xml'
    DEFAULTS_XML_PATH = b'scripts/bootcamp_docs/battle_defaults.xml'
    HINTS_PARAMS = {(HINT_TYPE.HINT_NO_MOVE): {b'seconds': (_HintParamType.FLOAT)}, (HINT_TYPE.HINT_NO_MOVE_TURRET): {b'seconds': (_HintParamType.FLOAT)}, (HINT_TYPE.HINT_AIM): {b'aimFactor': (_HintParamType.FLOAT), b'shootCount': (_HintParamType.INT)}, (HINT_TYPE.HINT_SECONDARY_SNIPER): {b'distance': (_HintParamType.FLOAT), b'angle': (_HintParamType.FLOAT)}, (HINT_TYPE.HINT_WAIT_RELOAD): {b'maxShootErrorsCount': (_HintParamType.INT)}, (HINT_TYPE.HINT_EXIT_GAME_AREA): {b'distanceToBorder': (_HintParamType.FLOAT)}, (HINT_TYPE.HINT_MOVE_TO_MARKER): {b'maxDistance': (_HintParamType.FLOAT)}, (HINT_TYPE.HINT_LOW_HP): {b'first_percent': (_HintParamType.FLOAT), b'second_percent': (_HintParamType.FLOAT)}, (HINT_TYPE.HINT_SHOT_WHILE_MOVING): {b'maxShootErrorsCount': (_HintParamType.INT)}}

    def __init__(self):
        super(BattleSettings, self).__init__()
        self.__defaults = {b'hints': {}, b'ribbons': [], b'panels': [], b'lessonPages': {}, b'prebattleHints': (set())}
        self.__config = {}
        try:
            self.__loadDefaults()
            self.__loadConfig()
        except Exception:
            LOG_CURRENT_EXCEPTION_BOOTCAMP()

        return

    def lessonConfiguration(self, lessonId):
        return self.__config.get(lessonId, _LessonConfiguration())

    @property
    def defaults(self):
        return self.__defaults

    def __readPrebattleSection(self, prebattleSection):
        prebattleSettings = {}
        if prebattleSection.has_key(b'timeout'):
            prebattleSettings[b'timeout'] = prebattleSection[b'timeout'].asFloat
        if prebattleSection.has_key(b'wwSound'):
            prebattleSettings[b'wwSound'] = prebattleSection[b'wwSound'].asString
        if prebattleSection.has_key(b'hints'):
            prebattleSettings[b'visible_hints'] = set(prebattleSection[b'hints'].asString.split())
            prebattleSettings[b'invisible_hints'] = self.__defaults[b'prebattle'] - prebattleSettings[b'visible_hints']
        return prebattleSettings

    def __readRibbonsSection(self, ribbonsSection):
        defaultRibbons = self.__defaults[b'ribbons']
        ribbonsSettings = []
        ribbonNames = ribbonsSection.asString.split()
        for ribName in ribbonNames:
            if ribName in defaultRibbons:
                ribbonsSettings.append(ribName)
            else:
                LOG_ERROR_BOOTCAMP(b'Unknown ribbon name (%s)' % ribName)

        return ribbonsSettings

    def __readLoadingLessonsSection(self, lessonsSection):
        return lessonsSection.asString.split()

    def __readPanelsSection(self, panelsSection):
        panels = []
        defaultPanels = self.__defaults[b'panels']
        panelNames = panelsSection.asString.split()
        for name in panelNames:
            if name in defaultPanels:
                panels.append(name)
            else:
                LOG_ERROR_BOOTCAMP(b'Unknown panel name (%s)' % name)

        return panels

    def __readHintSection(self, hintName, hintSection, isDefaultSection=False):
        singleHint = {}
        hintId = HINT_NAMES.index(hintName)
        hintParams = BattleSettings.HINTS_PARAMS.get(hintId, None)
        if hintParams is not None:
            for keyParam, valueType in hintParams.iteritems():
                if isDefaultSection or hintSection.has_key(keyParam):
                    if valueType == _HintParamType.FLOAT:
                        singleHint[keyParam] = hintSection[keyParam].asFloat
                    elif valueType == _HintParamType.STRING:
                        singleHint[keyParam] = makeString(hintSection[keyParam].asString)
                    elif valueType == _HintParamType.INT:
                        singleHint[keyParam] = hintSection[keyParam].asInt
                    else:
                        raise SoftException(b'Unknown hint param type (%d)', valueType)

        if hintSection.has_key(b'cooldown_after'):
            singleHint[b'cooldown_after'] = hintSection[b'cooldown_after'].asFloat
        if hintSection.has_key(b'time_completed'):
            singleHint[b'time_completed'] = hintSection[b'time_completed'].asFloat
        if hintSection.has_key(b'voiceover'):
            singleHint[b'voiceover'] = hintSection[b'voiceover'].asString
        if hintSection.has_key(b'timeout'):
            singleHint[b'timeout'] = hintSection[b'timeout'].asFloat
        if hintSection.has_key(b'message'):
            singleHint[b'message'] = makeString(hintSection[b'message'].asString)
        if not isDefaultSection and hintSection.has_key(b'names'):
            namesSection = hintSection[b'names']
            namesList = [value.asString for key, value in namesSection.items() if key == b'name']
            singleHint[b'names'] = namesList
        return singleHint

    def __loadDefaults(self):
        defaultSettingsConfig = ResMgr.openSection(BattleSettings.DEFAULTS_XML_PATH)
        if not defaultSettingsConfig:
            raise SoftException(b"Can't open defaults config file (%s)" % BattleSettings.DEFAULTS_XML_PATH)
        hints = self.__defaults[b'hints']
        for sectionName in (b'primary_hints', b'secondary_hints'):
            hintsSection = defaultSettingsConfig[sectionName]
            for hintName, hintDefaultSection in hintsSection.items():
                hints[hintName] = self.__readHintSection(hintName, hintDefaultSection, True)

        ribString = defaultSettingsConfig[b'ribbons'].asString
        self.__defaults[b'ribbons'] = ribString.split()
        panelsString = defaultSettingsConfig[b'panels'].asString
        self.__defaults[b'panels'] = panelsString.split()
        prebattleHintsString = defaultSettingsConfig[b'prebattle'].asString
        self.__defaults[b'prebattle'] = set(prebattleHintsString.split())
        self.__readDefaultPagesSection(defaultSettingsConfig[b'lesson_pages'])
        return

    def __loadConfig(self):
        settingsConfig = ResMgr.openSection(BattleSettings.SETTINGS_XML_PATH)
        if not settingsConfig:
            raise SoftException(b"Can't open defaults config file (%s)" % BattleSettings.SETTINGS_XML_PATH)
        for name, xmlSection in settingsConfig.items():
            if name == b'lesson':
                lessonId = xmlSection[b'id'].asInt
                lessonConf = _LessonConfiguration()
                self.__config[lessonId] = lessonConf
                defaultsHints = self.__defaults[b'hints']
                for sectionName in (b'primary_hints', b'secondary_hints'):
                    if xmlSection.has_key(sectionName):
                        hintsXmlSection = xmlSection[sectionName]
                        for hintName, hintSection in hintsXmlSection.items():
                            curHintInfo = deepcopy(defaultsHints[hintName])
                            curHintInfo.update(self.__readHintSection(hintName, hintSection, False))
                            lessonConf.hints[hintName] = curHintInfo

                if xmlSection.has_key(b'prebattle'):
                    lessonConf.prebattle = self.__readPrebattleSection(xmlSection[b'prebattle'])
                if xmlSection.has_key(b'ribbons'):
                    lessonConf.ribbons = self.__readRibbonsSection(xmlSection[b'ribbons'])
                if xmlSection.has_key(b'lesson_pages'):
                    lessonConf.lessonPages = self.__readLoadingLessonsSection(xmlSection[b'lesson_pages'])
                if xmlSection.has_key(b'panels'):
                    lessonConf.visiblePanels = self.__readPanelsSection(xmlSection[b'panels'])
                    lessonConf.hiddenPanels = list(set(self.__defaults[b'panels']) - set(lessonConf.visiblePanels))

        return

    def __readDefaultPagesSection(self, pagesXmlSection):
        lessonPagesDefaults = self.__defaults[b'lessonPages']
        for pageName, pageProps in pagesXmlSection.items():
            lessonProps = {}
            for itemName, itemProps in pageProps.items():
                lessonProps[itemName + b'Text'] = makeString(itemProps[b'text'].asString)
                lessonProps[itemName + b'AutoSize'] = itemProps[b'autoSize'].asString

            lessonPagesDefaults[pageName] = lessonProps

        return


_g_battleSettings = None

def _getBattleSettings():
    global _g_battleSettings
    if _g_battleSettings is None:
        _g_battleSettings = BattleSettings()
    return _g_battleSettings


def getBattleSettings(lessonId):
    return _getBattleSettings().lessonConfiguration(lessonId)


def getBattleDefaults():
    return _getBattleSettings().defaults
