from frameworks.wulf import ViewModel

class TankSetupConstants(ViewModel):
    __slots__ = ()
    OPT_DEVICES = b'optDevices'
    SHELLS = b'shells'
    CONSUMABLES = b'consumables'
    BATTLE_BOOSTERS = b'battleBoosters'
    BATTLE_ABILITIES = b'battleAbilities'
    TOGGLE_SHELLS = b'toggleShells'
    TOGGLE_CAMOUFLAGE = b'toggleCamouflage'
    EMPTY = b''
    APPLY_DEFAULT = b'apply'
    APPLY_VEHICLE = b'applyVehicle'
    APPLY_TYPE = b'applyType'
    SPECIAL_SETUP_INFO_SLOT_TOOLTIP = b'specialSetupInfoSlotTooltip'
    EQUIP_COIN_INFO_TOOLTIP = b'equipCoinInfo'
    TAB_SIMPLE = b'simple'
    TAB_MODERNIZED = b'modernized'

    def __init__(self, properties=0, commands=0):
        super(TankSetupConstants, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(TankSetupConstants, self)._initialize()
        return
