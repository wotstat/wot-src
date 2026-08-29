from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from gui.impl.lobby.vehicle_compare.modifications_panel import CompareModificationsPanelView

class VehicleCompareConfiguratorProgressionInject(InjectComponentAdaptor):

    def update(self):
        self.getInjectView().update()
        return

    def _makeInjectView(self):
        modificationsPanel = CompareModificationsPanelView()
        return modificationsPanel
