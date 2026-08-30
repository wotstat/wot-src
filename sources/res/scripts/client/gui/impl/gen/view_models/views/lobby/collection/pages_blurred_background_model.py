from frameworks.wulf import ViewModel

class PagesBlurredBackgroundModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(PagesBlurredBackgroundModel, self).__init__(properties=properties, commands=commands)
        return

    def getMain(self):
        return self._getString(0)

    def setMain(self, value):
        self._setString(0, value)
        return

    def _initialize(self):
        super(PagesBlurredBackgroundModel, self)._initialize()
        self._addStringProperty(b'main', b'img://gui/maps/icons/collections/collections_content/battlePass/battlePass10/bgMain.png')
        return
