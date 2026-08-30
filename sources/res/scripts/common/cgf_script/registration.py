from __future__ import absolute_import
import sys, CGF, BigWorld
from future.utils import viewitems
g_propertyIndex = 0

class ComponentProperty(object):

    def __init__(self, type=CGF.PropertyType.Int, value=None, editorName=b'', **kwarg):
        global g_propertyIndex
        if type == CGF.PropertyType.Link and value is None:
            value = CGF.GameObject
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
    name = (b'script::{}').format(cls.__name__)
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
        baseAttrs = vars(base)
        for key, value in viewitems(baseAttrs):
            if isinstance(value, ComponentProperty):
                setattr(cls, key, None)
                value.name = key
                value.ownerName = name
                value.applyIndex(basePropIndex)
                meta.append(value)

    for key, value in viewitems(attrs):
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
    user_visible = getattr(cls, b'userVisible', True)
    vse_visible = getattr(cls, b'vseVisible', True)
    name = getattr(cls, b'serialName', name)
    domain = getattr(cls, b'domain', CGF.Domain.All)
    if module_path is None:
        module_path = sys.modules[cls.__module__].__file__ if cls.__module__ != b'__builtin__' else b'__builtin__'
    CGF.registerComponent(cls, module_path, name, editor_title, user_visible, vse_visible, domain, category)
    g_propertyIndex = 0
    return cls


def registerComponent(cls):
    setattr(cls, CGF.CGF_COMPONENT_MARKER, None)
    return defaultRegistrator(cls)


def registerReplicableComponent(cls):
    setattr(cls, CGF.CGF_REPLICABLE_COMPONENT_MARKER, None)
    return defaultRegistrator(cls)


def registerModule(cls):
    modulePath = sys.modules[cls.__module__].__file__ if cls.__module__ != b'__builtin__' else b'__builtin__'
    CGF.registerModulePath(cls, modulePath)
    CGF.registerModule(cls)
    return


def bonusCapsPredicate(caps, spaceID):
    try:
        from Avatar import PlayerAvatar
        from ClientArena import ClientArena
        player = BigWorld.player()
    except:
        return False

    if spaceID != ClientArena.DEFAULT_ARENA_WORLD_ID and isinstance(player, PlayerAvatar):
        return player.hasBonusCap(caps)
    return False
