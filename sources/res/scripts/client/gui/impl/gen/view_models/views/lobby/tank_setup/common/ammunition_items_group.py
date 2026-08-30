from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.tank_setup.common.ammunition_items_section import AmmunitionItemsSection
from gui.impl.gen.view_models.views.lobby.tank_setup.common.ammunition_setup_selector import AmmunitionSetupSelector

class AmmunitionItemsGroup(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(AmmunitionItemsGroup, self).__init__(properties=properties, commands=commands)
        return

    @property
    def setupSelector(self):
        return self._getViewModel(0)

    @staticmethod
    def getSetupSelectorType():
        return AmmunitionSetupSelector

    def getSections(self):
        return self._getArray(1)

    def setSections(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getSectionsType():
        return AmmunitionItemsSection

    def getCurrentIndex(self):
        return self._getNumber(2)

    def setCurrentIndex(self, value):
        self._setNumber(2, value)
        return

    def getGroupId(self):
        return self._getNumber(3)

    def setGroupId(self, value):
        self._setNumber(3, value)
        return

    def getTotalCount(self):
        return self._getNumber(4)

    def setTotalCount(self, value):
        self._setNumber(4, value)
        return

    def _initialize(self):
        super(AmmunitionItemsGroup, self)._initialize()
        self._addViewModelProperty(b'setupSelector', AmmunitionSetupSelector())
        self._addArrayProperty(b'sections', Array())
        self._addNumberProperty(b'currentIndex', 0)
        self._addNumberProperty(b'groupId', 0)
        self._addNumberProperty(b'totalCount', 0)
        return
