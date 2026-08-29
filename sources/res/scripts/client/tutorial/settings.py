from collections import namedtuple
from soft_exception import SoftException
TUTORIAL_VERSION = b'0.4.0'
DOC_DIRECTORY = b'scripts/tutorial_docs'
BONUSES_REFS_FILE_PATH = (b'{0:>s}/bonuses-refs.xml').format(DOC_DIRECTORY)

class INITIAL_FLAG(object):
    GUI_LOADED = 1
    CHAPTER_RESOLVED = 2
    INITIALIZED = GUI_LOADED | CHAPTER_RESOLVED


_SettingsDesc = namedtuple(b'_SettingsDesc', (b'id', b'enabled', b'cacheEnabled', b'hintsEnabled', b'findChapterInCache', b'space', b'descriptorPath', b'descriptorParser', b'reqs', b'ctrl', b'gui', b'dispatcher', b'exParsers', b'chapterParser'))
_ClassPath = namedtuple(b'_ClassPath', (b'module', b'clazz', b'args'))
TUTORIAL_LOBBY_DISPATCHER = _ClassPath(b'gui.Scaleform.lobby', b'SfLobbyDispatcher', ())
TUTORIAL_BATTLE_DISPATCHER = _ClassPath(b'tutorial.gui.Scaleform.battle_v2', b'SfBattleDispatcher', ())
TUTORIAL_DESCRIPTOR_PARSER = _ClassPath(b'tutorial.doc_loader.parsers', b'DescriptorParser', ())
TUTORIAL_CHAPTER_PARSER = _ClassPath(b'tutorial.doc_loader.parsers', b'ChapterParser', ())

class TUTORIAL_SETTINGS(object):
    SALES_TRIGGERS = _SettingsDesc(b'SALES_TRIGGERS', True, True, True, False, b'SALES_TRIGGERS', (b'{0:>s}/sales-descriptor.xml').format(DOC_DIRECTORY), TUTORIAL_DESCRIPTOR_PARSER, _ClassPath(b'tutorial.control.sales.context', b'SalesStartReqs', ()), _ClassPath(b'tutorial.control.sales', b'SalesControlsFactory', ()), _ClassPath(b'gui.Scaleform.sales.proxy', b'SfSalesProxy', ()), TUTORIAL_LOBBY_DISPATCHER, b'tutorial.doc_loader.sub_parsers.sales', TUTORIAL_CHAPTER_PARSER)
    BOOTCAMP_LOBBY = _SettingsDesc(b'BOOTCAMP_LOBBY', True, False, False, False, b'BOOTCAMP_LOBBY', (b'{0:>s}/bootcamp-lobby-descriptor.xml').format(DOC_DIRECTORY), _ClassPath(b'tutorial.doc_loader.parsers.bootcamp_lobby', b'BootcampLobbyDescriptorParser', ()), _ClassPath(b'tutorial.control.bootcamp.lobby.context', b'BootcampLobbyStartReqs', {}), _ClassPath(b'tutorial.control.bootcamp.lobby', b'BootcampLobbyControlsFactory', {}), _ClassPath(b'gui.Scaleform.bootcamp.lobby.proxy', b'SfBootcampLobbyProxy', {}), TUTORIAL_LOBBY_DISPATCHER, b'tutorial.doc_loader.sub_parsers.bootcamp_lobby', _ClassPath(b'tutorial.doc_loader.parsers.bootcamp_lobby', b'BootcampLobbyChapterParser', ()))
    TANK_ACADEMY = _SettingsDesc(b'TANK_ACADEMY', True, True, False, False, b'TANK_ACADEMY', (b'{0:>s}/tank-academy-descriptor.xml').format(DOC_DIRECTORY), TUTORIAL_DESCRIPTOR_PARSER, _ClassPath(b'tutorial.control.sales.context', b'SalesStartReqs', ()), _ClassPath(b'tutorial.control.sales', b'SalesControlsFactory', ()), _ClassPath(b'tutorial.gui.Scaleform.sales.proxy', b'SfSalesProxy', ()), TUTORIAL_LOBBY_DISPATCHER, b'tutorial.doc_loader.sub_parsers.sales', TUTORIAL_CHAPTER_PARSER)
    SHORT_BOOTCAMP_LOBBY = _SettingsDesc(b'SHORT_BOOTCAMP_LOBBY', True, False, False, False, b'BOOTCAMP_LOBBY', (b'{0:>s}/short_bootcamp/short-bootcamp-lobby-descriptor.xml').format(DOC_DIRECTORY), _ClassPath(b'tutorial.doc_loader.parsers.bootcamp_lobby', b'BootcampLobbyDescriptorParser', ()), _ClassPath(b'tutorial.control.bootcamp.lobby.context', b'BootcampLobbyStartReqs', {}), _ClassPath(b'tutorial.control.bootcamp.lobby', b'BootcampLobbyControlsFactory', {}), _ClassPath(b'gui.Scaleform.bootcamp.lobby.proxy', b'SfBootcampLobbyProxy', {}), TUTORIAL_LOBBY_DISPATCHER, b'tutorial.doc_loader.sub_parsers.bootcamp_lobby', _ClassPath(b'tutorial.doc_loader.parsers.bootcamp_lobby', b'BootcampLobbyChapterParser', ()))


class _SettingsCollection(dict):

    def init(self, clazz):
        self.clear()
        for name, settings in clazz.__dict__.iteritems():
            if name.startswith(b'_'):
                continue
            self[settings.id] = settings

        return

    def getSettings(self, settingsID):
        settings = None
        if settingsID in self:
            return self[settingsID]
        else:
            return settings


def createSettingsCollection():
    collection = _SettingsCollection()
    collection.init(TUTORIAL_SETTINGS)
    return collection


def createTutorialElement(classPath, init=None):
    imported = __import__(classPath.module, globals(), locals(), [
     classPath.clazz])
    if not imported:
        raise SoftException((b'Can not find class {0.module} in {0.clazz}').format(classPath))
    clazz = getattr(imported, classPath.clazz)
    if init is None:
        init = classPath.args
    return clazz(*init)
