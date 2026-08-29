from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.post_progression.modification_model import ModificationModel
from gui.impl.gen.view_models.views.lobby.post_progression.step_model import StepModel

class MultiStepModel(StepModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(MultiStepModel, self).__init__(properties=properties, commands=commands)
        return

    def getParentId(self):
        return self._getNumber(6)

    def setParentId(self, value):
        self._setNumber(6, value)
        return

    def getReceivedIdx(self):
        return self._getNumber(7)

    def setReceivedIdx(self, value):
        self._setNumber(7, value)
        return

    def getSelectedIdx(self):
        return self._getNumber(8)

    def setSelectedIdx(self, value):
        self._setNumber(8, value)
        return

    def getModifications(self):
        return self._getArray(9)

    def setModifications(self, value):
        self._setArray(9, value)
        return

    @staticmethod
    def getModificationsType():
        return ModificationModel

    def _initialize(self):
        super(MultiStepModel, self)._initialize()
        self._addNumberProperty(b'parentId', 0)
        self._addNumberProperty(b'receivedIdx', -1)
        self._addNumberProperty(b'selectedIdx', -1)
        self._addArrayProperty(b'modifications', Array())
        return
