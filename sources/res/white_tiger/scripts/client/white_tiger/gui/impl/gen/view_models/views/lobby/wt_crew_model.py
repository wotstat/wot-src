from frameworks.wulf import ViewModel

class WtCrewModel(ViewModel):
    __slots__ = (b'onAboutClicked',)
    SKILL_TOOLTIP = b'crewPerkGf'

    def __init__(self, properties=4, commands=1):
        super(WtCrewModel, self).__init__(properties=properties, commands=commands)
        return

    def getTankmanID(self):
        return self._getString(0)

    def setTankmanID(self, value):
        self._setString(0, value)
        return

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)
        return

    def getInvID(self):
        return self._getNumber(2)

    def setInvID(self, value):
        self._setNumber(2, value)
        return

    def getHasSixthSense(self):
        return self._getBool(3)

    def setHasSixthSense(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(WtCrewModel, self)._initialize()
        self._addStringProperty(b'tankmanID', b'')
        self._addStringProperty(b'name', b'')
        self._addNumberProperty(b'invID', 0)
        self._addBoolProperty(b'hasSixthSense', False)
        self.onAboutClicked = self._addCommand(b'onAboutClicked')
        return
