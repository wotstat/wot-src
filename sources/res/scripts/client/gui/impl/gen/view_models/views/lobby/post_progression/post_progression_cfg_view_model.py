from gui.impl.gen.view_models.views.lobby.post_progression.post_progression_base_view_model import PostProgressionBaseViewModel
from gui.impl.gen.view_models.views.lobby.post_progression.post_progression_purchase_model import PostProgressionPurchaseModel

class PostProgressionCfgViewModel(PostProgressionBaseViewModel):
    __slots__ = (b'onGoBackAction', b'onResearchAction')

    def __init__(self, properties=6, commands=3):
        super(PostProgressionCfgViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def purchasePreview(self):
        return self._getViewModel(5)

    @staticmethod
    def getPurchasePreviewType():
        return PostProgressionPurchaseModel

    def _initialize(self):
        super(PostProgressionCfgViewModel, self)._initialize()
        self._addViewModelProperty(b'purchasePreview', PostProgressionPurchaseModel())
        self.onGoBackAction = self._addCommand(b'onGoBackAction')
        self.onResearchAction = self._addCommand(b'onResearchAction')
        return
