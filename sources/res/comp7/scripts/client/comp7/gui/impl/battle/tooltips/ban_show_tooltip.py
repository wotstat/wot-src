from comp7.gui.impl.gen.view_models.views.battle.tooltips.ban_show_tooltip_model import BanShowTooltipModel
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.pub import ViewImpl

class BanShowTooltip(ViewImpl):
    __slots__ = (b'__params',)

    def __init__(self, layoutID=R.views.comp7.mono.battle.tooltips.ban_show_tooltip(), params=None):
        settings = ViewSettings(layoutID)
        settings.model = BanShowTooltipModel()
        super(BanShowTooltip, self).__init__(settings)
        self.__params = params
        return

    @property
    def viewModel(self):
        return super(BanShowTooltip, self).getViewModel()

    def _onLoading(self):
        super(BanShowTooltip, self)._onLoading()
        with self.viewModel.transaction() as vm:
            vm.setLongName(self.__params[b'longName'])
            vm.setType(self.__params[b'type'])
            vm.setIsPremium(self.__params[b'isPremium'])
            vm.setConfirmedChoice(self.__params[b'confirmedChoice'])
            vm.setVehicleCD(self.__params[b'vehicleCD'])
            vm.setRoleKey(self.__params[b'roleKey'])
        return
