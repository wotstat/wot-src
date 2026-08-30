from gui.impl.gen.view_models.views.common_balance_content_model import CommonBalanceContentModel
from gui.impl.gen.view_models.views.lobby.blueprints.fragment_item_model import FragmentItemModel

class BlueprintBalanceContentModel(CommonBalanceContentModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(BlueprintBalanceContentModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def intelligenceBalance(self):
        return self._getViewModel(1)

    @staticmethod
    def getIntelligenceBalanceType():
        return FragmentItemModel

    def getAllianceName(self):
        return self._getString(2)

    def setAllianceName(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(BlueprintBalanceContentModel, self)._initialize()
        self._addViewModelProperty(b'intelligenceBalance', FragmentItemModel())
        self._addStringProperty(b'allianceName', b'')
        return
