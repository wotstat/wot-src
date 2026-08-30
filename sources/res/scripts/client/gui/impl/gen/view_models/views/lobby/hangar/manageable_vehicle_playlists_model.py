from frameworks.wulf import ViewModel

class ManageableVehiclePlaylistsModel(ViewModel):
    __slots__ = (b'onReset', b'onSelectVehicle')
    INVALID_VEHICLE_INTCD = -1

    def __init__(self, properties=1, commands=2):
        super(ManageableVehiclePlaylistsModel, self).__init__(properties=properties, commands=commands)
        return

    def getIntCD(self):
        return self._getNumber(0)

    def setIntCD(self, value):
        self._setNumber(0, value)
        return

    def _initialize(self):
        super(ManageableVehiclePlaylistsModel, self)._initialize()
        self._addNumberProperty(b'intCD', 0)
        self.onReset = self._addCommand(b'onReset')
        self.onSelectVehicle = self._addCommand(b'onSelectVehicle')
        return
