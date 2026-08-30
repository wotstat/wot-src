from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.common.multiple_items_content_model import MultipleItemsContentModel

class AmmunitionBuyContent(MultipleItemsContentModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(AmmunitionBuyContent, self).__init__(properties=properties, commands=commands)
        return

    def getLacksItem(self):
        return self._getArray(2)

    def setLacksItem(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getLacksItemType():
        return unicode

    def getDemountPairModification(self):
        return self._getBool(3)

    def setDemountPairModification(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(AmmunitionBuyContent, self)._initialize()
        self._addArrayProperty(b'lacksItem', Array())
        self._addBoolProperty(b'demountPairModification', False)
        return
