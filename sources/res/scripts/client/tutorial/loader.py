import logging, weakref, typing, BigWorld, account_helpers
from CurrentVehicle import g_currentVehicle
from skeletons.tutorial import ITutorialLoader
from tutorial.gui.Scaleform.gui_impl import ScaleformGuiImpl
from tutorial.gui.controller import GuiController
from tutorial.gui.impl import WulfGuiImpl
from tutorial import core
from tutorial import settings as _settings
from tutorial import cache as _cache
from tutorial.control.context import GlobalStorage
from tutorial.control.listener import AppLoaderListener
from tutorial.doc_loader import loadDescriptorData
from tutorial.hints_manager import HintsManager
from soft_exception import SoftException
if typing.TYPE_CHECKING:
    from tutorial.core import Tutorial
    from skeletons.tutorial import IGuiController
_SETTINGS = _settings.TUTORIAL_SETTINGS
_LOBBY_DISPATCHER = _settings.TUTORIAL_LOBBY_DISPATCHER
_BATTLE_DISPATCHER = _settings.TUTORIAL_BATTLE_DISPATCHER
_LOBBY_GUI_CONFIG = b'gui/tutorial-lobby-gui.xml'
_BATTLE_GUI_CONFIG = b''
_logger = logging.getLogger(__name__)

def _getGuiImplementations():
    sfTutorialGui = ScaleformGuiImpl()
    wulfTutorialGui = WulfGuiImpl(sfTutorialGui)
    return (wulfTutorialGui, sfTutorialGui)


class RunCtx(object):
    __slots__ = (b'cache', b'isFirstStart', b'databaseID', b'isAfterBattle', b'restart', b'bonusCompleted', b'battlesCount', b'newbieBattlesCount', b'initialChapter', b'globalFlags', b'canResolveChapterOnStart', b'byRequest')

    def __init__(self, cache, **kwargs):
        super(RunCtx, self).__init__()
        self.cache = cache
        self.databaseID = kwargs.get(b'databaseID', 0)
        self.restart = kwargs.get(b'restart', False)
        self.isFirstStart = kwargs.get(b'isFirstStart', False)
        self.isAfterBattle = kwargs.get(b'isAfterBattle', False)
        self.bonusCompleted = kwargs.get(b'bonusCompleted', 0)
        self.battlesCount = kwargs.get(b'battlesCount', 0)
        self.newbieBattlesCount = kwargs.get(b'newbieBattlesCount', 0)
        self.initialChapter = kwargs.get(b'initialChapter')
        self.globalFlags = kwargs.get(b'globalFlags', {})
        self.canResolveChapterOnStart = kwargs.get(b'canResolveChapterOnStart', True)
        self.byRequest = kwargs.get(b'byRequest', False)
        return

    def __repr__(self):
        return (b'RunCtx(databaseID={}, restart={}, first={}, battle={}, bonuses={}, battles={}, newbie={}, chapter={}, flags={} cache={})').format(self.databaseID, self.restart, self.isFirstStart, self.isAfterBattle, self.bonusCompleted, self.battlesCount, self.newbieBattlesCount, self.initialChapter, self.globalFlags, self.cache)


class TutorialLoader(ITutorialLoader):

    def __init__(self):
        super(TutorialLoader, self).__init__()
        self.__loggedDBIDs = set()
        self.__afterBattle = False
        self.__tutorial = None
        self.__dispatcher = None
        self.__restoreID = None
        self.__settings = _settings.createSettingsCollection()
        self.__hintsManager = None
        self.__listener = None
        self.__guiController = GuiController()
        return

    def init(self):
        self.__guiController.init(_getGuiImplementations())
        self.__listener = AppLoaderListener()
        self.__listener.start(weakref.proxy(self))
        return

    def fini(self):
        if self.__listener is not None:
            self.__listener.stop()
        if self.__hintsManager is not None:
            self.__hintsManager.stop()
        if self.__dispatcher is not None:
            self.__dispatcher.stop()
        if self.__tutorial is not None:
            self.__tutorial.onStopped -= self.__onTutorialStopped
            self.__tutorial.stop()
        self.__loggedDBIDs.clear()
        self.__settings.clear()
        self.__guiController.fini()
        return

    @property
    def tutorial(self):
        return self.__tutorial

    @property
    def tutorialID(self):
        result = b''
        if self.__tutorial is not None:
            result = self.__tutorial.getID()
        return result

    @property
    def hintsManager(self):
        return self.__hintsManager

    @property
    def isRunning(self):
        result = False
        if self.__tutorial is not None:
            result = not self.__tutorial.isStopped()
        return result

    @property
    def gui(self):
        return self.__guiController

    def isTutorialStopped(self):
        result = True
        if self.__tutorial is not None:
            result = self.__tutorial.isStopped()
        return result

    def run(self, settingsID, state=None):
        settings = self.__settings.getSettings(settingsID)
        if settings is None:
            _logger.error(b'Can not find settings: %r', settingsID)
            return False
        else:
            if state is None:
                state = {}
            else:
                self.__updateConditionalState(state)
            reloadIfRun = state.pop(b'reloadIfRun', False)
            restoreIfRun = state.pop(b'restoreIfRun', False)
            isStopForced = state.pop(b'isStopForced', False)
            if self.__tutorial is not None and not self.__tutorial.isStopped():
                isCurrent = self.__tutorial.getID() == settings.id
                if reloadIfRun and isCurrent:
                    if isStopForced:
                        self.__doStop()
                    else:
                        GlobalStorage.setFlags(state.get(b'globalFlags', {}))
                        _logger.debug(b'invalidateFlags from TutorialLoader.run')
                        self.__tutorial.invalidateFlags()
                        return True
                elif restoreIfRun and not isCurrent:
                    self.__restoreID = self.__tutorial.getID()
                    self.__doStop()
                else:
                    _logger.error(b'Tutorial already is running: %r', self.__tutorial.getID())
                    return False
            state.setdefault(b'isAfterBattle', self.__afterBattle)
            state.setdefault(b'restart', True)
            state[b'byRequest'] = True
            result = self.__doRun(settings, state)
            if not result:
                self.__restoreID = None
            return result

    def stop(self, restore=True):
        self.__doStop()
        self.__doStopHints()
        self.__guiController.clear()
        if restore:
            self.__doRestore()
        else:
            self.__restoreID = None
        return

    def refuse(self):
        if self.__tutorial is not None:
            self.__tutorial.refuse()
        return

    def goToLobby(self):
        databaseID = account_helpers.getAccountDatabaseID()
        if not databaseID:
            raise SoftException(b'Acoount database ID is not defined')
        self.__loggedDBIDs.add(databaseID)
        self.__setDispatcher(_LOBBY_DISPATCHER)
        self.__restoreID = None
        self.__hintsManager = HintsManager()
        self.__hintsManager.start()
        return

    def leaveLobby(self):
        self.stop(restore=False)
        return

    def goToBattleLoading(self):
        self.__doClear()
        return

    def goToBattle(self):
        if self.__tutorial is not None:
            self.__tutorial.startBattle()
        return

    def leaveBattle(self):
        self.stop(restore=False)
        return

    def goToLogin(self):
        self.__afterBattle = False
        self.__doClear()
        return

    def beforeEnterLobby(self):
        self.__guiController.setup(True, _LOBBY_GUI_CONFIG)
        return

    def beforeEnterBattle(self):
        self.__guiController.setup(False, _BATTLE_GUI_CONFIG)
        return

    def __doAutoRun(self, seq, state):
        for settings in seq:
            if self.__doRun(settings, state):
                return settings

        return

    def __doRun(self, settings, state):
        if not settings.enabled:
            return False
        else:
            reqs = _settings.createTutorialElement(settings.reqs)
            if not reqs.isEnabled():
                return False
            descriptor = loadDescriptorData(settings, settings.exParsers)
            if descriptor is None:
                _logger.error(b'Descriptor is not valid. Tutorial is not available: %r', settings)
                return False
            cache = _cache.TutorialCache(BigWorld.player().name)
            cache.read()
            cache.setSpace(settings.space, ioEnabled=settings.cacheEnabled)
            if state.get(b'byRequest', False):
                cache.setRefused(False)
            runCtx = RunCtx(cache, **state)
            reqs.prepare(runCtx)
            if not reqs.process(descriptor, runCtx):
                return False
            self.__doStop()
            if self.__dispatcher is None:
                self.__setDispatcher(settings.dispatcher)
            self.__tutorial = core.Tutorial(settings, descriptor)
            self.__tutorial.onStopped += self.__onTutorialStopped
            result = self.__tutorial.run(weakref.proxy(self.__dispatcher), runCtx)
            if not result:
                self.__tutorial.onStopped -= self.__onTutorialStopped
                self.__tutorial = None
            return result

    def __doStop(self):
        if self.__tutorial is not None:
            self.__tutorial.onStopped -= self.__onTutorialStopped
            self.__tutorial.stop()
            self.__tutorial = None
        GlobalStorage.clearFlags()
        return

    def __doStopHints(self):
        if self.__hintsManager is not None:
            self.__hintsManager.stop()
            self.__hintsManager = None
        return

    def __doClear(self):
        self.__restoreID = None
        self.__doStop()
        self.__doStopHints()
        if self.__dispatcher is not None:
            self.__dispatcher.stop()
            self.__dispatcher = None
        return

    def __doRestore(self):
        if self.__restoreID is not None:
            settingsID, self.__restoreID = self.__restoreID, None
            _logger.debug(b'Restore tutorial: %r', settingsID)
            self.run(settingsID)
        return

    def __setDispatcher(self, settings):
        if self.__dispatcher is not None:
            self.__dispatcher.stop()
            self.__dispatcher = None
        self.__dispatcher = _settings.createTutorialElement(settings)
        self.__dispatcher.start(weakref.proxy(self))
        return

    def __onTutorialStopped(self):
        self.__doRestore()
        return

    def __updateConditionalState(self, state):
        chaptersList = (b'goldTankmanCost', b'goldTankmanCostMultiplier', b'creditsTankmanCost', b'creditsTankmanCostMultiplier')
        if state[b'initialChapter'] in chaptersList:
            vehicle = g_currentVehicle.item
            everyone100 = True
            if vehicle:
                for _i, tankman in vehicle.crew:
                    if tankman is None or not tankman.isInNativeTank:
                        everyone100 = False
                        break

            if everyone100:
                state[b'initialChapter'] = b'retrainingCost'
            else:
                state[b'initialChapter'] = b'crewRetrainingCost'
        return
