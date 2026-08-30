from frameworks.wulf import ViewModel

class EquipmentPanelCmpRentStates(ViewModel):
    __slots__ = ()
    STATE_NORMAL = b'normal'
    STATE_TEST_DRIVE_AVAILABLE = b'testDriveAvailable'
    STATE_TEST_DRIVE_ACTIVE = b'testDriveActive'
    STATE_RENT_AVAILABLE = b'rentAvailable'
    STATE_RENT_ACTIVE = b'rentActive'

    def __init__(self, properties=0, commands=0):
        super(EquipmentPanelCmpRentStates, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(EquipmentPanelCmpRentStates, self)._initialize()
        return
