from frameworks.wulf import ViewModel

class SubscriptionDailyQuestsIntroModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=0, commands=1):
        super(SubscriptionDailyQuestsIntroModel, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(SubscriptionDailyQuestsIntroModel, self)._initialize()
        self.onClose = self._addCommand(b'onClose')
        return
