from frameworks.wulf import Array, ViewModel
from gui.impl.gen import R
from gui.impl.wrappers.user_list_model import UserListModel

class DialogWindowModel(ViewModel):
    __slots__ = (b'onClosed', b'onBtnClicked')

    def __init__(self, properties=14, commands=2):
        super(DialogWindowModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def buttons(self):
        return self._getViewModel(0)

    @staticmethod
    def getButtonsType():
        return UserListModel

    def getIcon(self):
        return self._getResource(1)

    def setIcon(self, value):
        self._setResource(1, value)
        return

    def getIconHighlight(self):
        return self._getResource(2)

    def setIconHighlight(self, value):
        self._setResource(2, value)
        return

    def getAnimationHighlight(self):
        return self._getResource(3)

    def setAnimationHighlight(self, value):
        self._setResource(3, value)
        return

    def getTitle(self):
        return self._getResource(4)

    def setTitle(self, value):
        self._setResource(4, value)
        return

    def getFormattedTitle(self):
        return self._getString(5)

    def setFormattedTitle(self, value):
        self._setString(5, value)
        return

    def getTitleArgs(self):
        return self._getArray(6)

    def setTitleArgs(self, value):
        self._setArray(6, value)
        return

    def getTitleFmtArgs(self):
        return self._getArray(7)

    def setTitleFmtArgs(self, value):
        self._setArray(7, value)
        return

    def getIsTitleFmtArgsNamed(self):
        return self._getBool(8)

    def setIsTitleFmtArgsNamed(self, value):
        self._setBool(8, value)
        return

    def getBackgroundImage(self):
        return self._getResource(9)

    def setBackgroundImage(self, value):
        self._setResource(9, value)
        return

    def getShowSoundId(self):
        return self._getResource(10)

    def setShowSoundId(self, value):
        self._setResource(10, value)
        return

    def getPreset(self):
        return self._getString(11)

    def setPreset(self, value):
        self._setString(11, value)
        return

    def getHasBalance(self):
        return self._getBool(12)

    def setHasBalance(self, value):
        self._setBool(12, value)
        return

    def getHasBottomContent(self):
        return self._getBool(13)

    def setHasBottomContent(self, value):
        self._setBool(13, value)
        return

    def _initialize(self):
        super(DialogWindowModel, self)._initialize()
        self._addViewModelProperty(b'buttons', UserListModel())
        self._addResourceProperty(b'icon', R.invalid())
        self._addResourceProperty(b'iconHighlight', R.invalid())
        self._addResourceProperty(b'animationHighlight', R.invalid())
        self._addResourceProperty(b'title', R.invalid())
        self._addStringProperty(b'formattedTitle', b'')
        self._addArrayProperty(b'titleArgs', Array())
        self._addArrayProperty(b'titleFmtArgs', Array())
        self._addBoolProperty(b'isTitleFmtArgsNamed', True)
        self._addResourceProperty(b'backgroundImage', R.invalid())
        self._addResourceProperty(b'showSoundId', R.invalid())
        self._addStringProperty(b'preset', b'default')
        self._addBoolProperty(b'hasBalance', False)
        self._addBoolProperty(b'hasBottomContent', False)
        self.onClosed = self._addCommand(b'onClosed')
        self.onBtnClicked = self._addCommand(b'onBtnClicked')
        return
