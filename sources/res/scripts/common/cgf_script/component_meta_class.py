import sys, CGF, inspect
from debug_utils import LOG_CURRENT_EXCEPTION

class CGFMetaTypes(object):
    BOOL = b'bool'
    STRING = b'string'
    FLOAT = b'real'
    INT = b'integer'
    STRING_LIST = b'CGF::ScriptList<string>'
    INT_LIST = b'CGF::ScriptList<int32>'
    FLOAT_LIST = b'CGF::ScriptList<float>'
    VECTOR2_LIST = b'CGF::ScriptList<Vector2>'
    VECTOR3_LIST = b'CGF::ScriptList<Vector3>'
    VECTOR4_LIST = b'CGF::ScriptList<Vector4>'
    LINK = b'BW::CGF::PyLinkConfig'
    VECTOR2 = b'Vector2'
    VECTOR3 = b'Vector3'
    VECTOR4 = b'Vector4'


class ReplicationType(object):
    LATEST_ONLY = 0
    VOLATILE = 1
    HISTORY = 2


class RPCType(object):
    SERVER_TO_CLIENT = 0
    CLIENT_TO_SERVER = 1


g_propertyIndex = 0

class ComponentProperty(object):

    def __init__(self, type=CGFMetaTypes.INT, value=0, editorName=b'', **kwarg):
        global g_propertyIndex
        kwarg.update({b'type': type, b'value': value, b'editorName': editorName, b'name': b'', b'ownerName': b''})
        self.__metadata = kwarg
        self.__index = 0
        self.__baseIndex = g_propertyIndex
        g_propertyIndex += 1
        return

    def __get__(self, instance, owner=None):
        return self.__metadata

    def __set__(self, instance, value):
        self.__metadata = value
        return

    def applyIndex(self, shift):
        self.__index = self.__baseIndex + shift
        return

    @property
    def metadata(self):
        return self.__metadata

    @property
    def name(self):
        return self.metadata[b'name']

    @name.setter
    def name(self, value):
        self.metadata[b'name'] = value
        return

    @property
    def ownerName(self):
        return self.metadata[b'ownerName']

    @ownerName.setter
    def ownerName(self, value):
        self.metadata[b'ownerName'] = value
        return

    @property
    def index(self):
        return self.__index

    def __call__(self, *args, **kwargs):
        return


def defaultRegistrator(cls):
    global g_propertyIndex
    name = cls.__name__
    meta = []
    all_meta = []
    bases = cls.__mro__
    attrs = vars(cls)
    basePropIndex = 0
    for base in bases:
        baseMeta = getattr(base, b'__meta', None)
        if baseMeta is not None:
            basePropIndex += len(baseMeta)
            all_meta.extend(baseMeta)

    for key, value in attrs.iteritems():
        if isinstance(value, ComponentProperty):
            setattr(cls, key, None)
            value.name = key
            value.ownerName = name
            value.applyIndex(basePropIndex)
            meta.append(value)

    all_meta.extend(meta)
    setattr(cls, b'__meta', all_meta)
    category = getattr(cls, b'category', b'Python')
    editor_title = getattr(cls, b'editorTitle', name)
    module_path = getattr(cls, b'modulePath', None)
    version = getattr(cls, b'version', 1)
    user_visible = getattr(cls, b'userVisible', True)
    vse_visible = getattr(cls, b'vseVisible', True)
    domain = getattr(cls, b'domain', CGF.DomainOption.DomainClient | CGF.DomainOption.DomainEditor)
    if module_path is None:
        module_path = sys.modules[cls.__module__].__file__ if cls.__module__ != b'__builtin__' else b'__builtin__'
    CGF.registerComponent(cls, module_path, name, editor_title, user_visible, vse_visible, domain, category, version)
    g_propertyIndex = 0
    return cls


def registerComponent(cls):
    setattr(cls, CGF.CGF_COMPONENT_MARKER, None)
    return defaultRegistrator(cls)


def registerReplicableComponent(cls):
    setattr(cls, CGF.CGF_REPLICABLE_COMPONENT_MARKER, None)
    setattr(cls, b'domain', CGF.DomainOption.DomainAll | CGF.DomainOption.LockDomain)
    return defaultRegistrator(cls)


class CGFConverterMetaClass(type):

    def __new__(metacls, name, bases, attrs):
        cls = type.__new__(metacls, name, bases, attrs)
        if name == b'CGFComponentConverter':
            return cls
        CGF.registerScriptComponentConverter(name, cls)
        return cls


class CGFComponentConverter(object):
    __metaclass__ = CGFConverterMetaClass

    def sourceVersion(self):
        return 0

    def targetVersion(self):
        return 0

    def convert(self, sourceConfig, convertedConfig):
        return
