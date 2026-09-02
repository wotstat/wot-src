from white_tiger.gui.impl.gen.view_models.views.lobby.common.wt_run_portal_model import WtRunPortalModel
from white_tiger.gui.impl.gen.view_models.views.lobby.portals.main_prize_model import MainPrizeModel
from white_tiger.gui.impl.gen.view_models.views.lobby.portals.wt_base_portals_view_model import WtBasePortalsViewModel

class WtTankPortalViewModel(WtBasePortalsViewModel):
    __slots__ = (b'onGoBack', b'onRunPortal', b'onPreviewTank')

    def __init__(self, properties=4, commands=5):
        super(WtTankPortalViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def portalRun(self):
        return self._getViewModel(1)

    @staticmethod
    def getPortalRunType():
        return WtRunPortalModel

    @property
    def mainPrize(self):
        return self._getViewModel(2)

    @staticmethod
    def getMainPrizeType():
        return MainPrizeModel

    def getBackButtonText(self):
        return self._getString(3)

    def setBackButtonText(self, value):
        self._setString(3, value)
        return

    def _initialize(self):
        super(WtTankPortalViewModel, self)._initialize()
        self._addViewModelProperty(b'portalRun', WtRunPortalModel())
        self._addViewModelProperty(b'mainPrize', MainPrizeModel())
        self._addStringProperty(b'backButtonText', b'')
        self.onGoBack = self._addCommand(b'onGoBack')
        self.onRunPortal = self._addCommand(b'onRunPortal')
        self.onPreviewTank = self._addCommand(b'onPreviewTank')
        return
