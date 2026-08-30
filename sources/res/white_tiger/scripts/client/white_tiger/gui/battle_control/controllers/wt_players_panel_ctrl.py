import logging
from gui.battle_control.arena_info.settings import VEHICLE_STATUS
from gui.battle_control.battle_constants import BATTLE_CTRL_ID
from gui.battle_control.arena_info.interfaces import IPlayersPanelController
from gui.battle_control.arena_info.arena_vos import EventKeys
from gui.shared.players_panel_items import PlayersPanelItems
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from wt_settings import g_wt_config
_logger = logging.getLogger(__name__)

@dependency.replace_none_kwargs(battleSession=IBattleSessionProvider)
def isBossBot(vehicleID=0, vInfo=None, battleSession=None):
    if vInfo is None:
        arenaDP = battleSession.getArenaDP()
        vInfo = arenaDP.getVehicleInfo(vehicleID)
    tags = vInfo.vehicleType.tags
    vehCD = vInfo.vehicleType.compactDescr
    isBoss = g_wt_config.isAnyTypeBoss(vehCD)
    return b'wt_bot' in tags and not isBoss


class IPlayersPanelListener(object):

    def updateCamp(self, campID, vehicles):
        return

    def destroyCamp(self, campID):
        return


class WTPlayersPanelController(IPlayersPanelController):
    __slots__ = (b'__processors', b'__camps')
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(WTPlayersPanelController, self).__init__()
        self.__processors = {(PlayersPanelItems.CAMP.name): (self.__processCamp)}
        self.__camps = {}
        return

    def getControllerID(self):
        return BATTLE_CTRL_ID.PLAYERS_PANEL_CTRL

    def setViewComponents(self, *components):
        self._viewComponents = list(components)
        self.invalidateArenaInfo()
        return

    def stopControl(self):
        if self.__processors is not None:
            self.__processors.clear()
            self.__processors = None
        if self.__camps is not None:
            self.__camps.clear()
            self.__camps = None
        return

    def show(self, params):
        self.__process(params)
        return

    def hide(self, params):
        self.__process(params)
        return

    def processReplay(self, params):
        self.__process(params)
        return

    def invalidateArenaInfo(self):
        self.invalidateVehiclesInfo(self.__sessionProvider.getArenaDP())
        return

    def invalidateVehiclesInfo(self, arenaDP):
        arenaDP = self.__sessionProvider.getArenaDP()
        for vInfo in arenaDP.getVehiclesInfoIterator():
            self.addVehicleInfo(vInfo, arenaDP)

        return

    def addVehicleInfo(self, vInfo, arenaDP):
        if not isBossBot(vInfo=vInfo):
            return
        campUdo = vInfo.gameModeSpecific.getValue(EventKeys.CAMP.value)
        if campUdo in self.__camps and vInfo.vehicleStatus & VEHICLE_STATUS.IS_ALIVE:
            for component in self._viewComponents:
                component.updateCamp(self.__camps[campUdo], [vInfo])

        return

    def __process(self, params):
        if params is None:
            return
        else:
            itemType = params.getType()
            processor = self.__processors.get(itemType)
            if processor is not None:
                processor(params)
            return

    def __processCamp(self, params):
        campUdo = params.campUdo
        campId = params.campId
        if params.isAlive:
            arenaDP = self.__sessionProvider.getArenaDP()
            vInfos = [vInfo for vInfo in arenaDP.getVehiclesInfoIterator() if isBossBot(vInfo=vInfo) and vInfo.isAlive() and vInfo.gameModeSpecific.getValue(EventKeys.CAMP.value) == campUdo]
            for component in self._viewComponents:
                component.updateCamp(campId, vInfos)

            self.__camps[campUdo] = campId
        else:
            self.__camps.pop(campUdo)
            for component in self._viewComponents:
                component.destroyCamp(campId)

        return
