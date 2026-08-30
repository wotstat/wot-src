from gui.Scaleform.daapi.view.lobby.vehicle_compare.cmp_configurator_base import VehicleCompareConfiguratorBaseView

class VehicleModulesViewMeta(VehicleCompareConfiguratorBaseView):

    def onModuleHover(self, id):
        self._printOverrideError(b'onModuleHover')
        return

    def onModuleClick(self, id):
        self._printOverrideError(b'onModuleClick')
        return

    def as_setItemS(self, nation, raw):
        if self._isDAAPIInited():
            return self.flashObject.as_setItem(nation, raw)
        return

    def as_setNodesStatesS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setNodesStates(data)
        return
