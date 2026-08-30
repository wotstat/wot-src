from frameworks.wulf import ViewModel
from gui.impl.gen import R

class RoleActionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(RoleActionModel, self).__init__(properties=properties, commands=commands)
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

    def _initialize(self):
        super(RoleActionModel, self)._initialize()
        self._addResourceProperty(b'image', R.invalid())
        self._addResourceProperty(b'description', R.invalid())
        return
