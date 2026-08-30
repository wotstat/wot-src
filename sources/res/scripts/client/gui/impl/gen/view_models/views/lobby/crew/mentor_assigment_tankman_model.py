from gui.impl.gen.view_models.views.lobby.crew.tankman_model import TankmanModel

class MentorAssigmentTankmanModel(TankmanModel):
    __slots__ = ()

    def __init__(self, properties=25, commands=0):
        super(MentorAssigmentTankmanModel, self).__init__(properties=properties, commands=commands)
        return

    def getTotalXP(self):
        return self._getNumber(23)

    def setTotalXP(self, value):
        self._setNumber(23, value)
        return

    def getLostXP(self):
        return self._getNumber(24)

    def setLostXP(self, value):
        self._setNumber(24, value)
        return

    def _initialize(self):
        super(MentorAssigmentTankmanModel, self)._initialize()
        self._addNumberProperty(b'totalXP', 0)
        self._addNumberProperty(b'lostXP', 0)
        return
