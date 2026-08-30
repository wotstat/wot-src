from helpers import dependency
from skeletons.gui.game_control import ISeniorityAwardsController
from gui.shared.event_dispatcher import showSeniorityRewardVehiclesWindow
from web.web_client_api import w2capi, w2c, W2CSchema

@w2capi(name=b'seniority_awards', key=b'action')
class SeniorityAwardsWebApi(object):
    __seniorityAwardsCtrl = dependency.descriptor(ISeniorityAwardsController)

    @w2c(W2CSchema, b'is_vehicle_selection_available')
    def isVehicleSelectionAvailable(self, _):
        return {b'isVehicleSelectionAvailable': (self.__seniorityAwardsCtrl.isVehicleSelectionAvailable)}


class OpenSeniorityAwardsWebApi(object):

    @w2c(W2CSchema, b'seniority_vehicle_selection')
    def showSeniorityVehicleSelectionWindow(self, _):
        showSeniorityRewardVehiclesWindow()
        return
