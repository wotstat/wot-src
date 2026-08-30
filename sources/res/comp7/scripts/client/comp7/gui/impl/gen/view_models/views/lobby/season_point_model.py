from comp7.gui.impl.gen.view_models.views.lobby.enums import SeasonName, SeasonPointState
from frameworks.wulf import ViewModel

class SeasonPointModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(SeasonPointModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return SeasonPointState(self._getString(0))

    def setState(self, value):
        self._setString(0, value.value)
        return

    def getSeason(self):
        return SeasonName(self._getString(1))

    def setSeason(self, value):
        self._setString(1, value.value)
        return

    def _initialize(self):
        super(SeasonPointModel, self)._initialize()
        self._addStringProperty(b'state')
        self._addStringProperty(b'season')
        return
