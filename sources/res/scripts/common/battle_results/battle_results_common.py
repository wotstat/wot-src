from __future__ import absolute_import
from battle_results.battle_results_constants import BATTLE_RESULT_ENTRY_TYPE as ENTRY_TYPE
from constants import FLAG_ACTION
from DictPackers import DictPacker, MergeDictPacker, SimpleDictPacker, DeltaPacker, ValueReplayPacker, roundToInt
from items.vehicles import VEHICLE_DEVICE_TYPE_NAMES, VEHICLE_TANKMAN_TYPE_NAMES
from items.badges_common import BadgesCommon
BATTLE_RESULTS = [
 (
  b'health', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'maxHealth', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'credits', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'xp', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'xp/attack', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'xp/assist', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'xp/other', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'xpPenalty', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'achievementCredits', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'achievementXP', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'achievementFreeXP', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'shots', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'directHits', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'directEnemyHits', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'directTeamHits', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'explosionHits', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'piercings', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'piercingEnemyHits', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'damageDealt', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'sniperDamageDealt', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'artilleryFortEquipDamageDealt', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'equipmentDamageDealt', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'damageAssistedRadio', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'damageAssistedTrack', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'damageAssistedStun', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'damageAssistedSmoke', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'damageAssistedInspire', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'stunNum', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'stunDuration', float, 0.0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'damageReceived', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'damageReceivedFromInvisibles', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'damageBlockedByArmor', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'directHitsReceived', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'noDamageDirectHitsReceived', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'explosionHitsReceived', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'piercingsReceived', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'tdamageDealt', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'tdestroyedModules', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'tkills', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'isTeamKiller', bool, False, None, b'max', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'capturePoints', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'capturingBase', None, None, None, b'any', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'droppedCapturePoints', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'mileage', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'lifeTime', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'killerID', int, 0, None, b'any', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'achievements', list, [], None, b'extend', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'inBattleAchievements', list, [], None, b'extend', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'potentialDamageReceived', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'rolloutsCount', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'deathCount', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'flagActions', list, [0] * len(FLAG_ACTION.RANGE), None, b'sumInEachPos', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'soloFlagCapture', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'flagCapture', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'winPoints', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'resourceAbsorbed', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'stopRespawn', bool, False, None, b'max', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'numRecovered', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'vehicleNumCaptured', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'destructiblesNumDestroyed', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'destructiblesDamageDealt', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'destructiblesHits', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'destructibleDeaths', list, [], None, b'extend', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'numDefended', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'accountDBID', int, 0, None, b'any', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'typeCompDescr', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'index', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'deathReason', int, -1, None, b'skip', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'team', int, 1, None, b'skip', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'kills', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'spotted', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'damaged', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'damagedHp', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'stunned', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'marksOnGun', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'outfit', str, b'', None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'repair', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'freeXP', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'details', None, None, None, b'any', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'creditsPenalty', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'creditsContributionIn', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'creditsContributionOut', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'originalCreditsToDraw', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'creditsToDraw', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'damageBeforeTeamWasDamaged', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'killsBeforeTeamWasDamaged', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'percentFromTotalTeamDamage', float, 0.0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'winAloneAgainstVehicleCount', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'percentFromSecondBestDamage', float, 0.0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'killedAndDamagedByAllSquadmates', int, 0, None, b'any', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'damagedWhileMoving', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'damagedWhileEnemyMoving', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'committedSuicide', bool, False, None, b'max', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'crystal', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'eventCoin', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'bpcoin', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'equipCoin', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'piggyBank', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'eventCredits', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'eventXP', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'eventFreeXP', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'eventTMenXP', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'eventGold', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'eventCrystal', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'eventEventCoin', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'eventBpcoin', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'eventEquipCoin', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'originalCredits', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'creditsReplay', str, b'', ValueReplayPacker(), b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'originalXP', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'pureXP', int, 0, None, b'sum', ENTRY_TYPE.SERVER),
 (
  b'xpReplay', str, b'', ValueReplayPacker(), b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'originalFreeXP', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'freeXPReplay', str, b'', ValueReplayPacker(), b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'originalTMenXP', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'tmenXPReplay', str, b'', ValueReplayPacker(), b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'tmenXP', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'originalGold', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'goldReplay', str, b'', ValueReplayPacker(), b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'gold', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'originalCrystal', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'crystalReplay', str, b'', ValueReplayPacker(), b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'originalEventCoin', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'originalBpcoin', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'originalEquipCoin', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'eventCoinReplay', str, b'', ValueReplayPacker(), b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'bpcoinReplay', str, b'', ValueReplayPacker(), b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'equipCoinReplay', str, b'', ValueReplayPacker(), b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'factualXP', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'factualFreeXP', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'factualCredits', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'subtotalCredits', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'subtotalXP', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'subtotalFreeXP', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'subtotalTMenXP', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'subtotalGold', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'subtotalCrystal', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'subtotalEventCoin', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'subtotalBpcoin', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'subtotalEquipCoin', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'eventCreditsList', list, [], None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'eventXPList', list, [], None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'eventFreeXPList', list, [], None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'eventTMenXPList', list, [], None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'eventGoldList', list, [], None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'eventCrystalList', list, [], None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'eventEventCoinList', list, [], None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'eventBpcoinList', list, [], None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'eventEquipCoinList', list, [], None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'eventCreditsFactor100List', list, [], None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'eventXPFactor100List', list, [], None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'eventFreeXPFactor100List', list, [], None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'eventTMenXPFactor100List', list, [], None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'eventGoldFactor100List', list, [], None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'originalXPPenalty', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'originalCreditsPenalty', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'originalCreditsContributionIn', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'originalCreditsContributionOut', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'premiumVehicleXP', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'premiumVehicleXPFactor100', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'squadXP', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'squadXPFactor100', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'isWoTPlus', bool, False, None, b'any', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'wotPlusTier', int, 0, None, b'any', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'wotPlusCredits', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'wotPlusCreditsFactor100', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'wotPlusXP', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'wotPlusXPFactor100', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'wotPlusCrewXP', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'wotPlusCrewXPFactor100', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'wotPlusFreeXP', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'wotPlusFreeXPFactor100', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'wotPlusProBoostCredits', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'wotPlusProBoostCreditsFactor100', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'wotPlusProBoostXP', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'wotPlusProBoostXPFactor100', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'wotPlusProBoostCrewXP', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'wotPlusProBoostCrewXPFactor100', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'wotPlusProBoostFreeXP', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'wotPlusProBoostFreeXPFactor100', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'referral20XP', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'referral20XPFactor100', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'referral20Credits', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'referral20CreditsFactor100', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'premiumXPFactor100', int, 0, None, b'any', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'premiumPlusXPFactor100', int, 0, None, b'any', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'appliedPremiumXPFactor100', int, 0, None, b'any', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'premiumTmenXPFactor100', int, 0, None, b'any', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'premiumPlusTmenXPFactor100', int, 0, None, b'any', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'appliedPremiumTmenXPFactor100', int, 0, None, b'any', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'premiumCreditsFactor100', int, 0, None, b'any', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'premiumPlusCreditsFactor100', int, 0, None, b'any', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'appliedPremiumCreditsFactor100', int, 0, None, b'any', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'premSquadCreditsFactor100', int, 0, None, b'any', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'originalPremSquadCredits', int, 0, None, b'any', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'premSquadCredits', int, 0, None, b'any', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'dailyXPFactor10', int, 0, None, b'max', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'additionalXPFactor10', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'igrXPFactor10', int, 0, None, b'max', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'aogasFactor10', int, 0, None, b'max', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'refSystemXPFactor10', int, 0, None, b'any', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'fairplayFactor10', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'orderCredits', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'orderXP', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'orderFreeXP', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'orderTMenXP', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'orderCreditsFactor100', int, 0, None, b'any', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'orderXPFactor100', int, 0, None, b'any', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'orderFreeXPFactor100', int, 0, None, b'any', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'orderTMenXPFactor100', int, 0, None, b'any', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'boosterCredits', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'boosterXP', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'boosterFreeXP', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'boosterTMenXP', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'boosterCreditsFactor100', int, 0, None, b'any', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'boosterXPFactor100', int, 0, None, b'any', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'boosterFreeXPFactor100', int, 0, None, b'any', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'boosterTMenXPFactor100', int, 0, None, b'any', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'playerRankXP', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'playerRankXPFactor100', int, 0, None, b'any', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'isPremium', bool, False, None, b'any', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'premMask', int, 0, None, b'any', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'xpByTmen', list, [], None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'autoRepairCost', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'autoLoadCost', tuple, (0, 0), None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'autoEquipCost', tuple, (0, 0, 0), None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'autoEquipBoostersCost', tuple, (0, 0, 0), None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'prevMarkOfMastery', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'markOfMastery', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'dossierPopUps', list, [], None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'dossierLogRecords', list, [], None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'vehTypeLockTime', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'serviceProviderID', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'movingAvgDamage', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'damageRating', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'battleNum', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'questsProgress', dict, {}, None, b'joinDicts', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'questTokensCount', dict, {}, None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'questTokensConvertion', dict, {}, None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'c11nProgress', dict, {}, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'originalCreditsToDrawSquad', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'originalCreditsPenaltySquad', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'originalCreditsContributionInSquad', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'originalCreditsContributionOutSquad', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'avatarDamageDealt', int, 0, None, b'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  b'avatarKills', int, 0, None, b'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  b'avatarDamaged', int, 0, None, b'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  b'totalDamaged', int, 0, None, b'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  b'fairplayViolations', tuple, (0, 0, 0), None, b'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  b'badges', tuple, BadgesCommon.selectedBadgesEmpty(), None, b'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  b'rankChange', int, 0, None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'avatarAmmo', list, [], None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'avatarDamageEventList', set, set(), None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'accountDBID', int, 0, None, b'any', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'team', int, 1, None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'clanDBID', int, 0, None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'fortClanDBIDs', list, [], None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'winnerIfDraw', int, 0, None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'isPrematureLeave', bool, False, None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'watchedBattleToTheEnd', bool, False, None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'vseBattleResults', dict, {}, None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'squadBonusInfo', None, None, None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'progressiveReward', None, None, None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'eligibleForCrystalRewards', bool, False, None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'activeRents', dict, {}, None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'recruitsIDs', list, [], None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'recruiterID', int, 0, None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'referralBonusVehicles', list, [], None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'fareTeamXPPosition', int, 0, None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'questsProgress', dict, {}, None, b'joinDicts', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'PM2Progress', dict, {}, None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'dogTags', dict, {}, None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'eventCredits', int, 0, None, b'sum', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'eventXP', int, 0, None, b'sum', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'eventFreeXP', int, 0, None, b'sum', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'eventTMenXP', int, 0, None, b'sum', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'eventGold', int, 0, None, b'sum', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'eventCrystal', int, 0, None, b'sum', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'eventEventCoin', int, 0, None, b'sum', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'eventBpcoin', int, 0, None, b'sum', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'eventEquipCoin', int, 0, None, b'sum', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'credits', int, 0, None, b'sum', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'xp', int, 0, None, b'sum', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'freeXP', int, 0, None, b'sum', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'crystal', int, 0, None, b'sum', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'name', str, b'', None, b'skip', ENTRY_TYPE.PLAYER_INFO),
 (
  b'realName', str, b'', None, b'skip', ENTRY_TYPE.PLAYER_INFO),
 (
  b'clanDBID', int, 0, None, b'skip', ENTRY_TYPE.PLAYER_INFO),
 (
  b'clanAbbrev', str, b'', None, b'skip', ENTRY_TYPE.PLAYER_INFO),
 (
  b'prebattleID', int, 0, None, b'skip', ENTRY_TYPE.PLAYER_INFO),
 (
  b'team', int, 1, None, b'skip', ENTRY_TYPE.PLAYER_INFO),
 (
  b'igrType', int, 0, None, b'skip', ENTRY_TYPE.PLAYER_INFO),
 (
  b'arenaTypeID', int, 0, None, b'skip', ENTRY_TYPE.COMMON),
 (
  b'arenaCreateTime', int, 0, None, b'skip', ENTRY_TYPE.COMMON),
 (
  b'winnerTeam', int, 0, None, b'skip', ENTRY_TYPE.COMMON),
 (
  b'finishReason', int, 0, None, b'skip', ENTRY_TYPE.COMMON),
 (
  b'gasAttackWinnerTeam', int, -1, None, b'skip', ENTRY_TYPE.COMMON),
 (
  b'duration', int, 0, None, b'skip', ENTRY_TYPE.COMMON),
 (
  b'bonusType', int, 0, None, b'skip', ENTRY_TYPE.COMMON),
 (
  b'guiType', int, 0, None, b'skip', ENTRY_TYPE.COMMON),
 (
  b'vehLockMode', int, 0, None, b'skip', ENTRY_TYPE.COMMON),
 (
  b'division', None, None, None, b'skip', ENTRY_TYPE.COMMON),
 (
  b'bots', dict, {}, None, b'skip', ENTRY_TYPE.COMMON),
 (
  b'commonNumStarted', int, 0, None, b'skip', ENTRY_TYPE.COMMON),
 (
  b'commonNumDestroyed', int, 0, None, b'skip', ENTRY_TYPE.COMMON),
 (
  b'commonNumDefended', int, 0, None, b'skip', ENTRY_TYPE.COMMON),
 (
  b'commonNumCaptured', int, 0, None, b'skip', ENTRY_TYPE.COMMON),
 (
  b'accountCompDescr', dict, {}, None, b'skip', ENTRY_TYPE.COMMON),
 (
  b'teamHealth', dict, {}, None, b'skip', ENTRY_TYPE.COMMON),
 (
  b'battleModifiersDescr', tuple, (), None, b'skip', ENTRY_TYPE.COMMON),
 (
  b'bonusCapsOverrides', dict, {}, None, b'skip', ENTRY_TYPE.COMMON),
 (
  b'canStun', bool, False, None, b'any', ENTRY_TYPE.SERVER),
 (
  b'potentialDamageDealt', int, 0, None, b'sum', ENTRY_TYPE.SERVER),
 (
  b'soloHitsAssisted', int, 0, None, b'sum', ENTRY_TYPE.SERVER),
 (
  b'isEnemyBaseCaptured', bool, False, None, b'max', ENTRY_TYPE.SERVER),
 (
  b'stucks', list, [], DeltaPacker(roundToInt), b'extend', ENTRY_TYPE.SERVER),
 (
  b'autoAimedShots', int, 0, None, b'sum', ENTRY_TYPE.SERVER),
 (
  b'presenceTime', int, 0, None, b'max', ENTRY_TYPE.SERVER),
 (
  b'spotList', list, [], None, b'extend', ENTRY_TYPE.SERVER),
 (
  b'ammo', list, [], None, b'skip', ENTRY_TYPE.SERVER),
 (
  b'crewActivityFlags', list, [], None, b'skip', ENTRY_TYPE.SERVER),
 (
  b'series', dict, {}, None, b'skip', ENTRY_TYPE.SERVER),
 (
  b'tkillRating', float, 0.0, None, b'sum', ENTRY_TYPE.SERVER),
 (
  b'thitPenalties', dict, {}, None, b'joinTHitPenalties', ENTRY_TYPE.SERVER),
 (
  b'destroyedObjects', dict, {}, None, b'sumByEackKey', ENTRY_TYPE.SERVER),
 (
  b'discloseShots', list, [], DeltaPacker(), b'extend', ENTRY_TYPE.SERVER),
 (
  b'critsCount', int, 0, None, b'sum', ENTRY_TYPE.SERVER),
 (
  b'aimerSeries', int, 0, None, b'max', ENTRY_TYPE.SERVER),
 (
  b'observedByEnemyTime', int, -1, None, b'any', ENTRY_TYPE.SERVER),
 (
  b'critsByType', dict, {},
  DictPacker((
   b'destroyed', dict, {}, SimpleDictPacker(int, VEHICLE_DEVICE_TYPE_NAMES), b'skip'), (
   b'critical', dict, {}, SimpleDictPacker(int, VEHICLE_DEVICE_TYPE_NAMES), b'skip'), (
   b'tankman', dict, {}, SimpleDictPacker(int, VEHICLE_TANKMAN_TYPE_NAMES), b'skip')),
  b'joinCritsByType', ENTRY_TYPE.SERVER),
 (
  b'innerModuleCritCount', int, 0, None, b'sum', ENTRY_TYPE.SERVER),
 (
  b'innerModuleDestrCount', int, 0, None, b'sum', ENTRY_TYPE.SERVER),
 (
  b'isAnyOurCrittedInnerModules', int, 0, None, b'max', ENTRY_TYPE.SERVER),
 (
  b'killsAssistedTrack', int, 0, None, b'sum', ENTRY_TYPE.SERVER),
 (
  b'killsAssistedRadio', int, 0, None, b'sum', ENTRY_TYPE.SERVER),
 (
  b'killsAssistedStun', int, 0, None, b'sum', ENTRY_TYPE.SERVER),
 (
  b'damagedVehicleCntAssistedTrack', int, 0, None, b'sum', ENTRY_TYPE.SERVER),
 (
  b'damagedVehicleCntAssistedRadio', int, 0, None, b'sum', ENTRY_TYPE.SERVER),
 (
  b'damagedVehicleCntAssistedStun', int, 0, None, b'sum', ENTRY_TYPE.SERVER),
 (
  b'isNotSpotted', bool, True, None, b'max', ENTRY_TYPE.SERVER),
 (
  b'isAnyHitReceivedWhileCapturing', bool, False, None, b'max', ENTRY_TYPE.SERVER),
 (
  b'damageAssistedRadioWhileInvisible', int, 0, None, b'sum', ENTRY_TYPE.SERVER),
 (
  b'damageAssistedTrackWhileInvisible', int, 0, None, b'sum', ENTRY_TYPE.SERVER),
 (
  b'damageAssistedStunWhileInvisible', int, 0, None, b'sum', ENTRY_TYPE.SERVER),
 (
  b'damageEventList', dict, {}, None, b'joinTargetEventLists', ENTRY_TYPE.SERVER),
 (
  b'stunEventList', dict, {}, None, b'joinTargetEventLists', ENTRY_TYPE.SERVER),
 (
  b'assistEventList', dict, {}, None, b'joinTargetEventLists', ENTRY_TYPE.SERVER),
 (
  b'damageFromEnemiesEventList', dict, {}, None, b'joinTargetEventLists', ENTRY_TYPE.SERVER),
 (
  b'multiDamageEvents', dict, {}, None, b'joinDicts', ENTRY_TYPE.SERVER),
 (
  b'multiStunEvents', dict, {}, None, b'joinDicts', ENTRY_TYPE.SERVER),
 (
  b'inBattleMaxSniperSeries', int, 0, None, b'max', ENTRY_TYPE.SERVER),
 (
  b'inBattleMaxKillingSeries', int, 0, None, b'max', ENTRY_TYPE.SERVER),
 (
  b'inBattleMaxPiercingSeries', int, 0, None, b'max', ENTRY_TYPE.SERVER),
 (
  b'firstDamageTime', int, 0, None, b'min', ENTRY_TYPE.SERVER),
 (
  b'consumedAmmo', None, None, None, b'skip', ENTRY_TYPE.SERVER),
 (
  b'ironShieldDamage', int, 0, None, b'sum', ENTRY_TYPE.SERVER),
 (
  b'occupyingForceDestruction', bool, False, None, b'max', ENTRY_TYPE.SERVER),
 (
  b'occupyingForceBasePoints', int, 0, None, b'sum', ENTRY_TYPE.SERVER),
 (
  b'directEnemyHits', int, 0, None, b'sum', ENTRY_TYPE.SERVER),
 (
  b'explosionEnemyHits', int, 0, None, b'sum', ENTRY_TYPE.SERVER),
 (
  b'piercingEnemyHits', int, 0, None, b'sum', ENTRY_TYPE.SERVER),
 (
  b'indirectEnemyHits', int, 0, None, b'sum', ENTRY_TYPE.SERVER),
 (
  b'enemyHits', int, 0, None, b'sum', ENTRY_TYPE.SERVER),
 (
  b'spottedBeforeWeBecameSpotted', int, 0, None, b'sum', ENTRY_TYPE.SERVER),
 (
  b'spottedAndDamagedSPG', int, 0, None, b'sum', ENTRY_TYPE.SERVER),
 (
  b'damageList', list, [], None, b'extend', ENTRY_TYPE.SERVER),
 (
  b'killList', list, [], None, b'extend', ENTRY_TYPE.SERVER),
 (
  b'vehLockTimeFactor', float, 0.0, None, b'skip', ENTRY_TYPE.SERVER),
 (
  b'misc', dict, {}, None, b'any', ENTRY_TYPE.SERVER),
 (
  b'vehsByClass', dict, {}, None, b'any', ENTRY_TYPE.SERVER),
 (
  b'avatarAmmoEquipped', set, set(), None, b'skip', ENTRY_TYPE.SERVER),
 (
  b'vehRankRaised', int, 0, None, b'skip', ENTRY_TYPE.SERVER),
 (
  b'eventGoldByEventID', dict, {}, None, b'skip', ENTRY_TYPE.SERVER),
 (
  b'playerRank', int, 0, None, b'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  b'quickShellChangerUsageCount', int, 0, None, b'skip', ENTRY_TYPE.SERVER),
 (
  b'goldBankGain', int, 0, None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'setupsIndexes', dict, {}, None, b'any', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'startAmmo', list, [], None, b'skip', ENTRY_TYPE.SERVER),
 (
  b'initialVehicleAmmo', list, [], None, b'skip', ENTRY_TYPE.SERVER),
 (
  b'replayURL', str, b'', None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'currencies', dict, {}, MergeDictPacker(), b'joinByEachPacker', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'entityCaptured', dict, {}, None, b'any', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'poiCapturedByOwnTeam', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'isFirstBlood', bool, False, None, b'skip', ENTRY_TYPE.VEHICLE_ALL),
 (
  b'finishAllPlayersLeft', bool, False, None, b'skip', ENTRY_TYPE.COMMON),
 (
  b'originalBattlePassPoints', int, 0, None, b'sum', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'battlePassPointsReplay', str, b'', ValueReplayPacker(), b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'battlePassPoints', int, 0, None, b'sum', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'eventBattlePassPointsList', list, [], None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'eventBattlePassPoints', int, 0, None, b'sum', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'prestigeResults', dict, {}, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'pbhResults', dict, {}, None, b'skip', ENTRY_TYPE.SERVER),
 (
  b'finalVehInfo', dict, {}, None, b'skip', ENTRY_TYPE.SERVER),
 (
  b'commendationsReceived', int, 0, None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'commendationsSent', int, 0, None, b'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  b'petSystemCredits', int, 0, None, b'sum', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'petSystemCreditsFactor100', int, 0, None, b'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  b'isBattleRigged', bool, False, None, b'skip', ENTRY_TYPE.SERVER)]
BATTLE_PASS_RESULTS = [
 (
  b'bpChaptersInfo', dict, {}, None, b'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  b'bpTopPoints', int, 0, None, b'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  b'bpTopExternalPoints', dict, {}, None, b'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  b'bpBonusPoints', int, 0, None, b'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  b'bpNonChapterPointsDiff', int, 0, None, b'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  b'hasBattlePass', bool, False, None, b'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  b'battlePassComplete', bool, False, None, b'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  b'availablePoints', int, 0, None, b'skip', ENTRY_TYPE.ACCOUNT_ALL)]
