from __future__ import absolute_import
import typing
if typing.TYPE_CHECKING:
    from typing import Dict, Generator, List, NamedTuple, Optional, Sequence, Set, Tuple, Union
    from collections import OrderedDict
    from gui.shared.gui_items.dossier.achievements.abstract import RegularAchievement
    from gui.shared.gui_items.gui_item_economics import ItemPrice
    from gui.shared.gui_items.loot_box import LootBox
    from gui.shared.money import Money, DynamicMoney
    from gui.shared.utils.requesters import InventoryRequester
    from gui.shared.utils.requesters.ShopRequester import DefaultShopRequester
    from gui.veh_post_progression.models.ext_money import ExtendedMoney
    from post_progression_common import VehicleState
    from items.vehicles import VehicleType
    PetID = int
    PetEventID = int
    PetNameID = int
    PetBonusID = int
    PetSynergy = int
    PetSynergyLevel = int

class IRequester(object):

    def request(self, callback=None):
        raise NotImplementedError
        return

    def isSynced(self):
        raise NotImplementedError
        return

    def clear(self):
        raise NotImplementedError
        return


class IAnonymizerRequester(IRequester):

    @property
    def isPlayerAnonymized(self):
        raise NotImplementedError
        return

    @property
    def contactsFeedback(self):
        raise NotImplementedError
        return


class IInventoryRequester(IRequester):

    def invalidateItem(self, itemTypeID, invIdx):
        raise NotImplementedError
        return

    def getC11nItemAppliedVehicles(self, itemCD):
        raise NotImplementedError
        return

    def getC11nItemAppliedOnVehicleCount(self, itemCD, vehicleIntCD):
        raise NotImplementedError
        return

    def initC11nItemsNoveltyData(self):
        raise NotImplementedError
        return

    def updateC11nItemNoveltyData(self, itemIntCD):
        raise NotImplementedError
        return

    def getC11nItemNoveltyData(self, itemIntCD):
        raise NotImplementedError
        return

    def getC11nItemsNoveltyCounters(self, vehicleType):
        raise NotImplementedError
        return

    def updateC11nProgressionDataForItem(self, itemIntCD):
        raise NotImplementedError
        return

    def updateC11nProgressionData(self):
        raise NotImplementedError
        return

    def getC11nProgressionDataForItem(self, itemIntCD):
        raise NotImplementedError
        return

    def getC11nProgressionDataForVehicle(self, vehicleIntCD):
        raise NotImplementedError
        return

    def getC11nProgressionData(self, itemIntCD, vehicleIntCD):
        raise NotImplementedError
        return

    def getItemsData(self, itemTypeID):
        raise NotImplementedError
        return

    def getItemData(self, typeCompDescr):
        raise NotImplementedError
        return

    def getTankmanData(self, tmanInvID):
        raise NotImplementedError
        return

    def getVehicleData(self, vehInvID):
        raise NotImplementedError
        return

    def getOutfitData(self, intCD, season):
        raise NotImplementedError
        return

    def getPreviousItem(self, itemTypeID, invDataIdx):
        raise NotImplementedError
        return

    def getItems(self, itemTypeIdx, dataIdx=None):
        raise NotImplementedError
        return

    def getC11nSerialNumber(self, itemCD):
        raise NotImplementedError
        return

    def getFreeSlots(self, vehiclesSlots):
        raise NotImplementedError
        return

    def getCacheValue(self, key, defaultValue):
        raise NotImplementedError
        return

    def getInventoryEnhancements(self):
        raise NotImplementedError
        return

    def getInstalledEnhancements(self):
        raise NotImplementedError
        return

    def getVehPostProgression(self, vehIntCD):
        raise NotImplementedError
        return

    def getVehExtData(self, vehIntCD):
        raise NotImplementedError
        return

    def getVehPostProgressionFeaturesListByCD(self, vehIntCD):
        raise NotImplementedError
        return

    def getDynSlotTypeID(self, vehIntCD):
        raise NotImplementedError
        return

    def getIventoryVehiclesCDs(self):
        raise NotImplementedError
        return

    def getInvIDsIterator(self):
        raise NotImplementedError
        return


class IStatsRequester(IRequester):

    @property
    def mayConsumeWalletResources(self):
        raise NotImplementedError
        return

    @property
    def currencyStatuses(self):
        raise NotImplementedError
        return

    @property
    def dynamicCurrencyStatuses(self):
        raise NotImplementedError
        return

    @property
    def credits(self):
        raise NotImplementedError
        return

    @property
    def gold(self):
        raise NotImplementedError
        return

    @property
    def crystal(self):
        raise NotImplementedError
        return

    @property
    def eventCoin(self):
        raise NotImplementedError
        return

    @property
    def equipCoin(self):
        raise NotImplementedError
        return

    @property
    def postProgressionXP(self):
        raise NotImplementedError
        return

    @property
    def bpcoin(self):
        raise NotImplementedError
        return

    @property
    def money(self):
        raise NotImplementedError
        return

    @property
    def actualCredits(self):
        raise NotImplementedError
        return

    @property
    def actualGold(self):
        raise NotImplementedError
        return

    @property
    def actualCrystal(self):
        raise NotImplementedError
        return

    @property
    def actualEventCoin(self):
        raise NotImplementedError
        return

    @property
    def actualBpcoin(self):
        raise NotImplementedError
        return

    @property
    def actualEquipCoin(self):
        raise NotImplementedError
        return

    @property
    def actualMoney(self):
        raise NotImplementedError
        return

    @property
    def freeXP(self):
        raise NotImplementedError
        return

    @property
    def actualFreeXP(self):
        raise NotImplementedError
        return

    @property
    def vehiclesXPs(self):
        raise NotImplementedError
        return

    @property
    def multipliedVehicles(self):
        raise NotImplementedError
        return

    @property
    def prestigeMilestonesAchieved(self):
        raise NotImplementedError
        return

    @property
    def applyAdditionalXPCount(self):
        raise NotImplementedError
        return

    @property
    def applyAdditionalWoTPlusXPCount(self):
        raise NotImplementedError
        return

    @property
    def dailyAppliedAdditionalXP(self):
        raise NotImplementedError
        return

    @property
    def multipliedRankedVehicles(self):
        raise NotImplementedError
        return

    @property
    def eliteVehicles(self):
        raise NotImplementedError
        return

    @property
    def vehicleTypeLocks(self):
        raise NotImplementedError
        return

    @property
    def globalVehicleLocks(self):
        raise NotImplementedError
        return

    @property
    def attributes(self):
        raise NotImplementedError
        return

    def isActivePremium(self, checkPremiumType):
        raise NotImplementedError
        return

    @property
    def activePremiumType(self):
        raise NotImplementedError
        return

    @property
    def isPremium(self):
        raise NotImplementedError
        return

    @property
    def totalPremiumExpiryTime(self):
        raise NotImplementedError
        return

    @property
    def activePremiumExpiryTime(self):
        raise NotImplementedError
        return

    @property
    def premiumInfo(self):
        raise NotImplementedError
        return

    @property
    def isTeamKiller(self):
        raise NotImplementedError
        return

    @property
    def restrictions(self):
        raise NotImplementedError
        return

    @property
    def unlocks(self):
        raise NotImplementedError
        return

    @property
    def initialUnlocks(self):
        raise NotImplementedError
        return

    @property
    def vehicleSlots(self):
        raise NotImplementedError
        return

    @property
    def dailyPlayHours(self):
        raise NotImplementedError
        return

    @property
    def todayPlayHours(self):
        raise NotImplementedError
        return

    @property
    def playLimits(self):
        raise NotImplementedError
        return

    def getDailyTimeLimits(self):
        raise NotImplementedError
        return

    def getWeeklyTimeLimits(self):
        raise NotImplementedError
        return

    def getPlayTimeLimits(self):
        raise NotImplementedError
        return

    @property
    def tankmenBerthsCount(self):
        raise NotImplementedError
        return

    @property
    def vehicleSellsLeft(self):
        raise NotImplementedError
        return

    @property
    def freeTankmenLeft(self):
        raise NotImplementedError
        return

    @property
    def accountDossier(self):
        raise NotImplementedError
        return

    @property
    def denunciationsLeft(self):
        raise NotImplementedError
        return

    @property
    def freeVehiclesLeft(self):
        raise NotImplementedError
        return

    @property
    def clanDBID(self):
        raise NotImplementedError
        return

    @property
    def clanInfo(self):
        raise NotImplementedError
        return

    @property
    def globalRating(self):
        raise NotImplementedError
        return

    @property
    def SPA(self):
        raise NotImplementedError
        return

    @property
    def piggyBank(self):
        raise NotImplementedError
        return

    @property
    def entitlements(self):
        raise NotImplementedError
        return

    @property
    def dummySessionStats(self):
        raise NotImplementedError
        return

    @property
    def additionalXPCache(self):
        raise NotImplementedError
        return

    @property
    def isAnonymousRestricted(self):
        raise NotImplementedError
        return

    @property
    def isSsrPlayEnabled(self):
        raise NotImplementedError
        return

    @property
    def oldVehInvIDs(self):
        raise NotImplementedError
        return

    @property
    def dynamicCurrencies(self):
        raise NotImplementedError
        return

    @property
    def isEmergencyModeEnabled(self):
        raise NotImplementedError
        return

    def getMapsBlackList(self):
        raise NotImplementedError
        return

    def getMaxResearchedLevelByNations(self):
        raise NotImplementedError
        return

    def getMaxResearchedLevel(self, nationID):
        raise NotImplementedError
        return

    def getMoneyExt(self, vehCD):
        raise NotImplementedError
        return

    def getDynamicMoney(self):
        raise NotImplementedError
        return

    def getWeeklyVehicleCrystals(self, vehCD):
        raise NotImplementedError
        return

    @property
    def luiVersion(self):
        raise NotImplementedError
        return

    def getABGroup(self, feature):
        raise NotImplementedError
        return

    def getCacheValue(self, key, defaultValue):
        raise NotImplementedError
        return


class IDossierRequester(IRequester):

    def getVehicleDossier(self, vehTypeCompDescr):
        raise NotImplementedError
        return

    def getVehDossiersIterator(self):
        raise NotImplementedError
        return

    def getUserDossierRequester(self, databaseID):
        raise NotImplementedError
        return

    def closeUserDossier(self, databaseID):
        raise NotImplementedError
        return

    def onCenterIsLongDisconnected(self, isLongDisconnected):
        raise NotImplementedError
        return


class IShopCommonStats(object):

    def getPrices(self):
        raise NotImplementedError
        return

    def getBoosterPrices(self):
        raise NotImplementedError
        return

    def getHiddens(self):
        raise NotImplementedError
        return

    def getHiddenBoosters(self):
        raise NotImplementedError
        return

    def getNotToBuyVehicles(self):
        raise NotImplementedError
        return

    def getVehicleRentPrices(self):
        raise NotImplementedError
        return

    def getVehiclesForGold(self):
        raise NotImplementedError
        return

    def getVehiclesSellPriceFactors(self):
        raise NotImplementedError
        return

    def getItemPrice(self, intCD):
        raise NotImplementedError
        return

    def getBoosterPricesTuple(self, boosterID):
        raise NotImplementedError
        return

    def getOperationPrices(self):
        raise NotImplementedError
        return

    def getItem(self, intCD):
        raise NotImplementedError
        return

    def getAchievementReward(self, achievement, arenaType=0):
        raise NotImplementedError
        return

    @property
    def revision(self):
        raise NotImplementedError
        return

    @property
    def paidRemovalCost(self):
        raise NotImplementedError
        return

    @property
    def paidDeluxeRemovalCost(self):
        raise NotImplementedError
        return

    def getPaidModernizedRemovalCost(self, level):
        raise NotImplementedError
        return

    @property
    def paidTrophyBasicRemovalCost(self):
        raise NotImplementedError
        return

    @property
    def paidTrophyUpgradedRemovalCost(self):
        raise NotImplementedError
        return

    @property
    def exchangeRate(self):
        raise NotImplementedError
        return

    @property
    def crystalExchangeRate(self):
        raise NotImplementedError
        return

    @property
    def exchangeRateForShellsAndEqs(self):
        raise NotImplementedError
        return

    @property
    def sellPriceModif(self):
        raise NotImplementedError
        return

    @property
    def vehiclesRestoreConfig(self):
        raise NotImplementedError
        return

    @property
    def tankmenRestoreConfig(self):
        raise NotImplementedError
        return

    def sellPriceModifiers(self, compDescr):
        raise NotImplementedError
        return

    @property
    def slotsPrices(self):
        raise NotImplementedError
        return

    def getVehicleSlotsPrice(self, currentSlotsCount):
        raise NotImplementedError
        return

    @property
    def dropSkillsCost(self):
        raise NotImplementedError
        return

    @property
    def dailyXPFactor(self):
        raise NotImplementedError
        return

    @property
    def winXPFactorMode(self):
        raise NotImplementedError
        return

    @property
    def berthsPrices(self):
        raise NotImplementedError
        return

    def getTankmanBerthPrice(self, berthsCount):
        raise NotImplementedError
        return

    @property
    def isEnabledBuyingGoldShellsForCredits(self):
        raise NotImplementedError
        return

    @property
    def isEnabledBuyingGoldEqsForCredits(self):
        raise NotImplementedError
        return

    @property
    def tankmanCost(self):
        raise NotImplementedError
        return

    @property
    def changeRoleCost(self):
        raise NotImplementedError
        return

    @property
    def tankman(self):
        raise NotImplementedError
        return

    @property
    def freeXPConversion(self):
        raise NotImplementedError
        return

    @property
    def freeXPToTManXPRate(self):
        raise NotImplementedError
        return

    def getItemsData(self):
        raise NotImplementedError
        return

    def getGoodiesData(self):
        raise NotImplementedError
        return

    def getVehCamouflagePriceFactor(self, typeCompDescr):
        raise NotImplementedError
        return

    def getEmblemsGroupPriceFactors(self):
        raise NotImplementedError
        return

    def getEmblemsGroupHiddens(self):
        raise NotImplementedError
        return

    def getInscriptionsGroupPriceFactors(self, nationID):
        raise NotImplementedError
        return

    def getInscriptionsGroupHiddens(self, nationID):
        raise NotImplementedError
        return

    def getCamouflagesPriceFactors(self, nationID):
        raise NotImplementedError
        return

    def getCamouflagesHiddens(self, nationID):
        raise NotImplementedError
        return

    @property
    def premiumCost(self):
        raise NotImplementedError
        return

    @property
    def goodies(self):
        raise NotImplementedError
        return

    def getGoodieByID(self, discountID):
        raise NotImplementedError
        return

    def getGoodiesByVariety(self, variety):
        raise NotImplementedError
        return

    def getBattlePassCost(self):
        raise NotImplementedError
        return

    def getBattlePassLevelCost(self):
        raise NotImplementedError
        return

    @property
    def boosters(self):
        raise NotImplementedError
        return

    @property
    def discounts(self):
        raise NotImplementedError
        return

    @property
    def demountKits(self):
        raise NotImplementedError
        return

    @property
    def recertificationForms(self):
        raise NotImplementedError
        return

    @property
    def mentoringLicenses(self):
        raise NotImplementedError
        return

    def getPremiumPacketCost(self, days):
        raise NotImplementedError
        return

    @property
    def camouflageCost(self):
        raise NotImplementedError
        return

    def getCamouflageCost(self, days=0):
        raise NotImplementedError
        return

    @property
    def playerInscriptionCost(self):
        raise NotImplementedError
        return

    def getInscriptionCost(self, days=0):
        raise NotImplementedError
        return

    @property
    def playerEmblemCost(self):
        raise NotImplementedError
        return

    def getEmblemCost(self, days=0):
        raise NotImplementedError
        return


class IShopRequester(IShopCommonStats, IRequester):
    defaults = None

    def __init__(self):
        super(IShopRequester, self).__init__()
        self.defaults = None
        return

    def getPremiumCostWithDiscount(self, premiumPacketDiscounts=None):
        raise NotImplementedError
        return

    def isActionOnPremium(self):
        raise NotImplementedError
        return

    def getTankmanCostWithGoodyDiscount(self, vehLevel):
        raise NotImplementedError
        return

    @property
    def personalPremiumPacketsDiscounts(self):
        raise NotImplementedError
        return

    @property
    def personalSlotDiscounts(self):
        raise NotImplementedError
        return

    @property
    def personalTankmanDiscounts(self):
        raise NotImplementedError
        return

    @property
    def personalVehicleDiscounts(self):
        raise NotImplementedError
        return

    def getVehicleDiscountDescriptions(self):
        raise NotImplementedError
        return

    def getPersonalVehicleDiscountPrice(self, typeCompDescr):
        raise NotImplementedError
        return

    def bestGoody(self, goodies):
        raise NotImplementedError
        return

    def customRoleSlotChangeCost(self, vehType, isRaw=False):
        raise NotImplementedError
        return

    def getVehicleSlotsItemPrice(self, currentSlotsCount):
        raise NotImplementedError
        return

    def getTankmanCostItemPrices(self, vehLevel):
        raise NotImplementedError
        return

    def getNotInShopProgressionLvlItems(self):
        raise NotImplementedError
        return


class IGoodiesRequester(IRequester):

    @property
    def goodies(self):
        raise NotImplementedError
        return

    def getActiveClanReserves(self):
        raise NotImplementedError
        return


class IRecycleBinRequester(IRequester):

    @property
    def recycleBin(self):
        raise NotImplementedError
        return

    @property
    def vehiclesBuffer(self):
        raise NotImplementedError
        return

    def getVehicleRestoreInfo(self, intCD, restoreDuration, restoreCooldown):
        raise NotImplementedError
        return

    def getVehiclesIntCDs(self):
        raise NotImplementedError
        return

    def getTankmen(self, maxDuration):
        raise NotImplementedError
        return

    def getTankman(self, invID, maxDuration):
        raise NotImplementedError
        return


class IVehicleRotationRequester(IRequester):

    def getBattlesCount(self, groupNum):
        raise NotImplementedError
        return

    def isGroupLocked(self, groupNum):
        raise NotImplementedError
        return

    def getGroupNum(self, vehIntCD):
        raise NotImplementedError
        return

    def isInfinite(self, groupNum):
        raise NotImplementedError
        return


class IRankedRequester(IRequester):

    @property
    def accRank(self):
        raise NotImplementedError
        return

    @property
    def season(self):
        raise NotImplementedError
        return

    @property
    def maxRank(self):
        raise NotImplementedError
        return

    @property
    def stepsCount(self):
        raise NotImplementedError
        return

    @property
    def seasonStepsCount(self):
        raise NotImplementedError
        return

    @property
    def seasonEfficiencyStamp(self):
        raise NotImplementedError
        return

    @property
    def shields(self):
        raise NotImplementedError
        return

    @property
    def persistentBonusBattles(self):
        raise NotImplementedError
        return

    @property
    def dailyBonusBattles(self):
        raise NotImplementedError
        return

    @property
    def divisionsStats(self):
        raise NotImplementedError
        return


class IBattleRoyaleRequester(IRequester):

    @property
    def accTitle(self):
        raise NotImplementedError
        return

    @property
    def battleCount(self):
        raise NotImplementedError
        return

    @property
    def killCount(self):
        raise NotImplementedError
        return

    @property
    def topCount(self):
        raise NotImplementedError
        return

    @property
    def dailyBonusUsedVehicles(self):
        raise NotImplementedError
        return

    def getStats(self, arenaBonusType, playerDatabaseID=None):
        raise NotImplementedError
        return


class IBadgesRequester(IRequester):

    @property
    def available(self):
        raise NotImplementedError
        return

    @property
    def selected(self):
        raise NotImplementedError
        return


class IEpicMetaGameRequester(IRequester):

    @property
    def playerLevelInfo(self):
        raise NotImplementedError
        return

    @property
    def seasonData(self):
        raise NotImplementedError
        return

    @property
    def skillPoints(self):
        raise NotImplementedError
        return

    def selectedSkills(self, vehicleCD):
        raise NotImplementedError
        return

    @property
    def skillLevels(self):
        raise NotImplementedError
        return

    @property
    def battleCount(self):
        raise NotImplementedError
        return

    @property
    def averageXP(self):
        raise NotImplementedError
        return


class IBlueprintsRequester(IRequester):

    def getBlueprintCount(self, vehicleCD, vLevel):
        raise NotImplementedError
        return

    def getBlueprintData(self, vehicleCD, vLevel):
        raise NotImplementedError
        return

    def getBlueprintDiscount(self, vehicleCD, vLevel, potentialFilledCount=0):
        raise NotImplementedError
        return

    def getRequiredCountAndDiscount(self, vehicleCD, vLevel):
        raise NotImplementedError
        return

    def getFragmentDiscountAndCost(self, vehicleCD, vLevel, xpFullCost):
        raise NotImplementedError
        return

    def getAllNationalFragmentsData(self):
        raise NotImplementedError
        return

    def calculateCost(self, oldCost, discount):
        raise NotImplementedError
        return

    def getNationalFragments(self, fragmentCD):
        raise NotImplementedError
        return

    def getNationalAllianceFragments(self, fragmentCD, vehicleLevel):
        raise NotImplementedError
        return

    def getNationalRequiredOptions(self, fragmentCD, vehicleLevel):
        raise NotImplementedError
        return

    def getIntelligenceCount(self):
        raise NotImplementedError
        return

    def getRequiredIntelligenceAndNational(self, vehicleLevel):
        raise NotImplementedError
        return

    def hasUniversalFragments(self):
        raise NotImplementedError
        return

    def isLastFragment(self, totalCount, filledCount):
        raise NotImplementedError
        return

    def canConvertToVehicleFragment(self, vehicleCD, vehicleLevel):
        raise NotImplementedError
        return

    def getConvertibleFragmentCount(self, vehicleCD, vehicleLevel):
        raise NotImplementedError
        return

    def getLayout(self, vehicleCD, vLevel):
        raise NotImplementedError
        return

    def isBlueprintsAvailable(self):
        raise NotImplementedError
        return

    def hasBlueprintsOrFragments(self):
        raise NotImplementedError
        return


class ITokensRequester(IRequester):

    def getTokens(self):
        raise NotImplementedError
        return

    def getToken(self, tokenID):
        raise NotImplementedError
        return

    def getTokenInfo(self, tokenID):
        raise NotImplementedError
        return

    def getTokenCount(self, tokenID):
        raise NotImplementedError
        return

    def getTokenExpiryTime(self, tokenID):
        raise NotImplementedError
        return

    def isTokenAvailable(self, tokenID):
        raise NotImplementedError
        return

    def getAttemptsAfterGuaranteedRewards(self, box):
        raise NotImplementedError
        return

    def getLootBoxesStats(self):
        raise NotImplementedError
        return

    def getLootBoxes(self):
        raise NotImplementedError
        return

    def getLootBoxByTokenID(self, tokenID):
        raise NotImplementedError
        return

    def getLootBoxByID(self, boxID):
        raise NotImplementedError
        return

    def getFreeLootBoxes(self):
        raise NotImplementedError
        return

    def getLootBoxesTotalCount(self):
        raise NotImplementedError
        return

    def getLootBoxesCountByType(self):
        raise NotImplementedError
        return

    def getLastViewedProgress(self, tokenId):
        raise NotImplementedError
        return

    def markTokenProgressAsViewed(self, tokenId):
        raise NotImplementedError
        return

    def hasTokenCountChanged(self, tokenId):
        raise NotImplementedError
        return

    def onDisconnected(self):
        raise NotImplementedError
        return

    def getTokensByPrefixAndPostfix(self, prefix=b'', postfix=b''):
        raise NotImplementedError
        return


class IBaseSessionStats(object):

    @property
    def battleCnt(self):
        raise NotImplementedError
        return

    @property
    def incomeCredits(self):
        raise NotImplementedError
        return

    @property
    def xp(self):
        raise NotImplementedError
        return

    @property
    def incomeCrystal(self):
        raise NotImplementedError
        return

    @property
    def freeXP(self):
        raise NotImplementedError
        return

    @property
    def averageXp(self):
        raise NotImplementedError
        return

    @property
    def ratioDamage(self):
        raise NotImplementedError
        return

    @property
    def helpDamage(self):
        raise NotImplementedError
        return

    @property
    def ratioKill(self):
        raise NotImplementedError
        return

    @property
    def averageDamage(self):
        raise NotImplementedError
        return

    @property
    def blockedDamage(self):
        raise NotImplementedError
        return

    @property
    def winRate(self):
        raise NotImplementedError
        return

    @property
    def wins(self):
        raise NotImplementedError
        return

    @property
    def averageFrags(self):
        raise NotImplementedError
        return

    @property
    def survivedRatio(self):
        raise NotImplementedError
        return

    @property
    def spotted(self):
        raise NotImplementedError
        return


class IBaseAccountStats(IBaseSessionStats):

    @property
    def netCredits(self):
        raise NotImplementedError
        return

    @property
    def netCrystal(self):
        raise NotImplementedError
        return

    @property
    def averageVehicleLevel(self):
        raise NotImplementedError
        return


class IBaseVehStats(IBaseSessionStats):
    pass


class IRandomAccountStats(IBaseAccountStats):

    @property
    def wtr(self):
        raise NotImplementedError
        return


class IRandomVehStats(IBaseVehStats):

    @property
    def wtr(self):
        raise NotImplementedError
        return


class ISessionStatsRequester(IRequester):

    def getAccountStats(self, arenaType):
        raise NotImplementedError
        return

    def getVehiclesStats(self, arenaType, vehId):
        raise NotImplementedError
        return

    def getStatsVehList(self, arenaType):
        raise NotImplementedError
        return

    def getAccountWtr(self):
        raise NotImplementedError
        return


class IOffersRequester(IRequester):

    def isBannerSeen(self, offerID):
        raise NotImplementedError
        return

    def getReceivedGifts(self, offerID):
        raise NotImplementedError
        return


class IBattlePassRequester(IRequester):

    def getSeasonID(self):
        raise NotImplementedError
        return

    def getState(self):
        raise NotImplementedError
        return

    def getActiveChapterID(self):
        raise NotImplementedError
        return

    def getPointsForVehicle(self, vehicleID, default=0):
        raise NotImplementedError
        return

    def getChapterStats(self):
        raise NotImplementedError
        return

    def getCurrentLevelByChapterID(self, chapterID):
        raise NotImplementedError
        return

    def getPointsByChapterID(self, chapterID):
        raise NotImplementedError
        return

    def getNonChapterPoints(self):
        raise NotImplementedError
        return


class IGiftSystemRequester(IRequester):

    @property
    def isHistoryReady(self):
        raise NotImplementedError
        return


class IGameRestrictionsRequester(IRequester):

    @property
    def session(self):
        raise NotImplementedError
        return

    @property
    def hasSessionLimit(self):
        raise NotImplementedError
        return

    def getKickAt(self):
        raise NotImplementedError
        return

    @property
    def settings(self):
        raise NotImplementedError
        return

    @property
    def privateChat(self):
        raise NotImplementedError
        return


class IAchievements20Requester(IRequester):

    def getLayout(self):
        raise NotImplementedError
        return

    def getLayoutState(self):
        raise NotImplementedError
        return

    def getAchievementBitmask(self):
        raise NotImplementedError
        return

    def getLayoutLength(self):
        raise NotImplementedError
        return


class IPetSystemRequester(IRequester):

    def isPetUnlocked(self, petId):
        raise NotImplementedError
        return

    def getActivePetID(self):
        raise NotImplementedError
        return

    def getActiveEventID(self):
        raise NotImplementedError
        return

    def getUnlockedPetIDs(self):
        raise NotImplementedError
        return

    def getStateBehavior(self):
        raise NotImplementedError
        return

    def getSelectedName(self, petID):
        raise NotImplementedError
        return

    def getBonuses(self):
        raise NotImplementedError
        return

    def getActiveBonus(self):
        raise NotImplementedError
        return

    def getAppliedBonusCount(self):
        raise NotImplementedError
        return

    def getSynergyPoints(self, petID):
        raise NotImplementedError
        return

    def getSynergyLevel(self, petID):
        raise NotImplementedError
        return

    def getFirstClickedSynergyPets(self):
        raise NotImplementedError
        return


class IChallengesRequester(IRequester):

    def getUsedFreeRestarts(self, challengeID):
        raise NotImplementedError
        return
