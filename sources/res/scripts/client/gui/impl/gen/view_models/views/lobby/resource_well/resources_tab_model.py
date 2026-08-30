from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.resource_well.resource_model import ResourceModel

class ResourcesTabModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(ResourcesTabModel, self).__init__(properties=properties, commands=commands)
        return

    def getType(self):
        return self._getString(0)

    def setType(self, value):
        self._setString(0, value)
        return

    def getResources(self):
        return self._getArray(1)

    def setResources(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getResourcesType():
        return ResourceModel

    def _initialize(self):
        super(ResourcesTabModel, self)._initialize()
        self._addStringProperty(b'type', b'')
        self._addArrayProperty(b'resources', Array())
        return
