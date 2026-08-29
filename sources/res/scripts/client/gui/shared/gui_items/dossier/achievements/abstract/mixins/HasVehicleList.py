from collections import namedtuple
from gui import nationCompareByIndex
from helpers import dependency
from skeletons.gui.shared import IItemsCache

class HasVehiclesList(object):
    _LIST_NAME = b'vehicles'
    VehicleData = namedtuple(b'VehicleData', b'name nation level type icon')
    itemsCache = dependency.descriptor(IItemsCache)

    def getVehiclesData(self):
        result = []
        for vCD in self._getVehiclesDescrsList():
            vehicle = self.itemsCache.items.getItemByCD(vCD)
            result.append(self.VehicleData(vehicle.userName, vehicle.nationID, vehicle.level, vehicle.type, vehicle.iconSmall))

        return map((lambda i: i._asdict()), sorted(result, cmp=self.__sortFunc))

    @classmethod
    def getVehiclesListTitle(cls):
        return cls._LIST_NAME

    def _getVehiclesDescrsList(self):
        raise NotImplemented
        return

    def hasVehiclesList(self):
        return True

    @classmethod
    def __sortFunc(cls, i1, i2):
        res = i1.level - i2.level
        if res:
            return res
        return nationCompareByIndex(i1.nation, i2.nation)
