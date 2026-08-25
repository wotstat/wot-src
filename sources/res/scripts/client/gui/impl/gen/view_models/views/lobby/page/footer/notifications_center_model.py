from frameworks.wulf import ViewModel

class NotificationsCenterModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(NotificationsCenterModel, self).__init__(properties=properties, commands=commands)
        return

    def getNewNotificationsCount(self):
        return self._getNumber(0)

    def setNewNotificationsCount(self, value):
        self._setNumber(0, value)
        return

    def getHasImportantNotification(self):
        return self._getBool(1)

    def setHasImportantNotification(self, value):
        self._setBool(1, value)
        return

    def _initialize(self):
        super(NotificationsCenterModel, self)._initialize()
        self._addNumberProperty(b'newNotificationsCount', 0)
        self._addBoolProperty(b'hasImportantNotification', False)
        return
