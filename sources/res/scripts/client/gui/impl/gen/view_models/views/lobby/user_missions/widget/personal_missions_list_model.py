from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.user_missions.widget.personal_mission_model import PersonalMissionModel

class PersonalMissionsListModel(ViewModel):
    __slots__ = (b'onClick', b'onMarkAsViewed')

    def __init__(self, properties=2, commands=2):
        super(PersonalMissionsListModel, self).__init__(properties=properties, commands=commands)
        return

    def getMissions(self):
        return self._getArray(0)

    def setMissions(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getMissionsType():
        return PersonalMissionModel

    def getReadyForAnimations(self):
        return self._getBool(1)

    def setReadyForAnimations(self, value):
        self._setBool(1, value)
        return

    def _initialize(self):
        super(PersonalMissionsListModel, self)._initialize()
        self._addArrayProperty(b'missions', Array())
        self._addBoolProperty(b'readyForAnimations', False)
        self.onClick = self._addCommand(b'onClick')
        self.onMarkAsViewed = self._addCommand(b'onMarkAsViewed')
        return
