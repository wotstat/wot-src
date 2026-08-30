from __future__ import absolute_import
from skeletons.gui.game_control import IGameController

class ILSVehicleSelectionController(IGameController):

    def activate(self):
        raise NotImplementedError
        return

    def deactivate(self):
        raise NotImplementedError
        return

    def selectModeVehicle(self, vehInvID=0):
        raise NotImplementedError
        return

    def selectVehicle(self, vehInvID):
        raise NotImplementedError
        return
