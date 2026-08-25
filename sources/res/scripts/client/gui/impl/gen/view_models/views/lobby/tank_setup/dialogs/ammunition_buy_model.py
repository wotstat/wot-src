from gui.impl.gen.view_models.views.lobby.common.dialog_with_exchange import DialogWithExchange
from gui.impl.gen.view_models.views.lobby.tank_setup.common.deal_panel_model import DealPanelModel
from gui.impl.gen.view_models.views.lobby.tank_setup.dialogs.main_content.ammunition_buy_content import AmmunitionBuyContent

class AmmunitionBuyModel(DialogWithExchange):
    __slots__ = ()

    def __init__(self, properties=20, commands=3):
        super(AmmunitionBuyModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def mainContent(self):
        return self._getViewModel(15)

    @staticmethod
    def getMainContentType():
        return AmmunitionBuyContent

    @property
    def dealPanel(self):
        return self._getViewModel(16)

    @staticmethod
    def getDealPanelType():
        return DealPanelModel

    def getWithRollback(self):
        return self._getBool(17)

    def setWithRollback(self, value):
        self._setBool(17, value)
        return

    def getVehicleType(self):
        return self._getString(18)

    def setVehicleType(self, value):
        self._setString(18, value)
        return

    def getApplyForAllVehiclesByType(self):
        return self._getBool(19)

    def setApplyForAllVehiclesByType(self, value):
        self._setBool(19, value)
        return

    def _initialize(self):
        super(AmmunitionBuyModel, self)._initialize()
        self._addViewModelProperty(b'mainContent', AmmunitionBuyContent())
        self._addViewModelProperty(b'dealPanel', DealPanelModel())
        self._addBoolProperty(b'withRollback', False)
        self._addStringProperty(b'vehicleType', b'')
        self._addBoolProperty(b'applyForAllVehiclesByType', False)
        return
