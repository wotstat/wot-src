from __future__ import absolute_import
from collections import namedtuple
from future.utils import viewitems
from fun_random_common.fun_constants import DEFAULT_ASSETS_PACK, DEFAULT_SETTINGS_KEY, DEFAULT_PRIORITY, UNKNOWN_WWISE_REMAPPING, UNKNOWN_EVENT_ID, FunSubModeImpl
from shared_utils import makeTupleByDict

class FunSubModeClientConfig(namedtuple(b'_FunSubModeClientConfig', (b'subModeImpl', b'assetsPointer', b'settingsKey', b'priority', b'wwiseRemapping', b'battleModifiersDescr', b'postbattle', b'infoPageUrl', b'performanceAnalyzerType'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(subModeImpl=FunSubModeImpl.DEFAULT, assetsPointer=DEFAULT_ASSETS_PACK, settingsKey=DEFAULT_SETTINGS_KEY, priority=DEFAULT_PRIORITY, wwiseRemapping=UNKNOWN_WWISE_REMAPPING, battleModifiersDescr=(), postbattle={}, infoPageUrl=b'', performanceAnalyzerType=b'')
        defaults.update(kwargs)
        return super(FunSubModeClientConfig, cls).__new__(cls, **defaults)

    @classmethod
    def defaults(cls):
        return cls()


class FunSubModeFiltrationConfig(namedtuple(b'FunSubModeFiltrationConfig', (b'levels', b'forbiddenClassTags', b'forbiddenVehTypes', b'allowedVehTypes', b'squadRestrictions'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(levels=(), forbiddenClassTags=set(), forbiddenVehTypes=set(), allowedVehTypes=set(), squadRestrictions={})
        defaults.update(kwargs)
        return super(FunSubModeFiltrationConfig, cls).__new__(cls, **defaults)

    @classmethod
    def defaults(cls):
        return cls()


class FunSubModeSeasonalityConfig(namedtuple(b'FunSubModeSeasonalityConfig', (b'isEnabled', b'peripheryIDs', b'seasons', b'primeTimes', b'cycleTimes'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(isEnabled=False, peripheryIDs=set(), seasons={}, primeTimes={}, cycleTimes=())
        defaults.update(kwargs)
        cls.__packSeasonalityConfig(defaults)
        return super(FunSubModeSeasonalityConfig, cls).__new__(cls, **defaults)

    @classmethod
    def defaults(cls):
        return cls()

    def asDict(self):
        return self._asdict()

    @classmethod
    def __packSeasonalityConfig(cls, data):
        data[b'primeTimes'] = {int(peripheryID): value for peripheryID, value in viewitems(data[b'primeTimes'])}
        data[b'seasons'] = {int(seasonID): value for seasonID, value in viewitems(data[b'seasons'])}
        return


class FunSubModeConfig(namedtuple(b'_FunSubModeConfig', (b'eventID', b'isEnabled', b'seasonality', b'filtration', b'client'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(eventID=UNKNOWN_EVENT_ID, isEnabled=False, seasonality={}, filtration={}, client={})
        allowedFields = set(defaults)
        defaults.update(kwargs)
        cls.__packConfigPart(FunSubModeClientConfig, b'client', defaults)
        cls.__packConfigPart(FunSubModeFiltrationConfig, b'filtration', defaults)
        cls.__packConfigPart(FunSubModeSeasonalityConfig, b'seasonality', defaults)
        defaults = cls.__filterAllowedFields(defaults, allowedFields)
        return super(FunSubModeConfig, cls).__new__(cls, **defaults)

    @classmethod
    def defaults(cls):
        return cls()

    @classmethod
    def __filterAllowedFields(cls, data, allowedFields):
        return {k: v for k, v in viewitems(data) if k in allowedFields}

    @classmethod
    def __packConfigPart(cls, configPartCls, configPartName, data):
        data[configPartName] = makeTupleByDict(configPartCls, data)
        return


class FunProgressionConfig(namedtuple(b'_FunProgressionConfig', (b'name', b'executors', b'triggers', b'unlimitedTrigger', b'unlimitedExecutor', b'visibleLBAwardsNames'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(name=b'', executors=(), triggers=(), unlimitedTrigger=None, unlimitedExecutor=None, visibleLBAwardsNames=())
        defaults.update(kwargs)
        return super(FunProgressionConfig, cls).__new__(cls, **defaults)

    @classmethod
    def defaults(cls):
        return cls()


class FunMetaProgressionConfig(namedtuple(b'_FunMetaProgressionConfig', (b'isEnabled', b'progressions'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(isEnabled=False, progressions=())
        defaults.update(kwargs)
        cls.__packProgressionsConfigs(defaults)
        return super(FunMetaProgressionConfig, cls).__new__(cls, **defaults)

    @classmethod
    def defaults(cls):
        return cls()

    @classmethod
    def __packProgressionsConfigs(cls, data):
        data[b'progressions'] = tuple(makeTupleByDict(FunProgressionConfig, p) for p in data[b'progressions'])
        return


class FunRandomConfig(namedtuple(b'_FunRandomConfig', (b'isEnabled', b'subModes', b'metaProgression', b'assetsPointer', b'settingsKey', b'infoPageUrl'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(isEnabled=False, subModes={}, metaProgression={}, assetsPointer=DEFAULT_ASSETS_PACK, settingsKey=DEFAULT_SETTINGS_KEY, infoPageUrl=b'')
        allowedFields = set(defaults)
        defaults.update(kwargs)
        cls.__packSubModesConfigs(defaults)
        cls.__packMetaProgressionConfig(defaults)
        defaults = cls.__filterAllowedFields(defaults, allowedFields)
        return super(FunRandomConfig, cls).__new__(cls, **defaults)

    @classmethod
    def defaults(cls):
        return cls()

    def replace(self, data):
        data = self.__packSubModesConfigs(data)
        data = self.__packMetaProgressionConfig(data)
        dataToUpdate = self.__filterAllowedFields(data, self._fields)
        return self._replace(**dataToUpdate)

    @classmethod
    def __filterAllowedFields(cls, data, allowedFields):
        return {k: v for k, v in viewitems(data) if k in allowedFields}

    @classmethod
    def __packMetaProgressionConfig(cls, data):
        progression = data[b'metaProgression'] if data[b'isEnabled'] else {}
        data[b'metaProgression'] = makeTupleByDict(FunMetaProgressionConfig, progression)
        return data

    @classmethod
    def __packSubModesConfigs(cls, data):
        events = data[b'events'] if data[b'isEnabled'] else {}
        data[b'subModes'] = {int(eID): FunSubModeConfig(**eData) for eID, eData in viewitems(events) if eData.get(b'isEnabled', False) and eData.get(b'eventID', UNKNOWN_EVENT_ID)}
        return data
