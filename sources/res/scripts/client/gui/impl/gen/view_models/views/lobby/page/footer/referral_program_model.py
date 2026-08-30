from frameworks.wulf import ViewModel

class ReferralProgramModel(ViewModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=4, commands=1):
        super(ReferralProgramModel, self).__init__(properties=properties, commands=commands)
        return

    def getFirstIndication(self):
        return self._getBool(0)

    def setFirstIndication(self, value):
        self._setBool(0, value)
        return

    def getNewReferralSeason(self):
        return self._getBool(1)

    def setNewReferralSeason(self, value):
        self._setBool(1, value)
        return

    def getEnabled(self):
        return self._getBool(2)

    def setEnabled(self, value):
        self._setBool(2, value)
        return

    def getBubbleCount(self):
        return self._getNumber(3)

    def setBubbleCount(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(ReferralProgramModel, self)._initialize()
        self._addBoolProperty(b'firstIndication', False)
        self._addBoolProperty(b'newReferralSeason', False)
        self._addBoolProperty(b'enabled', False)
        self._addNumberProperty(b'bubbleCount', 0)
        self.onClick = self._addCommand(b'onClick')
        return
