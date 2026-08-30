from frameworks.wulf import ViewModel

class NationChangeTooltips(ViewModel):
    __slots__ = ()
    TOOLTIP_NC_VEHICLE = b'carouselVehicle'
    TOOLTIP_NC_TANKMAN = b'tankman'
    TOOLTIP_NC_HANGARMODULE = b'nationChangeHangarModule'
    TOOLTIP_NC_HANGARSHELL = b'nationChangeHangarShell'
    TOOLTIP_NC_BATTLEBOOSTER = b'nationChangeBattleBooster'

    def __init__(self, properties=0, commands=0):
        super(NationChangeTooltips, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(NationChangeTooltips, self)._initialize()
        return
