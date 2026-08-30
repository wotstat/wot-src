from frameworks.wulf import ViewModel
from gui.impl.gen import R

class MapsTrainingMapModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(MapsTrainingMapModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)
        return

    def getTitle(self):
        return self._getResource(1)

    def setTitle(self, value):
        self._setResource(1, value)
        return

    def getImage(self):
        return self._getResource(2)

    def setImage(self, value):
        self._setResource(2, value)
        return

    def getIsEnabled(self):
        return self._getBool(3)

    def setIsEnabled(self, value):
        self._setBool(3, value)
        return

    def getIsCompleted(self):
        return self._getBool(4)

    def setIsCompleted(self, value):
        self._setBool(4, value)
        return

    def getGroupId(self):
        return self._getNumber(5)

    def setGroupId(self, value):
        self._setNumber(5, value)
        return

    def _initialize(self):
        super(MapsTrainingMapModel, self)._initialize()
        self._addStringProperty(b'id', b'')
        self._addResourceProperty(b'title', R.invalid())
        self._addResourceProperty(b'image', R.invalid())
        self._addBoolProperty(b'isEnabled', False)
        self._addBoolProperty(b'isCompleted', False)
        self._addNumberProperty(b'groupId', 0)
        return
