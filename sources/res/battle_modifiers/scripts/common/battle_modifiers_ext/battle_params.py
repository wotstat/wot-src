from __future__ import absolute_import
from future.utils import listvalues, viewitems
from typing import Any, Optional, Set, Tuple, Union, TYPE_CHECKING
from battle_modifiers_common.battle_modifiers import BattleParams, ModifierScope
from battle_modifiers_ext.battle_modifier.modifier_appliers import registerParamAppliers
from battle_modifiers_ext.battle_modifier.modifier_helpers import Serializable
from battle_modifiers_ext.battle_modifier.modifier_restrictions import readRestrictions
from battle_modifiers_ext.battle_modifier.modifier_readers import registerParamReaders
from battle_modifiers_ext.constants_ext import BATTLE_PARAMS_XML_PATH, DataType, UseType, PhysicalType, ModifierDomain, ClientDomain
from constants import IS_CLIENT
from extension_utils import ResMgr
from soft_exception import SoftException
if TYPE_CHECKING:
    from ResMgr import DataSection
_ERR_TEMPLATE = b"[BattleParams] {} for param '{}'"
g_cache = None

class BaseClientParamData(Serializable):
    __slots__ = (b'resName', b'domain', b'physicalType', b'useTypes')

    def __init__(self, source, techName):
        self.resName = b''
        self.domain = ClientDomain.UNDEFINED
        self.physicalType = PhysicalType.UNDEFINED
        self.useTypes = set()
        super(BaseClientParamData, self).__init__(source, techName)
        return


class ClientParamData(BaseClientParamData):
    __slots__ = ()

    def __repr__(self):
        return (b'ClientParamData(resName={}, domain = {}, physicalTypeName={}, useTypesName={})').format(self.resName, self.domain, PhysicalType.ID_TO_NAME[self.physicalType], (UseType.ID_TO_NAME[useType] for useType in self.useTypes))

    def _initFromConfig(self, clientConfig, techName=b''):
        self.resName = self._readResName(techName, clientConfig)
        self.physicalType = self.__readPhysicalType(techName, clientConfig)
        self.useTypes = self._readUseTypes(techName, self.physicalType, clientConfig)
        self.domain = self.__readDomain(techName, self.useTypes, clientConfig)
        return

    @classmethod
    def _readResName(cls, techName, _):
        return techName

    @staticmethod
    def _readUseTypes(tName, physicalType, dataSection):
        useTypes = set()
        if not dataSection.has_key(b'useTypes'):
            return useTypes
        for useTypeName in dataSection[b'useTypes'].asString.split():
            if useTypeName not in UseType.NAMES:
                raise SoftException(_ERR_TEMPLATE.format((b"Unknown client use type '{}'").format(useTypeName), tName))
            useTypes.add(UseType.NAME_TO_ID[useTypeName])

        if physicalType == PhysicalType.UNDEFINED and useTypes & UseType.DIMENSIONAL_TYPES:
            raise SoftException(_ERR_TEMPLATE.format((b"Client physical type should be defined in order to show dimensional use types '{}'").format((b', ').join(UseType.ID_TO_NAME[useType] for useType in UseType.DIMENSIONAL_TYPES)), tName))
        return useTypes

    @staticmethod
    def __readDomain(tName, useTypes, dataSection):
        clientDomain = ClientDomain.UNDEFINED
        if not useTypes:
            return clientDomain
        if not dataSection.has_key(b'domain'):
            raise SoftException(_ERR_TEMPLATE.format(b'Missing client domain', tName))
        clientDomain = dataSection[b'domain'].asString
        if clientDomain not in ClientDomain.ALL:
            raise SoftException(_ERR_TEMPLATE.format((b"Unknown client domain '{}'").format(clientDomain), tName))
        return clientDomain

    @staticmethod
    def __readPhysicalType(tName, dataSection):
        if not dataSection.has_key(b'physicalType'):
            return PhysicalType.UNDEFINED
        physTypeName = dataSection[b'physicalType'].asString
        if physTypeName not in PhysicalType.NAMES:
            raise SoftException(_ERR_TEMPLATE.format((b"Unknown client phys. type '{}'").format(physTypeName), tName))
        return PhysicalType.NAME_TO_ID[physTypeName]


class DefaultClientParamData(BaseClientParamData):
    __slots__ = ()

    def _initFromDescr(self, descr):
        return

    def _initFromConfig(self, source, *args):
        return


class FakeClientParamData(ClientParamData):
    __slots__ = (b'__descr',)

    def __init__(self, source, techName):
        super(FakeClientParamData, self).__init__(source, techName)
        self.__descr = None
        return

    def __repr__(self):
        return (b'FakeClientParamData(descr = {})').format(self.descr())

    def descr(self):
        if self.__descr is None:
            self.__descr = self.__makeDescr()
        return self.__descr

    @classmethod
    def _readResName(cls, techName, config):
        if not config.has_key(b'view'):
            raise SoftException(b'Missing view for a FakeBattleModifier')
        return config[b'view'].asString

    @classmethod
    def _readUseTypes(cls, tName, physicalType, dataSection):
        return cls.__getUseTypes(physicalType)

    def _initFromDescr(self, descr):
        self.resName, self.domain, self.physicalType = descr
        self.useTypes = self.__getUseTypes(self.physicalType)
        self.__descr = descr
        return

    @classmethod
    def __getUseTypes(cls, _):
        return UseType.ALL_WITH_UNDEFINED

    def __makeDescr(self):
        return (
         self.resName, self.domain, self.physicalType)


class BaseBattleParam(Serializable):
    __slots__ = (b'id', b'scope', b'domain', b'clientData')

    def __init__(self, source):
        self.id = b''
        self.scope = 0
        self.domain = ModifierDomain.DEFAULT
        self.clientData = DefaultClientParamData(source, self.id)
        super(BaseBattleParam, self).__init__(source)
        return

    def isHashable(self):
        return False


class BattleParam(BaseBattleParam):
    __slots__ = (b'dataType', b'validators', b'minValue', b'maxValue')

    def __repr__(self):
        return (b'BattleParam(id = {}, dataTypeName = {}, clientData={})').format(self.id, DataType.ID_TO_NAME[self.dataType], self.clientData)

    @staticmethod
    def readId(config):
        return config.name

    @staticmethod
    def readDataType(config):
        if not config.has_key(b'dataType'):
            raise SoftException(_ERR_TEMPLATE.format(b'Missing data type', config.name))
        dataTypeName = config[b'dataType'].asString
        if dataTypeName not in DataType.NAMES:
            raise SoftException(_ERR_TEMPLATE.format((b"Unknown data type '{}'").format(dataTypeName), config.name))
        return DataType.NAME_TO_ID[dataTypeName]

    @staticmethod
    def readScope(config):
        if not config.has_key(b'scope'):
            raise SoftException(_ERR_TEMPLATE.format(b'Missing scope', config.name))
        scope = 0
        for scopeName in config[b'scope'].asString.split():
            if scopeName not in ModifierScope.NAMES:
                raise SoftException(_ERR_TEMPLATE.format((b"Unknown scope '{}'").format(scopeName), config.name))
            scope |= ModifierScope.NAME_TO_ID[scopeName]

        return scope

    @staticmethod
    def readDomain(config):
        if not config.has_key(b'domain'):
            return ModifierDomain.DEFAULT
        domain = 0
        for domainName in config[b'domain'].asString.split():
            if domainName not in ModifierDomain.NAMES:
                raise SoftException(_ERR_TEMPLATE.format((b"Unknown domain '{}'").format(domainName), config.name))
            domain |= ModifierDomain.NAME_TO_ID[domainName]

        return domain

    @staticmethod
    def readClientData(config):
        if not IS_CLIENT:
            return None
        else:
            clientSection = config[b'client'] if config.has_key(b'client') else config
            return ClientParamData(clientSection, config.name)

    def isHashable(self):
        return self.dataType in DataType.HASHABLE_TYPES

    def _initFromConfig(self, config, *args):
        paramId = self.readId(config)
        dataType = self.readDataType(config)
        registerParamReaders(paramId, dataType)
        registerParamAppliers(paramId, dataType)
        self.id = paramId
        self.dataType = dataType
        self.scope = self.readScope(config)
        self.domain = self.readDomain(config)
        self.clientData = self.readClientData(config)
        self.validators, self.minValue, self.maxValue = readRestrictions(config, self.id)
        return


class BattleParamStub(BaseBattleParam):
    __slots__ = ()

    def __repr__(self):
        return (b'BattleParamStub(id = {})').format(self.id)

    def _initFromConfig(self, config, *args):
        self.id = BattleParam.readId(config)
        self.scope = BattleParam.readScope(config)
        self.domain = BattleParam.readDomain(config)
        return


class FakeBattleParam(BaseBattleParam):
    __slots__ = (b'__descr',)

    def __init__(self, source):
        super(FakeBattleParam, self).__init__(source)
        self.__descr = None
        return

    def __repr__(self):
        return (b'FakeBattleParam(descr = {})').format(self.descr())

    def descr(self):
        if self.__descr is None:
            self.__descr = self.__makeDescr()
        return self.__descr

    def _initFromDescr(self, descr):
        self.__initialize(descr)
        self.__descr = descr
        return

    def _initFromConfig(self, config, *args):
        self.__initialize(config)
        return

    def __initialize(self, source):
        global g_cache
        fakeParamStub = g_cache[BattleParams.FAKE_MODIFIER]
        self.id = fakeParamStub.id
        self.scope = fakeParamStub.scope
        self.domain = fakeParamStub.domain
        self.clientData = FakeClientParamData(source, self.id)
        return

    def __makeDescr(self):
        return self.clientData.descr()


class BattleParamsCache(object):
    __slots__ = (b'__params',)

    def __init__(self):
        self.__initFromConfig()
        return

    def __iter__(self):
        return iter(viewitems(self.__params))

    def __getitem__(self, id):
        return self.__params[id]

    def __len__(self):
        return len(self.__params)

    def __contains__(self, id):
        return id in self.__params

    def __repr__(self):
        return (b'BattleParams({})').format(listvalues(self.__params))

    def get(self, id):
        return self.__params.get(id)

    def __initFromConfig(self):
        config = ResMgr.openSection(BATTLE_PARAMS_XML_PATH)
        if config is None:
            raise SoftException((b"[BattleParams] Cannot open or read '{}'").format(BATTLE_PARAMS_XML_PATH))
        self.__params = params = {}
        for paramId, paramSection in config.items():
            if paramId == b'xmlns:xmlref':
                continue
            param = BattleParamStub(paramSection) if paramId in BattleParams.DYNAMIC else BattleParam(paramSection)
            if param.id in params:
                raise SoftException((b'[BattleParams] Not unique id {}').format(param.id))
            params[param.id] = param

        return


def init():
    global g_cache
    g_cache = BattleParamsCache()
    return
