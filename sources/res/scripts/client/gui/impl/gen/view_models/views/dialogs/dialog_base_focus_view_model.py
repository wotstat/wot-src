from frameworks.wulf import ViewModel

class DialogBaseFocusViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(DialogBaseFocusViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getFocusedIndex(self):
        return self._getNumber(0)

    def setFocusedIndex(self, value):
        self._setNumber(0, value)
        return

    def _initialize(self):
        super(DialogBaseFocusViewModel, self)._initialize()
        self._addNumberProperty(b'focusedIndex', -1)
        return
