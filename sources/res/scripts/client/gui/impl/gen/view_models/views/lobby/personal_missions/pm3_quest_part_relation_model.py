from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.personal_missions.pm3_quest_relation_group_model import Pm3QuestRelationGroupModel

class QuestRelationType(Enum):
    AND = b'and'
    OR = b'or'


class Pm3QuestPartRelationModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(Pm3QuestPartRelationModel, self).__init__(properties=properties, commands=commands)
        return

    def getRelationType(self):
        return QuestRelationType(self._getString(0))

    def setRelationType(self, value):
        self._setString(0, value.value)
        return

    def getGroups(self):
        return self._getArray(1)

    def setGroups(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getGroupsType():
        return Pm3QuestRelationGroupModel

    def _initialize(self):
        super(Pm3QuestPartRelationModel, self)._initialize()
        self._addStringProperty(b'relationType')
        self._addArrayProperty(b'groups', Array())
        return
