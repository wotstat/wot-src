from __future__ import absolute_import
from collections import namedtuple
from future.utils import listitems
import BigWorld
VehInfoDiffBufferEntry = namedtuple(b'VehInfoDiffBufferEntry', (b'new', b'prev'))

class AvatarVehiclesInfoBase(BigWorld.DynamicScriptComponent):
    SET_VEH_INFO_FMT = b'setVehInfo_{}'

    def __init__(self):
        super(AvatarVehiclesInfoBase, self).__init__()
        self._isOwnedByPlayer = self.avatar.id == self.entity.avatarID
        self.__arena = self.avatar.arena
        self.__diffBuffer = {}
        if self._isOwnedByPlayer:
            self.__arena.updateVehiclesList(self.vehiclesInfo)
        return

    @property
    def avatar(self):
        return BigWorld.player()

    def setNested_vehiclesInfo(self, changePath, prev):
        if not self._isOwnedByPlayer:
            return
        else:
            if changePath[1] != b'__generation':
                self.__diffBuffer[changePath[1]] = VehInfoDiffBufferEntry(self.vehiclesInfo[changePath[0]][changePath[1]], prev)
                return
            vehInfoIndex = changePath[0]
            vehInfo = self.vehiclesInfo[vehInfoIndex]
            self._updateVehicleInfo(vehInfo, self.__diffBuffer)
            for attrName, diff in listitems(self.__diffBuffer):
                if diff.prev is None or diff.new is None:
                    continue
                setter = getattr(self, self.SET_VEH_INFO_FMT.format(attrName), None)
                if setter is not None:
                    setter(vehInfo, self.__diffBuffer.pop(attrName))

            if self.__diffBuffer:
                self._onVehicleUpdated(vehInfo)
            self.__diffBuffer.clear()
            return

    def setSlice_vehiclesInfo(self, changePath, prev):
        if not self._isOwnedByPlayer:
            return
        begin, end = changePath[0]
        for vehInfo in self.vehiclesInfo[begin:end]:
            self.__arena.addVehInfo(vehInfo)

        return

    def setVehInfo_isAlive(self, vehInfo, diff):
        vehID = vehInfo[b'vehicleID']
        self.__arena.updateVehicleIsAlive(vehID, vehInfo[b'compDescr'], self.avatar.playerVehicleID == vehID)
        return

    def setVehInfo_isTeamKiller(self, vehInfo, diff):
        self.__arena.updateVehicleIsTeamKiller(vehInfo[b'vehicleID'])
        return

    def setVehInfo_isAvatarReady(self, vehInfo, diff):
        self.__arena.updateVehicleIsAvatarReady(vehInfo[b'vehicleID'])
        return

    def setVehInfo_frags(self, vehInfo, diff):
        self.__arena.updateVehiclesFrags(vehInfo[b'vehicleID'], diff.new)
        return

    def setVehInfo_tkills(self, vehInfo, diff):
        self.__arena.updateVehiclesTkills(vehInfo[b'vehicleID'], diff.new)
        return

    def setVehInfo_fogOfWar(self, vehInfo, diff):
        self.__arena.updateFogOfWar(diff.new)
        return

    def setVehInfo_position(self, vehInfo, diff):
        self.__arena.updateVehiclesPosition(vehInfo[b'vehicleID'], diff.new)
        return

    def _updateVehicleInfo(self, vehInfo, diffBuffer):
        self.__arena.updateVehicleInfo(vehInfo[b'vehicleID'], {name: vehInfo[name] for name in diffBuffer})
        return

    def _onVehicleUpdated(self, vehInfo):
        self.__arena.onVehicleUpdated(vehInfo[b'vehicleID'])
        return
