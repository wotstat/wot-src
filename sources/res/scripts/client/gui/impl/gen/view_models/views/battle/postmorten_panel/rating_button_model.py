from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen import R

class RateButtonEnum(Enum):
    WORSE = b'worse'
    USUAL = b'usual'
    BETTER = b'better'
    UNSET = b'unset'


class RatingButtonModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(RatingButtonModel, self).__init__(properties=properties, commands=commands)
        return

    def getButtonVariant(self):
        return RateButtonEnum(self._getString(0))

    def setButtonVariant(self, value):
        self._setString(0, value.value)
        return

    def getFeedbackString(self):
        return self._getResource(1)

    def setFeedbackString(self, value):
        self._setResource(1, value)
        return

    def _initialize(self):
        super(RatingButtonModel, self)._initialize()
        self._addStringProperty(b'buttonVariant')
        self._addResourceProperty(b'feedbackString', R.invalid())
        return
