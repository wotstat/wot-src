from gui.impl.gen.view_models.windows.full_screen_dialog_window_model import FullScreenDialogWindowModel

class ActiveTestConfirmViewModel(FullScreenDialogWindowModel):
    __slots__ = (b'onOpenPortalClicked',)

    def __init__(self, properties=14, commands=4):
        super(ActiveTestConfirmViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getClusterName(self):
        return self._getString(11)

    def setClusterName(self, value):
        self._setString(11, value)
        return

    def getTimeRangeStart(self):
        return self._getNumber(12)

    def setTimeRangeStart(self, value):
        self._setNumber(12, value)
        return

    def getTimeRangeEnd(self):
        return self._getNumber(13)

    def setTimeRangeEnd(self, value):
        self._setNumber(13, value)
        return

    def _initialize(self):
        super(ActiveTestConfirmViewModel, self)._initialize()
        self._addStringProperty(b'clusterName', b'')
        self._addNumberProperty(b'timeRangeStart', 0)
        self._addNumberProperty(b'timeRangeEnd', 0)
        self.onOpenPortalClicked = self._addCommand(b'onOpenPortalClicked')
        return
