from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.vehicle_mechanic_model import VehicleMechanicModel
from gui.impl.gen.view_models.views.lobby.loadout.crew.slot_model import SlotModel

class BenefitsEnum(Enum):
    EXPERIENCE = b'experience'
    CREDITS = b'credits'
    CREWS_TRAIN = b'crewsTrain'
    REPAIR_KIT = b'repairKit'
    BONDS = b'bonds'


class OverviewModel(ViewModel):
    __slots__ = (b'onWatchMechanicsVideo',)

    def __init__(self, properties=5, commands=1):
        super(OverviewModel, self).__init__(properties=properties, commands=commands)
        return

    def getMechanics(self):
        return self._getArray(0)

    def setMechanics(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getMechanicsType():
        return VehicleMechanicModel

    def getHistoricalReference(self):
        return self._getString(1)

    def setHistoricalReference(self, value):
        self._setString(1, value)
        return

    def getCustomDescription(self):
        return self._getString(2)

    def setCustomDescription(self, value):
        self._setString(2, value)
        return

    def getCrew(self):
        return self._getArray(3)

    def setCrew(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getCrewType():
        return SlotModel

    def getBenefits(self):
        return self._getArray(4)

    def setBenefits(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getBenefitsType():
        return BenefitsEnum

    def _initialize(self):
        super(OverviewModel, self)._initialize()
        self._addArrayProperty(b'mechanics', Array())
        self._addStringProperty(b'historicalReference', b'')
        self._addStringProperty(b'customDescription', b'')
        self._addArrayProperty(b'crew', Array())
        self._addArrayProperty(b'benefits', Array())
        self.onWatchMechanicsVideo = self._addCommand(b'onWatchMechanicsVideo')
        return
