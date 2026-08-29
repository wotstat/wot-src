from collections import namedtuple
from frameworks.wulf import Array
import ResMgr
MapConfig = namedtuple(b'MapConfig', (b'mapPoints',))
MapPoint = namedtuple(b'MapPoint', (b'id', b'typeName', b'position'))

class TacticalMapsConfig(object):

    def __init__(self, mapsData):
        super(TacticalMapsConfig, self).__init__()
        self._mapsData = mapsData
        return

    def getMapConfig(self, geometryName):
        return self._mapsData.get(geometryName, MapConfig([]))

    def getMapsIds(self):
        return self._mapsData.keys()


class TacticalMapsConfigReader(object):

    @staticmethod
    def readXml(xmlPath):
        section = ResMgr.openSection(xmlPath)
        mapsData = dict()
        mapsSection = section[b'maps']
        for mapSection in mapsSection.values():
            mapId = mapSection.readString(b'geometryName', b'')
            mapPointsSection = mapSection[b'mapPoints']
            mapPointsValues = mapPointsSection.values() if mapPointsSection else ()
            mapPointsData = tuple([MapPoint(mapPointsSection.readInt(b'id', 0), mapPointsSection.readString(b'typeName', b''), mapPointsSection.readVector2(b'position')) for mapPointsSection in mapPointsValues])
            mapsData[mapId] = MapConfig(mapPointsData)

        ResMgr.purge(xmlPath)
        return TacticalMapsConfig(mapsData)
