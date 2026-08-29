from frameworks.wulf import ViewModel

class DefaultDialogPlaceHolders(ViewModel):
    __slots__ = ()
    TOP_RIGHT = b'topRight'
    ICON = b'icon'
    TITLE = b'title'
    CONTENT = b'content'
    FOOTER = b'footer'

    def __init__(self, properties=0, commands=0):
        super(DefaultDialogPlaceHolders, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(DefaultDialogPlaceHolders, self)._initialize()
        return
