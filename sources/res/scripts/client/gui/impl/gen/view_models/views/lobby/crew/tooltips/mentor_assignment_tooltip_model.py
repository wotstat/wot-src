from frameworks.wulf import ViewModel

class MentorAssignmentTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(MentorAssignmentTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getFullName(self):
        return self._getString(0)

    def setFullName(self, value):
        self._setString(0, value)
        return

    def getHasFreeSkills(self):
        return self._getBool(1)

    def setHasFreeSkills(self, value):
        self._setBool(1, value)
        return

    def _initialize(self):
        super(MentorAssignmentTooltipModel, self)._initialize()
        self._addStringProperty(b'fullName', b'')
        self._addBoolProperty(b'hasFreeSkills', False)
        return
