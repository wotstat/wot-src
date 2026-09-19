from frameworks.wulf import ViewModel

class StyleGuideViewModel(ViewModel):
    __slots__ = (b'onSaveThemeFile',)

    def __init__(self, properties=0, commands=1):
        super(StyleGuideViewModel, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(StyleGuideViewModel, self)._initialize()
        self.onSaveThemeFile = self._addCommand(b'onSaveThemeFile')
        return
