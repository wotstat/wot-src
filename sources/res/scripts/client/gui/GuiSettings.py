import logging
from collections import namedtuple
import nations, constants, resource_helper
from helpers import getClientLanguage, time_utils
from gui import macroses
from soft_exception import SoftException
_logger = logging.getLogger(__name__)
GUI_SETTINGS_FILE_PATH = b'gui/gui_settings.xml'
VIDEO_SETTINGS_FILE_PATH = b'gui/video_settings.xml'
LoginRssFeedProps = namedtuple(b'LoginRssFeedProps', b'show url internalBrowser')
BrowserProps = namedtuple(b'BrowserProps', b'url params')
PostBattleExchangeProps = namedtuple(b'PostBattleExchangeProps', b'enabled url')
EasterEggProps = namedtuple(b'EasterEggProps', b'enabled ruLangGroup')
_MacrosValue = namedtuple(b'MacrosValue', b'macros dictValue')

class EULAProps(object):
    __slots__ = (b'__full', b'__url')

    def __init__(self, full=None, url=b''):
        super(EULAProps, self).__init__()
        self.__full = full or ()
        self.__url = url
        return

    @property
    def full(self):
        return getClientLanguage() in self.__full

    @property
    def url(self):
        return self.__url


def _readMacros(xmlCtx, section, valueName=b'value'):
    result = {}
    name = resource_helper.readItemName(xmlCtx, section)
    macros = _readItemMacros(xmlCtx, section)
    subCtx, subSection = resource_helper.getSubSection(xmlCtx, section, valueName)
    for nextCtx, nextSection in resource_helper.getIterator(subCtx, subSection):
        item = resource_helper.readItem(nextCtx, nextSection)
        if not item.name:
            raise resource_helper.ResourceError(nextCtx, (b'{0}: name is required in each item').format(name))
        result[item.name] = item.value

    return resource_helper.ResourceItem(b'macros', name, _MacrosValue(macros, result))


def _readItemMacros(xmlCtx, section, keys=None):
    return resource_helper.readItemAttr(xmlCtx, section, b'macros', default=b'', keys=keys)


def _convertVector4ToTuple(_, item_value):
    return item_value.tuple()


def _convertToNamedTuple(settings, item_value):
    return settings._replace(**item_value)


def _convertEULASetting(_, item_value):
    return EULAProps(**item_value)


def _dummyConverter(_, item_value):
    return item_value


_SETTING_CONVERTERS = {b'loginRssFeed': _convertToNamedTuple, 
   b'eula': _convertEULASetting, 
   b'markerScaleSettings': _convertVector4ToTuple, 
   b'browser': _convertToNamedTuple, 
   b'postBattleExchange': _convertToNamedTuple, 
   b'easterEgg': _convertToNamedTuple, 
   b'baseUrls': _dummyConverter, 
   b'battlePassBaseUrls': _dummyConverter}
_DEFAULT_SETTINGS = {b'registrationURL': b'', 
   b'registrationProxyURL': b'', 
   b'recoveryPswdURL': b'', 
   b'paymentURL': b'', 
   b'securitySettingsURL': b'', 
   b'supportURL': b'', 
   b'migrationURL': b'', 
   b'nations_order': (nations.AVAILABLE_NAMES[:]), 
   b'language_bar': [], b'guiEnabled': True, 
   b'disabledUIElements': [], b'trainingObserverModeEnabled': False, 
   b'minimapSize': True, 
   b'goldTransfer': False, 
   b'voiceChat': True, 
   b'technicalInfo': True, 
   b'nationHangarSpace': False, 
   b'customizationHorns': False, 
   b'showMinimapSuperHeavy': False, 
   b'showMinimapDeath': True, 
   b'permanentMinimapDeath': False, 
   b'markerHitSplashDuration': 0, 
   b'sixthSenseDuration': 0, 
   b'minimapDeathDuration': 0, 
   b'rememberPassVisible': True, 
   b'clearLoginValue': False, 
   b'markerScaleSettings': (0, 0, 0, 0), 
   b'specPrebatlesVisible': True, 
   b'roaming': True, 
   b'loginRssFeed': (LoginRssFeedProps(True, b'', False)), 
   b'eula': (EULAProps()), 
   b'igrCredentialsReset': False, 
   b'igrEnabled': False, 
   b'battleEndWarningEnabled': True, 
   b'isPollEnabled': False, 
   b'csisRequestRate': 0, 
   b'showSectorLines': False, 
   b'showDirectionLine': False, 
   b'isBattleCmdCoolDownVisible': True, 
   b'browser': (BrowserProps(b'about:blank', b'')), 
   b'reportBugLinks': [], b'cache': [], b'imageCache': [], b'postBattleExchange': (PostBattleExchangeProps(False, b'')), 
   b'actionComeToEnd': (time_utils.QUARTER_HOUR), 
   b'goldFishActionShowCooldown': 86400, 
   b'guiScale': [], b'playerFeedbackDelay': 0.75, 
   b'allowedNotSupportedGraphicSettings': {}, b'userRoomsService': b'', 
   b'cryptLoginInfo': True, 
   b'compulsoryIntroVideos': [], b'useDefaultGunMarkers': False, 
   b'spgAlternativeAimingCameraEnabled': False, 
   b'tokenShopAvailabilityURL': b'', 
   b'frontlineChangedURL': b'', 
   b'tokenShopAPIKey': b'', 
   b'personalMissions': {}, b'progressiveItems': {}, b'rankedBattles': {}, b'referralProgram': {}, b'easterEgg': (EasterEggProps(True, [])), 
   b'premiumInfo': {}, b'crew': {b'welcomeScreens': {}}, b'checkPromoFrequencyInBattles': 5, 
   b'vivoxLicense': b'', 
   b'spgHitDirectionDelta': 10.0, 
   b'vehicleDisclaimerURLs': {}, b'baseUrls': {}, b'battlePassBaseUrls': {}}

class GuiSettings(object):

    def __init__(self):
        self.__settings = _DEFAULT_SETTINGS.copy()
        settings = {}
        for item in resource_helper.root_iterator(GUI_SETTINGS_FILE_PATH, customReaders={b'macros': _readMacros}):
            if item.name in _SETTING_CONVERTERS:
                setting = _DEFAULT_SETTINGS[item.name]
                converter = _SETTING_CONVERTERS[item.name]
                value = converter(setting, self.__applyMacros(item.value))
            else:
                value = item.value
            settings[item.name] = value

        if constants.IS_DEVELOPMENT:
            diff = set(self.__settings.keys()) - set(settings.keys())
            if diff:
                _logger.info(b'Settings are not in %s: %r', GUI_SETTINGS_FILE_PATH, diff)
        self.__settings.update(settings)
        return

    def __getattr__(self, name):
        if name in self.__settings:
            return self.__applyMacros(self.__settings[name])
        raise AttributeError((b'Setting not found in {0}: {1}').format(self.__class__, name))
        return

    def __setattr__(self, name, value):
        if name == b'_GuiSettings__settings':
            self.__dict__[name] = value
        elif name in self.__settings:
            raise AttributeError((b'Assignment is forbidden for {0}. Argument name: {1}').format(self.__class__, name))
        return

    def __contains__(self, item):
        return item in self.__settings

    @property
    def isShowLanguageBar(self):
        try:
            return getClientLanguage() in self.language_bar
        except Exception as ex:
            _logger.exception(ex)
            return False

        return

    def isEmpty(self, name):
        value = None
        if name in self.__settings:
            value = self.__applyMacros(self.__settings[name])
        return not value

    def isGuiEnabled(self):
        return self.guiEnabled or not constants.IS_DEVELOPMENT

    def lookup(self, name):
        settings = None
        if name in self.__settings:
            settings = self.__applyMacros(self.__settings[name])
        return settings

    def checkAndReplaceWebShopMacros(self, url):
        return self.__checkAndReplaceMacros(b'webShopRootURL', url)

    def checkAndReplaceWebBridgeMacros(self, url):
        return self.__checkAndReplaceMacros(b'webBridgeRootURL', url)

    def __checkAndReplaceMacros(self, rootUrlName, url):
        rootUrl = self.baseUrls.get(rootUrlName)
        macros = (b'{_}').replace(b'_', rootUrlName)
        if rootUrl is not None:
            return url.replace(macros, rootUrl)
        else:
            return url

    def __applyMacros(self, value):
        if isinstance(value, _MacrosValue):
            macros = value.macros
            dictValue = value.dictValue
            simpleMacroses = macroses.getSyncMacroses()
            if macros in simpleMacroses:
                macrosKey = simpleMacroses[macros]()
            elif macros == b'MACROS_DICT':
                value = {}
                for key, mValue in dictValue.iteritems():
                    value[key] = self.__applyMacros(mValue)

                return value
            raise SoftException((b"Unsupported macros '{0}', not found in {1}").format(macros, simpleMacroses))
            if macrosKey in dictValue:
                return self.__applyMacros(dictValue[macrosKey])
            if b'default' in dictValue:
                return self.__applyMacros(dictValue[b'default'])
            raise SoftException((b"Incorrect section in {0}, dict {1} with macros '{2}' should contains item '{3}' or 'default'").format(GUI_SETTINGS_FILE_PATH, dictValue, macros, macrosKey))
        return value
