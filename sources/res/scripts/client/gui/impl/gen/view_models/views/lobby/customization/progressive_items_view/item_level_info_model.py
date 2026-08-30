from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.customization.progressive_items_view.progress_block import ProgressBlock

class ItemLevelInfoModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(ItemLevelInfoModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def progressBlock(self):
        return self._getViewModel(0)

    @staticmethod
    def getProgressBlockType():
        return ProgressBlock

    def getLevel(self):
        return self._getNumber(1)

    def setLevel(self, value):
        self._setNumber(1, value)
        return

    def getLevelText(self):
        return self._getString(2)

    def setLevelText(self, value):
        self._setString(2, value)
        return

    def getUnlocked(self):
        return self._getBool(3)

    def setUnlocked(self, value):
        self._setBool(3, value)
        return

    def getInProgress(self):
        return self._getBool(4)

    def setInProgress(self, value):
        self._setBool(4, value)
        return

    def getSelected(self):
        return self._getBool(5)

    def setSelected(self, value):
        self._setBool(5, value)
        return

    def getIcon(self):
        return self._getString(6)

    def setIcon(self, value):
        self._setString(6, value)
        return

    def getTooltipId(self):
        return self._getString(7)

    def setTooltipId(self, value):
        self._setString(7, value)
        return

    def _initialize(self):
        super(ItemLevelInfoModel, self)._initialize()
        self._addViewModelProperty(b'progressBlock', ProgressBlock())
        self._addNumberProperty(b'level', -1)
        self._addStringProperty(b'levelText', b'')
        self._addBoolProperty(b'unlocked', False)
        self._addBoolProperty(b'inProgress', False)
        self._addBoolProperty(b'selected', False)
        self._addStringProperty(b'icon', b'')
        self._addStringProperty(b'tooltipId', b'')
        return
