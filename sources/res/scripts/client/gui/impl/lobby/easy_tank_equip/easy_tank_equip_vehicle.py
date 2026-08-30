class _EasyTankEquipCopyVehicle(object):
    __slots__ = (b'__vehicle',)

    def __init__(self):
        super(_EasyTankEquipCopyVehicle, self).__init__()
        self.__vehicle = None
        return

    def setVehicle(self, value):
        self.__vehicle = value
        return

    @property
    def item(self):
        return self.__vehicle

    def isPresent(self):
        return self.__vehicle is not None

    def clear(self):
        self.__vehicle = None
        return


g_easyTankEquipCopyVehicle = _EasyTankEquipCopyVehicle()
