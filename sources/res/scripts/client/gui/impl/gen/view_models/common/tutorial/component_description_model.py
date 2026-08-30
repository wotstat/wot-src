from frameworks.wulf import ViewModel

class ComponentDescriptionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(ComponentDescriptionModel, self).__init__(properties=properties, commands=commands)
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

    def getPath(self):
        return self._getString(2)

    def setPath(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(ComponentDescriptionModel, self)._initialize()
        self._addStringProperty(b'viewId', b'')
        self._addStringProperty(b'componentId', b'')
        self._addStringProperty(b'path', b'')
        return
