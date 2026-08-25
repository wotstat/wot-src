from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.dog_tags.dt_component import DtComponent

class DtDogTag(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(DtDogTag, self).__init__(properties=properties, commands=commands)
        return

    @property
    def engraving(self):
        return self._getViewModel(0)

    @staticmethod
    def getEngravingType():
        return DtComponent

    @property
    def background(self):
        return self._getViewModel(1)

    @staticmethod
    def getBackgroundType():
        return DtComponent

    def getPlayerName(self):
        return self._getString(2)

    def setPlayerName(self, value):
        self._setString(2, value)
        return

    def getClanTag(self):
        return self._getString(3)

    def setClanTag(self, value):
        self._setString(3, value)
        return

    def _initialize(self):
        super(DtDogTag, self)._initialize()
        self._addViewModelProperty(b'engraving', DtComponent())
        self._addViewModelProperty(b'background', DtComponent())
        self._addStringProperty(b'playerName', b'')
        self._addStringProperty(b'clanTag', b'')
        return
