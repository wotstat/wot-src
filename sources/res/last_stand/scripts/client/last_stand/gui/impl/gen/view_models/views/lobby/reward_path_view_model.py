from frameworks.wulf import Array, ViewModel
from last_stand.gui.impl.gen.view_models.views.lobby.reward_path_artefact_view_model import RewardPathArtefactViewModel

class RewardPathViewModel(ViewModel):
    __slots__ = (b'onClose', b'onViewLoaded', b'onAbout', b'onShowIntro', b'goToMission')

    def __init__(self, properties=4, commands=5):
        super(RewardPathViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getArtefacts(self):
        return self._getArray(0)

    def setArtefacts(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getArtefactsType():
        return RewardPathArtefactViewModel

    def getPoints(self):
        return self._getNumber(1)

    def setPoints(self, value):
        self._setNumber(1, value)
        return

    def getCurrentArtefactID(self):
        return self._getString(2)

    def setCurrentArtefactID(self, value):
        self._setString(2, value)
        return

    def getOpenFromQuestCard(self):
        return self._getBool(3)

    def setOpenFromQuestCard(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(RewardPathViewModel, self)._initialize()
        self._addArrayProperty(b'artefacts', Array())
        self._addNumberProperty(b'points', 0)
        self._addStringProperty(b'currentArtefactID', b'')
        self._addBoolProperty(b'openFromQuestCard', False)
        self.onClose = self._addCommand(b'onClose')
        self.onViewLoaded = self._addCommand(b'onViewLoaded')
        self.onAbout = self._addCommand(b'onAbout')
        self.onShowIntro = self._addCommand(b'onShowIntro')
        self.goToMission = self._addCommand(b'goToMission')
        return
