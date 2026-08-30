from collections import namedtuple
from operator import getitem
import resource_helper
from debug_utils import LOG_ERROR
from gui.Scaleform.genConsts.TWEEN_EFFECT_TYPES import TWEEN_EFFECT_TYPES
__all__ = (b'readConfig', b'clearConfig')
_cache = {}

def readConfig(path, forced=False):
    global _cache
    if not forced and path in _cache:
        return _cache[path]
    else:
        scenes, items, commands = (None, None, None)
        with resource_helper.root_generator(path) as ctx, root:
            scenes = _readConfig(ctx, root, b'scenes', b'scene', _SceneConfig)
            items = _readConfig(ctx, root, b'gui-items', b'item', _ItemConfig)
            commands = _readConfig(ctx, root, b'gui-commands', b'command', _CommandData)
        _cache[path] = _TutorialConfig(scenes, items, commands)
        return _cache[path]


def clearConfig(path):
    if path in _cache:
        del _cache[path]
    return


def _getEnumValueByName(name, enum):
    if isinstance(enum, dict):
        valGetter = getitem
        invalidFlagExceptionType = KeyError
    else:
        valGetter = getattr
        invalidFlagExceptionType = AttributeError
    try:
        flagVal = valGetter(enum, name)
        return flagVal
    except invalidFlagExceptionType:
        LOG_ERROR(b'name not found in enum:', name, enum)
        return name

    return


def _listToBitmask(flagNamesList, flagsEnum):
    mask = 0
    for flagName in flagNamesList:
        flagVal = _getEnumValueByName(flagName, flagsEnum)
        try:
            mask |= _getEnumValueByName(flagName, flagsEnum)
        except TypeError:
            LOG_ERROR(b'invalid flag value (expecting integer):', flagName, flagVal)

    return mask


class _ItemConfig(object):
    __slots__ = (b'__view', b'__path', b'__padding', b'__anim', b'__bootcampHint', b'__effectBuilders')

    def __init__(self, view=b'', path=b'', padding=None, anim=None, bootcampHint=None, effectBuilders=None):
        self.__view = view
        self.__path = path
        self.__padding = self._defaultPadding()
        self.__anim = self._defaultAnimConfig()
        self.__bootcampHint = self._defaultBootcampHintConfig()
        self.__effectBuilders = effectBuilders.copy() if effectBuilders is not None else {}
        if padding is not None:
            self.__padding.update(padding)
        if anim is not None:
            if b'tween' in anim and b'flags' in anim[b'tween']:
                anim[b'tween'][b'flags'] = _listToBitmask(anim[b'tween'][b'flags'], TWEEN_EFFECT_TYPES)
            self.__anim.update(anim)
        if bootcampHint is not None:
            self.__bootcampHint.update(bootcampHint)
        return

    @property
    def view(self):
        return self.__view

    @property
    def path(self):
        return self.__path

    @property
    def padding(self):
        return self.__padding

    @property
    def anim(self):
        return self.__anim

    @property
    def bootcampHint(self):
        return self.__bootcampHint

    @property
    def effectBuilders(self):
        return self.__effectBuilders

    @staticmethod
    def _defaultPadding():
        return {b'left': 0, 
           b'top': 0, 
           b'right': 0, 
           b'bottom': 0}

    @staticmethod
    def _defaultAnimConfig():
        return {b'tween': {b'flags': (TWEEN_EFFECT_TYPES.ALPHA), 
                      b'delay': 0}, 
           b'clip': {b'linkage': b'BCLobbySlotUI', 
                     b'offsetX': 0, 
                     b'offsetY': 0}, 
           b'overlay': {b'x': 0, 
                        b'y': 0, 
                        b'width': 100, 
                        b'height': 100}}

    @staticmethod
    def _defaultBootcampHintConfig():
        return {b'padding': (_ItemConfig._defaultPadding()), 
           b'hideBorder': False, 
           b'customLinkage': b''}


_SceneConfig = namedtuple(b'_SceneConfig', (b'sceneID', b'event'))
_CommandData = namedtuple(b'_CommandData', (b'type', b'name', b'args'))

class _TutorialConfig(object):
    __slots__ = (b'__scenes', b'__guiItems', b'__commands')

    def __init__(self, scenes=None, items=None, commands=None):
        super(_TutorialConfig, self).__init__()
        self.__scenes = scenes or {}
        self.__guiItems = items or {}
        self.__commands = commands or {}
        return

    def isEmpty(self):
        return not self.__scenes and not self.__guiItems and not self.__commands

    def getSceneID(self, guiPage):
        try:
            return self.__scenes[guiPage].sceneID
        except KeyError:
            return b''

        return

    def getSceneEvent(self, sceneID):
        scenes = dict((scene.sceneID, scene.event) for scene in self.__scenes.itervalues())
        try:
            return scenes[sceneID]
        except KeyError:
            return b''

        return

    def getItem(self, targetID):
        if targetID in self.__guiItems:
            return self.__guiItems[targetID]
        else:
            return

    def getItems(self):
        for itemID, item in self.__guiItems.iteritems():
            yield (
             itemID, item)

        return

    def getCommand(self, commandID):
        try:
            return self.__commands[commandID]
        except KeyError:
            return

        return

    def getCommands(self):
        for commandID, command in self.__commands.iteritems():
            yield (
             commandID, command)

        return


_ITEM_TYPE = resource_helper.RESOURCE_ITEM_TYPE

def _readConfig(ctx, root, parentTag, childTag, itemClass):
    ctx, section = resource_helper.getSubSection(ctx, root, parentTag, safe=True)
    if not section:
        return {}
    config = {}
    for xmlCtx, subSection in resource_helper.getIterator(ctx, section):
        item = resource_helper.readItem(xmlCtx, subSection, childTag)
        name = item.name
        if name in config:
            raise resource_helper.ResourceError(xmlCtx, (b'Item {0} is duplicated.').format(name))
        config[name] = itemClass(**item.value)

    return config
