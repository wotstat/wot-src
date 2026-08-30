from frameworks.wulf import ViewModel

class LootBoxCompensationTooltipTypes(ViewModel):
    __slots__ = ()
    BASE = b'base'
    VEHICLE = b'vehicle'
    CREW_SKINS = b'crewSkin'

    def __init__(self, properties=0, commands=0):
        super(LootBoxCompensationTooltipTypes, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(LootBoxCompensationTooltipTypes, self)._initialize()
        return
