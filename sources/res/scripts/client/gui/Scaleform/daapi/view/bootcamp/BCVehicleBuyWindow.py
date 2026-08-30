from gui.Scaleform.daapi.view.lobby.vehicle_obtain_windows import VehicleBuyWindow
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.genConsts.VEHICLE_BUY_WINDOW_ALIASES import VEHICLE_BUY_WINDOW_ALIASES

class BCVehicleBuyWindow(VehicleBuyWindow):

    def _getContentLinkageFields(self):
        return {b'contentLinkage': (VEHICLE_BUY_WINDOW_ALIASES.CONTENT_BUY_BOOTCAMP_VIEW_UI), 
           b'isContentDAAPI': True, 
           b'contentAlias': (VIEW_ALIAS.BOOTCAMP_VEHICLE_BUY_VIEW)}
