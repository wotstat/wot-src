from enum import Enum
from frameworks.wulf import ViewModel

class Type(Enum):
    NEWS = b'news'
    SHOPPROMO = b'shopPromo'
    NONE = b'none'


class TeaserModel(ViewModel):
    __slots__ = (b'onClick', b'onClose')

    def __init__(self, properties=7, commands=2):
        super(TeaserModel, self).__init__(properties=properties, commands=commands)
        return

    def getType(self):
        return Type(self._getString(0))

    def setType(self, value):
        self._setString(0, value.value)
        return

    def getPostCounter(self):
        return self._getNumber(1)

    def setPostCounter(self, value):
        self._setNumber(1, value)
        return

    def getDescription(self):
        return self._getString(2)

    def setDescription(self, value):
        self._setString(2, value)
        return

    def getText(self):
        return self._getString(3)

    def setText(self, value):
        self._setString(3, value)
        return

    def getIsVideo(self):
        return self._getBool(4)

    def setIsVideo(self, value):
        self._setBool(4, value)
        return

    def getFinishTime(self):
        return self._getNumber(5)

    def setFinishTime(self, value):
        self._setNumber(5, value)
        return

    def getImage(self):
        return self._getString(6)

    def setImage(self, value):
        self._setString(6, value)
        return

    def _initialize(self):
        super(TeaserModel, self)._initialize()
        self._addStringProperty(b'type', Type.NONE.value)
        self._addNumberProperty(b'postCounter', 0)
        self._addStringProperty(b'description', b'')
        self._addStringProperty(b'text', b'')
        self._addBoolProperty(b'isVideo', False)
        self._addNumberProperty(b'finishTime', -1)
        self._addStringProperty(b'image', b'')
        self.onClick = self._addCommand(b'onClick')
        self.onClose = self._addCommand(b'onClose')
        return
