from __future__ import absolute_import
import typing
from CurrentVehicle import g_currentVehicle
from gui.Scaleform.daapi.view.lobby.battle_queue.battle_queue import RandomQueueProvider
from gui.impl import backport
from gui.impl.gen import R
from soft_exception import SoftException
from white_tiger.gui.Scaleform.daapi.view.lobby import getTypeBigWtIconRPath
from white_tiger.gui.wt_event_helpers import isBoss
from white_tiger_common.wt_constants import WT_VEHICLE_TAGS
if typing.TYPE_CHECKING:
    from gui.shared.gui_items.Vehicle import Vehicle

def _timeLabel(time):
    return b'%d:%02d' % divmod(time, 60)


class WhiteTigerQueueProvider(RandomQueueProvider):
    EVENT_TYPES_ORDERED = [
     WT_VEHICLE_TAGS.BOSS, WT_VEHICLE_TAGS.HUNTER]

    def getIconPath(self, _):
        return backport.image(R.images.white_tiger.gui.maps.icons.battleTypes.c_136x136.white_tiger())

    def getTitle(self, guiType):
        titleRes = R.strings.white_tiger_lobby.loading.battleTypes.wt
        if titleRes.exists():
            return backport.text(titleRes())
        return b''

    def processQueueInfo(self, qInfo):
        bosses = qInfo.get(b'bosses', 0)
        hunters = qInfo.get(b'hunters', 0)
        total = bosses + hunters
        self._createCommonPlayerString(total)
        uiData = []
        counts = {(WT_VEHICLE_TAGS.BOSS): bosses, (WT_VEHICLE_TAGS.HUNTER): hunters}
        for vTypeName in self.EVENT_TYPES_ORDERED:
            uiData.append({b'type': (backport.text(R.strings.white_tiger_lobby.vehicle.tags.dyn(vTypeName).name())), 
               b'icon': (getTypeBigWtIconRPath(vTypeName)), 
               b'count': (counts[vTypeName])})

        self._proxy.as_setDPS(uiData)
        vehicle = g_currentVehicle.item
        if not vehicle:
            raise SoftException(b"Can't get event prebattle vehicle")
        isPlayerBoss = self.__isBossPlayer()
        avgWaitTime = qInfo.get(b'avgWaitTimeBosses', 0) if isPlayerBoss else qInfo.get(b'avgWaitTimeHunters', 0)
        self._setAverageWaitingTime(vehicle.userName, avgWaitTime)
        return

    def _setAverageWaitingTime(self, vehicleName, averageWaitingTime):
        avgWaitTimeLabel = backport.text(R.strings.white_tiger_lobby.battleQueue.avgWaitTime.label(), vehName=vehicleName)
        avgWaitTime = _timeLabel(averageWaitingTime)
        self._proxy.as_setAverageTimeS(avgWaitTimeLabel, avgWaitTime)
        return

    def getTankIcon(self, vehicle):
        tag = next((t for t in self.EVENT_TYPES_ORDERED if t in vehicle.tags), b'')
        return getTypeBigWtIconRPath(tag)

    def __isBossPlayer(self):
        vehicle = g_currentVehicle.item
        return isBoss(vehicle.tags)
