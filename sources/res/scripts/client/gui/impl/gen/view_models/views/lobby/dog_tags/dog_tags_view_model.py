from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.dog_tags.dt_dog_tag import DtDogTag
from gui.impl.gen.view_models.views.lobby.dog_tags.dt_grid_section import DtGridSection

class DogTagsViewModel(ViewModel):
    __slots__ = (b'onEquip', b'onReset', b'onTabSelect', b'onInfoButtonClick', b'onPlayVideo', b'onUpdateSelectedDT', b'onOnboardingCloseClick', b'onNewComponentHover', b'onBack')

    def __init__(self, properties=12, commands=9):
        super(DogTagsViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def equippedDogTag(self):
        return self._getViewModel(0)

    @staticmethod
    def getEquippedDogTagType():
        return DtDogTag

    def getNewEngravingComponentCount(self):
        return self._getNumber(1)

    def setNewEngravingComponentCount(self, value):
        self._setNumber(1, value)
        return

    def getNewBackgroundComponentCount(self):
        return self._getNumber(2)

    def setNewBackgroundComponentCount(self, value):
        self._setNumber(2, value)
        return

    def getNewEngravingDedicationCount(self):
        return self._getNumber(3)

    def setNewEngravingDedicationCount(self, value):
        self._setNumber(3, value)
        return

    def getNewEngravingTriumphCount(self):
        return self._getNumber(4)

    def setNewEngravingTriumphCount(self, value):
        self._setNumber(4, value)
        return

    def getNewEngravingSkillCount(self):
        return self._getNumber(5)

    def setNewEngravingSkillCount(self, value):
        self._setNumber(5, value)
        return

    def getTab(self):
        return self._getNumber(6)

    def setTab(self, value):
        self._setNumber(6, value)
        return

    def getBackgroundGrid(self):
        return self._getArray(7)

    def setBackgroundGrid(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getBackgroundGridType():
        return DtGridSection

    def getEngravingGrid(self):
        return self._getArray(8)

    def setEngravingGrid(self, value):
        self._setArray(8, value)
        return

    @staticmethod
    def getEngravingGridType():
        return DtGridSection

    def getOnboardingEnabled(self):
        return self._getBool(9)

    def setOnboardingEnabled(self, value):
        self._setBool(9, value)
        return

    def getIsTopView(self):
        return self._getBool(10)

    def setIsTopView(self, value):
        self._setBool(10, value)
        return

    def getIsAnimatedDogTagSelected(self):
        return self._getBool(11)

    def setIsAnimatedDogTagSelected(self, value):
        self._setBool(11, value)
        return

    def _initialize(self):
        super(DogTagsViewModel, self)._initialize()
        self._addViewModelProperty(b'equippedDogTag', DtDogTag())
        self._addNumberProperty(b'newEngravingComponentCount', 0)
        self._addNumberProperty(b'newBackgroundComponentCount', 0)
        self._addNumberProperty(b'newEngravingDedicationCount', 0)
        self._addNumberProperty(b'newEngravingTriumphCount', 0)
        self._addNumberProperty(b'newEngravingSkillCount', 0)
        self._addNumberProperty(b'tab', 0)
        self._addArrayProperty(b'backgroundGrid', Array())
        self._addArrayProperty(b'engravingGrid', Array())
        self._addBoolProperty(b'onboardingEnabled', False)
        self._addBoolProperty(b'isTopView', False)
        self._addBoolProperty(b'isAnimatedDogTagSelected', False)
        self.onEquip = self._addCommand(b'onEquip')
        self.onReset = self._addCommand(b'onReset')
        self.onTabSelect = self._addCommand(b'onTabSelect')
        self.onInfoButtonClick = self._addCommand(b'onInfoButtonClick')
        self.onPlayVideo = self._addCommand(b'onPlayVideo')
        self.onUpdateSelectedDT = self._addCommand(b'onUpdateSelectedDT')
        self.onOnboardingCloseClick = self._addCommand(b'onOnboardingCloseClick')
        self.onNewComponentHover = self._addCommand(b'onNewComponentHover')
        self.onBack = self._addCommand(b'onBack')
        return
