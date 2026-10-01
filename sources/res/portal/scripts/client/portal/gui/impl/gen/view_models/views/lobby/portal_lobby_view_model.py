from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from portal.gui.impl.gen.view_models.views.lobby.complexity_level_widget import ComplexityLevelWidget
from portal.gui.impl.gen.view_models.views.lobby.portal_ammunition_panel import PortalAmmunitionPanel
from portal.gui.impl.gen.view_models.views.lobby.portal_carousel_tank_model import PortalCarouselTankModel
from portal.gui.impl.gen.view_models.views.lobby.portal_quest_widget import PortalQuestWidget
from portal.gui.impl.gen.view_models.views.lobby.portal_token_model import PortalTokenModel

class PortalLobbyViewModel(ViewModel):
    __slots__ = (b'onClose', b'onAboutEvent', b'onShopClicked', b'onProgressionClicked', b'onComplexityChange', b'onVehicleSelect', b'onMoveSpace', b'onStartMoving', b'onUpgradeVehicle', b'onShowSettings')

    def __init__(self, properties=5, commands=10):
        super(PortalLobbyViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def tanks(self):
        return self._getViewModel(0)

    @staticmethod
    def getTanksType():
        return PortalCarouselTankModel

    @property
    def portalAmmunitionPanel(self):
        return self._getViewModel(1)

    @staticmethod
    def getPortalAmmunitionPanelType():
        return PortalAmmunitionPanel

    @property
    def portalQuestWidget(self):
        return self._getViewModel(2)

    @staticmethod
    def getPortalQuestWidgetType():
        return PortalQuestWidget

    @property
    def portalTokens(self):
        return self._getViewModel(3)

    @staticmethod
    def getPortalTokensType():
        return PortalTokenModel

    @property
    def complexityLevelWidget(self):
        return self._getViewModel(4)

    @staticmethod
    def getComplexityLevelWidgetType():
        return ComplexityLevelWidget

    def _initialize(self):
        super(PortalLobbyViewModel, self)._initialize()
        self._addViewModelProperty(b'tanks', UserListModel())
        self._addViewModelProperty(b'portalAmmunitionPanel', PortalAmmunitionPanel())
        self._addViewModelProperty(b'portalQuestWidget', PortalQuestWidget())
        self._addViewModelProperty(b'portalTokens', PortalTokenModel())
        self._addViewModelProperty(b'complexityLevelWidget', ComplexityLevelWidget())
        self.onClose = self._addCommand(b'onClose')
        self.onAboutEvent = self._addCommand(b'onAboutEvent')
        self.onShopClicked = self._addCommand(b'onShopClicked')
        self.onProgressionClicked = self._addCommand(b'onProgressionClicked')
        self.onComplexityChange = self._addCommand(b'onComplexityChange')
        self.onVehicleSelect = self._addCommand(b'onVehicleSelect')
        self.onMoveSpace = self._addCommand(b'onMoveSpace')
        self.onStartMoving = self._addCommand(b'onStartMoving')
        self.onUpgradeVehicle = self._addCommand(b'onUpgradeVehicle')
        self.onShowSettings = self._addCommand(b'onShowSettings')
        return
