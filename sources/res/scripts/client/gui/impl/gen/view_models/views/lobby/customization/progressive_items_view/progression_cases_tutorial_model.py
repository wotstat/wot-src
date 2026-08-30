from frameworks.wulf import ViewModel

class ProgressionCasesTutorialModel(ViewModel):
    __slots__ = (b'onClose', b'showVideo')

    def __init__(self, properties=0, commands=2):
        super(ProgressionCasesTutorialModel, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(ProgressionCasesTutorialModel, self)._initialize()
        self.onClose = self._addCommand(b'onClose')
        self.showVideo = self._addCommand(b'showVideo')
        return
