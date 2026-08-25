from __future__ import absolute_import
import typing
from future.utils import viewitems
import SoundGroups
from PlayerEvents import g_playerEvents
from PveHudWidgetsStateComponent import PveHudWidgetHasCtxEvent
from constants import ARENA_PERIOD
from gui.Scaleform.daapi.view.battle.pve_base.base.state_machine.events import ToStateEvent
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from helpers import dependency
from pve_battle_hud import WidgetType, getPveHudLogger
from skeletons.gui.battle_session import IBattleSessionProvider
_logger = getPveHudLogger()

class BasePveHudWidget(object):
    _sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self, widgetType, stateMachineClass, serverSettingsModel):
        super(BasePveHudWidget, self).__init__()
        self._widgetType = widgetType
        self._sounds = {}
        self._stateMachineClass = stateMachineClass
        self._serverSettingsModel = serverSettingsModel
        return

    def playSound(self, soundName):
        sound = SoundGroups.g_instance.getSound2D(soundName)
        if sound is not None:
            sound.play()
            self._sounds[soundName] = sound
        return

    def _populate(self):
        super(BasePveHudWidget, self)._populate()
        g_playerEvents.onArenaPeriodChange += self._onArenaPeriodChange
        self._addListener(PveHudWidgetHasCtxEvent.INIT_STATE, self._onInitState)
        self._addListener(PveHudWidgetHasCtxEvent.CHANGE_STATE, self._onChangeState)
        self._addListener(PveHudWidgetHasCtxEvent.UPDATE_STATE, self._onUpdateState)
        self._addListener(PveHudWidgetHasCtxEvent.RESTORE_STATE, self._onRestoreState)
        settingsCtrl = self._sessionProvider.dynamic.vseHUDSettings
        if settingsCtrl is not None:
            settingsCtrl.onItemSettingsChanged += self._onClientSettingsChanged
        return

    def _dispose(self):
        settingsCtrl = self._sessionProvider.dynamic.vseHUDSettings
        if settingsCtrl is not None:
            settingsCtrl.onItemSettingsChanged -= self._onClientSettingsChanged
        g_playerEvents.onArenaPeriodChange -= self._onArenaPeriodChange
        self._removeListener(PveHudWidgetHasCtxEvent.INIT_STATE, self._onInitState)
        self._removeListener(PveHudWidgetHasCtxEvent.CHANGE_STATE, self._onChangeState)
        self._removeListener(PveHudWidgetHasCtxEvent.UPDATE_STATE, self._onUpdateState)
        self._removeListener(PveHudWidgetHasCtxEvent.RESTORE_STATE, self._onRestoreState)
        for sound in self._sounds.values():
            sound.stop()

        self._sounds.clear()
        super(BasePveHudWidget, self)._dispose()
        return

    def _addListener(self, eventName, func):
        eventType = eventName.format(widgetType=self._widgetType.name)
        g_eventBus.addListener(eventType, func, scope=EVENT_BUS_SCOPE.BATTLE)
        return

    def _removeListener(self, eventName, func):
        eventType = eventName.format(widgetType=self._widgetType.name)
        g_eventBus.removeListener(eventType, func, scope=EVENT_BUS_SCOPE.BATTLE)
        return

    def _onArenaPeriodChange(self, period, *_):
        if period == ARENA_PERIOD.AFTERBATTLE:
            self._onAfterBattlePeriod()
        elif period == ARENA_PERIOD.PREBATTLE:
            self._onPrebattlePeriod()
        return

    def _onPrebattlePeriod(self):
        return

    def _onAfterBattlePeriod(self):
        return

    def _onClientSettingsChanged(self, widgetType, widgetId):
        widgetKey = (
         widgetType, widgetId)
        serverSettings, clientSettings = self.getSettings(widgetKey)
        if serverSettings is None:
            return
        else:
            if widgetType == serverSettings.type and widgetId == serverSettings.id:
                isRestoring = clientSettings is None
                _logger.debug(b'onClientSettingsChanged: isRestoring=%s, server=%s, client=%s', isRestoring, serverSettings, clientSettings)
                if isRestoring:
                    clientSettings = self._getClientSettings(widgetKey)
                    self._setSettings(serverSettings, clientSettings)
                    self._restoreState(serverSettings)
                else:
                    self._changeState(serverSettings)
            return

    def _onInitState(self, event):
        serverSettings, clientSettings = self._updateSettings(event.ctx)
        _logger.debug(b'onInitState: server=%s, client=%s', serverSettings, clientSettings)
        if clientSettings is not None:
            self._initState(serverSettings)
        return

    def _onRestoreState(self, event):
        serverSettings, clientSettings = self._updateSettings(event.ctx)
        _logger.debug(b'onRestoreState: server=%s, client=%s', serverSettings, clientSettings)
        if clientSettings is not None:
            self._restoreState(serverSettings)
        return

    def _onChangeState(self, event):
        serverSettings, clientSettings = self._updateSettings(event.ctx)
        _logger.debug(b'onChangeState: server=%s, client=%s', serverSettings, clientSettings)
        self._changeState(serverSettings)
        return

    def _onUpdateState(self, event):
        serverSettings, clientSettings = self._updateSettings(event.ctx)
        _logger.debug(b'onUpdateState: server=%s, client=%s', serverSettings, clientSettings)
        self._updateState(serverSettings)
        return

    def _initState(self, serverSettings):
        widgetKey = (serverSettings.type, serverSettings.id)
        machine = self._getStateMachine(widgetKey)
        if machine is not None:
            if machine.isRunning():
                machine.postFinalState()
            machine.stop()
        else:
            machine = self._stateMachineClass()
            self._setStateMachine(widgetKey, machine)
        machine.configure(self, serverSettings.type, serverSettings.id)
        machine.start()
        machine.post(ToStateEvent(serverSettings.state.name))
        return

    def _restoreState(self, serverSettings):
        stateToRestore = self._getStateToRestore(serverSettings)
        if stateToRestore is not None:
            serverSettings.state = stateToRestore
            self._initState(serverSettings)
        return

    def _changeState(self, serverSettings):
        widgetKey = (
         serverSettings.type, serverSettings.id)
        machine = self._getStateMachine(widgetKey)
        if machine is None:
            _logger.debug(b'Cannot change state: serverSettings=%s', serverSettings)
            return
        else:
            machine.post(ToStateEvent(serverSettings.state.name))
            return

    def _updateState(self, serverSettings):
        widgetKey = (
         serverSettings.type, serverSettings.id)
        machine = self._getStateMachine(widgetKey)
        if machine is None:
            _logger.debug(b'Cannot update state: serverSettings=%s', serverSettings)
            return
        else:
            machine.update()
            return

    def _getStateToRestore(self, serverSettings):
        return serverSettings.state

    def _updateSettings(self, serverSettings):
        widgetKey = (
         serverSettings[b'type'], serverSettings[b'id'])
        serverSettings = self._getServerSettings(serverSettings)
        clientSettings = self._getClientSettings(widgetKey)
        self._setSettings(serverSettings, clientSettings)
        return (serverSettings, clientSettings)

    def _getServerSettings(self, serverSettings):
        return self._serverSettingsModel(**serverSettings)

    def _getClientSettings(self, widgetKey):
        widgetType, widgetId = widgetKey
        settingsCtrl = self._sessionProvider.dynamic.vseHUDSettings
        if settingsCtrl is None:
            _logger.error(b'VseHUDSettings controller not set.')
            return
        else:
            settings = settingsCtrl.getItemSettings(settingsID=widgetType, itemID=widgetId)
            if settings is None:
                _logger.debug(b'No settings for widgetType=%s, widgetId=%s', widgetType, widgetId)
                return
            return settings

    def _getStateMachine(self, widgetKey):
        raise NotImplementedError
        return

    def _setStateMachine(self, _, stateMachine):
        raise NotImplementedError
        return

    def getSettings(self, widgetKey):
        raise NotImplementedError
        return

    def _setSettings(self, serverSettings, clientSettings):
        raise NotImplementedError
        return


class SingleItemPveHudWidget(BasePveHudWidget):

    def __init__(self, widgetType, stateMachineClass, serverSettingsModel):
        super(SingleItemPveHudWidget, self).__init__(widgetType, stateMachineClass, serverSettingsModel)
        self._stateMachine = None
        self._settings = (None, None)
        return

    def _dispose(self):
        if self._stateMachine is not None:
            self._stateMachine.stop()
        self._stateMachine = None
        self._settings = None
        super(SingleItemPveHudWidget, self)._dispose()
        return

    def _onAfterBattlePeriod(self):
        if self._stateMachine is not None:
            self._stateMachine.postFinalState()
        return

    def _getStateMachine(self, _):
        return self._stateMachine

    def _setStateMachine(self, _, stateMachine):
        self._stateMachine = stateMachine
        return

    def getSettings(self, _):
        return self._settings

    def _setSettings(self, serverSettings, clientSettings):
        self._settings = (
         serverSettings, clientSettings)
        return


class SeveralItemsPveHudWidget(BasePveHudWidget):
    MAX_ITEMS_COUNT = None

    def __init__(self, widgetType, stateMachineClass, serverSettingsModel):
        super(SeveralItemsPveHudWidget, self).__init__(widgetType, stateMachineClass, serverSettingsModel)
        self._stateMachines = {}
        self._settings = {}
        return

    def _dispose(self):
        for machine in self._stateMachines.values():
            machine.stop()

        self._stateMachines.clear()
        self._settings.clear()
        super(SeveralItemsPveHudWidget, self)._dispose()
        return

    def _onInitState(self, event):
        if self.MAX_ITEMS_COUNT is not None:
            serverSettings = self._getServerSettings(event.ctx)
            widgetKey = (serverSettings.type, serverSettings.id)
            activeItems = self._getActiveItems() - {widgetKey}
            if len(activeItems) >= self.MAX_ITEMS_COUNT:
                _logger.error(b'New item=<%s> cannot be added. Maximum number of items has been reached. activeItems=%s.', widgetKey, activeItems)
                return
        super(SeveralItemsPveHudWidget, self)._onInitState(event)
        return

    def _getActiveItems(self):
        return {key for key, machine in viewitems(self._stateMachines) if machine.isRunning()}

    def _onAfterBattlePeriod(self):
        for machine in self._stateMachines.values():
            machine.postFinalState()

        return

    def _getStateMachine(self, widgetKey):
        return self._stateMachines.get(widgetKey)

    def _setStateMachine(self, widgetKey, stateMachine):
        self._stateMachines[widgetKey] = stateMachine
        return

    def getSettings(self, widgetKey):
        serverSettings, clientSettings = self._settings.get(widgetKey, (None, None))
        return (serverSettings, clientSettings)

    def _setSettings(self, serverSettings, clientSettings):
        widgetKey = (
         serverSettings.type, serverSettings.id)
        self._settings[widgetKey] = (serverSettings, clientSettings)
        return
