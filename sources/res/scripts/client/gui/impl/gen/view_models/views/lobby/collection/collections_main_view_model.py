from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.collection.collection_model import CollectionModel

class CollectionsMainViewModel(ViewModel):
    __slots__ = (b'onOpenCollection', b'onClose', b'setCompletionWasShown', b'onSetNewCollectionShown')

    def __init__(self, properties=2, commands=4):
        super(CollectionsMainViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsViewActive(self):
        return self._getBool(0)

    def setIsViewActive(self, value):
        self._setBool(0, value)
        return

    def getCollections(self):
        return self._getArray(1)

    def setCollections(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getCollectionsType():
        return CollectionModel

    def _initialize(self):
        super(CollectionsMainViewModel, self)._initialize()
        self._addBoolProperty(b'isViewActive', False)
        self._addArrayProperty(b'collections', Array())
        self.onOpenCollection = self._addCommand(b'onOpenCollection')
        self.onClose = self._addCommand(b'onClose')
        self.setCompletionWasShown = self._addCommand(b'setCompletionWasShown')
        self.onSetNewCollectionShown = self._addCommand(b'onSetNewCollectionShown')
        return
