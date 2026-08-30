from gui.impl.gen.view_models.views.loot_box_compensation_tooltip_model import LootBoxCompensationTooltipModel
from gui.impl.gen.view_models.views.loot_box_compensation_tooltip_types import LootBoxCompensationTooltipTypes
from gui.impl.gen.view_models.views.loot_box_vehicle_compensation_tooltip_model import LootBoxVehicleCompensationTooltipModel
from gui.impl.pub import ViewImpl

class CompensationTooltipContent(ViewImpl):
    __slots__ = ()

    @property
    def viewModel(self):
        return super(CompensationTooltipContent, self).getViewModel()

    def _initialize(self, *args, **kwargs):
        with self.viewModel.transaction() as tx:
            tx.setIconBefore(kwargs.get(b'iconBefore', b''))
            tx.setLabelBefore(kwargs.get(b'labelBefore', b''))
            tx.setIconAfter(kwargs.get(b'iconAfter', b''))
            tx.setLabelAfter(kwargs.get(b'labelAfter', b''))
            tx.setBonusName(kwargs.get(b'bonusName', b''))
            tx.setCountBefore(kwargs.get(b'countBefore', 1))
            tx.setTooltipType(kwargs.get(b'tooltipType', LootBoxCompensationTooltipTypes.BASE))
        return


class CrewSkinsCompensationTooltipContent(CompensationTooltipContent):
    __slots__ = ()

    def _initialize(self, *args, **kwargs):
        super(CrewSkinsCompensationTooltipContent, self)._initialize(*args, **kwargs)
        with self.viewModel.transaction() as tx:
            tx.setLabelBefore(kwargs.get(b'labelBefore', b''))
        return


class VehicleCompensationTooltipContent(CompensationTooltipContent):
    __slots__ = ()

    @property
    def viewModel(self):
        return super(VehicleCompensationTooltipContent, self).getViewModel()

    def _initialize(self, *args, **kwargs):
        super(VehicleCompensationTooltipContent, self)._initialize(*args, **kwargs)
        with self.viewModel.transaction() as tx:
            tx.setVehicleName(kwargs.get(b'vehicleName', b''))
            tx.setVehicleType(kwargs.get(b'vehicleType', b''))
            tx.setIsElite(kwargs.get(b'isElite', True))
            tx.setVehicleLvl(kwargs.get(b'vehicleLvl', b''))
            tx.setTooltipType(LootBoxCompensationTooltipTypes.VEHICLE)
        return
