from frameworks.wulf import ViewModel

class MainRewardModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(MainRewardModel, self).__init__(properties=properties, commands=commands)
        return

    def getImage(self):
        return self._getString(0)

    def setImage(self, value):
        self._setString(0, value)
        return

    def getDescription(self):
        return self._getString(1)

    def setDescription(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(MainRewardModel, self)._initialize()
        self._addStringProperty(b'image', b'')
        self._addStringProperty(b'description', b'')
        return
