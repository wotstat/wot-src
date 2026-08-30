from gui.impl.gen import R
from frameworks.wulf import ViewModel

class ImageResStrModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(ImageResStrModel, self).__init__(properties=properties, commands=commands)
        return

    def getImgSource(self):
        return self._getResource(0)

    def setImgSource(self, value):
        self._setResource(0, value)
        return

    def _initialize(self):
        super(ImageResStrModel, self)._initialize()
        self._addResourceProperty(b'imgSource', R.invalid())
        return
