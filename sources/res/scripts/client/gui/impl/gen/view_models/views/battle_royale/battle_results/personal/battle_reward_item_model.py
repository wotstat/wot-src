from frameworks.wulf import ViewModel

class BattleRewardItemModel(ViewModel):
    __slots__ = ()
    XP = b'xp'
    CREDITS = b'credits'
    CRYSTALS = b'crystal'
    PROGRESSION_POINTS = b'progression'
    BATTLE_PASS_POINTS = b'battlePassPoints'
    BATTLE_ROYALE_COIN = b'brcoin'
    BR_PROGRESSION_TOKEN = b'brProgressionToken'

    def __init__(self, properties=2, commands=0):
        super(BattleRewardItemModel, self).__init__(properties=properties, commands=commands)
        return

    def getType(self):
        return self._getString(0)

    def setType(self, value):
        self._setString(0, value)
        return

    def getValue(self):
        return self._getNumber(1)

    def setValue(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(BattleRewardItemModel, self)._initialize()
        self._addStringProperty(b'type', b'')
        self._addNumberProperty(b'value', 0)
        return
