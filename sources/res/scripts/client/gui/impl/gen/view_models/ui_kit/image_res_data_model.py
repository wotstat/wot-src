from frameworks.wulf import ViewModel
from gui.impl.gen import R

class ImageResDataModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(ImageResDataModel, self).__init__(properties=properties, commands=commands)
        return

    def getImgSource(self):
        return self._getResource(0)

    def setImgSource(self, value):
        self._setResource(0, value)
        return

    def _initialize(self):
        super(ImageResDataModel, self)._initialize()
        self._addResourceProperty(b'imgSource', R.invalid())
        return
