from frameworks.wulf import ViewModel

class HeaderWidgetViewModel(ViewModel):
    __slots__ = (b'onChangeLayout',)
    ARG_TOP = b'top'
    ARG_RIGHT = b'right'
    ARG_LEFT = b'left'

    def __init__(self, properties=0, commands=1):
        super(HeaderWidgetViewModel, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(HeaderWidgetViewModel, self)._initialize()
        self.onChangeLayout = self._addCommand(b'onChangeLayout')
        return
