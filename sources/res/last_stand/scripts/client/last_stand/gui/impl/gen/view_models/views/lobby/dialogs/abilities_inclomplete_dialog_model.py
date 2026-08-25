from frameworks.wulf import ViewModel

class AbilitiesInclompleteDialogModel(ViewModel):
    __slots__ = (b'onSubmitClick', b'onCancelClick', b'onCloseClick')

    def __init__(self, properties=0, commands=3):
        super(AbilitiesInclompleteDialogModel, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(AbilitiesInclompleteDialogModel, self)._initialize()
        self.onSubmitClick = self._addCommand(b'onSubmitClick')
        self.onCancelClick = self._addCommand(b'onCancelClick')
        self.onCloseClick = self._addCommand(b'onCloseClick')
        return
