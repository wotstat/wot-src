from __future__ import absolute_import
from future.utils import viewvalues
from typing import List, Dict, Iterable
from items import _xml
from realm_utils import ResMgr

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
        for group in viewvalues(self.__groupById):
            if vehicleTypeName in group.tankList:
                return group

        return

    def iterGroups(self):
        return viewvalues(self.__groupById)

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
