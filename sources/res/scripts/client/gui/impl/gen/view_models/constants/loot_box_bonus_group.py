from frameworks.wulf import ViewModel

class LootBoxBonusGroup(ViewModel):
    __slots__ = ()
    VEHICLE = b'vehicle'
    PREMIUM = b'premium'
    CURRENCY = b'currency'
    VEHICLECUSTOMIZATIONS = b'vehicleCustomizations'
    CREW = b'crew'
    BOOSTERS = b'boosters'
    EQUIPMENTS = b'equipments'
    ACCOUNTCUSTOMIZATIONS = b'accountCustomizations'
    FEATUREITEMS = b'featureItems'
    LOOTBOX_STAGE_ROTATION = b'lootboxStageRotation'
    LOOTBOXES = b'lootboxes'

    def __init__(self, properties=0, commands=0):
        super(LootBoxBonusGroup, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(LootBoxBonusGroup, self)._initialize()
        return
