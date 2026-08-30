from collections import namedtuple
from fun_random_common.fun_constants import DEFAULT_ASSETS_PACK, DEFAULT_SETTINGS_KEY, DEFAULT_PRIORITY, UNKNOWN_WWISE_REMAPPING, UNKNOWN_EVENT_ID, FunSubModeImpl
from fun_random.gui.fun_gui_constants import FUN_RANDOM_ARCADE_FEP_TYPE
from shared_utils import makeTupleByDict

class FunSubModeClientConfig(namedtuple(b'_FunSubModeClientConfig', (b'subModeImpl', b'assetsPointer', b'settingsKey', b'priority', b'wwiseRemapping', b'battleModifiersDescr', b'infoPageUrl'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(subModeImpl=FunSubModeImpl.DEFAULT, assetsPointer=DEFAULT_ASSETS_PACK, settingsKey=DEFAULT_SETTINGS_KEY, priority=DEFAULT_PRIORITY, wwiseRemapping=UNKNOWN_WWISE_REMAPPING, battleModifiersDescr=(), infoPageUrl=b'')
        defaults.update(kwargs)
        return super(FunSubModeClientConfig, cls).__new__(cls, **defaults)

    @classmethod
    def defaults(cls):
        return cls(FunSubModeImpl.DEFAULT, DEFAULT_ASSETS_PACK, DEFAULT_SETTINGS_KEY, DEFAULT_PRIORITY, UNKNOWN_WWISE_REMAPPING, (), b'')


class FunSubModeFiltrationConfig(namedtuple(b'FunSubModeFiltrationConfig', (b'levels', b'forbiddenClassTags', b'forbiddenVehTypes', b'allowedVehTypes'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(levels=(), forbiddenClassTags=set(), forbiddenVehTypes=set(), allowedVehTypes=set())
        defaults.update(kwargs)
        return super(FunSubModeFiltrationConfig, cls).__new__(cls, **defaults)

    @classmethod
    def defaults(cls):
        return cls((), set(), set(), set())


class FunSubModeSeasonalityConfig(namedtuple(b'FunSubModeSeasonalityConfig', (b'isEnabled', b'peripheryIDs', b'seasons', b'primeTimes', b'cycleTimes', b'geometryIDs'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(isEnabled=False, peripheryIDs=set(), seasons={}, primeTimes={}, cycleTimes=(), geometryIDs=set())
        defaults.update(kwargs)
        cls.__packSeasonalityConfig(defaults)
        return super(FunSubModeSeasonalityConfig, cls).__new__(cls, **defaults)

    @classmethod
    def defaults(cls):
        return cls(False, set(), {}, {}, (), set())

    def asDict(self):
        return self._asdict()

    @classmethod
    def __packSeasonalityConfig(cls, data):
        data[b'primeTimes'] = {int(peripheryID): value for peripheryID, value in data[b'primeTimes'].iteritems()}
        data[b'seasons'] = {int(seasonID): value for seasonID, value in data[b'seasons'].iteritems()}
        return


class FunSubModeConfig(namedtuple(b'_FunSubModeConfig', (b'eventID', b'isEnabled', b'seasonality', b'filtration', b'client', b'isFunRandomMapsVisible'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(eventID=UNKNOWN_EVENT_ID, isEnabled=False, seasonality={}, filtration={}, client={}, isFunRandomMapsVisible=False)
        allowedFields = defaults.keys()
        defaults.update(kwargs)
        cls.__packConfigPart(FunSubModeClientConfig, b'client', defaults)
        cls.__packConfigPart(FunSubModeFiltrationConfig, b'filtration', defaults)
        cls.__packConfigPart(FunSubModeSeasonalityConfig, b'seasonality', defaults)
        defaults = cls.__filterAllowedFields(defaults, allowedFields)
        return super(FunSubModeConfig, cls).__new__(cls, **defaults)

    @classmethod
    def defaults(cls):
        return cls(UNKNOWN_EVENT_ID, False, {}, {}, {}, False)

    @classmethod
    def __filterAllowedFields(cls, data, allowedFields):
        return dict((k, v) for k, v in data.iteritems() if k in allowedFields)

    @classmethod
    def __packConfigPart(cls, configPartCls, configPartName, data):
        data[configPartName] = makeTupleByDict(configPartCls, data)
        return


class FunProgressionConfig(namedtuple(b'_FunProgressionConfig', (b'name', b'executors', b'conditions'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(name=b'', executors=(), conditions=())
        defaults.update(kwargs)
        return super(FunProgressionConfig, cls).__new__(cls, **defaults)

    @classmethod
    def defaults(cls):
        return cls(b'', (), ())


class FunMetaProgressionConfig(namedtuple(b'_FunMetaProgressionConfig', (b'isEnabled', b'progressions'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(isEnabled=False, progressions=())
        defaults.update(kwargs)
        cls.__packProgressionsConfigs(defaults)
        return super(FunMetaProgressionConfig, cls).__new__(cls, **defaults)

    @classmethod
    def defaults(cls):
        return cls(False, ())

    @classmethod
    def __packProgressionsConfigs(cls, data):
        data[b'progressions'] = tuple(makeTupleByDict(FunProgressionConfig, p) for p in data[b'progressions'])
        return


class FunRandomConfig(namedtuple(b'_FunRandomConfig', (b'isEnabled', b'FEPType', b'subModes', b'metaProgression', b'assetsPointer', b'settingsKey', b'infoPageUrl'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(isEnabled=False, FEPType=FUN_RANDOM_ARCADE_FEP_TYPE, subModes={}, metaProgression={}, assetsPointer=DEFAULT_ASSETS_PACK, settingsKey=DEFAULT_SETTINGS_KEY, infoPageUrl=b'')
        allowedFields = defaults.keys()
        defaults.update(kwargs)
        cls.__packSubModesConfigs(defaults)
        cls.__packMetaProgressionConfig(defaults)
        defaults = cls.__filterAllowedFields(defaults, allowedFields)
        return super(FunRandomConfig, cls).__new__(cls, **defaults)

    @classmethod
    def defaults(cls):
        return cls(False, FUN_RANDOM_ARCADE_FEP_TYPE, {}, {}, DEFAULT_ASSETS_PACK, DEFAULT_SETTINGS_KEY, b'')

    def replace(self, data):
        data = self.__packSubModesConfigs(data)
        data = self.__packMetaProgressionConfig(data)
        dataToUpdate = self.__filterAllowedFields(data, self._fields)
        return self._replace(**dataToUpdate)

    @classmethod
    def __filterAllowedFields(cls, data, allowedFields):
        return dict((k, v) for k, v in data.iteritems() if k in allowedFields)

    @classmethod
    def __packMetaProgressionConfig(cls, data):
        progression = data[b'metaProgression'] if data[b'isEnabled'] else {}
        data[b'metaProgression'] = makeTupleByDict(FunMetaProgressionConfig, progression)
        return data

    @classmethod
    def __packSubModesConfigs(cls, data):
        events = data[b'events'] if data[b'isEnabled'] else {}
        data[b'subModes'] = {int(eID): FunSubModeConfig(**eData) for eID, eData in events.iteritems() if eData.get(b'isEnabled', False) and eData.get(b'eventID', UNKNOWN_EVENT_ID)}
        return data
