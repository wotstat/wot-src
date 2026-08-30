from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from cosmic_event.gui.impl.gen.view_models.views.battle.cosmic_hud.ability_model import AbilityModel
from cosmic_event.gui.impl.gen.view_models.views.battle.cosmic_hud.cosmic_progress_bar import CosmicProgressBar
from cosmic_event.gui.impl.gen.view_models.views.battle.cosmic_hud.direction_marker_model import DirectionMarkerModel
from cosmic_event.gui.impl.gen.view_models.views.battle.cosmic_hud.loot_marker_model import LootMarkerModel
from cosmic_event.gui.impl.gen.view_models.views.battle.cosmic_hud.marker_model import MarkerModel
from cosmic_event.gui.impl.gen.view_models.views.battle.cosmic_hud.player_record_model import PlayerRecordModel
from cosmic_event.gui.impl.gen.view_models.views.battle.cosmic_hud.super_loot_scanning import SuperLootScanning
from cosmic_event.gui.impl.gen.view_models.views.battle.cosmic_hud.vehicle_marker_model import VehicleMarkerModel
from cosmic_event.gui.impl.gen.view_models.views.lobby.cosmic_lobby_view.scoring_model import ScoringModel

class AnnouncementTypeEnum(Enum):
    NONE = b'none'
    AWAITINGPLAYERS = b'awaiting_players'
    CUSTOM = b'custom'
    PREBATTLE = b'pre_battle'
    STARTBATTLE = b'start_battle'
    PICKUPS = b'pickups'
    RESPAWN = b'respawn'
    PREPARETOSCAN = b'prepare_to_scan'
    SCANAVAILABLE = b'scan_available'
    PREPARETOSCANFINAL = b'prepare_to_scan_final'
    FINALSCANAVAILABLE = b'final_scan_available'
    SCANNING = b'scanning'
    MISSIONCOMPLETED = b'mission_completed'
    PREPARETOLOOTPICKUP = b'prepare_to_loot_pickup'


class ArenaPhaseEnum(Enum):
    PREBATTLE = b'pre_battle'
    PHASE1 = b'phase_1'
    PHASE2 = b'phase_2'


class CosmicHudViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=25, commands=0):
        super(CosmicHudViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def crosshair(self):
        return self._getViewModel(0)

    @staticmethod
    def getCrosshairType():
        return MarkerModel

    @property
    def aim(self):
        return self._getViewModel(1)

    @staticmethod
    def getAimType():
        return MarkerModel

    @property
    def lootMarker(self):
        return self._getViewModel(2)

    @staticmethod
    def getLootMarkerType():
        return LootMarkerModel

    @property
    def superLootScanning(self):
        return self._getViewModel(3)

    @staticmethod
    def getSuperLootScanningType():
        return SuperLootScanning

    def getVehicleMarkers(self):
        return self._getArray(4)

    def setVehicleMarkers(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getVehicleMarkersType():
        return VehicleMarkerModel

    def getPoiMarkers(self):
        return self._getArray(5)

    def setPoiMarkers(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getPoiMarkersType():
        return DirectionMarkerModel

    def getProgressBars(self):
        return self._getArray(6)

    def setProgressBars(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getProgressBarsType():
        return CosmicProgressBar

    def getArenaTimeLeft(self):
        return self._getReal(7)

    def setArenaTimeLeft(self, value):
        self._setReal(7, value)
        return

    def getArenaPhase(self):
        return ArenaPhaseEnum(self._getString(8))

    def setArenaPhase(self, value):
        self._setString(8, value.value)
        return

    def getReloadTimeLeft(self):
        return self._getReal(9)

    def setReloadTimeLeft(self, value):
        self._setReal(9, value)
        return

    def getReloadTime(self):
        return self._getReal(10)

    def setReloadTime(self, value):
        self._setReal(10, value)
        return

    def getAnnouncementType(self):
        return AnnouncementTypeEnum(self._getString(11))

    def setAnnouncementType(self, value):
        self._setString(11, value.value)
        return

    def getAnnouncementSecondsToEvent(self):
        return self._getNumber(12)

    def setAnnouncementSecondsToEvent(self, value):
        self._setNumber(12, value)
        return

    def getAnnouncementCustomTitle(self):
        return self._getString(13)

    def setAnnouncementCustomTitle(self, value):
        self._setString(13, value)
        return

    def getAnnouncementCustomSubtitle(self):
        return self._getString(14)

    def setAnnouncementCustomSubtitle(self, value):
        self._setString(14, value)
        return

    def getPlayerName(self):
        return self._getString(15)

    def setPlayerName(self, value):
        self._setString(15, value)
        return

    def getPlayerList(self):
        return self._getArray(16)

    def setPlayerList(self, value):
        self._setArray(16, value)
        return

    @staticmethod
    def getPlayerListType():
        return PlayerRecordModel

    def getMessages(self):
        return self._getArray(17)

    def setMessages(self, value):
        self._setArray(17, value)
        return

    @staticmethod
    def getMessagesType():
        return ScoringModel

    def getAbilities(self):
        return self._getArray(18)

    def setAbilities(self, value):
        self._setArray(18, value)
        return

    @staticmethod
    def getAbilitiesType():
        return AbilityModel

    def getIsRespawning(self):
        return self._getBool(19)

    def setIsRespawning(self, value):
        self._setBool(19, value)
        return

    def getShowLootMarker(self):
        return self._getBool(20)

    def setShowLootMarker(self, value):
        self._setBool(20, value)
        return

    def getIsTargeting(self):
        return self._getBool(21)

    def setIsTargeting(self, value):
        self._setBool(21, value)
        return

    def getAbilityDuration(self):
        return self._getNumber(22)

    def setAbilityDuration(self, value):
        self._setNumber(22, value)
        return

    def getVehicleOverturned(self):
        return self._getBool(23)

    def setVehicleOverturned(self, value):
        self._setBool(23, value)
        return

    def getSelectedVehicleID(self):
        return self._getNumber(24)

    def setSelectedVehicleID(self, value):
        self._setNumber(24, value)
        return

    def _initialize(self):
        super(CosmicHudViewModel, self)._initialize()
        self._addViewModelProperty(b'crosshair', MarkerModel())
        self._addViewModelProperty(b'aim', MarkerModel())
        self._addViewModelProperty(b'lootMarker', LootMarkerModel())
        self._addViewModelProperty(b'superLootScanning', SuperLootScanning())
        self._addArrayProperty(b'vehicleMarkers', Array())
        self._addArrayProperty(b'poiMarkers', Array())
        self._addArrayProperty(b'progressBars', Array())
        self._addRealProperty(b'arenaTimeLeft', 0.0)
        self._addStringProperty(b'arenaPhase', ArenaPhaseEnum.PREBATTLE.value)
        self._addRealProperty(b'reloadTimeLeft', 0.0)
        self._addRealProperty(b'reloadTime', 0.0)
        self._addStringProperty(b'announcementType', AnnouncementTypeEnum.NONE.value)
        self._addNumberProperty(b'announcementSecondsToEvent', -1)
        self._addStringProperty(b'announcementCustomTitle', b'')
        self._addStringProperty(b'announcementCustomSubtitle', b'')
        self._addStringProperty(b'playerName', b'')
        self._addArrayProperty(b'playerList', Array())
        self._addArrayProperty(b'messages', Array())
        self._addArrayProperty(b'abilities', Array())
        self._addBoolProperty(b'isRespawning', False)
        self._addBoolProperty(b'showLootMarker', False)
        self._addBoolProperty(b'isTargeting', False)
        self._addNumberProperty(b'abilityDuration', 0)
        self._addBoolProperty(b'vehicleOverturned', False)
        self._addNumberProperty(b'selectedVehicleID', 0)
        return
