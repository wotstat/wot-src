from frameworks.wulf import ViewModel

class CrewMembersFlagModel(ViewModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=1, commands=1):
        super(CrewMembersFlagModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsHidden(self):
        return self._getBool(0)

    def setIsHidden(self, value):
        self._setBool(0, value)
        return

    def _initialize(self):
        super(CrewMembersFlagModel, self)._initialize()
        self._addBoolProperty(b'isHidden', False)
        self.onClick = self._addCommand(b'onClick')
        return
