from gui.Scaleform.daapi.view.lobby.vehicle_preview.vehicle_preview import VehiclePreview
from shared_utils import CONST_CONTAINER

class OptionalBlocks(CONST_CONTAINER):
    BUYING_PANEL = b'buyingPanel'
    CLOSE_BUTTON = b'closeBtn'
    ALL = (BUYING_PANEL, CLOSE_BUTTON)


class ConfigurableVehiclePreview(VehiclePreview):

    def __init__(self, ctx):
        super(ConfigurableVehiclePreview, self).__init__(ctx)
        self.__hiddenBlocks = ctx.get(b'hiddenBlocks')
        self.__showCloseBtn = OptionalBlocks.CLOSE_BUTTON not in self.__hiddenBlocks
        return

    def setBottomPanel(self):
        if OptionalBlocks.BUYING_PANEL in self.__hiddenBlocks:
            self.as_setBottomPanelS(b'')
        else:
            super(ConfigurableVehiclePreview, self).setBottomPanel()
        return

    def _getData(self):
        result = super(ConfigurableVehiclePreview, self)._getData()
        result.update({b'showCloseBtn': (self.__showCloseBtn)})
        return result

    def _getExitEvent(self):
        exitEvent = super(ConfigurableVehiclePreview, self)._getExitEvent()
        exitEvent.ctx.update({b'hiddenBlocks': (self.__hiddenBlocks)})
        return exitEvent
