from gui.impl.gen.view_models.views.lobby.personal_missions_30.common.enums import MissionCategory
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.personal_missions_30.missions_model import MissionsModel

class MissionsStateModel(ViewModel):
    __slots__ = (b'changeCategory',)

    def __init__(self, properties=2, commands=1):
        super(MissionsStateModel, self).__init__(properties=properties, commands=commands)
        return

    def getAllMissions(self):
        return self._getArray(0)

    def setAllMissions(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getAllMissionsType():
        return MissionsModel

    def getMissionsCategory(self):
        return MissionCategory(self._getString(1))

    def setMissionsCategory(self, value):
        self._setString(1, value.value)
        return

    def _initialize(self):
        super(MissionsStateModel, self)._initialize()
        self._addArrayProperty(b'allMissions', Array())
        self._addStringProperty(b'missionsCategory')
        self.changeCategory = self._addCommand(b'changeCategory')
        return
