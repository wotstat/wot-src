from copy import deepcopy
import BigWorld
from gui.prb_control.entities.listener import IGlobalListener
from helpers import dependency, aop
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.battle_session import IBattleSessionProvider
from skeletons.gui.game_control import IWhiteTigerSettingsController
from skeletons.prebattle_vehicle import IPrebattleVehicle
from skeletons.gui.game_control import IWhiteTigerController
from wt_disabled_settings import WhiteTigerDisabledSettings
from wt_settings import g_wt_config

class WtSettingsController(IWhiteTigerSettingsController, IGlobalListener):
    __settingsCore = dependency.descriptor(ISettingsCore)
    __wtController = dependency.descriptor(IWhiteTigerController)
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)
    __prebattleVehicle = dependency.descriptor(IPrebattleVehicle)
    _DAMAGE_INDICATOR_SETTINGS_FOR_BOSS = {b'damageIndicatorType': 0, 
       b'damageIndicatorCrits': 1, 
       b'damageIndicatorAllies': 1, 
       b'damageIndicatorDamageValue': 0, 
       b'damageIndicatorDynamicIndicator': 0, 
       b'damageIndicatorVehicleInfo': 0, 
       b'damageIndicatorAnimation': 0}
    _DAMAGE_INDICATOR_SETTINGS_FOR_NONBOSS = {b'damageIndicatorType': 1, 
       b'damageIndicatorCrits': 1, 
       b'damageIndicatorAllies': 1, 
       b'damageIndicatorDamageValue': 1, 
       b'damageIndicatorDynamicIndicator': 1, 
       b'damageIndicatorVehicleInfo': 1, 
       b'damageIndicatorAnimation': 1}
    _BATTLE_EVENTS_SETTINGS = {b'battleEventsEnemyBurning': 1, 
       b'battleEventsEnemyWorldCollision': 1, b'battleEventsBaseCapture': 0, b'battleEventsEnemyCriticalHit': 1, 
       b'battleEventsBaseCaptureDrop': 0, b'battleEventsReceivedDamage': 1, b'battleEventsEnemyAssistStun': 0, 
       b'battleEventsEnemyRamAttack': 1, b'battleEventsShowInBattle': 1, b'battleEventsEnemyKill': 1, 
       b'battleEventsVehicleInfo': 1, b'battleEventsEnemyHpDamage': 1, b'battleEventsEnemyDetection': 1, 
       b'battleEventsEnemyDetectionDamage': 1, b'battleEventsEnemyTrackDamage': 1, b'battleEventsBlockedDamage': 1, 
       b'battleEventsReceivedCrits': 1, b'battleEventsEventName': 1, b'battleEventsEnemyStun': 0, 
       b'battleEventsHealthAdded': 1}
    _DAMAGE_LOG_SETTINGS = {b'damageLogShowDetails': 2, 
       b'damageLogShowEventTypes': 0, b'damageLogAssistStun': 0, b'damageLogEventsPosition': 0, 
       b'damageLogAssistDamage': 1, b'damageLogBlockedDamage': 1, b'damageLogTotalDamage': 1}
    _QUESTS_PROGRESS = {b'progressViewType': 1L, b'progressViewConditions': 1L, b'showHPBar': 0, 
       b'showHPValues': 0, b'enableTierGrouping': 0, b'showHPDifference': 0}
    _COMMON_MARKER_VALUES = {b'markerBaseIcon': 0, 
       b'markerAltIcon': 1, 
       b'markerBaseLevel': 0, 
       b'markerAltLevel': 0, 
       b'markerBaseVehicleName': 1, 
       b'markerAltVehicleName': 1, 
       b'markerBasePlayerName': 1, 
       b'markerAltPlayerName': 1, 
       b'markerBaseDamage': 1, 
       b'markerAltDamage': 1}
    _MARKERS = {b'enemy': (deepcopy(_COMMON_MARKER_VALUES)), 
       b'ally': (deepcopy(_COMMON_MARKER_VALUES)), 
       b'dead': (deepcopy(_COMMON_MARKER_VALUES))}
    _MARKERS[b'enemy'].update({b'markerBaseHpIndicator': 1, 
       b'markerAltHpIndicator': 1, 
       b'markerBaseAimMarker2D': 1, 
       b'markerAltAimMarker2D': 1, 
       b'markerBaseHp': 1, 
       b'markerAltHp': 1})
    _MARKERS[b'ally'].update({b'markerBaseHpIndicator': 1, 
       b'markerAltHpIndicator': 1, 
       b'markerBaseHp': 1, 
       b'markerAltHp': 1})
    _MARKERS[b'dead'].update({b'markerBaseHpIndicator': 0, 
       b'markerAltHpIndicator': 1, 
       b'markerBaseHp': 0, 
       b'markerAltHp': 1})
    _ALL_EVENT_SETTINGS = {}
    _ALL_EVENT_SETTINGS.update(_DAMAGE_INDICATOR_SETTINGS_FOR_NONBOSS)
    _ALL_EVENT_SETTINGS.update(_BATTLE_EVENTS_SETTINGS)
    _ALL_EVENT_SETTINGS.update(_DAMAGE_LOG_SETTINGS)
    _ALL_EVENT_SETTINGS.update(_QUESTS_PROGRESS)
    _ALL_EVENT_SETTINGS.update(_MARKERS)
    _DISABLED_STORAGES = (b'damageIndicator', b'damageLog', b'battleEvents', b'questsProgress', b'battleHud', b'markers')

    def __init__(self):
        self.__userSettings = None
        self.__disabledSettings = None
        self.__weaver = None
        self.__eventSettingEnabled = False
        self.__settingsChanged = False
        return

    def init(self):
        self.__disabledSettings = WhiteTigerDisabledSettings()
        self.__weaver = aop.Weaver()
        self.__prebattleVehicle.onChanged += self.__onCurrentVehicleChanged
        return

    def fini(self):
        self.__weaver.clear()
        self.__weaver = None
        self.__disabledSettings = None
        self.__userSettings = None
        self.__eventSettingEnabled = False
        self.__settingsChanged = False
        self.__settingsCore.onSettingsReady -= self.__swapAfter
        self.__prebattleVehicle.onChanged -= self.__onCurrentVehicleChanged
        return

    @property
    def disabledSettings(self):
        return self.__disabledSettings.disabledSetting

    def onDisconnected(self):
        self.stopGlobalListening()
        if self.__weaver is not None:
            self.__weaver.clear()
        if self.__userSettings is not None:
            self.__settingsCore.unsetOverrideSettings()
            self.__settingsCore.clearStorages()
            self.__userSettings = None
        self.__eventSettingEnabled = False
        return

    def onAvatarBecomePlayer(self):
        self.stopGlobalListening()
        self.__swapSettings()
        vehicle = BigWorld.player().vehicle
        if vehicle:
            self.__applyIndicatorSettings(vehicle.typeDescriptor.type)
        return

    def onLobbyInited(self, event):
        self.__swapSettings()
        self.startGlobalListening()
        return

    def onPrbEntitySwitched(self):
        self.__swapSettings()
        return

    @property
    def __isInEvent(self):
        isActive = self.__wtController.isEventPrbActive()
        return isActive or self.__sessionProvider.arenaVisitor.gui.isWhiteTigerBattle()

    def __onCurrentVehicleChanged(self):
        vehicle = self.__prebattleVehicle.item
        if vehicle is not None:
            self.__applyIndicatorSettings(vehicle.descriptor.type)
        return

    def __applyIndicatorSettings(self, vehicleType):
        if not vehicleType or not self.__isInEvent:
            return
        vehCD = vehicleType.compactDescr
        isBoss = g_wt_config.isAnyTypeBoss(vehCD)
        settings = self._DAMAGE_INDICATOR_SETTINGS_FOR_BOSS if isBoss else self._DAMAGE_INDICATOR_SETTINGS_FOR_NONBOSS
        self.__settingsCore.applySettings(settings)
        return

    def __swapSettings(self):
        if not self.__settingsCore.isReady:
            self.__settingsCore.onSettingsReady += self.__swapAfter
            return
        if self.__isInEvent == self.__eventSettingEnabled:
            return
        if self.__isInEvent:
            self.__disable()
        else:
            self.__enable()
        return

    def __swapAfter(self):
        self.__settingsCore.onSettingsReady -= self.__swapAfter
        self.__swapSettings()
        return

    def __disable(self):
        self.__userSettings = {setting: self.__settingsCore.getSetting(setting) for setting in self._ALL_EVENT_SETTINGS}
        self.__settingsCore.setOverrideSettings(self._ALL_EVENT_SETTINGS, self._DISABLED_STORAGES)
        if self.__weaver.findPointcut(PointcutDisableSettingsControls) == -1:
            self.__weaver.weave(pointcut=PointcutDisableSettingsControls)
        self.__eventSettingEnabled = True
        return

    def __enable(self):
        if self.__weaver is not None:
            self.__weaver.clear()
        if self.__userSettings is not None:
            self.__settingsCore.unsetOverrideSettings()
            self.__settingsCore.clearStorages()
            self.__userSettings = None
        self.__eventSettingEnabled = False
        return


class PointcutDisableSettingsControls(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, b'gui.Scaleform.daapi.view.common.settings.SettingsWindow', b'SettingsWindow', b'as_setDataS', aspects=(
         _AspectDisableSettingsControls,))
        return


class _AspectDisableSettingsControls(aop.Aspect):
    __wtSettingsController = dependency.descriptor(IWhiteTigerSettingsController)

    def atCall(self, cd):
        for disableItem in self.__wtSettingsController.disabledSettings:
            self.__disableControl(cd, disableItem)

        return

    def __disableControl(self, cd, controlPath):
        page = b''
        subpage = b''
        control = b''
        if len(controlPath) == 2:
            page, control = controlPath
        elif len(controlPath) == 3:
            page, subpage, control = controlPath
        cd.self.as_disableControlS(page, control, subpage)
        return
