from gui.impl.gen import R
from frameworks.wulf import ViewModel

class IntroSlideModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(IntroSlideModel, self).__init__(properties=properties, commands=commands)
        return

    def getIcon(self):
        return self._getResource(0)

    def setIcon(self, value):
        self._setResource(0, value)
        return

    def getTitle(self):
        return self._getResource(1)

    def setTitle(self, value):
        self._setResource(1, value)
        return

    def getDescription(self):
        return self._getString(2)

    def setDescription(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(IntroSlideModel, self)._initialize()
        self._addResourceProperty(b'icon', R.invalid())
        self._addResourceProperty(b'title', R.invalid())
        self._addStringProperty(b'description', b'')
        return
