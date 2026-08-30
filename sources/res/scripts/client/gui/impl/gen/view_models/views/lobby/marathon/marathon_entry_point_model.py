from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.marathon.base_event_model import BaseEventModel

class MarathonEntryPointModel(ViewModel):
    __slots__ = (b'onClick',)
    STATE_MARATHON_DISABLED = -1
    STATE_MARATHON_NOT_STARTED = 0
    STATE_MARATHON_IN_PROGRESS = 1
    STATE_MARATHON_FINISHED = 3

    def __init__(self, properties=19, commands=1):
        super(MarathonEntryPointModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def progressGrind(self):
        return self._getViewModel(0)

    @staticmethod
    def getProgressGrindType():
        return BaseEventModel

    @property
    def progressPro(self):
        return self._getViewModel(1)

    @staticmethod
    def getProgressProType():
        return BaseEventModel

    @property
    def progressPost(self):
        return self._getViewModel(2)

    @staticmethod
    def getProgressPostType():
        return BaseEventModel

    def getState(self):
        return self._getNumber(3)

    def setState(self, value):
        self._setNumber(3, value)
        return

    def getTimeTillNextState(self):
        return self._getNumber(4)

    def setTimeTillNextState(self, value):
        self._setNumber(4, value)
        return

    def getFormattedTimeTillNextState(self):
        return self._getString(5)

    def setFormattedTimeTillNextState(self, value):
        self._setString(5, value)
        return

    def getCurrentPhase(self):
        return self._getNumber(6)

    def setCurrentPhase(self, value):
        self._setNumber(6, value)
        return

    def getRewardObtained(self):
        return self._getBool(7)

    def setRewardObtained(self, value):
        self._setBool(7, value)
        return

    def getIsPremShopURL(self):
        return self._getBool(8)

    def setIsPremShopURL(self, value):
        self._setBool(8, value)
        return

    def getIsPostProgression(self):
        return self._getBool(9)

    def setIsPostProgression(self, value):
        self._setBool(9, value)
        return

    def getIsVehicleInHangar(self):
        return self._getBool(10)

    def setIsVehicleInHangar(self, value):
        self._setBool(10, value)
        return

    def getIsVehicleStyleInHangar(self):
        return self._getBool(11)

    def setIsVehicleStyleInHangar(self, value):
        self._setBool(11, value)
        return

    def getIsPostQuestDone(self):
        return self._getBool(12)

    def setIsPostQuestDone(self, value):
        self._setBool(12, value)
        return

    def getCurrentPostQuestIndex(self):
        return self._getNumber(13)

    def setCurrentPostQuestIndex(self, value):
        self._setNumber(13, value)
        return

    def getFormattedTimeTillPostQuestFinish(self):
        return self._getString(14)

    def setFormattedTimeTillPostQuestFinish(self, value):
        self._setString(14, value)
        return

    def getDiscount(self):
        return self._getReal(15)

    def setDiscount(self, value):
        self._setReal(15, value)
        return

    def getTokenTemplate(self):
        return self._getString(16)

    def setTokenTemplate(self, value):
        self._setString(16, value)
        return

    def getTokenDoneTemplate(self):
        return self._getString(17)

    def setTokenDoneTemplate(self, value):
        self._setString(17, value)
        return

    def getUserTokens(self):
        return self._getArray(18)

    def setUserTokens(self, value):
        self._setArray(18, value)
        return

    @staticmethod
    def getUserTokensType():
        return unicode

    def _initialize(self):
        super(MarathonEntryPointModel, self)._initialize()
        self._addViewModelProperty(b'progressGrind', UserListModel())
        self._addViewModelProperty(b'progressPro', UserListModel())
        self._addViewModelProperty(b'progressPost', UserListModel())
        self._addNumberProperty(b'state', -1)
        self._addNumberProperty(b'timeTillNextState', -1)
        self._addStringProperty(b'formattedTimeTillNextState', b'')
        self._addNumberProperty(b'currentPhase', -1)
        self._addBoolProperty(b'rewardObtained', False)
        self._addBoolProperty(b'isPremShopURL', False)
        self._addBoolProperty(b'isPostProgression', False)
        self._addBoolProperty(b'isVehicleInHangar', False)
        self._addBoolProperty(b'isVehicleStyleInHangar', False)
        self._addBoolProperty(b'isPostQuestDone', False)
        self._addNumberProperty(b'currentPostQuestIndex', 0)
        self._addStringProperty(b'formattedTimeTillPostQuestFinish', b'')
        self._addRealProperty(b'discount', 0.0)
        self._addStringProperty(b'tokenTemplate', b'')
        self._addStringProperty(b'tokenDoneTemplate', b'')
        self._addArrayProperty(b'userTokens', Array())
        self.onClick = self._addCommand(b'onClick')
        return
