from frameworks.wulf import Array, ViewModel

class SlotModel(ViewModel):
    __slots__ = ()
    COMMANDER_ROLE = b'commander'
    RADIOMAN_ROLE = b'radioman'
    DRIVER_ROLE = b'driver'
    GUNNER_ROLE = b'gunner'
    LOADER_ROLE = b'loader'

    def __init__(self, properties=3, commands=0):
        super(SlotModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getNumber(0)

    def setId(self, value):
        self._setNumber(0, value)
        return

    def getTankmanId(self):
        return self._getNumber(1)

    def setTankmanId(self, value):
        self._setNumber(1, value)
        return

    def getRoles(self):
        return self._getArray(2)

    def setRoles(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getRolesType():
        return unicode

    def _initialize(self):
        super(SlotModel, self)._initialize()
        self._addNumberProperty(b'id', 0)
        self._addNumberProperty(b'tankmanId', -1)
        self._addArrayProperty(b'roles', Array())
        return
