from gui.impl.gen.view_models.common.notification_base_model import NotificationBaseModel

class StartNotificationModel(NotificationBaseModel):
    __slots__ = (b'onOpenBundle',)

    def __init__(self, properties=4, commands=1):
        super(StartNotificationModel, self).__init__(properties=properties, commands=commands)
        return

    def getBundleID(self):
        return self._getNumber(1)

    def setBundleID(self, value):
        self._setNumber(1, value)
        return

    def getBundleType(self):
        return self._getString(2)

    def setBundleType(self, value):
        self._setString(2, value)
        return

    def getIsButtonDisabled(self):
        return self._getBool(3)

    def setIsButtonDisabled(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(StartNotificationModel, self)._initialize()
        self._addNumberProperty(b'bundleID', 0)
        self._addStringProperty(b'bundleType', b'')
        self._addBoolProperty(b'isButtonDisabled', False)
        self.onOpenBundle = self._addCommand(b'onOpenBundle')
        return
