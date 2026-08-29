import logging, typing
from frameworks.wulf import WindowFlags, WindowLayer, ViewSettings
from gui.impl.gen import R
from gui.impl.pub import ViewImpl
from gui.impl.pub.lobby_window import LobbyWindow
if typing.TYPE_CHECKING:
    from frameworks.wulf import Window, View, ViewModel
_logger = logging.getLogger(__name__)
_HANDLERS_TYPES_LIST = []

def getUniqueRewardHandler(resultData):
    for handlerType in _HANDLERS_TYPES_LIST:
        possibleHandler = handlerType.createHandler(resultData)
        if possibleHandler is not None:
            return possibleHandler

    return


class IUniqueRewardHandler(object):

    def __init__(self, _):
        super(IUniqueRewardHandler, self).__init__()
        return

    @classmethod
    def createHandler(cls, resultData):
        raise NotImplementedError
        return

    def getRewardsData(self):
        raise NotImplementedError
        return

    def getRewardsViewID(self):
        raise NotImplementedError
        return

    def showRewardsWindow(self, parent):
        raise NotImplementedError
        return

    def _getRewardsViewClass(self):
        raise NotImplementedError
        return


class BaseUniqueRewardHandler(IUniqueRewardHandler):
    __slots__ = (b'_rewardsData', b'_window')

    def __init__(self, rewardsData):
        super(BaseUniqueRewardHandler, self).__init__(rewardsData)
        self._rewardsData = rewardsData
        self._window = None
        return

    @classmethod
    def createHandler(cls, resultData):
        return

    def getRewardsData(self):
        return self._rewardsData

    def getRewardsViewID(self):
        return R.invalid()

    def showRewardsWindow(self, parent):
        self._window = UniqueLootBoxesRewardsWindow(self._getRewardsViewClass()(self.getRewardsViewID(), self._rewardsData), parent=parent)
        self._window.load()
        return

    def _getRewardsViewClass(self):
        return BaseUniqueRewardsView


class UniqueLootBoxesRewardsWindow(LobbyWindow):

    def __init__(self, content, parent=None):
        super(UniqueLootBoxesRewardsWindow, self).__init__(WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, None, content, parent, WindowLayer.OVERLAY)
        return


class BaseUniqueRewardsView(ViewImpl):
    __slots__ = (b'_rewards',)

    def __init__(self, layoutID, rewards, model=None):
        settings = ViewSettings(layoutID)
        settings.model = model
        super(BaseUniqueRewardsView, self).__init__(settings)
        self._rewards = rewards
        return


def registerHandler(handlerType):
    _HANDLERS_TYPES_LIST.append(handlerType)
    return


def unregisterHandler(handlerType):
    if handlerType in _HANDLERS_TYPES_LIST:
        _HANDLERS_TYPES_LIST.remove(handlerType)
    return
