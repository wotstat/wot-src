from __future__ import absolute_import
from collections import namedtuple
from gui import nationSortKeyByIndex
from helpers import dependency
from skeletons.gui.shared import IItemsCache

class HasVehiclesList(object):
    _LIST_NAME = b'vehicles'
    VehicleData = namedtuple(b'VehicleData', b'name nation level type icon innationID')
    itemsCache = dependency.descriptor(IItemsCache)

    def getVehiclesData(self):
        result = []
        for vCD in self._getVehiclesDescrsList():
            vehicle = self.itemsCache.items.getItemByCD(vCD)
            result.append(self.VehicleData(vehicle.userName, vehicle.nationID, vehicle.level, vehicle.type, vehicle.iconSmall, vehicle.innationID))

        return [i._asdict() for i in sorted(result, key=self._sortKey)]

    @classmethod
    def getVehiclesListTitle(cls):
        return cls._LIST_NAME

    def _getVehiclesDescrsList(self):
        raise NotImplementedError
        return

    def hasVehiclesList(self):
        return True

    @classmethod
    def _sortKey(cls, v):
        return (v.level, nationSortKeyByIndex(v.nation))
