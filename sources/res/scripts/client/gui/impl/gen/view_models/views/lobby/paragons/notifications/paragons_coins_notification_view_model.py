from gui.impl.gen.view_models.views.lobby.notifications.notification_model import NotificationModel

class ParagonsCoinsNotificationViewModel(NotificationModel):
    __slots__ = (b'goToTechTree', b'goToParagons')

    def __init__(self, properties=4, commands=2):
        super(ParagonsCoinsNotificationViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsEntryPointAvailable(self):
        return self._getBool(1)

    def setIsEntryPointAvailable(self, value):
        self._setBool(1, value)
        return

    def getCount(self):
        return self._getNumber(2)

    def setCount(self, value):
        self._setNumber(2, value)
        return

    def getMinVehicleCount(self):
        return self._getNumber(3)

    def setMinVehicleCount(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(ParagonsCoinsNotificationViewModel, self)._initialize()
        self._addBoolProperty(b'isEntryPointAvailable', False)
        self._addNumberProperty(b'count', 1)
        self._addNumberProperty(b'minVehicleCount', 1)
        self.goToTechTree = self._addCommand(b'goToTechTree')
        self.goToParagons = self._addCommand(b'goToParagons')
        return
