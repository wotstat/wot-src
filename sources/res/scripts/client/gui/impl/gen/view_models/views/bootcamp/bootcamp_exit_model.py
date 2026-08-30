from gui.impl.gen.view_models.views.bootcamp.bootcamp_progress_model import BootcampProgressModel

class BootcampExitModel(BootcampProgressModel):
    __slots__ = (b'onLeaveBootcamp',)

    def __init__(self, properties=7, commands=1):
        super(BootcampExitModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsInBattle(self):
        return self._getBool(4)

    def setIsInBattle(self, value):
        self._setBool(4, value)
        return

    def getIsNeedAwarding(self):
        return self._getBool(5)

    def setIsNeedAwarding(self, value):
        self._setBool(5, value)
        return

    def getIsReferral(self):
        return self._getBool(6)

    def setIsReferral(self, value):
        self._setBool(6, value)
        return

    def _initialize(self):
        super(BootcampExitModel, self)._initialize()
        self._addBoolProperty(b'isInBattle', False)
        self._addBoolProperty(b'isNeedAwarding', False)
        self._addBoolProperty(b'isReferral', False)
        self.onLeaveBootcamp = self._addCommand(b'onLeaveBootcamp')
        return
