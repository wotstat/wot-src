from frameworks.wulf import Array
from gui.impl.gen import R
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.player_subscriptions.subscription import Subscription

class PlayerSubscriptionsModel(ViewModel):
    __slots__ = (b'onBack', b'onCardClick', b'onButtonClick')

    def __init__(self, properties=2, commands=3):
        super(PlayerSubscriptionsModel, self).__init__(properties=properties, commands=commands)
        return

    def getSubscriptions(self):
        return self._getArray(0)

    def setSubscriptions(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getSubscriptionsType():
        return Subscription

    def getWarningTitle(self):
        return self._getResource(1)

    def setWarningTitle(self, value):
        self._setResource(1, value)
        return

    def _initialize(self):
        super(PlayerSubscriptionsModel, self)._initialize()
        self._addArrayProperty(b'subscriptions', Array())
        self._addResourceProperty(b'warningTitle', R.invalid())
        self.onBack = self._addCommand(b'onBack')
        self.onCardClick = self._addCommand(b'onCardClick')
        self.onButtonClick = self._addCommand(b'onButtonClick')
        return
