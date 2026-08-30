from frameworks.wulf import ViewModel

class DialogTemplatePlaceHolderViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(DialogTemplatePlaceHolderViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getResourceID(self):
        return self._getNumber(0)

    def setResourceID(self, value):
        self._setNumber(0, value)
        return

    def getPlaceHolder(self):
        return self._getString(1)

    def setPlaceHolder(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(DialogTemplatePlaceHolderViewModel, self)._initialize()
        self._addNumberProperty(b'resourceID', 0)
        self._addStringProperty(b'placeHolder', b'')
        return
