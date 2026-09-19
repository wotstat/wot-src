from frameworks.wulf import Array, ViewModel
from halloween.gui.impl.gen.view_models.views.lobby.crew_member_view_model import CrewMemberViewModel

class CrewShowcaseViewModel(ViewModel):
    __slots__ = (b'onClose', b'onClaim', b'onShop', b'onPlaySound')

    def __init__(self, properties=3, commands=4):
        super(CrewShowcaseViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getCrewMembers(self):
        return self._getArray(0)

    def setCrewMembers(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getCrewMembersType():
        return CrewMemberViewModel

    def getSkills(self):
        return self._getArray(1)

    def setSkills(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getSkillsType():
        return unicode

    def getGroupVoiceover(self):
        return self._getString(2)

    def setGroupVoiceover(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(CrewShowcaseViewModel, self)._initialize()
        self._addArrayProperty(b'crewMembers', Array())
        self._addArrayProperty(b'skills', Array())
        self._addStringProperty(b'groupVoiceover', b'')
        self.onClose = self._addCommand(b'onClose')
        self.onClaim = self._addCommand(b'onClaim')
        self.onShop = self._addCommand(b'onShop')
        self.onPlaySound = self._addCommand(b'onPlaySound')
        return
