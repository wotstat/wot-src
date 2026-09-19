from enum import Enum
from frameworks.wulf import Array, ViewModel
from halloween.gui.impl.gen.view_models.views.lobby.reward_view_model import RewardViewModel

class GenderEnum(Enum):
    MALE = b'male'
    FEMALE = b'female'


class RewardSelectionViewModel(ViewModel):
    __slots__ = (b'onClose', b'onClaim')

    def __init__(self, properties=3, commands=2):
        super(RewardSelectionViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getMaxCertificates(self):
        return self._getNumber(0)

    def setMaxCertificates(self, value):
        self._setNumber(0, value)
        return

    def getRewards(self):
        return self._getArray(1)

    def setRewards(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getRewardsType():
        return RewardViewModel

    def getGender(self):
        return GenderEnum(self._getString(2))

    def setGender(self, value):
        self._setString(2, value.value)
        return

    def _initialize(self):
        super(RewardSelectionViewModel, self)._initialize()
        self._addNumberProperty(b'maxCertificates', 0)
        self._addArrayProperty(b'rewards', Array())
        self._addStringProperty(b'gender')
        self.onClose = self._addCommand(b'onClose')
        self.onClaim = self._addCommand(b'onClaim')
        return
