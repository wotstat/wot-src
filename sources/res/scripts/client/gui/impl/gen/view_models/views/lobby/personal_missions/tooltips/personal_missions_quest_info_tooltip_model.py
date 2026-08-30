from frameworks.wulf import ViewModel

class PersonalMissionsQuestInfoTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(PersonalMissionsQuestInfoTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getType(self):
        return self._getString(0)

    def setType(self, value):
        self._setString(0, value)
        return

    def _initialize(self):
        super(PersonalMissionsQuestInfoTooltipModel, self)._initialize()
        self._addStringProperty(b'type', b'')
        return
