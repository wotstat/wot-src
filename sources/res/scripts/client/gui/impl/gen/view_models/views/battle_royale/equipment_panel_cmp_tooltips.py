from frameworks.wulf import ViewModel

class EquipmentPanelCmpTooltips(ViewModel):
    __slots__ = ()
    TOOLTIP_SHELL = b'hangarShell'
    TOOLTIP_EQUIPMENT = b'battleRoyaleEquipment'
    TOOLTIP_RESPAWN = b'battleRoyaleRespawn'

    def __init__(self, properties=0, commands=0):
        super(EquipmentPanelCmpTooltips, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(EquipmentPanelCmpTooltips, self)._initialize()
        return
