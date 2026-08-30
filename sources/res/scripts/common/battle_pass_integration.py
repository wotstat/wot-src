from copy import copy
from collections import namedtuple
from constants import ARENA_BONUS_TYPE, ARENA_BONUS_TYPE_NAMES
from items import vehicles
from soft_exception import SoftException
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Type, Union
NON_VEH_CD = 0
BpPointsSettings = namedtuple(b'BpPointsSettings', b'isWinner, rank')

class BattlePassIntegrationInterface(object):
    __slots__ = (b'teamSize', b'bonusTypeName', b'bonusType')

    def getTeamSize(self):
        raise NotImplementedError()
        return

    def validatePoints(self, season):
        raise NotImplementedError()
        return

    def calculatePointsSettings(self, avatarResults, battleResults):
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

    @staticmethod
    def _isWinnerTeam(battleResults):
        return b'winnerTeam' in battleResults and b'team' in battleResults and battleResults[b'team'] == battleResults[b'winnerTeam']

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
        for key, value in points.iteritems():
            if key != b'win' and key != b'lose' and key != b'enabled':
                vehCD = key
                if not vehicles.g_list.isVehicleExistingByCD(vehCD):
                    raise SoftException((b'[BattlePass] wrong vehCD={}').format(vehCD))
                winPoints = points[vehCD][b'win']
                losePoints = points[vehCD][b'lose']
                checkPointsList(winPoints, (b'{}/{}/win').format(self.bonusTypeName, str(vehCD)))
                checkPointsList(losePoints, (b'{}/{}/lose').format(self.bonusTypeName, str(vehCD)))

        return

    def calculatePointsSettings(self, avatarResults, battleResults):
        rank = avatarResults.get(b'fareTeamXPPosition', 0)
        isWinner = self._isWinnerTeam(battleResults)
        return BpPointsSettings(isWinner, rank)


class BattlePassIntegrationEpicBattle(BattlePassIntegrationRandom):
    __slots__ = (b'teamSize', b'bonusTypeName', b'bonusType')

    def calculatePointsSettings(self, avatarResults, battleResults):
        rank = avatarResults.get(b'fareTeamXPPosition', 0)
        isWinner = self._isWinnerTeam(battleResults)
        return BpPointsSettings(isWinner, rank)

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
    __slots__ = (b'teamSize', b'bonusTypeName', b'bonusType', b'twinBonusType')

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

    def calculatePointsSettings(self, avatarResults, battleResults):
        place = avatarResults[b'brPosInBattle']
        isWinner = place == 1
        return BpPointsSettings(isWinner, place)

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


class BattlePassIntegrationComp7(BattlePassIntegrationRandom):

    def calculatePointsSettings(self, avatarResults, battleResults):
        rank = avatarResults.get(b'fareTeamPrestigePointsPosition', 0)
        isWinner = self._isWinnerTeam(battleResults)
        return BpPointsSettings(isWinner, rank)


_GAMEMODE_WITH_NON_VEHICLE_DESC = {
 ARENA_BONUS_TYPE.BATTLE_ROYALE_SOLO,
 ARENA_BONUS_TYPE.BATTLE_ROYALE_SQUAD}

def isGameModeWithNonVehicleDesc(arenaBonusType):
    return arenaBonusType in _GAMEMODE_WITH_NON_VEHICLE_DESC


_BATTLEPASS_BY_GAMEMODE = {(ARENA_BONUS_TYPE.REGULAR): (BattlePassIntegrationRandom(teamSize=15, bonusTypeName=b'REGULAR')), 
   (ARENA_BONUS_TYPE.RANKED): (BattlePassIntegrationRandom(teamSize=10, bonusTypeName=b'RANKED')), 
   (ARENA_BONUS_TYPE.COMP7): (BattlePassIntegrationComp7(teamSize=7, bonusTypeName=b'COMP7')), 
   (ARENA_BONUS_TYPE.EPIC_BATTLE): (BattlePassIntegrationEpicBattle(teamSize=30, bonusTypeName=b'EPIC_BATTLE')), 
   (ARENA_BONUS_TYPE.BATTLE_ROYALE_SOLO): (BattlePassIntegrationBattleRoyale(teamSize=15, bonusTypeName=b'BATTLE_ROYALE_SOLO')), 
   (ARENA_BONUS_TYPE.BATTLE_ROYALE_SQUAD): (BattlePassIntegrationBattleRoyale(teamSize=10, bonusTypeName=b'BATTLE_ROYALE_SQUAD')), 
   (ARENA_BONUS_TYPE.SORTIE_2): (BattlePassIntegrationRandom(teamSize=7, bonusTypeName=b'SORTIE_2')), 
   (ARENA_BONUS_TYPE.FORT_BATTLE_2): (BattlePassIntegrationRandom(teamSize=15, bonusTypeName=b'FORT_BATTLE_2')), 
   (ARENA_BONUS_TYPE.VERSUS_AI): (BattlePassIntegrationRandom(teamSize=12, bonusTypeName=b'VERSUS_AI'))}

def getBattlePassByGameMode(arenaBonusType):
    return _BATTLEPASS_BY_GAMEMODE.get(arenaBonusType)


def getAllIntergatedGameModes():
    return _BATTLEPASS_BY_GAMEMODE.keys()
