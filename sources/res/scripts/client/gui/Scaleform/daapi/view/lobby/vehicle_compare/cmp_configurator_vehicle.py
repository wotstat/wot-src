from __future__ import absolute_import

class _CompareConfiguratorVehicle(object):
    __slots__ = (b'__vehicle',)

    def __init__(self):
        super(_CompareConfiguratorVehicle, self).__init__()
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


g_cmpConfiguratorVehicle = _CompareConfiguratorVehicle()
