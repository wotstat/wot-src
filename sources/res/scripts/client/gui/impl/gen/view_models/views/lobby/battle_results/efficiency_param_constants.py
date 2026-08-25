from frameworks.wulf import ViewModel

class EfficiencyParamConstants(ViewModel):
    __slots__ = ()
    KILLS = b'kills'
    SPOTTED = b'spotted'
    DAMAGE_DEALT = b'damageDealt'
    STUN = b'damageAssistedStun'
    DAMAGE_ASSISTED = b'damageAssisted'
    DAMAGE_BLOCKED_BY_ARMOR = b'damageBlockedByArmor'
    CAPTURE_POINTS = b'capturePoints'
    DROPPED_CAPTURE_POINTS = b'droppedCapturePoints'

    def __init__(self, properties=0, commands=0):
        super(EfficiencyParamConstants, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(EfficiencyParamConstants, self)._initialize()
        return
