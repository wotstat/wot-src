from frameworks.wulf import ViewModel

class SpaceInteractionModel(ViewModel):
    __slots__ = (b'onMoveSpace', b'onMouseOver3dScene')

    def __init__(self, properties=0, commands=2):
        super(SpaceInteractionModel, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(SpaceInteractionModel, self)._initialize()
        self.onMoveSpace = self._addCommand(b'onMoveSpace')
        self.onMouseOver3dScene = self._addCommand(b'onMouseOver3dScene')
        return
