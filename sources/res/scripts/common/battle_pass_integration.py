from __future__ import absolute_import
from copy import copy
from collections import namedtuple
from constants import ARENA_BONUS_TYPE, ARENA_BONUS_TYPE_NAMES
from items import vehicles
from soft_exception import SoftException
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Type, Union
NON_VEH_CD = 0
BpPointsSettings = namedtuple(b'BpPointsSettings', b'vehTypeCompDescr, isWinner, rank')

class BattlePassIntegrationInterface(object):
    __slots__ = ()

    def getTeamSize(self):
        raise NotImplementedError()
        return

    def validatePoints(self, season):
        raise NotImplementedError()
        return

    def calculatePointsSettings(self, storage):
        raise NotImplementedError()
        return


class BattlePassIntegrationRandom(BattlePassIntegrationInterface):
    __slots__ = (b'teamSize', b'bonusTypeName', b'bonusType')

    def __init__(self, teamSize, bonusTypeName):
        self.teamSize = teamSize
        self.bonusTypeName = bonusTypeName.upper()
        self.bonusType = ARENA_BONUS_TYPE_NAMES[self.bonusTypeName]
        return

    def getTeamSize(self):
        return self.teamSize

    def validatePoints(self, season):
        points = season[b'points'][self.bonusType]
        winPoints = points[b'win']
        losePoints = points[b'lose']

        def checkPointsList(pointsList, path):
            if len(pointsList) != self.getTeamSize():
                raise SoftException((b'[BattlePass] len(season/points/{}) {} != {}').format(path, len(pointsList), self.getTeamSize()))
            return

        checkPointsList(winPoints, (b'{}/win').format(self.bonusTypeName))
        checkPointsList(losePoints, (b'{}/lose').format(self.bonusTypeName))
        for key in points:
            if key not in (b'win', b'lose', b'enabled', b'visible'):
                vehCD = key
                if not vehicles.g_list.isVehicleExistingByCD(vehCD):
                    raise SoftException((b'[BattlePass] wrong vehCD={}').format(vehCD))
                winPoints = points[vehCD][b'win']
                losePoints = points[vehCD][b'lose']
                checkPointsList(winPoints, (b'{}/{}/win').format(self.bonusTypeName, str(vehCD)))
                checkPointsList(losePoints, (b'{}/{}/lose').format(self.bonusTypeName, str(vehCD)))

        return

    def calculatePointsSettings(self, storage):
        vehTypeCompDescr, results = storage[b'tempResults'].items()[0]
        rank = storage[b'avatarResults'].get(b'fareTeamXPPosition', 0)
        isWinner = b'winnerTeam' in results and b'team' in results and results[b'team'] == results[b'winnerTeam']
        return BpPointsSettings(vehTypeCompDescr, isWinner, rank)


class BattlePassIntegrationEpicBattle(BattlePassIntegrationRandom):
    __slots__ = ()

    def calculatePointsSettings(self, storage):
        _, isWinner, rank = super(BattlePassIntegrationEpicBattle, self).calculatePointsSettings(storage)
        return BpPointsSettings(NON_VEH_CD, isWinner, rank)

    def validatePoints(self, season):
        points = season[b'points'][self.bonusType]
        placesCount = self.teamSize
        bonusTypeName = self.bonusTypeName

        def checkPointsList(path):
            if len(points[path]) != placesCount:
                raise SoftException((b'[BattlePass] len(season/points/{}/{}) {} != {}').format(bonusTypeName, path, points[path], placesCount))
            return

        checkPointsList(b'win')
        checkPointsList(b'lose')
        return


class BattlePassIntegrationBattleRoyale(BattlePassIntegrationRandom):
    __slots__ = (b'twinBonusType',)

    def __init__(self, teamSize, bonusTypeName):
        super(BattlePassIntegrationBattleRoyale, self).__init__(teamSize, bonusTypeName)
        if self.bonusType == ARENA_BONUS_TYPE.BATTLE_ROYALE_SOLO:
            self.twinBonusType = ARENA_BONUS_TYPE.BATTLE_ROYALE_SQUAD
        else:
            self.twinBonusType = ARENA_BONUS_TYPE.BATTLE_ROYALE_SOLO
        return

    def validatePoints(self, season):
        if self.twinBonusType not in season[b'points']:
            raise SoftException((b'[BattlePass] bonus type {} must be present with {}').format(self.twinBonusType, self.bonusType))
        points = season[b'points'][self.bonusType]
        if points[b'enabled'] != season[b'points'][self.twinBonusType][b'enabled']:
            raise SoftException((b'[BattlePass] bonus type {} must has same enabled flag as {}').format(self.twinBonusType, self.bonusType))

        def checkPointsList(path):
            if len(points[path]) != self.getTeamSize():
                raise SoftException((b'[BattlePass] len(season/points/{}/{}) {} != {}').format(self.bonusType, path, points[path], self.getTeamSize()))
            return

        checkPointsList(b'win')
        checkPointsList(b'lose')
        if not self._checkBattleRoyalePointsSequence(points, 3):
            raise SoftException(b'BattlePass royale points are wrong.Example: win: 10 0 0 0..., lose: 0 7 7 5 5 5 0 0 ..3 thresholds. Should decrease')
        return

    def calculatePointsSettings(self, storage):
        vehTypeCompDescr, _ = storage[b'tempResults'].items()[0]
        place = storage[b'avatarResults'][b'brPosInBattle']
        isWinner = place == 1
        return BpPointsSettings(vehTypeCompDescr, isWinner, place)

    @staticmethod
    def _checkBattleRoyalePointsSequence(points, thresholdTargetCount):
        if any(point != 0 for point in points[b'win'][1:]):
            return False
        mergedPoints = list(points[b'lose'])
        mergedPoints[0] = points[b'win'][0]
        sortedMergedPoints = copy(mergedPoints)
        sortedMergedPoints.sort(reverse=True)
        if sortedMergedPoints != mergedPoints:
            return False
        pointsValues = set(sortedMergedPoints)
        pointsValues.discard(0)
        if len(pointsValues) != thresholdTargetCount:
            return False
        return True


class BattlePassIntegrationComp7Base(BattlePassIntegrationRandom):

    def calculatePointsSettings(self, storage):
        vehTypeCompDescr, results = storage[b'tempResults'].items()[0]
        rank = storage[b'avatarResults'].get(b'fareTeamPrestigePointsPosition', 0)
        isWinner = b'winnerTeam' in results and b'team' in results and results[b'team'] == results[b'winnerTeam']
        return BpPointsSettings(vehTypeCompDescr, isWinner, rank)


class BattlePassIntegrationComp7(BattlePassIntegrationComp7Base):
    pass


class BattlePassIntegrationComp7Light(BattlePassIntegrationComp7Base):
    pass


_BATTLEPASS_BY_GAMEMODE = {(ARENA_BONUS_TYPE.REGULAR): (BattlePassIntegrationRandom(teamSize=15, bonusTypeName=b'REGULAR')), 
   (ARENA_BONUS_TYPE.MAPBOX): (BattlePassIntegrationRandom(teamSize=15, bonusTypeName=b'MAPBOX')), 
   (ARENA_BONUS_TYPE.COMP7): (BattlePassIntegrationComp7(teamSize=7, bonusTypeName=b'COMP7')), 
   (ARENA_BONUS_TYPE.COMP7_LIGHT): (BattlePassIntegrationComp7Light(teamSize=7, bonusTypeName=b'COMP7_LIGHT')), 
   (ARENA_BONUS_TYPE.WINBACK): (BattlePassIntegrationRandom(teamSize=15, bonusTypeName=b'WINBACK')), 
   (ARENA_BONUS_TYPE.RANDOM_NP2): (BattlePassIntegrationRandom(teamSize=15, bonusTypeName=b'RANDOM_NP2')), 
   (ARENA_BONUS_TYPE.EPIC_BATTLE): (BattlePassIntegrationEpicBattle(teamSize=30, bonusTypeName=b'EPIC_BATTLE')), 
   (ARENA_BONUS_TYPE.BATTLE_ROYALE_SOLO): (BattlePassIntegrationBattleRoyale(teamSize=15, bonusTypeName=b'BATTLE_ROYALE_SOLO')), 
   (ARENA_BONUS_TYPE.BATTLE_ROYALE_SQUAD): (BattlePassIntegrationBattleRoyale(teamSize=10, bonusTypeName=b'BATTLE_ROYALE_SQUAD'))}

def getBattlePassByGameMode(arenaBonusType):
    return _BATTLEPASS_BY_GAMEMODE.get(arenaBonusType)


def getAllIntergatedGameModes():
    return list(_BATTLEPASS_BY_GAMEMODE)
