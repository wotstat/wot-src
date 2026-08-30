from gui.impl.gen import R
from gui.impl.gen.view_models.views.loot_box_view.loot_def_renderer_model import LootDefRendererModel

class LootAnimatedRendererModel(LootDefRendererModel):
    __slots__ = ()
    SWF_ANIMATION = 0
    MC_ANIMATION = 1

    def __init__(self, properties=16, commands=0):
        super(LootAnimatedRendererModel, self).__init__(properties=properties, commands=commands)
        return

    def getAnimationType(self):
        return self._getNumber(13)

    def setAnimationType(self, value):
        self._setNumber(13, value)
        return

    def getAnimation(self):
        return self._getResource(14)

    def setAnimation(self, value):
        self._setResource(14, value)
        return

    def getAnimationSound(self):
        return self._getResource(15)

    def setAnimationSound(self, value):
        self._setResource(15, value)
        return

    def _initialize(self):
        super(LootAnimatedRendererModel, self)._initialize()
        self._addNumberProperty(b'animationType', 0)
        self._addResourceProperty(b'animation', R.invalid())
        self._addResourceProperty(b'animationSound', R.invalid())
        return
