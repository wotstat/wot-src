from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.daily.session_progress_reward_bonus_model import SessionProgressRewardBonusModel

class SessionProgressRewardScreenModel(ViewModel):
    __slots__ = (b'onClose', b'onShowInHangar')

    def __init__(self, properties=1, commands=2):
        super(SessionProgressRewardScreenModel, self).__init__(properties=properties, commands=commands)
        return

    def getRewards(self):
        return self._getArray(0)

    def setRewards(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getRewardsType():
        return SessionProgressRewardBonusModel

    def _initialize(self):
        super(SessionProgressRewardScreenModel, self)._initialize()
        self._addArrayProperty(b'rewards', Array())
        self.onClose = self._addCommand(b'onClose')
        self.onShowInHangar = self._addCommand(b'onShowInHangar')
        return
