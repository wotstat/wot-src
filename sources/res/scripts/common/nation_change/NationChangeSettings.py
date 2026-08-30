from typing import List, Dict, Iterable
from realm_utils import ResMgr
from items import _xml

class NationGroup(object):
    __slots__ = (b'ID', b'tankList')

    def __init__(self, ID):
        self.ID = ID
        self.tankList = []
        return


class NationChangeSettings(object):

    def __init__(self, xmlPath):
        self.__groupById = self.__readSettings(xmlPath)
        return

    def getGroupById(self, groupId):
        return self.__groupById.get(groupId)

    def findVehicleGroup(self, vehicleTypeName):
        for groupId, group in self.__groupById.iteritems():
            if vehicleTypeName in group.tankList:
                return group

        return

    def iterGroups(self):
        return self.__groupById.itervalues()

    @staticmethod
    def __readSettings(xmlPath):
        configXml = ResMgr.openSection(xmlPath)
        if configXml is None:
            _xml.raiseWrongXml(None, xmlPath, b'can not open or read')
        xmlCtx = (None, xmlPath)
        unique = set()
        resDict = {}
        for id_, childSection in enumerate(_xml.getChildren(xmlCtx, configXml, b'nation_groups')):
            _, changeableVehicles = childSection
            for vehicle in changeableVehicles.values():
                vehicleType = vehicle.asString
                if vehicleType in unique:
                    ctx = (
                     xmlCtx, b'group')
                    _xml.raiseWrongXml(ctx, b'', b'%s is not unique' % (vehicleType,))
                    continue
                unique.add(vehicleType)
                nationGroup = resDict.setdefault(id_, NationGroup(id_))
                nationGroup.tankList.append(vehicleType)

        ResMgr.purge(xmlPath, True)
        return resDict
