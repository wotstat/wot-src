import typing, BattleReplay, BigWorld, SoundGroups
from Event import EventsSubscriber
from gui.battle_control.battle_constants import BATTLE_CTRL_ID
from gui.battle_control.controllers.interfaces import IBattleController
from helpers import dependency, isPlayerAvatar
from skeletons.gui.battle_session import IBattleSessionProvider
from shared_utils import nextTick
from vehicle_systems.tankStructure import TankSoundObjectsIndexes

class SoundObjectStub(object):

    def play(self, *_, **__):
        return

    def setRTPC(self, *_, **__):
        return


SOUND_OBJECT_STUB = SoundObjectStub()

def getGunSoundObject(vehicle):
    if vehicle.appearance is not None and vehicle.appearance.engineAudition is not None:
        soundObject = vehicle.appearance.engineAudition.getSoundObject(TankSoundObjectsIndexes.GUN)
        if soundObject is not None:
            return soundObject
        return SOUND_OBJECT_STUB
    return SOUND_OBJECT_STUB


class SoundPlayersController(object):

    def __init__(self):
        self._soundPlayers = set()
        return

    def init(self):
        for player in self._soundPlayers:
            player.init()

        return

    def destroy(self):
        for player in self._soundPlayers:
            player.destroy()

        self._soundPlayers = None
        return


class SoundPlayersBattleController(IBattleController):

    def __init__(self):
        self.__soundPlayers = self._initializeSoundPlayers()
        return

    def startControl(self, *args):
        self.__startPlayers()
        return

    def stopControl(self):
        self.__destroyPlayers()
        return

    def getControllerID(self):
        return BATTLE_CTRL_ID.SOUND_PLAYERS_CTRL

    def _initializeSoundPlayers(self):
        raise NotImplementedError
        return

    def __startPlayers(self):
        for player in self.__soundPlayers:
            player.init()

        return

    def __destroyPlayers(self):
        for player in self.__soundPlayers:
            player.destroy()

        self.__soundPlayers = None
        return


class SoundPlayer(object):

    def init(self):
        nextTick(self._subscribe)()
        return

    def destroy(self):
        self._unsubscribe()
        return

    def _subscribe(self):
        raise NotImplementedError
        return

    def _unsubscribe(self):
        raise NotImplementedError
        return

    @staticmethod
    def _playSound2D(event, checkAlive=False):
        if BattleReplay.g_replayCtrl.isTimeWarpInProgress:
            return
        else:
            if checkAlive:
                vehicle = BigWorld.player().getVehicleAttached()
                if vehicle is not None and not vehicle.isAlive():
                    return
            SoundGroups.g_instance.playSound2D(event)
            return


class VehicleStateSoundPlayer(SoundPlayer):
    _sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def _subscribe(self):
        ctrl = self._sessionProvider.shared.vehicleState
        ctrl.onVehicleStateUpdated += self._onVehicleStateUpdated
        BigWorld.player().onSwitchingViewPoint += self._onSwitchViewPoint
        return

    def _unsubscribe(self):
        ctrl = self._sessionProvider.shared.vehicleState
        if ctrl is not None:
            ctrl.onVehicleStateUpdated -= self._onVehicleStateUpdated
        if isPlayerAvatar():
            BigWorld.player().onSwitchingViewPoint -= self._onSwitchViewPoint
        return

    def _onVehicleStateUpdated(self, state, value):
        return

    def _onSwitchViewPoint(self):
        return


class BaseEfficiencySoundPlayer(SoundPlayer):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def _subscribe(self):
        ctrl = self.__sessionProvider.shared.personalEfficiencyCtrl
        ctrl.onPersonalEfficiencyReceived += self._onEfficiencyReceived
        return

    def _unsubscribe(self):
        ctrl = self.__sessionProvider.shared.personalEfficiencyCtrl
        if ctrl is not None:
            ctrl.onPersonalEfficiencyReceived -= self._onEfficiencyReceived
        return

    def _onEfficiencyReceived(self, events):
        return


class EquipmentComponentSoundPlayer(object):
    __slots__ = (b'__eventsSubscriber',)
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        self.__eventsSubscriber = None
        return

    def init(self):
        self.__eventsSubscriber = EventsSubscriber()
        self.__eventsSubscriber.subscribeToContextEvent(self.__sessionProvider.shared.vehicleState.onEquipmentComponentUpdated, self._onEquipmentComponentUpdated, self._getEquipmentName())
        self.__eventsSubscriber.subscribeToEvent(self.__sessionProvider.shared.vehicleState.onVehicleControlling, self.__onVehicleControlling)
        return

    def destroy(self):
        self.__eventsSubscriber.unsubscribeFromAllEvents()
        self.__eventsSubscriber = None
        return

    def _onEquipmentComponentUpdated(self, equipmentName, vehicleID, equipmentInfo):
        raise NotImplementedError
        return

    def _getEquipmentName(self):
        raise NotImplementedError
        return

    def _stopSounds(self):
        raise NotImplementedError
        return

    def _getComponentName(self):
        raise NotImplementedError
        return

    def __onVehicleControlling(self, vehicle):
        self._stopSounds()
        component = vehicle.dynamicComponents.get(self._getComponentName())
        if component is not None:
            self._onEquipmentComponentUpdated(component.EQUIPMENT_NAME, vehicle.id, component.getInfo())
        return
