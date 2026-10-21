from portal.gui.impl.gen.view_models.views.lobby.tooltips.portal_shell_stat import PortalShellStat
from frameworks.wulf import ViewSettings
from portal.gui.impl.gen.view_models.views.lobby.tooltips.shell_tooltip_model import ShellTooltipModel
from gui.impl.pub import ViewImpl
from gui.impl.gen import R
from items import vehicles

class ShellTooltip(ViewImpl):
    __slots__ = (b'_vehicle',)

    def __init__(self, vehicle):
        settings = ViewSettings(R.views.portal.lobby.tooltips.ShellTooltip())
        settings.model = ShellTooltipModel()
        self._vehicle = vehicle
        super(ShellTooltip, self).__init__(settings)
        return

    @property
    def viewModel(self):
        return super(ShellTooltip, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(ShellTooltip, self)._onLoading(*args, **kwargs)
        self.__updateData()
        return

    def __updateData(self):
        with self.viewModel.transaction() as vm:
            self.__fillModel(vm)
        return

    def __fillModel(self, model):
        self._fillShellInfo(model)
        self._fillStats(model.getStats())
        return

    def _fillShellInfo(self, model):
        shellDescr = vehicles.getItemByCompactDescr(self._vehicle.shells.installed[0].intCD)
        model.setName(self._vehicle.shells.installed[0].userName)
        model.setType(self._vehicle.shells.installed[0].type)
        model.setCaliber(shellDescr.caliber)
        return

    def _fillStats(self, array):
        array.clear()
        shellDescr = vehicles.getItemByCompactDescr(self._vehicle.shells.installed[0].intCD)
        damageLimits = shellDescr.randomizationDmgLimits
        pPower = self._vehicle.gun.descriptor.shots[0].piercingPower
        speed = self._vehicle.gun.descriptor.shots[0].speed
        stats = [{b'from': (damageLimits[0]), b'to': (damageLimits[1]), b'name': b'damage'}, {b'from': (pPower[1]), b'to': (pPower[0]), b'name': b'armor_penetration'}, {b'from': speed, b'to': 0, b'name': b'flight_speed'}]
        for stat in stats:
            statModel = PortalShellStat()
            statModel.setFrom(stat[b'from'])
            statModel.setTo(stat[b'to'])
            statModel.setName(stat[b'name'])
            array.addViewModel(statModel)

        array.invalidate()
        return
