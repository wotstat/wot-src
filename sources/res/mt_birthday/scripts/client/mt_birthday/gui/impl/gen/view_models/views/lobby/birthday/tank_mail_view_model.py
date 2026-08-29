from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from mt_birthday.gui.impl.gen.view_models.views.lobby.birthday.progression import Progression
from mt_birthday.gui.impl.gen.view_models.views.lobby.birthday.user_item import UserItem

class TankMailViewModel(ViewModel):
    __slots__ = (b'onPhraseChange', b'onPlayerSelect', b'onSent', b'onTasks', b'onAnimationEnded', b'onComponentDestroyed')

    def __init__(self, properties=7, commands=6):
        super(TankMailViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def progression(self):
        return self._getViewModel(0)

    @staticmethod
    def getProgressionType():
        return Progression

    def getCurrencyCount(self):
        return self._getNumber(1)

    def setCurrencyCount(self, value):
        self._setNumber(1, value)
        return

    def getIsSentError(self):
        return self._getBool(2)

    def setIsSentError(self, value):
        self._setBool(2, value)
        return

    def getIsPostError(self):
        return self._getBool(3)

    def setIsPostError(self, value):
        self._setBool(3, value)
        return

    def getIsSending(self):
        return self._getBool(4)

    def setIsSending(self, value):
        self._setBool(4, value)
        return

    def getPhraseID(self):
        return self._getNumber(5)

    def setPhraseID(self, value):
        self._setNumber(5, value)
        return

    def getSelectedUsers(self):
        return self._getArray(6)

    def setSelectedUsers(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getSelectedUsersType():
        return UserItem

    def _initialize(self):
        super(TankMailViewModel, self)._initialize()
        self._addViewModelProperty(b'progression', Progression())
        self._addNumberProperty(b'currencyCount', 0)
        self._addBoolProperty(b'isSentError', False)
        self._addBoolProperty(b'isPostError', False)
        self._addBoolProperty(b'isSending', False)
        self._addNumberProperty(b'phraseID', 1)
        self._addArrayProperty(b'selectedUsers', Array())
        self.onPhraseChange = self._addCommand(b'onPhraseChange')
        self.onPlayerSelect = self._addCommand(b'onPlayerSelect')
        self.onSent = self._addCommand(b'onSent')
        self.onTasks = self._addCommand(b'onTasks')
        self.onAnimationEnded = self._addCommand(b'onAnimationEnded')
        self.onComponentDestroyed = self._addCommand(b'onComponentDestroyed')
        return
