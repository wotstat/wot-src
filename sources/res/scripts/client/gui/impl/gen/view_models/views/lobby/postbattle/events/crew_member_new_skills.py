from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.postbattle.events.base_event_model import BaseEventModel
from gui.impl.gen.view_models.views.lobby.postbattle.events.crew_member import CrewMember

class CrewMemberNewSkills(BaseEventModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=1):
        super(CrewMemberNewSkills, self).__init__(properties=properties, commands=commands)
        return

    def getCrewMembers(self):
        return self._getArray(2)

    def setCrewMembers(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getCrewMembersType():
        return CrewMember

    def _initialize(self):
        super(CrewMemberNewSkills, self)._initialize()
        self._addArrayProperty(b'crewMembers', Array())
        return
