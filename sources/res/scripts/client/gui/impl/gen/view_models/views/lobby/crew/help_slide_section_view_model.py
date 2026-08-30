from enum import Enum
from gui.impl.gen import R
from frameworks.wulf import ViewModel

class SlideSectionSize(Enum):
    SMALL = b'small'
    BIG = b'big'


class HelpSlideSectionViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(HelpSlideSectionViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getImage(self):
        return self._getResource(0)

    def setImage(self, value):
        self._setResource(0, value)
        return

    def getDescription(self):
        return self._getResource(1)

    def setDescription(self, value):
        self._setResource(1, value)
        return

    def getSize(self):
        return SlideSectionSize(self._getString(2))

    def setSize(self, value):
        self._setString(2, value.value)
        return

    def _initialize(self):
        super(HelpSlideSectionViewModel, self)._initialize()
        self._addResourceProperty(b'image', R.invalid())
        self._addResourceProperty(b'description', R.invalid())
        self._addStringProperty(b'size')
        return
