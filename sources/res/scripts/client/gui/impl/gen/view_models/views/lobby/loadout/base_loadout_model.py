from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.tank_setup.common.deal_panel_model import DealPanelModel

class BaseLoadoutModel(ViewModel):
    __slots__ = (b'onSlotAction',)

    def __init__(self, properties=1, commands=1):
        super(BaseLoadoutModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def dealPanel(self):
        return self._getViewModel(0)

    @staticmethod
    def getDealPanelType():
        return DealPanelModel

    def _initialize(self):
        super(BaseLoadoutModel, self)._initialize()
        self._addViewModelProperty(b'dealPanel', DealPanelModel())
        self.onSlotAction = self._addCommand(b'onSlotAction')
        return
