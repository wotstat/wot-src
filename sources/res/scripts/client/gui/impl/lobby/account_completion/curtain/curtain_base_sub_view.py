import typing
from typing import Type
from Event import Event
from frameworks.wulf import ViewModel, ViewSettings
from gui.impl.gen import R
from gui.impl.pub import ViewImpl
if typing.TYPE_CHECKING:
    from gui.impl.gen_utils import DynAccessor

class CurtainBaseSubView(ViewImpl):
    __slots__ = (b'_isActive', b'_isHidden', b'onWaitingChanged', b'_isWaitingVisible', b'_waitingMsgResID')
    _LAYOUT_DYN_ACCESSOR = R.invalid
    _VIEW_MODEL_CLASS = ViewModel

    def __init__(self):
        settings = ViewSettings(self._LAYOUT_DYN_ACCESSOR())
        settings.model = self._VIEW_MODEL_CLASS()
        super(CurtainBaseSubView, self).__init__(settings)
        self._isActive = False
        self._isHidden = False
        self.onWaitingChanged = Event()
        self._isWaitingVisible = False
        self._waitingMsgResID = R.invalid()
        return

    @property
    def isActive(self):
        return self._isActive

    @property
    def isWaitingVisible(self):
        return self._isWaitingVisible

    @property
    def waitingMsgResID(self):
        return self._waitingMsgResID

    @property
    def isHidden(self):
        return self._isHidden

    def activate(self, *args, **kwargs):
        self._isActive = True
        return

    def deactivate(self):
        self._isActive = False
        return

    def hide(self):
        self._isHidden = True
        return

    def reveal(self):
        self._isHidden = False
        return

    def _finalize(self):
        if self._isActive:
            self.deactivate()
        self._doFinalize()
        super(CurtainBaseSubView, self)._finalize()
        return

    def _doFinalize(self):
        return

    def _setWaiting(self, isVisible, msgResID=R.invalid()):
        self._isWaitingVisible = isVisible
        self._waitingMsgResID = msgResID
        self.onWaitingChanged(isVisible, msgResID)
        return
