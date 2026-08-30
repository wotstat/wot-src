from constants import ARENA_GUI_TYPE, QUEUE_TYPE
from gui.battle_control.arena_visitor import createByAvatar
from gui.shared.system_factory import collectCanSelectPrbEntity

class LocalStorage(object):
    __slots__ = ()

    def init(self):
        return

    def fini(self):
        return

    def swap(self):
        return

    def release(self, *args):
        return

    def suspend(self):
        return

    def isModeSelected(self):
        return False

    def clear(self):
        return

    def onAvatarBecomePlayer(self):
        return


class SessionStorage(LocalStorage):
    __slots__ = (b'_isSelected',)
    _GUI_TYPE = ARENA_GUI_TYPE.UNKNOWN

    def __init__(self):
        super(SessionStorage, self).__init__()
        self._isSelected = False
        return

    def clear(self):
        self._isSelected = False
        return

    def release(self):
        self._isSelected = True
        return

    def suspend(self):
        self.clear()
        return

    def isModeSelected(self):
        return self._isSelected

    def onAvatarBecomePlayer(self):
        arenaVisitor = createByAvatar()
        self._isSelected = self._determineSelection(arenaVisitor)
        return

    def _determineSelection(self, arenaVisitor):
        return arenaVisitor.gui.guiType == self._GUI_TYPE


class RecentPrbStorage(LocalStorage):
    __slots__ = (b'_queueType',)

    def __init__(self):
        super(RecentPrbStorage, self).__init__()
        self._queueType = QUEUE_TYPE.UNKNOWN
        return

    def clear(self):
        self._queueType = QUEUE_TYPE.UNKNOWN
        return

    @property
    def queueType(self):
        return self._queueType

    @queueType.setter
    def queueType(self, queueType):
        self._queueType = queueType
        return

    def isModeSelected(self):
        return collectCanSelectPrbEntity(self._queueType)()

    def onAvatarBecomePlayer(self):
        arenaVisitor = createByAvatar()
        self._queueType = arenaVisitor.extra.queueType
        return
