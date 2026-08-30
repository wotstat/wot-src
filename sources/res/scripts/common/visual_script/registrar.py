import inspect
from block import Block
from context import VScriptContext
from type import VScriptType, VScriptEnum, VScriptStruct
__all__ = [
 b'VSBlockRegistrar']

def _findVScriptConponentsInModule(module, cls):
    return list(value for key, value in inspect.getmembers(module, inspect.isclass) if issubclass(value, cls) and value is not cls and inspect.getmodule(value) is module)


def _collectContextMetaData(cls):
    membersData = []
    for _, mem in inspect.getmembers(cls):
        if inspect.ismethod(mem) and hasattr(mem, b'vse_meta'):
            membersData.append(mem.vse_meta)

    return (
     cls.__name__, membersData)


class VSBlockRegistrar(object):

    def __init__(self, *aspect):
        self._aspects = set(aspect)
        self._domainBlocks = []
        self._domainContexts = {}
        self._domainTypes = []
        self._domainEnums = []
        self._domainStructs = []
        self._isEngineLoadBlocks = False
        self._isEngineLoadContexts = False
        self._isEngineLoadTypes = False
        return

    @property
    def aspects(self):
        return (b' | ').join(self._aspects)

    def regBlock(self, block):
        if block not in self._domainBlocks:
            self._domainBlocks.append(block)
        return

    def regBlocksFromModule(self, module):
        for block in _findVScriptConponentsInModule(module, Block):
            self.regBlock(block)

        return

    def getBlocks(self):
        self._isEngineLoadBlocks = True
        return self._domainBlocks

    def regContext(self, ctx):
        name, data = _collectContextMetaData(ctx)
        if name not in self._domainContexts:
            self._domainContexts[name] = data
        return

    def getContexts(self):
        self._isEngineLoadContexts = True
        return self._domainContexts

    def regType(self, cls):
        if issubclass(cls, VScriptType) and cls not in self._domainTypes:
            self._domainTypes.append(cls)
        elif issubclass(cls, VScriptEnum) and cls not in self._domainEnums:
            self._domainEnums.append(cls)
        elif issubclass(cls, VScriptStruct) and cls not in self._domainStructs:
            self._domainStructs.append(cls)
        return

    def regTypesFromModule(self, module):
        for cls in _findVScriptConponentsInModule(module, VScriptType):
            self.regType(cls)

        for cls in _findVScriptConponentsInModule(module, VScriptEnum):
            self.regType(cls)

        for cls in _findVScriptConponentsInModule(module, VScriptStruct):
            self.regType(cls)

        return

    def getTypes(self):
        self._isEngineLoadTypes = True
        return self._domainTypes

    def getEnums(self):
        self._isEngineLoadTypes = True
        return self._domainEnums

    def getStructs(self):
        self._isEngineLoadTypes = True
        return self._domainStructs
