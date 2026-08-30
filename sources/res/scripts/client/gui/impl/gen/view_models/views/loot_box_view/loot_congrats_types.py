from frameworks.wulf import ViewModel

class LootCongratsTypes(ViewModel):
    __slots__ = ()
    CONGRAT_TYPE_BLUEPRINT = b'BlueprintFinalFragmentCongrats'
    CONGRAT_TYPE_BLUEPRINT_PART = b'BlueprintVehicleFragmentCongrats'
    CONGRAT_TYPE_VEHICLE = b'VehicleLootBoxCongrats'
    CONGRAT_TYPE_STYLE = b'StyleLootBoxCongrats'
    CONGRAT_TYPE_TANKMAN = b'TankmanLootBoxCongrats'
    INIT_CONGRAT_TYPE_USUAL = b'UsualCongrats'
    INIT_CONGRAT_TYPE_PROGRESSIVE_REWARDS = b'ProgressiveRewardCongrats'
    INIT_CONGRAT_TYPE_CREW_BOOKS = b'CrewBookCongrats'
    INIT_CONGRAT_TYPE_EPIC_REWARDS = b'EpicRewardCongrats'
    INIT_CONGRAT_TYPE_BATTLE_PASS = b'BattlePassCongrats'
    INIT_CONGRAT_TYPE_AC_EMAIL_CONFIRMATION = b'ACEmailConfirmation'

    def __init__(self, properties=0, commands=0):
        super(LootCongratsTypes, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(LootCongratsTypes, self)._initialize()
        return
