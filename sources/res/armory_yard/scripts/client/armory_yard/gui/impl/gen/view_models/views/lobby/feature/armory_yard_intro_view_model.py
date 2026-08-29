from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel

class ArmoryYardIntroViewModel(VehicleInfoModel):
    __slots__ = (b'onClose', b'onContinue', b'onGoBack')

    def __init__(self, properties=13, commands=3):
        super(ArmoryYardIntroViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getStartDate(self):
        return self._getNumber(10)

    def setStartDate(self, value):
        self._setNumber(10, value)
        return

    def getEndDate(self):
        return self._getNumber(11)

    def setEndDate(self, value):
        self._setNumber(11, value)
        return

    def getHasIntroVideoLink(self):
        return self._getBool(12)

    def setHasIntroVideoLink(self, value):
        self._setBool(12, value)
        return

    def _initialize(self):
        super(ArmoryYardIntroViewModel, self)._initialize()
        self._addNumberProperty(b'startDate', 0)
        self._addNumberProperty(b'endDate', 0)
        self._addBoolProperty(b'hasIntroVideoLink', False)
        self.onClose = self._addCommand(b'onClose')
        self.onContinue = self._addCommand(b'onContinue')
        self.onGoBack = self._addCommand(b'onGoBack')
        return
