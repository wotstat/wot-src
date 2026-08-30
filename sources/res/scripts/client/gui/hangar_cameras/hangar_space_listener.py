from helpers import dependency
from skeletons.gui.shared.utils import IHangarSpace

class HangarSpaceListener(object):
    hangarSpace = dependency.descriptor(IHangarSpace)

    def __init__(self):
        self.hangarSpace.onSpaceCreate += self._activate
        self.hangarSpace.onSpaceDestroy += self._deactivate
        return

    def destroy(self):
        self.hangarSpace.onSpaceCreate -= self._activate
        self.hangarSpace.onSpaceDestroy -= self._deactivate
        return

    def _activate(self):
        return

    def _deactivate(self, inited):
        return
