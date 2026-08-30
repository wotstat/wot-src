from frameworks.wulf import ViewModel

class AllChaptersViewModel(ViewModel):
    __slots__ = (b'onSelectChapter', b'onToChapterRewards')

    def __init__(self, properties=0, commands=2):
        super(AllChaptersViewModel, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(AllChaptersViewModel, self)._initialize()
        self.onSelectChapter = self._addCommand(b'onSelectChapter')
        self.onToChapterRewards = self._addCommand(b'onToChapterRewards')
        return
