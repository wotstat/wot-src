from gui.impl.gen.view_models.views.battle.battle_context_hints.base_battle_context_hint_model import BaseBattleContextHintModel

class InfoBattleContextHintModel(BaseBattleContextHintModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=1):
        super(InfoBattleContextHintModel, self).__init__(properties=properties, commands=commands)
        return

    def getDuration(self):
        return self._getReal(1)

    def setDuration(self, value):
        self._setReal(1, value)
        return

    def getHintId(self):
        return self._getString(2)

    def setHintId(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(InfoBattleContextHintModel, self)._initialize()
        self._addRealProperty(b'duration', 0.0)
        self._addStringProperty(b'hintId', b'')
        return
