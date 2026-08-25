from frameworks.wulf import Array, Map, ViewModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.research_item_display_model import ResearchItemDisplayModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.research_item_model import ResearchItemModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.field_modification_model import FieldModificationModel

class ModulesModel(ViewModel):
    __slots__ = (b'onVehicleChange', b'onInstallItem', b'onUnlockItem', b'onBuyAndInstallItem', b'onSellItem')

    def __init__(self, properties=4, commands=5):
        super(ModulesModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def fieldModificationModel(self):
        return self._getViewModel(0)

    @staticmethod
    def getFieldModificationModelType():
        return FieldModificationModel

    def getPrevResearchItems(self):
        return self._getArray(1)

    def setPrevResearchItems(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getPrevResearchItemsType():
        return ResearchItemDisplayModel

    def getCurrentResearchItems(self):
        return self._getArray(2)

    def setCurrentResearchItems(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getCurrentResearchItemsType():
        return ResearchItemDisplayModel

    def getResearchItems(self):
        return self._getMap(3)

    def setResearchItems(self, value):
        self._setMap(3, value)
        return

    @staticmethod
    def getResearchItemsType():
        return (int, ResearchItemModel)

    def _initialize(self):
        super(ModulesModel, self)._initialize()
        self._addViewModelProperty(b'fieldModificationModel', FieldModificationModel())
        self._addArrayProperty(b'prevResearchItems', Array())
        self._addArrayProperty(b'currentResearchItems', Array())
        self._addMapProperty(b'researchItems', Map(int, ResearchItemModel))
        self.onVehicleChange = self._addCommand(b'onVehicleChange')
        self.onInstallItem = self._addCommand(b'onInstallItem')
        self.onUnlockItem = self._addCommand(b'onUnlockItem')
        self.onBuyAndInstallItem = self._addCommand(b'onBuyAndInstallItem')
        self.onSellItem = self._addCommand(b'onSellItem')
        return
