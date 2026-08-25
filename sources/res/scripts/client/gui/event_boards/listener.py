from gui.shared.utils.listeners_collection import ListenersCollection

class IEventBoardsListener(ListenersCollection):

    def __init__(self):
        super(IEventBoardsListener, self).__init__()
        self._setListenerClass(IEventBoardsListener)
        return

    def onUpdateHangarFlag(self):
        return
