from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.achievements.views.summary.dog_tag_model import DogTagModel

class OtherPlayerInfoModel(ViewModel):
    __slots__ = (b'onOpenProfile',)

    def __init__(self, properties=7, commands=1):
        super(OtherPlayerInfoModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def dogTagModel(self):
        return self._getViewModel(0)

    @staticmethod
    def getDogTagModelType():
        return DogTagModel

    def getIsInClan(self):
        return self._getBool(1)

    def setIsInClan(self, value):
        self._setBool(1, value)
        return

    def getClanEmblem(self):
        return self._getString(2)

    def setClanEmblem(self, value):
        self._setString(2, value)
        return

    def getClanName(self):
        return self._getString(3)

    def setClanName(self, value):
        self._setString(3, value)
        return

    def getClanPost(self):
        return self._getString(4)

    def setClanPost(self, value):
        self._setString(4, value)
        return

    def getClanJoiningTime(self):
        return self._getString(5)

    def setClanJoiningTime(self, value):
        self._setString(5, value)
        return

    def getShowClanButton(self):
        return self._getBool(6)

    def setShowClanButton(self, value):
        self._setBool(6, value)
        return

    def _initialize(self):
        super(OtherPlayerInfoModel, self)._initialize()
        self._addViewModelProperty(b'dogTagModel', DogTagModel())
        self._addBoolProperty(b'isInClan', False)
        self._addStringProperty(b'clanEmblem', b'')
        self._addStringProperty(b'clanName', b'')
        self._addStringProperty(b'clanPost', b'')
        self._addStringProperty(b'clanJoiningTime', b'')
        self._addBoolProperty(b'showClanButton', True)
        self.onOpenProfile = self._addCommand(b'onOpenProfile')
        return
