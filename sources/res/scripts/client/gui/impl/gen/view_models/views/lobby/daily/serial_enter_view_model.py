from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.daily.serial_enter_day_model import SerialEnterDayModel

class SerialEnterViewModel(ViewModel):
    __slots__ = (b'onPreviewVehicle',)

    def __init__(self, properties=2, commands=1):
        super(SerialEnterViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsEnabled(self):
        return self._getBool(0)

    def setIsEnabled(self, value):
        self._setBool(0, value)
        return

    def getDays(self):
        return self._getArray(1)

    def setDays(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getDaysType():
        return SerialEnterDayModel

    def _initialize(self):
        super(SerialEnterViewModel, self)._initialize()
        self._addBoolProperty(b'isEnabled', False)
        self._addArrayProperty(b'days', Array())
        self.onPreviewVehicle = self._addCommand(b'onPreviewVehicle')
        return
