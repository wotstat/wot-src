import typing
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.impl import backport
from gui.impl.gen import R
from new_year.gui.impl.new_year.history_navigation import NavigationHistory
from new_year.gui.impl.new_year.navigation import NewYearNavigation, NewYearTabCache
from new_year.ny_constants import ViewAliases
from new_year.gui.impl.new_year.sounds import NewYearSoundsManager
from gui.shared import EVENT_BUS_SCOPE, g_eventBus
from gui.shared.vignette_settings_switcher import checkVignetteSettings
from helpers import dependency
from new_year.gui.shared.events import NewYearEvent
from new_year.ny_constants import InternalViewState
from skeletons.gui.shared import IItemsCache
from new_year.skeletons.new_year import INewYearController
if typing.TYPE_CHECKING:
    from typing import Callable, Optional, Sequence, Tuple
    from Event import Event
    from frameworks.wulf import View
    from cgf_components.view_camera_sync import IViewCameraSync

class SubModelPresenter(object):
    __slots__ = (b'__viewModel', b'__isLoaded', b'__parentView', b'__soundsManager')
    _INTERNAL_VIEW_STATE = InternalViewState.DEFAULT

    def __init__(self, viewModel, parentView, soundConfig=None):
        super(SubModelPresenter, self).__init__()
        self.__parentView = parentView
        self.__viewModel = viewModel
        self.__isLoaded = False
        self.__soundsManager = NewYearSoundsManager({} if soundConfig is None else soundConfig)
        return

    @property
    def isLoaded(self):
        return self.__isLoaded

    @property
    def parentView(self):
        return self.__parentView

    @property
    def skipCameraFlightOnInit(self):
        return False

    @property
    def skipCameraFlightOnClose(self):
        return True

    def setInternalViewState(self, state, skipFlight=None):
        self.parentView.setInternalViewState(state, skipFlight)
        return

    def setSwitchState(self, state):
        self.__parentView.viewModel.setSwitchState(state)
        return

    def getViewModel(self):
        return self.__viewModel

    def getParentWindow(self):
        return self.parentView.getParentWindow()

    def initialize(self, *args, **kwargs):
        self.__soundsManager.onEnterView()
        self.__subscribe()
        if self._INTERNAL_VIEW_STATE is not None:
            self.setInternalViewState(self._INTERNAL_VIEW_STATE, kwargs.get(b'skipFlight', None))
        self.__isLoaded = True
        return

    def finalize(self):
        self.__isLoaded = False
        self.__unsubscribe()
        self.__soundsManager.onExitView()
        return

    def switchFinalize(self):
        self.__isLoaded = False
        self.__soundsManager.onExitView()
        return

    def clear(self):
        self.__viewModel = None
        self.__parentView = None
        self.__soundsManager.clear()
        return

    def createToolTip(self, event):
        return

    def createToolTipContent(self, event, ctID):
        return

    def createPopOverContent(self, event):
        return

    def createPopOver(self, event):
        return

    def setCameraState(self, cameraState):
        return

    def setCameraSubState(self, subState, cameraState):
        return

    def _getCallbacks(self):
        return ()

    def _getListeners(self):
        return ()

    def _getEvents(self):
        return ()

    def __subscribe(self):
        g_clientUpdateManager.addCallbacks(dict(self._getCallbacks()))
        for eventBusArgs in self._getListeners():
            g_eventBus.addListener(*eventBusArgs)

        for event, handler in self._getEvents():
            event += handler

        return

    def __unsubscribe(self):
        for event, handler in reversed(self._getEvents()):
            event -= handler

        for eventBusArgs in reversed(self._getListeners()):
            g_eventBus.removeListener(*eventBusArgs[:3])

        g_clientUpdateManager.removeObjectCallbacks(self)
        return


class HistorySubModelPresenter(SubModelPresenter):
    __slots__ = (b'__isPreLoaded',)
    _navigationHistory = NavigationHistory()
    _tabCache = NewYearTabCache()
    _itemsCache = dependency.descriptor(IItemsCache)
    _nyController = dependency.descriptor(INewYearController)
    _isScopeWatcher = True
    _navigationAlias = None

    def __init__(self, viewModel, parentView, soundConfig=None):
        super(HistorySubModelPresenter, self).__init__(viewModel, parentView, soundConfig)
        self.__isPreLoaded = False
        return

    def preLoad(self, *args, **kwargs):
        self.__isPreLoaded = True
        return

    def initialize(self, *args, **kwargs):
        if not self.__isPreLoaded:
            self.preLoad()
        super(HistorySubModelPresenter, self).initialize(*args, **kwargs)
        if kwargs.get(b'clearHistoryNavigation', False):
            self._navigationHistory.clear()
        if self._isScopeWatcher:
            checkVignetteSettings(b'ny_navigation')
        self._updateBackButton()
        return

    def finalize(self):
        if self._isScopeWatcher:
            self._navigationHistory.invalidateViewState(self._getNavigationAlias())
        self.__isPreLoaded = False
        super(HistorySubModelPresenter, self).finalize()
        return

    @classmethod
    def clearNavigationHistory(cls):
        cls._navigationHistory.clear()
        return

    @classmethod
    def clearTabCache(cls):
        cls._tabCache.clear()
        return

    def addToHistoryForced(self):
        self.__preserveHistory()
        return

    @property
    def currentTab(self):
        return

    def goToAlbumView(self, tabName=None, *args, **kwargs):
        self._switchToView(ViewAliases.ALBUM_VIEW, tabName, *args, **kwargs)
        return

    def _goToRewardsView(self, tabName=None, *args, **kwargs):
        self._switchToView(ViewAliases.REWARDS_VIEW, tabName, *args, **kwargs)
        return

    def _goToByViewAlias(self, viewAlias, tabName=None, instantly=False, *args, **kwargs):
        self._switchToView(viewAlias, tabName, instantly, *args, **kwargs)
        return

    def _goToMainView(self, tabName=None, *args, **kwargs):
        self._switchToView(ViewAliases.CITY_VIEW, tabName, *args, **kwargs)
        return

    def _switchToView(self, aliasName, *args, **kwargs):
        saveHistory = kwargs.pop(b'saveHistory', False)
        popHistory = kwargs.pop(b'popHistory', False)
        if popHistory:
            self._navigationHistory.pop()
        if saveHistory:
            self.__preserveHistory()
        NewYearNavigation.switchToView(aliasName, *args, **kwargs)
        return

    def _goBack(self):
        if self._navigationHistory.isEmpty:
            return
        backPageAlias = self._navigationHistory.getLast()
        if backPageAlias:
            self._navigationHistory.setGoingBack(True)
            self._switchToView(backPageAlias, saveHistory=False, popHistory=True, **self.__getStateFromHistory())
        return

    def _getInfoForHistory(self):
        return

    def _getBackPageName(self):
        lastViewed = self._navigationHistory.getLast()
        if lastViewed:
            return R.strings.ny.backButton.dyn(lastViewed)()
        return R.invalid()

    def _updateBackButton(self):
        lastViewed = self._navigationHistory.getLast()
        if lastViewed:
            ctx = {b'isVisible': True, b'goTo': (backport.text(self._getBackPageName())), 
               b'callback': (self._goBack)}
        else:
            ctx = {b'isVisible': False}
        g_eventBus.handleEvent(NewYearEvent(NewYearEvent.UPDATE_BACK_BUTTON, ctx=ctx), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def _getNavigationAlias(self):
        return self._navigationAlias or self.__class__.__name__

    def __preserveHistory(self):
        viewInfo = self._getInfoForHistory()
        if viewInfo is not None:
            name = self._getNavigationAlias()
            self._navigationHistory.addToHistory(name, viewInfo)
        return

    def __getStateFromHistory(self):
        lastAlias = self._navigationHistory.getLast()
        stateInfo = self._navigationHistory.getState(lastAlias)
        if stateInfo is None:
            return {}
        else:
            return stateInfo
