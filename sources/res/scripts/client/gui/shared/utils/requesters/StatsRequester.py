from __future__ import absolute_import
import json
from collections import namedtuple
import typing
from future.utils import iteritems
import BigWorld
from account_helpers.premium_info import PremiumInfo
from constants import SPA_ATTRS, MIN_VEHICLE_LEVEL
from gui.shared.money import Money, Currency, DynamicMoney
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
from gui.veh_post_progression.models.ext_money import ExtendedMoney
from helpers import time_utils, dependency
from nation_change.nation_change_helpers import NationalGroupDataAccumulator
from skeletons.gui.game_control import IWalletController, IWotPlusController
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared.utils.requesters import IStatsRequester
if typing.TYPE_CHECKING:
    from typing import List, Tuple
_ADDITIONAL_XP_DATA_KEY = b'_additionalXPCache'
_ControllableXPData = namedtuple(b'_ControllableXPData', (b'vehicleID', b'bonusType', b'extraXP', b'extraFreeXP', b'extraTmenXP', b'isXPToTMan', b'premMask', b'dailyXPFactor'))

class StatsRequester(AbstractSyncDataRequester, IStatsRequester):
    wallet = dependency.descriptor(IWalletController)
    lobbyContext = dependency.descriptor(ILobbyContext)
    wotPlusController = dependency.descriptor(IWotPlusController)

    @property
    def mayConsumeWalletResources(self):
        return bool(self.getCacheValue(b'mayConsumeWalletResources', 0))

    @property
    def currencyStatuses(self):
        return self.wallet.componentsStatuses

    @property
    def dynamicCurrencyStatuses(self):
        return self.wallet.dynamicComponentsStatuses

    @property
    def credits(self):
        return max(self.actualCredits, 0)

    @property
    def gold(self):
        return max(self.actualGold, 0)

    @property
    def crystal(self):
        return max(self.actualCrystal, 0)

    @property
    def eventCoin(self):
        return max(self.actualEventCoin, 0)

    @property
    def bpcoin(self):
        return max(self.actualBpcoin, 0)

    @property
    def equipCoin(self):
        return max(self.actualEquipCoin, 0)

    @property
    def postProgressionXP(self):
        return self.getCacheValue(b'XPpp', 0)

    @property
    def money(self):
        return Money(credits=self.credits, gold=self.gold, crystal=self.crystal, eventCoin=self.eventCoin, bpcoin=self.bpcoin, equipCoin=self.equipCoin)

    @property
    def actualCredits(self):
        return self.getCacheValue(Currency.CREDITS, 0)

    @property
    def actualGold(self):
        if self.mayConsumeWalletResources or not self.wallet.useGold:
            return self.getCacheValue(Currency.GOLD, 0)
        return 0

    @property
    def actualCrystal(self):
        return self.getCacheValue(Currency.CRYSTAL, 0)

    @property
    def actualEventCoin(self):
        return self.getCacheValue(Currency.EVENT_COIN, 0)

    @property
    def actualBpcoin(self):
        return self.getCacheValue(Currency.BPCOIN, 0)

    @property
    def actualEquipCoin(self):
        return self.getCacheValue(Currency.EQUIP_COIN, 0)

    @property
    def actualMoney(self):
        return Money(credits=self.actualCredits, gold=self.actualGold, crystal=self.actualCrystal, eventCoin=self.actualEventCoin, bpcoin=self.actualBpcoin, equipCoin=self.actualEquipCoin)

    @property
    def freeXP(self):
        return max(self.actualFreeXP, 0)

    @property
    def actualFreeXP(self):
        if self.mayConsumeWalletResources or not self.wallet.useFreeXP:
            return self.getCacheValue(b'freeXP', 0)
        return 0

    @property
    def vehiclesXPs(self):
        return NationalGroupDataAccumulator(self.getCacheValue(b'vehTypeXP', {}))

    @property
    def multipliedVehicles(self):
        return self.getCacheValue(b'multipliedXPVehs', [])

    @property
    def prestigeMilestonesAchieved(self):
        return self.getCacheValue(b'prestigeMilestonesAchieved', {})

    @property
    def applyAdditionalXPCount(self):
        maxCount = self.lobbyContext.getServerSettings().getAdditionalBonusConfig().get(b'applyCount', 0)
        return max(maxCount - self.getCacheValue(b'applyAdditionalXPCount', maxCount), 0)

    @property
    def applyAdditionalWoTPlusXPCount(self):
        maxCount = self.wotPlusController.getSettingsStorage().getAdditionalXPBonusCount()
        return max(maxCount - self.getCacheValue(b'applyAdditionalWoTPlusXPCount', maxCount), 0)

    @property
    def dailyAppliedAdditionalXP(self):
        return self.dummySessionStats.get(b'totalDailyAppliedAdditionalXP', 0)

    @property
    def multipliedRankedVehicles(self):
        return self.getCacheValue(b'multipliedRankedBattlesVehs', set())

    @property
    def eliteVehicles(self):
        return self.getCacheValue(b'eliteVehicles', set())

    @property
    def vehicleTypeLocks(self):
        return self.getCacheValue(b'vehTypeLocks', {})

    @property
    def globalVehicleLocks(self):
        return self.getCacheValue(b'globalVehicleLocks', {})

    @property
    def attributes(self):
        return self.getCacheValue(b'attrs', 0)

    def isActivePremium(self, checkPremiumType):
        return self.getCacheValue(b'premiumInfo', PremiumInfo()).isActivePremium(checkPremiumType)

    @property
    def activePremiumType(self):
        return self.getCacheValue(b'premiumInfo', PremiumInfo()).activePremiumType

    @property
    def isPremium(self):
        return self.getCacheValue(b'premiumInfo', PremiumInfo()).isPremium

    @property
    def totalPremiumExpiryTime(self):
        return self.getCacheValue(b'premiumInfo', PremiumInfo()).totalPremiumExpiryTime

    @property
    def activePremiumExpiryTime(self):
        return self.getCacheValue(b'premiumInfo', PremiumInfo()).activePremiumExpiryTime

    @property
    def premiumInfo(self):
        return self.getCacheValue(b'premiumInfo', PremiumInfo()).data

    @property
    def isSubscriptionEnabled(self):
        subscriptionKey = b'/wot/game/premium_subscription'
        return subscriptionKey in self.SPA

    @property
    def isTeamKiller(self):
        return self.getCacheValue(b'tkillIsSuspected', False)

    @property
    def restrictions(self):
        return self.getCacheValue(b'restrictions', {})

    @property
    def unlocks(self):
        return self.getCacheValue(b'unlocks', set())

    @property
    def initialUnlocks(self):
        return self.getCacheValue((b'initial', b'unlocks'), set())

    @property
    def vehicleSlots(self):
        return self.getCacheValue(b'slots', 0)

    @property
    def dailyPlayHours(self):
        return self.getCacheValue(b'dailyPlayHours', [0])

    @property
    def todayPlayHours(self):
        return self.dailyPlayHours[0]

    @property
    def playLimits(self):
        return self.getCacheValue(b'playLimits', ((time_utils.ONE_DAY, b''), (time_utils.ONE_WEEK, b'')))

    def getDailyTimeLimits(self):
        return self.playLimits[0][0]

    def getWeeklyTimeLimits(self):
        return self.playLimits[1][0]

    def getPlayTimeLimits(self):
        return (
         self.getDailyTimeLimits(), self.getWeeklyTimeLimits())

    @property
    def tankmenBerthsCount(self):
        return self.getCacheValue(b'berths', 0)

    @property
    def vehicleSellsLeft(self):
        return self.getCacheValue(b'vehicleSellsLeft', 0)

    @property
    def freeTankmenLeft(self):
        return self.getCacheValue(b'freeTMenLeft', 0)

    @property
    def accountDossier(self):
        return self.getCacheValue(b'dossier', b'')

    @property
    def denunciationsLeft(self):
        return self.getCacheValue(b'denunciationsLeft', 0)

    @property
    def freeVehiclesLeft(self):
        return self.getCacheValue(b'freeVehiclesLeft', b'')

    @property
    def clanDBID(self):
        return self.getCacheValue(b'clanDBID', 0)

    @property
    def clanInfo(self):
        return self.getCacheValue(b'clanInfo', set())

    @property
    def globalRating(self):
        return self.getCacheValue(b'globalRating', 0)

    @property
    def SPA(self):
        return self.getCacheValue(b'SPA', {})

    @property
    def piggyBank(self):
        return self.getCacheValue(b'piggyBank', {})

    @property
    def entitlements(self):
        return self.getCacheValue(b'entitlements', {})

    @property
    def dummySessionStats(self):
        return self.getCacheValue(b'dummySessionStats', {})

    @property
    def additionalXPCache(self):
        return self.getCacheValue(_ADDITIONAL_XP_DATA_KEY, {})

    @property
    def isAnonymousRestricted(self):
        gfKey = SPA_ATTRS.ANONYM_RESTRICTED
        result = False
        spaDict = self.SPA
        if gfKey in spaDict:
            result = int(spaDict[gfKey])
        return result

    def getTelecomBundleId(self):
        for key, attrValue in iteritems(self.SPA):
            if key.startswith(SPA_ATTRS.RSS):
                value = json.loads(attrValue)
                return value[b'bundleID']

        return

    @property
    def isSsrPlayEnabled(self):
        return self.getCacheValue(b'isSsrPlayEnabled', False)

    @property
    def oldVehInvIDs(self):
        return self.getCacheValue(b'oldVehInvIDs', ())

    @property
    def dynamicCurrencies(self):
        return self.getCacheValue(b'dynamicCurrencies', {})

    @property
    def isEmergencyModeEnabled(self):
        return self.getCacheValue(b'isEmergencyModeEnabled', False)

    def getMapsBlackList(self):
        blackList = self.getCacheValue(b'preferredMaps', {}).get(b'blackList', ())
        return blackList

    def getMaxResearchedLevelByNations(self):
        return self.getCacheValue(b'maxResearchedLevelByNation', {})

    def getMaxResearchedLevel(self, nationID):
        return self.getMaxResearchedLevelByNations().get(nationID, MIN_VEHICLE_LEVEL)

    def getMoneyExt(self, vehCD):
        vehicleXP = self.vehiclesXPs.get(vehCD, 0)
        return ExtendedMoney(xp=(self.freeXP + vehicleXP), vehXP=vehicleXP, freeXP=self.freeXP, **self.money.toDict())

    def getDynamicMoney(self):
        money = self.money.toDict()
        money.update(self.dynamicCurrencies)
        return DynamicMoney(**money)

    def getWeeklyVehicleCrystals(self, vehCD):
        return self.getCacheValue(b'weeklyVehicleCrystals', {}).get(vehCD, 0)

    @property
    def luiVersion(self):
        return self.getCacheValue(b'limitedUi', {}).get(b'ver', 1)

    def getABGroup(self, feature):
        return self.getCacheValue(b'abFeatureTest', {}).get(feature)

    def _requestCache(self, callback=None):
        BigWorld.player().stats.getCache((lambda resID, value: self._response(resID, value, callback)))
        return

    def _preprocessValidData(self, data):
        result = super(StatsRequester, self)._preprocessValidData(data)
        extraXPInfo = result.get(_ADDITIONAL_XP_DATA_KEY, {})
        if extraXPInfo:
            result[_ADDITIONAL_XP_DATA_KEY] = processedXP = {}
            for vehicleID, XPData in iteritems(extraXPInfo):
                if XPData:
                    arenaUniqueID = XPData[0]
                    processedXP[arenaUniqueID] = _ControllableXPData(vehicleID, *XPData[1:])

        return result
