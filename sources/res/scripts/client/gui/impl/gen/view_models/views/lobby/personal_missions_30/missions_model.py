from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.personal_missions_30.missions_categorizations_model import MissionsCategorizationsModel

class MissionsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(MissionsModel, self).__init__(properties=properties, commands=commands)
        return

    def getOperationId(self):
        return self._getNumber(0)

    def setOperationId(self, value):
        self._setNumber(0, value)
        return

    def getOperationName(self):
        return self._getString(1)

    def setOperationName(self, value):
        self._setString(1, value)
        return

    def getMinRequiredVehicle(self):
        return self._getNumber(2)

    def setMinRequiredVehicle(self, value):
        self._setNumber(2, value)
        return

    def getMaxRequiredVehicle(self):
        return self._getNumber(3)

    def setMaxRequiredVehicle(self, value):
        self._setNumber(3, value)
        return

    def getMissionsCategorizations(self):
        return self._getArray(4)

    def setMissionsCategorizations(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getMissionsCategorizationsType():
        return MissionsCategorizationsModel

    def _initialize(self):
        super(MissionsModel, self)._initialize()
        self._addNumberProperty(b'operationId', 0)
        self._addStringProperty(b'operationName', b'')
        self._addNumberProperty(b'minRequiredVehicle', 0)
        self._addNumberProperty(b'maxRequiredVehicle', 0)
        self._addArrayProperty(b'missionsCategorizations', Array())
        return
