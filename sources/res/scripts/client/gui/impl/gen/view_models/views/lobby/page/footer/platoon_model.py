from frameworks.wulf import Array, ViewModel
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.page.footer.platoon_member_model import PlatoonMemberModel

class PlatoonModel(ViewModel):
    __slots__ = (b'onInPlatoonAction',)
    SEARCHING = b'SEARCHING'
    IN_PLATOON = b'IN_PLATOON'
    CREATE = b'CREATE'
    DISABLED = b'DISABLED'

    def __init__(self, properties=8, commands=1):
        super(PlatoonModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return self._getString(0)

    def setState(self, value):
        self._setString(0, value)
        return

    def getUseWelcomeLayout(self):
        return self._getBool(1)

    def setUseWelcomeLayout(self, value):
        self._setBool(1, value)
        return

    def getTooltipHeader(self):
        return self._getResource(2)

    def setTooltipHeader(self, value):
        self._setResource(2, value)
        return

    def getTooltipBody(self):
        return self._getResource(3)

    def setTooltipBody(self, value):
        self._setResource(3, value)
        return

    def getTooltipParams(self):
        return self._getString(4)

    def setTooltipParams(self, value):
        self._setString(4, value)
        return

    def getCommanderIndex(self):
        return self._getNumber(5)

    def setCommanderIndex(self, value):
        self._setNumber(5, value)
        return

    def getPlayerIndex(self):
        return self._getNumber(6)

    def setPlayerIndex(self, value):
        self._setNumber(6, value)
        return

    def getMembers(self):
        return self._getArray(7)

    def setMembers(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getMembersType():
        return PlatoonMemberModel

    def _initialize(self):
        super(PlatoonModel, self)._initialize()
        self._addStringProperty(b'state', b'')
        self._addBoolProperty(b'useWelcomeLayout', False)
        self._addResourceProperty(b'tooltipHeader', R.invalid())
        self._addResourceProperty(b'tooltipBody', R.invalid())
        self._addStringProperty(b'tooltipParams', b'')
        self._addNumberProperty(b'commanderIndex', 0)
        self._addNumberProperty(b'playerIndex', 0)
        self._addArrayProperty(b'members', Array())
        self.onInPlatoonAction = self._addCommand(b'onInPlatoonAction')
        return
