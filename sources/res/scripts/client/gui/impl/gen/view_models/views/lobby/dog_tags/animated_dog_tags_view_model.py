from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.dog_tags.animated_dog_tag_component import AnimatedDogTagComponent

class AnimatedDogTagsViewModel(ViewModel):
    __slots__ = (b'onEquip', b'onGoToAchievement', b'onInfoButtonClick', b'onPlayVideo', b'onOnboardingCloseClick', b'onHideNewBubble', b'onClose')

    def __init__(self, properties=3, commands=7):
        super(AnimatedDogTagsViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getDogTags(self):
        return self._getArray(0)

    def setDogTags(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getDogTagsType():
        return AnimatedDogTagComponent

    def getOnboardingEnabled(self):
        return self._getBool(1)

    def setOnboardingEnabled(self, value):
        self._setBool(1, value)
        return

    def getInitialIndex(self):
        return self._getNumber(2)

    def setInitialIndex(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(AnimatedDogTagsViewModel, self)._initialize()
        self._addArrayProperty(b'dogTags', Array())
        self._addBoolProperty(b'onboardingEnabled', False)
        self._addNumberProperty(b'initialIndex', 0)
        self.onEquip = self._addCommand(b'onEquip')
        self.onGoToAchievement = self._addCommand(b'onGoToAchievement')
        self.onInfoButtonClick = self._addCommand(b'onInfoButtonClick')
        self.onPlayVideo = self._addCommand(b'onPlayVideo')
        self.onOnboardingCloseClick = self._addCommand(b'onOnboardingCloseClick')
        self.onHideNewBubble = self._addCommand(b'onHideNewBubble')
        self.onClose = self._addCommand(b'onClose')
        return
