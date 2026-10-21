from frameworks.wulf import ViewModel

class PortalUpgradeAbilityItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(PortalUpgradeAbilityItemModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getIsReceived(self):
        return self._getBool(1)

    def setIsReceived(self, value):
        self._setBool(1, value)
        return

    def _initialize(self):
        super(PortalUpgradeAbilityItemModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addBoolProperty(b'isReceived', False)
        return
