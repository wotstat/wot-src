from frameworks.wulf import Array, ViewModel

class TankmanInfoModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(TankmanInfoModel, self).__init__(properties=properties, commands=commands)
        return

    def getSkills(self):
        return self._getArray(0)

    def setSkills(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getSkillsType():
        return unicode

    def _initialize(self):
        super(TankmanInfoModel, self)._initialize()
        self._addArrayProperty(b'skills', Array())
        return
