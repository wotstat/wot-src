from frameworks.wulf import Array
from frontline.gui.impl.gen.view_models.views.battle.fl_progression_model import FlProgressionModel
from frontline.gui.impl.gen.view_models.views.battle.quests_model import QuestsModel

class QuestsTabModel(QuestsModel):
    __slots__ = ()

    def __init__(self, properties=13, commands=0):
        super(QuestsTabModel, self).__init__(properties=properties, commands=commands)
        return

    def getSectorName(self):
        return self._getString(9)

    def setSectorName(self, value):
        self._setString(9, value)
        return

    def getIsClientReady(self):
        return self._getBool(10)

    def setIsClientReady(self, value):
        self._setBool(10, value)
        return

    def getIsLastLine(self):
        return self._getBool(11)

    def setIsLastLine(self, value):
        self._setBool(11, value)
        return

    def getProgressions(self):
        return self._getArray(12)

    def setProgressions(self, value):
        self._setArray(12, value)
        return

    @staticmethod
    def getProgressionsType():
        return FlProgressionModel

    def _initialize(self):
        super(QuestsTabModel, self)._initialize()
        self._addStringProperty(b'sectorName', b'')
        self._addBoolProperty(b'isClientReady', False)
        self._addBoolProperty(b'isLastLine', False)
        self._addArrayProperty(b'progressions', Array())
        return
