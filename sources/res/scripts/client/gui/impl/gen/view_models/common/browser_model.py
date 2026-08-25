from enum import Enum
from frameworks.wulf import ViewModel

class BrowserState(Enum):
    INITIALIZATION = b'initialization'
    LOADING = b'loading'
    FORCELOADING = b'forceLoading'
    LOADED = b'loaded'


class PageState(Enum):
    INITIALIZATION = b'initialization'
    LOADING = b'loading'
    LOADED = b'loaded'
    FAILED = b'failed'


class TetxureState(Enum):
    INITIALIZATION = b'initialization'
    LOADED = b'loaded'
    FAILED = b'failed'


class BrowserModel(ViewModel):
    __slots__ = (b'createWebView', b'focus', b'unfocus', b'reload')

    def __init__(self, properties=7, commands=4):
        super(BrowserModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getNumber(0)

    def setId(self, value):
        self._setNumber(0, value)
        return

    def getBrowserState(self):
        return BrowserState(self._getString(1))

    def setBrowserState(self, value):
        self._setString(1, value.value)
        return

    def getPageState(self):
        return PageState(self._getString(2))

    def setPageState(self, value):
        self._setString(2, value.value)
        return

    def getTexState(self):
        return TetxureState(self._getString(3))

    def setTexState(self, value):
        self._setString(3, value.value)
        return

    def getHttpStatusCode(self):
        return self._getNumber(4)

    def setHttpStatusCode(self, value):
        self._setNumber(4, value)
        return

    def getTitle(self):
        return self._getString(5)

    def setTitle(self, value):
        self._setString(5, value)
        return

    def getWaitingMessage(self):
        return self._getString(6)

    def setWaitingMessage(self, value):
        self._setString(6, value)
        return

    def _initialize(self):
        super(BrowserModel, self)._initialize()
        self._addNumberProperty(b'id', 0)
        self._addStringProperty(b'browserState')
        self._addStringProperty(b'pageState')
        self._addStringProperty(b'texState')
        self._addNumberProperty(b'httpStatusCode', 0)
        self._addStringProperty(b'title', b'')
        self._addStringProperty(b'waitingMessage', b'')
        self.createWebView = self._addCommand(b'createWebView')
        self.focus = self._addCommand(b'focus')
        self.unfocus = self._addCommand(b'unfocus')
        self.reload = self._addCommand(b'reload')
        return
