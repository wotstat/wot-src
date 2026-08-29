class ISelectableObject(object):

    def __init__(self):
        super(ISelectableObject, self).__init__()
        if not hasattr(self, b'selectionId'):
            self.selectionId = b''
        if not hasattr(self, b'mouseOverSoundName'):
            self.mouseOverSoundName = b''
        return

    @property
    def enabled(self):
        raise NotImplementedError
        return

    def setEnable(self, enabled):
        raise NotImplementedError
        return

    def setHighlight(self, show):
        raise NotImplementedError
        return

    def onMouseDown(self):
        return

    def onMouseUp(self):
        return

    def onMouseClick(self):
        return


class ISelectableLogic(object):
    __slots__ = ()

    def init(self, callback=None):
        raise NotImplementedError
        return

    def fini(self):
        raise NotImplementedError
        return

    def _onMouseEnter(self, entity):
        raise NotImplementedError
        return

    def _onMouseExit(self, entity):
        raise NotImplementedError
        return

    def _onMouseDown(self):
        raise NotImplementedError
        return

    def _onMouseUp(self):
        raise NotImplementedError
        return

    def _onNotifyCursorOver3dScene(self, isCursorOver3dScene):
        raise NotImplementedError
        return

    def _filterEntity(self, entity):
        raise NotImplementedError
        return


class ISelectableLogicCallback(object):

    def onHighlight3DEntity(self, entity):
        raise NotImplementedError
        return

    def onFade3DEntity(self, entity):
        raise NotImplementedError
        return
