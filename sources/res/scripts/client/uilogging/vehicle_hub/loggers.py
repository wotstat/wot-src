import typing
from uilogging.base.logger import MetricsLogger, createPartnerID
from uilogging.vehicle_hub.constants import LogActions, Features, Tabs, TIME_LIMIT
from uilogging.vehicle_hub.constants import LogItems

class ArmorTabLogger(MetricsLogger):
    __slots__ = (b'_vehicleCD', b'_partnerID', b'_tooltipOpenTime')

    def __init__(self, vehCD):
        super(ArmorTabLogger, self).__init__(Features.ARMOR_INSPECTOR)
        self._vehicleCD = str(vehCD)
        self._partnerID = createPartnerID()
        return

    @property
    def vehicleCD(self):
        return self._vehicleCD

    @property
    def partnerID(self):
        return self._partnerID

    def logOpen(self):
        self.log(action=LogActions.OPEN, item=Tabs.ARMOR_TAB, itemState=self._vehicleCD, partnerID=self._partnerID)
        return

    def logClose(self):
        self.log(action=LogActions.CLOSE, item=Tabs.ARMOR_TAB, itemState=self._vehicleCD, partnerID=self._partnerID)
        return

    def tooltipOpened(self):
        self.startAction(LogActions.TOOLTIP_ACTION)
        return

    def armorTooltipClosed(self):
        self._tooltipClosed(LogItems.ARMOR_TOOLTIP)
        return

    def _tooltipClosed(self, item):
        self.stopAction(action=LogActions.TOOLTIP_ACTION, item=item, parentScreen=Tabs.ARMOR_TAB, itemState=self._vehicleCD, partnerID=self._partnerID, timeLimit=TIME_LIMIT)
        return
