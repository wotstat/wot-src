from gui.impl.gen.view_models.views.lobby.notifications.notification_model import NotificationModel

class LootboxNotificationViewModel(NotificationModel):
    __slots__ = (b'goToContainers',)

    def __init__(self, properties=3, commands=1):
        super(LootboxNotificationViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getCount(self):
        return self._getNumber(1)

    def setCount(self, value):
        self._setNumber(1, value)
        return

    def getIsSmallContainer(self):
        return self._getBool(2)

    def setIsSmallContainer(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(LootboxNotificationViewModel, self)._initialize()
        self._addNumberProperty(b'count', 1)
        self._addBoolProperty(b'isSmallContainer', True)
        self.goToContainers = self._addCommand(b'goToContainers')
        return
