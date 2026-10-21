import Event, typing, BattleReplay, logging
from gui.battle_control.arena_info.interfaces import IMapZonesController
from portal_constants import PORTAL_BATTLE_CTRL_ID
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
if typing.TYPE_CHECKING:
    from portal_client_cgf.portal_2d_markers.components import PortalAreaMarker
    from gui.battle_control.controllers import BattleSessionSetup
    import Math
_logger = logging.getLogger(__name__)

class PortalMarkersController(IMapZonesController):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self, setup):
        super(PortalMarkersController, self).__init__()
        self.__eManager = Event.EventManager()
        self.onMarkerToZoneAdded = Event.Event(self.__eManager)
        self.onMarkerFromZoneRemoved = Event.Event(self.__eManager)
        self.onMarkerProgressUpdated = Event.Event(self.__eManager)
        self.__zoneMarkers = {}
        return

    def startControl(self, *args):
        return

    def stopControl(self):
        self.__eManager.clear()
        self.__zoneMarkers.clear()
        return

    def getControllerID(self):
        return PORTAL_BATTLE_CTRL_ID.PORTAL_MARKERS_CTRL

    def addMarkerToZone(self, zoneMarker, markerPos):
        if not (zoneMarker.markerMinimapEntryID or zoneMarker.marker2DEntryID):
            return
        self.__zoneMarkers[zoneMarker.id] = (zoneMarker, markerPos)
        self.onMarkerToZoneAdded(zoneMarker, markerPos)
        return

    def removeMarkerFromZone(self, areaMarker):
        self.onMarkerFromZoneRemoved(areaMarker)
        self.__zoneMarkers.pop(areaMarker.id)
        return

    def addTransformedZone(self, zone):
        return

    def removeTransformedZone(self, zone):
        return

    def enterDangerZone(self, zone):
        return

    def exitDangerZone(self, zone):
        return

    def removeDangerZone(self, zone):
        return

    def getZoneMarkers(self):
        return self.__zoneMarkers

    def getTransformedZones(self):
        return


class ReplayPortalMarkersController(PortalMarkersController):
    pass


def createPortalMarkersController(setup):
    if BattleReplay.g_replayCtrl.isPlaying:
        return ReplayPortalMarkersController(setup)
    return PortalMarkersController(setup)
