from collections import namedtuple
import ResMgr
from maps_training_common.maps_training_constants import VEHICLE_CLASSES_ORDER
MapConfig = namedtuple(b'MapConfig', (b'teams', b'scenarios'))
Team = namedtuple(b'Team', (b'position', b'tooltipImage', b'isLeft', b'scenarioPoints'))
Point = namedtuple(b'Point', (b'id', b'textKeys', b'position', b'tooltipImage', b'isLeft'))
Scenario = namedtuple(b'Scenario', (b'team', b'vehicleType'))
_BASE_OFFSET = (24, 24)
_POINT_OFFSET = (6, 6)

class TacticalMapsConfig(object):

    def __init__(self, mapsData):
        super(TacticalMapsConfig, self).__init__()
        self._mapsData = mapsData
        return

    def getMapConfig(self, geometryName):
        return self._mapsData.get(geometryName, MapConfig({}, []))


class TacticalMapsConfigReader(object):

    @staticmethod
    def readXml(xmlPath):
        section = ResMgr.openSection(xmlPath)
        mapsData = dict()
        mapsSection = section[b'maps']
        for mapSection in mapsSection.values():
            mapId = mapSection.readString(b'geometryName', b'')
            scenarios = []
            teamsData = dict()
            teamsSection = mapSection[b'teams']
            for teamSection in teamsSection.values():
                teamId = teamSection.readInt(b'id', 0)
                teamPosition = teamSection.readVector2(b'position') + _BASE_OFFSET
                teamTooltipImage = teamSection.readString(b'tooltipImage', b'')
                teamIsLeft = teamSection.readBool(b'isLeft', False)
                scenarioPoints = dict()
                configsSection = teamSection[b'configs']
                for configSection in configsSection.values():
                    vehicleType = configSection.readString(b'type', b'')
                    scenarios.append(Scenario(teamId, vehicleType))
                    pointsSection = configSection[b'points']
                    if not pointsSection:
                        scenarioPoints[vehicleType] = tuple()
                        continue
                    scenarioPoints[vehicleType] = tuple([Point(pointSection.readString(b'id', b''), pointSection.readString(b'textKeys', b'').split(), pointSection.readVector2(b'position') + _POINT_OFFSET, pointSection.readString(b'tooltipImage', b''), pointSection.readBool(b'isLeft', False)) for pointSection in pointsSection.values()])

                teamsData[teamId] = Team(teamPosition, teamTooltipImage, teamIsLeft, scenarioPoints)

            scenarios = sorted(scenarios, key=(lambda scenario: VEHICLE_CLASSES_ORDER.index(scenario.vehicleType)))
            mapsData[mapId] = MapConfig(teamsData, scenarios)

        ResMgr.purge(xmlPath)
        return TacticalMapsConfig(mapsData)
