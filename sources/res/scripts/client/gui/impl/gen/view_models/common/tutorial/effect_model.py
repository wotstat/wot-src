from frameworks.wulf import ViewModel

class EffectModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(EffectModel, self).__init__(properties=properties, commands=commands)
        return

    def getViewId(self):
        return self._getString(0)

    def setViewId(self, value):
        self._setString(0, value)
        return

    def getComponentId(self):
        return self._getString(1)

    def setComponentId(self, value):
        self._setString(1, value)
        return

    def getType(self):
        return self._getString(2)

    def setType(self, value):
        self._setString(2, value)
        return

    def getBuilder(self):
        return self._getString(3)

    def setBuilder(self, value):
        self._setString(3, value)
        return

    def _initialize(self):
        super(EffectModel, self)._initialize()
        self._addStringProperty(b'viewId', b'')
        self._addStringProperty(b'componentId', b'')
        self._addStringProperty(b'type', b'')
        self._addStringProperty(b'builder', b'')
        return
