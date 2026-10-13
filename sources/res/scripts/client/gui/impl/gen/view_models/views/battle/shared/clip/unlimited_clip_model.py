from frameworks.wulf import ViewModel

class UnlimitedClipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(UnlimitedClipModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsUnlimitedClip(self):
        return self._getBool(0)

    def setIsUnlimitedClip(self, value):
        self._setBool(0, value)
        return

    def _initialize(self):
        super(UnlimitedClipModel, self)._initialize()
        self._addBoolProperty(b'isUnlimitedClip', False)
        return
