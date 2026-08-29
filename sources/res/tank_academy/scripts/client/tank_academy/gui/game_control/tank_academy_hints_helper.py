import BigWorld
from PlayerEvents import g_playerEvents
from account_helpers.settings_core.settings_constants import OnceOnlyHints
from constants import QUEUE_TYPE, ARENA_BONUS_TYPE, IS_DEVELOPMENT
from gui.Scaleform.daapi.view.lobby.header import battle_selector_items
from gui.Scaleform.genConsts.TUTORIAL_TRIGGER_TYPES import TUTORIAL_TRIGGER_TYPES
from gui.impl import backport
from gui.impl.gen import R
from gui.prb_control.entities.listener import IGlobalListener
from gui.prb_control.settings import FUNCTIONAL_FLAG
from gui.shared import g_eventBus, events, EVENT_BUS_SCOPE
from gui.shared.events import TutorialEvent
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCache
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.game_control import ITankAcademyController
from skeletons.gui.server_events import IEventsCache
from skeletons.gui.shared import IItemsCache
from skeletons.tutorial import ITutorialLoader

class TankAcademyHintsHelper(object):
    __settingsCache = dependency.descriptor(ISettingsCache)
    __slots__ = (b'__hints', b'__hasHintListeners', b'__tankAcademyController')

    def __init__(self, controller):
        super(TankAcademyHintsHelper, self).__init__()
        self.__hasHintListeners = False
        self.__tankAcademyController = controller
        self.__hints = self.__getDefaultHints()
        self.__addHintsListeners()
        g_playerEvents.onDisconnected += self.__onDisconnected
        return

    def fini(self):
        self.__removeHintsListeners()
        g_playerEvents.onDisconnected -= self.__onDisconnected
        self.__tankAcademyController = None
        self.__stopHints()
        return

    @staticmethod
    def __getDefaultHints():
        return (EntryPointHint(), FightBtnMultiShowHint())

    def __addHintsListeners(self):
        self.__hasHintListeners = True
        g_playerEvents.onAccountBecomeNonPlayer += self.__onAccountBecomeNonPlayer
        g_playerEvents.onAccountBecomePlayer += self.__onAccountBecomePlayer
        return

    def __removeHintsListeners(self):
        g_playerEvents.onAccountBecomeNonPlayer -= self.__onAccountBecomeNonPlayer
        g_playerEvents.onAccountBecomePlayer -= self.__onAccountBecomePlayer
        self.__tankAcademyController.onStateChanged -= self.__onStateChanged
        self.__settingsCache.onSyncCompleted -= self.__onSettingsSyncCompleted
        self.__hasHintListeners = False
        return

    def __onAccountBecomePlayer(self):
        self.__tankAcademyController.onStateChanged += self.__onStateChanged
        self.__settingsCache.onSyncCompleted += self.__onSettingsSyncCompleted
        self.__startHints()
        return

    def __onDisconnected(self):
        self.__hints = self.__getDefaultHints()
        if not self.__hasHintListeners:
            self.__addHintsListeners()
        return

    def __onAccountBecomeNonPlayer(self):
        self.__stopHints()
        self.__tankAcademyController.onStateChanged -= self.__onStateChanged
        self.__settingsCache.onSyncCompleted -= self.__onSettingsSyncCompleted
        return

    def __onSettingsSyncCompleted(self):
        self.__checkHints()
        return

    def __checkHints(self):
        availableHints = []
        for hint in self.__hints:
            if hint.isShown() and not hint.canBeShownInFuture():
                hint.stop()
            else:
                availableHints.append(hint)

        self.__hints = availableHints
        if self.__hints:
            self.__startHints()
        else:
            self.__removeHintsListeners()
        return

    def __startHints(self):
        if self.__tankAcademyController.isActive():
            for hint in self.__hints:
                hint.start()

        return

    def __stopHints(self):
        for hint in self.__hints:
            hint.stop()

        return

    def __onStateChanged(self):
        if self.__tankAcademyController.isActive():
            self.__startHints()
        else:
            self.__stopHints()
        return


class _TAManualTriggeredHint(object):
    _eventsCache = dependency.descriptor(IEventsCache)
    _tankAcademyController = dependency.descriptor(ITankAcademyController)
    _settingsCore = dependency.descriptor(ISettingsCore)
    _tutorialLoader = dependency.descriptor(ITutorialLoader)
    _HINT_NAME = None
    _CONTROL_NAME = None
    __slots__ = (b'_isStarted', b'_tankAcademyController', b'_isHintVisible', b'_controlOnScene', b'_controlIsEnabled')

    def __init__(self):
        super(_TAManualTriggeredHint, self).__init__()
        self._isStarted = False
        self._isHintVisible = False
        self._controlOnScene = False
        self._controlIsEnabled = False
        return

    def getName(self):
        return self._CONTROL_NAME

    def isShown(self):
        return bool(self._settingsCore.serverSettings.getOnceOnlyHintsSetting(self._HINT_NAME, default=False))

    def start(self):
        if not self._isStarted and self.canBeShownInFuture():
            self._controlOnScene = self.__checkControlOnScene()
            if self._controlOnScene:
                self.__setTriggers()
            self.__addTutorialListeners()
            self._eventsCache.onSyncCompleted += self._onEventsCacheSyncCompleted
            self._onStart()
        return

    def stop(self):
        if self._isStarted:
            self.__removeTutorialListeners()
            self._eventsCache.onSyncCompleted -= self._onEventsCacheSyncCompleted
            self._onStop()
            self._isHintVisible = False
        return

    def canBeShownInFuture(self):
        return not self.isShown()

    def _getHintSettings(self):
        return {}

    def _onStart(self):
        self._isStarted = True
        return

    def _onStop(self):
        self._isStarted = False
        return

    def _onEventsCacheSyncCompleted(self):
        raise NotImplementedError
        return

    def _isReadyToShow(self):
        return self._controlOnScene and self._controlIsEnabled

    def _show(self):
        if not self._isHintVisible:
            self._isHintVisible = self._tutorialLoader.gui.showInteractiveHint(self._CONTROL_NAME, self._getHintSettings(), [], False)
            if self._isHintVisible:
                g_eventBus.handleEvent(TutorialEvent(TutorialEvent.IMPORTANT_HINT_SHOWING, state=True), scope=EVENT_BUS_SCOPE.GLOBAL)
        return

    def _hide(self):
        if self._isHintVisible:
            self._tutorialLoader.gui.closeInteractiveHint(self._CONTROL_NAME)
            g_eventBus.handleEvent(TutorialEvent(TutorialEvent.IMPORTANT_HINT_SHOWING, state=False), scope=EVENT_BUS_SCOPE.GLOBAL)
        self._isHintVisible = False
        return

    def _checkControlConditions(self, componentIsEnabled):
        return

    def _onItemFound(self, event):
        if event.targetID == self._CONTROL_NAME:
            self._controlOnScene = True
            self.__setTriggers()
        return

    def _onItemLost(self, event):
        if event.targetID == self._CONTROL_NAME:
            self._controlOnScene = False
            self._isHintVisible = False
        return

    def _onTriggerActivated(self, event):
        if event.targetID == self._CONTROL_NAME:
            self._controlIsEnabled = event.componentState
            self._checkControlConditions(self._controlIsEnabled)
        return

    def _getTutorialTriggers(self):
        return (
         TUTORIAL_TRIGGER_TYPES.ENABLED_CHANGE,)

    def __setTriggers(self):
        triggers = self._getTutorialTriggers()
        if triggers:
            self._tutorialLoader.gui.setTriggers(self._CONTROL_NAME, triggers)
        return

    def __checkControlOnScene(self):
        return self._CONTROL_NAME in self._tutorialLoader.gui.getFoundComponentsIDs()

    def __addTutorialListeners(self):
        addListener = g_eventBus.addListener
        addListener(events.TutorialEvent.ON_COMPONENT_FOUND, self._onItemFound, scope=EVENT_BUS_SCOPE.GLOBAL)
        addListener(events.TutorialEvent.ON_COMPONENT_LOST, self._onItemLost, scope=EVENT_BUS_SCOPE.GLOBAL)
        if self._getTutorialTriggers():
            addListener(events.TutorialEvent.ON_TRIGGER_ACTIVATED, self._onTriggerActivated, scope=EVENT_BUS_SCOPE.GLOBAL)
        return

    def __removeTutorialListeners(self):
        removeListener = g_eventBus.removeListener
        removeListener(events.TutorialEvent.ON_COMPONENT_FOUND, self._onItemFound, scope=EVENT_BUS_SCOPE.GLOBAL)
        removeListener(events.TutorialEvent.ON_COMPONENT_LOST, self._onItemLost, scope=EVENT_BUS_SCOPE.GLOBAL)
        if self._getTutorialTriggers():
            removeListener(events.TutorialEvent.ON_TRIGGER_ACTIVATED, self._onTriggerActivated, scope=EVENT_BUS_SCOPE.GLOBAL)
        return


class FightBtnMultiShowHint(_TAManualTriggeredHint, IGlobalListener):
    _CONTROL_NAME = b'FightButton'
    _HINT_NAME = OnceOnlyHints.TANK_ACADEMY_FIGHT_BUTTON_HINT
    __slots__ = (b'__waitingBattle',)

    def __init__(self):
        super(FightBtnMultiShowHint, self).__init__()
        self.__waitingBattle = False
        return

    def onPrbEntitySwitched(self):
        self.__waitingBattle = self.prbEntity.getQueueType() == QUEUE_TYPE.RANDOMS or self.__isDevBattle()
        if self.__waitingBattle:
            g_playerEvents.onAvatarBecomePlayer += self.__onAvatarBecomePlayer
        else:
            g_playerEvents.onAvatarBecomePlayer -= self.__onAvatarBecomePlayer
        self.__checkFightBtnHint()
        return

    def canBeShownInFuture(self):
        return super(FightBtnMultiShowHint, self).canBeShownInFuture() and not self._tankAcademyController.isFirstQuestCompleted()

    def _getHintSettings(self):
        return {b'updateRuntime': True}

    def _onStart(self):
        super(FightBtnMultiShowHint, self)._onStart()
        self.__waitingBattle = False
        if self.canBeShownInFuture():
            if self.prbDispatcher is None:
                g_playerEvents.onPrbDispatcherCreated += self.__onPrbDispatcherCreated
            else:
                self.startGlobalListening()
            if self._controlOnScene:
                self._controlIsEnabled = self.__isReadyToFightInRandom()
                self.__checkFightBtnHint()
        return

    def _onStop(self):
        super(FightBtnMultiShowHint, self)._onStop()
        if not self.__waitingBattle:
            g_playerEvents.onAvatarBecomePlayer -= self.__onAvatarBecomePlayer
        self.stopGlobalListening()
        g_playerEvents.onPrbDispatcherCreated -= self.__onPrbDispatcherCreated
        self._hide()
        self.__resetTriggers()
        return

    def _checkControlConditions(self, componentIsEnabled):
        self.__checkFightBtnHint()
        return

    def _onEventsCacheSyncCompleted(self):
        self.__checkFightBtnHint()
        return

    def _isReadyToShow(self):
        return super(FightBtnMultiShowHint, self)._isReadyToShow() and self.canBeShownInFuture() and self.__isReadyToFightInRandom()

    def __isDevBattle(self):
        return IS_DEVELOPMENT and self.prbEntity.getModeFlags() == FUNCTIONAL_FLAG.TRAINING

    def __resetTriggers(self):
        self._tutorialLoader.gui.setTriggers(self._CONTROL_NAME, [])
        return

    def __onAvatarBecomePlayer(self):
        if BigWorld.player().arenaBonusType in ARENA_BONUS_TYPE.RANDOM_RANGE:
            self._settingsCore.serverSettings.setOnceOnlyHintsSettings({(self._HINT_NAME): True})
        self.__waitingBattle = False
        g_playerEvents.onAvatarBecomePlayer -= self.__onAvatarBecomePlayer
        return

    def __onPrbDispatcherCreated(self):
        self.startGlobalListening()
        return

    def __checkFightBtnHint(self):
        if self._isReadyToShow():
            self._show()
        elif self.canBeShownInFuture():
            self._hide()
        else:
            self.stop()
        return

    def __isReadyToFightInRandom(self):
        prbEntity = self.prbEntity
        if prbEntity is not None:
            isRandom = prbEntity and prbEntity.getEntityFlags() != FUNCTIONAL_FLAG.UNDEFINED and prbEntity.getQueueType() == QUEUE_TYPE.RANDOMS
            prbDispatcher = self.prbDispatcher
            if isRandom and prbDispatcher is not None:
                items = battle_selector_items.getItems()
                selected = items.update(prbDispatcher.getFunctionalState())
                return prbEntity.canPlayerDoAction().isValid and not selected.isLocked()
        else:
            return False
        return


class EntryPointHint(_TAManualTriggeredHint):
    __itemsCache = dependency.descriptor(IItemsCache)
    _CONTROL_NAME = b'TankAcademyEntryPoint'
    _HINT_NAME = OnceOnlyHints.TANK_ACADEMY_ENTRY_POINT_HINT
    __slots__ = ()

    def _getHintSettings(self):
        return {b'updateRuntime': True, 
           b'hintText': (backport.text(self.__getHintText())), 
           b'hasArrow': True, 
           b'arrowDir': b'B', 
           b'arrowLoop': True, 
           b'positionValue': 0.5}

    def _onStart(self):
        super(EntryPointHint, self)._onStart()
        self.__checkHint()
        return

    def _onStop(self):
        super(EntryPointHint, self)._onStop()
        self._hide()
        return

    def _onEventsCacheSyncCompleted(self):
        self.__checkHint()
        return

    def _isReadyToShow(self):
        result = False
        if self._controlOnScene and not self._eventsCache.waitForSync and not self._tutorialLoader.isRunning:
            result = self._tankAcademyController.getCompletedTankAcademyQuestsCount() >= 1 and not self.isShown()
        return result

    def _onItemFound(self, event):
        super(EntryPointHint, self)._onItemFound(event)
        if event.targetID == self._CONTROL_NAME:
            self.__checkHint()
        return

    def _onItemLost(self, event):
        if event.targetID == self._CONTROL_NAME:
            self._hide()
        super(EntryPointHint, self)._onItemLost(event)
        return

    def _getTutorialTriggers(self):
        return []

    def __checkHint(self):
        if self._isReadyToShow():
            self._show()
        return

    def __getHintText(self):
        if self._settingsCore.serverSettings.isTankAcademyWelcomeScreenShown():
            return R.strings.tank_academy.entryPoint.hint.quests()
        return R.strings.tank_academy.entryPoint.hint.rewards()
