from helpers import dependency
from skeletons.gui.game_control import ISeniorityAwardsController
from web.client_web_api.api import C2WHandler, c2w

class SeniorityAwardsEventHandler(C2WHandler):
    __seniorityAwardsCtrl = dependency.descriptor(ISeniorityAwardsController)

    def init(self):
        super(SeniorityAwardsEventHandler, self).init()
        self.__seniorityAwardsCtrl.onVehicleSelectionChanged += self.__seniorityAwardsVehicleSelectionUpdated
        return

    def fini(self):
        self.__seniorityAwardsCtrl.onVehicleSelectionChanged -= self.__seniorityAwardsVehicleSelectionUpdated
        super(SeniorityAwardsEventHandler, self).fini()
        return

    @c2w(name=b'seniority_awards_vehicle_selection_changed')
    def __seniorityAwardsVehicleSelectionUpdated(self, *args):
        return {b'isVehicleSelectionAvailable': (self.__seniorityAwardsCtrl.isVehicleSelectionAvailable)}
