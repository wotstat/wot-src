from frameworks.wulf import ViewModel

class StoryChoiceViewModel(ViewModel):
    __slots__ = (b'onClose', b'onSelectSide')
    OPTION_1 = b'option_1'
    OPTION_2 = b'option_2'

    def __init__(self, properties=0, commands=2):
        super(StoryChoiceViewModel, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(StoryChoiceViewModel, self)._initialize()
        self.onClose = self._addCommand(b'onClose')
        self.onSelectSide = self._addCommand(b'onSelectSide')
        return
