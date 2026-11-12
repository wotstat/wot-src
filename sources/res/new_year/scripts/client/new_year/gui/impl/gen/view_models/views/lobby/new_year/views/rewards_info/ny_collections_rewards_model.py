from enum import IntEnum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.rewards_info.new_year_collection_additional import NewYearCollectionAdditional
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.rewards_info.new_year_collection_style_tab import NewYearCollectionStyleTab

class CollectionState(IntEnum):
    CURRENTYEAR = 0
    MAXLVLNOTREACHED = 1
    LACKSHARDS = 2
    READYTOGET = 3
    RECEIVED = 4
    RECEIVEDEARLIER = 5


class NyCollectionsRewardsModel(ViewModel):
    __slots__ = (b'onGetStyleButton', b'onGoToCollectionButton', b'onPreviewStyleButton', b'onCollectionNameChanged')

    def __init__(self, properties=11, commands=4):
        super(NyCollectionsRewardsModel, self).__init__(properties=properties, commands=commands)
        return

    def getStyleName(self):
        return self._getString(0)

    def setStyleName(self, value):
        self._setString(0, value)
        return

    def getNations(self):
        return self._getArray(1)

    def setNations(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getNationsType():
        return unicode

    def getLevels(self):
        return self._getArray(2)

    def setLevels(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getLevelsType():
        return int

    def getStyleTooltipId(self):
        return self._getNumber(3)

    def setStyleTooltipId(self, value):
        self._setNumber(3, value)
        return

    def getCost(self):
        return self._getNumber(4)

    def setCost(self, value):
        self._setNumber(4, value)
        return

    def getCollectionState(self):
        return CollectionState(self._getNumber(5))

    def setCollectionState(self, value):
        self._setNumber(5, value.value)
        return

    def getCurrentCollectionName(self):
        return self._getString(6)

    def setCurrentCollectionName(self, value):
        self._setString(6, value)
        return

    def getYear(self):
        return self._getString(7)

    def setYear(self, value):
        self._setString(7, value)
        return

    def getIsPremium(self):
        return self._getBool(8)

    def setIsPremium(self, value):
        self._setBool(8, value)
        return

    def getStyleAdditionals(self):
        return self._getArray(9)

    def setStyleAdditionals(self, value):
        self._setArray(9, value)
        return

    @staticmethod
    def getStyleAdditionalsType():
        return NewYearCollectionAdditional

    def getStyleTabs(self):
        return self._getArray(10)

    def setStyleTabs(self, value):
        self._setArray(10, value)
        return

    @staticmethod
    def getStyleTabsType():
        return NewYearCollectionStyleTab

    def _initialize(self):
        super(NyCollectionsRewardsModel, self)._initialize()
        self._addStringProperty(b'styleName', b'')
        self._addArrayProperty(b'nations', Array())
        self._addArrayProperty(b'levels', Array())
        self._addNumberProperty(b'styleTooltipId', 0)
        self._addNumberProperty(b'cost', 0)
        self._addNumberProperty(b'collectionState')
        self._addStringProperty(b'currentCollectionName', b'NewYear')
        self._addStringProperty(b'year', b'ny21')
        self._addBoolProperty(b'isPremium', False)
        self._addArrayProperty(b'styleAdditionals', Array())
        self._addArrayProperty(b'styleTabs', Array())
        self.onGetStyleButton = self._addCommand(b'onGetStyleButton')
        self.onGoToCollectionButton = self._addCommand(b'onGoToCollectionButton')
        self.onPreviewStyleButton = self._addCommand(b'onPreviewStyleButton')
        self.onCollectionNameChanged = self._addCommand(b'onCollectionNameChanged')
        return
