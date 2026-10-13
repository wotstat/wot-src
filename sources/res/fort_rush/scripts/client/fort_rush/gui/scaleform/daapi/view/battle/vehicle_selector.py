from __future__ import absolute_import
import logging
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from fort_rush.gui.impl.battle.fort_rush_vehicle_selector import FortRushVehicleSelectorView
from fort_rush.gui.battle_control.controllers.respawn_ctrl import ISpawnListener
_logger = logging.getLogger(__name__)

class FortRushVehicleSelectorComponent(InjectComponentAdaptor, ISpawnListener):

    def _makeInjectView(self):
        return FortRushVehicleSelectorView()

    def setSpawnPoints(self, points, pointId=None):
        return

    def showSpawnPoints(self):
        return

    def closeSpawnPoints(self):
        return

    def updatePoint(self, vehicleId, pointId, prevPointId):
        return

    def updateCloseTime(self, timeLeft, state):
        return

    def onSelectPoint(self, pointId):
        return

    def setSpawnType(self, spawnType):
        return
