from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.comp7.meta_view.pages.rank_rewards_item_model import RankRewardsItemModel
from gui.impl.gen.view_models.views.lobby.comp7.meta_view.progression_base_model import ProgressionBaseModel
from gui.impl.gen.view_models.views.lobby.comp7.qualification_model import QualificationModel

class RankRewardsModel(ProgressionBaseModel):
    __slots__ = (b'onPreviewOpen', b'onComp7ShopOpen')
    DEFAULT_ITEM_INDEX = -1

    def __init__(self, properties=4, commands=2):
        super(RankRewardsModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def qualificationModel(self):
        return self._getViewModel(1)

    @staticmethod
    def getQualificationModelType():
        return QualificationModel

    def getItems(self):
        return self._getArray(2)

    def setItems(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getItemsType():
        return RankRewardsItemModel

    def getInitialItemIndex(self):
        return self._getNumber(3)

    def setInitialItemIndex(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(RankRewardsModel, self)._initialize()
        self._addViewModelProperty(b'qualificationModel', QualificationModel())
        self._addArrayProperty(b'items', Array())
        self._addNumberProperty(b'initialItemIndex', -1)
        self.onPreviewOpen = self._addCommand(b'onPreviewOpen')
        self.onComp7ShopOpen = self._addCommand(b'onComp7ShopOpen')
        return
