from gui.Scaleform.daapi.view.meta.VehicleCompareConfiguratorBaseViewMeta import VehicleCompareConfiguratorBaseViewMeta

class VehicleCompareConfiguratorBaseView(VehicleCompareConfiguratorBaseViewMeta):

    def __init__(self):
        super(VehicleCompareConfiguratorBaseView, self).__init__()
        self._container = None
        self.__isInited = False
        return

    def onShow(self):
        return

    def onCamouflageUpdated(self):
        return

    def onShellsUpdated(self, updateShells=False, selectedIndex=-1):
        return

    def onOptDeviceUpdated(self):
        return

    def onEquipmentUpdated(self):
        return

    def onBattleBoosterUpdated(self):
        return

    def onModulesUpdated(self):
        return

    def onCrewSkillUpdated(self):
        return

    def onCrewLevelUpdated(self, newLvl):
        return

    def onPostProgressionUpdated(self):
        return

    def onResetToDefault(self):
        return

    def onBasketParametersChanged(self, basketVehData):
        return

    def setContainer(self, container):
        self._container = container
        self.__tryToInit()
        return

    def _init(self):
        return

    def _populate(self):
        super(VehicleCompareConfiguratorBaseView, self)._populate()
        self.__tryToInit()
        return

    def _dispose(self):
        self._container = None
        super(VehicleCompareConfiguratorBaseView, self)._dispose()
        return

    def __tryToInit(self):
        if self.isCreated() and self._container is not None and not self.__isInited:
            self.__isInited = True
            self._init()
        return
