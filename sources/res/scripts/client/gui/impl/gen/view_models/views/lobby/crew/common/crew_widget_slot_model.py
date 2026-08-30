from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.crew.common.crew_widget_tankman_model import CrewWidgetTankmanModel

class CrewWidgetSlotModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(CrewWidgetSlotModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def tankman(self):
        return self._getViewModel(0)

    @staticmethod
    def getTankmanType():
        return CrewWidgetTankmanModel

    def getSlotIdx(self):
        return self._getNumber(1)

    def setSlotIdx(self, value):
        self._setNumber(1, value)
        return

    def getRoles(self):
        return self._getArray(2)

    def setRoles(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getRolesType():
        return unicode

    def _initialize(self):
        super(CrewWidgetSlotModel, self)._initialize()
        self._addViewModelProperty(b'tankman', CrewWidgetTankmanModel())
        self._addNumberProperty(b'slotIdx', 0)
        self._addArrayProperty(b'roles', Array())
        return
