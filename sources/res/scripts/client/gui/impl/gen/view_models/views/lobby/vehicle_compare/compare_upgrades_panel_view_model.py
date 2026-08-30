from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.vehicle_compare.upgrades_model import UpgradesModel

class CompareUpgradesPanelViewModel(ViewModel):
    __slots__ = (b'onSelectUpgrades',)

    def __init__(self, properties=1, commands=1):
        super(CompareUpgradesPanelViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getUpgrades(self):
        return self._getArray(0)

    def setUpgrades(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getUpgradesType():
        return UpgradesModel

    def _initialize(self):
        super(CompareUpgradesPanelViewModel, self)._initialize()
        self._addArrayProperty(b'upgrades', Array())
        self.onSelectUpgrades = self._addCommand(b'onSelectUpgrades')
        return
