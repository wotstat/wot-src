import json
from collections import namedtuple
from copy import deepcopy
from typing import TYPE_CHECKING
import BigWorld
from account_helpers.premium_info import PremiumInfo
from adisp import adisp_async
from constants import CURRENT_GAME_ID, MIN_VEHICLE_LEVEL, SPA_ATTRS
from gui.shared.ext_money import ExtendedMoney
from gui.shared.money import Currency, DynamicMoney, Money
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
from helpers import dependency, time_utils
from nation_change.nation_change_helpers import NationalGroupDataAccumulator
from skeletons.gui.game_control import IWalletController
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared.utils.requesters import IStatsRequester
if TYPE_CHECKING:
    from typing import Dict, Set, Tuple
_ADDITIONAL_XP_DATA_KEY = b'_additionalXPCache'
_ControllableXPData = namedtuple(b'_ControllableXPData', (b'vehicleID', b'bonusType', b'extraXP', b'extraFreeXP', b'extraTmenXP', b'isXPToTMan'))

class StatsRequester(AbstractSyncDataRequester, IStatsRequester):
    wallet = dependency.descriptor(IWalletController)
    lobbyContext = dependency.descriptor(ILobbyContext)

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
    def money(self):
        return Money(credits=self.credits, gold=self.gold, crystal=self.crystal, eventCoin=self.eventCoin, bpcoin=self.bpcoin, equipCoin=self.equipCoin)

    @property
    def extMoney(self):
        return ExtendedMoney(freeXP=self.freeXP, credits=self.credits, gold=self.gold, crystal=self.crystal, eventCoin=self.eventCoin, bpcoin=self.bpcoin, equipCoin=self.equipCoin)

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
        return NationalGroupDataAccumulator(self.getCacheValue(b'vehTypeXP', dict()))

    @property
    def multipliedVehicles(self):
        return self.getCacheValue(b'multipliedXPVehs', list())

    @property
    def applyAdditionalXPCount(self):
        maxCount = self.lobbyContext.getServerSettings().getAdditionalBonusConfig().get(b'applyCount', 0)
        return max(maxCount - self.getCacheValue(b'applyAdditionalXPCount', maxCount), 0)

    @property
    def multipliedRankedVehicles(self):
        return self.getCacheValue(b'multipliedRankedBattlesVehs', set())

    @property
    def eliteVehicles(self):
        return self.getCacheValue(b'eliteVehicles', list())

    @property
    def vehicleTypeLocks(self):
        return self.getCacheValue(b'vehTypeLocks', dict())

    @property
    def globalVehicleLocks(self):
        return self.getCacheValue(b'globalVehicleLocks', dict())

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
        subscriptionKey = b'/%s/game/premium_subscription' % CURRENT_GAME_ID
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
        return self.getCacheValue((b'initial', b'unlocks'), list())

    @property
    def vehicleSlots(self):
        return self.getCacheValue(b'slots', 0)

    @property
    def dailyPlayHours(self):
        return self.getCacheValue(b'dailyPlayHours', [0])

    @property
    def todayPlayHours(self):
        if not self.dailyPlayHours:
            return 0
        return self.dailyPlayHours[-1]

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
        return self.getCacheValue(b'denunciations', {}).get(b'left', (0, 0))

    @property
    def battleDenunciationsLeft(self):
        return self.denunciationsLeft[1]

    @property
    def hangarDenunciationsLeft(self):
        return self.denunciationsLeft[0]

    @property
    def hangarDenunciations(self):
        return self.getCacheValue(b'denunciations', {}).get(b'hangarDenunciations', {})

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
    def refSystem20(self):
        return self.getCacheValue(b'refSystem20', {})

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
    def isGoldFishBonusApplied(self):
        gfKey = SPA_ATTRS.GOLFISH_BONUS_APPLIED
        result = False
        spaDict = self.SPA
        if gfKey in spaDict:
            result = int(spaDict[gfKey])
        return result

    @property
    def isAnonymousRestricted(self):
        gfKey = SPA_ATTRS.ANONYM_RESTRICTED
        result = False
        spaDict = self.SPA
        if gfKey in spaDict:
            result = int(spaDict[gfKey])
        return result

    def getTelecomBundleId(self):
        for key, attrValue in self.SPA.iteritems():
            if key.startswith(SPA_ATTRS.RSS):
                value = json.loads(attrValue)
                return value[b'bundleID']

        return

    @property
    def isSsrPlayEnabled(self):
        return self.getCacheValue(b'isSsrPlayEnabled', False)

    @property
    def comp7(self):
        return self.getCacheValue(b'comp7', {})

    @property
    def tutorialsCompleted(self):
        return self.getCacheValue(b'tutorialsCompleted', 0)

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
        return deepcopy(self.getCacheValue(b'preferredMaps', {}).get(b'blackList', {}))

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

    @adisp_async
    def _requestCache(self, callback):
        BigWorld.player().stats.getCache((lambda resID, value: self._response(resID, value, callback)))
        return

    def _preprocessValidData(self, data):
        result = super(StatsRequester, self)._preprocessValidData(data)
        extraXPInfo = result.get(_ADDITIONAL_XP_DATA_KEY, {})
        if extraXPInfo:
            result[_ADDITIONAL_XP_DATA_KEY] = processedXP = {}
            for vehicleID, XPData in extraXPInfo.iteritems():
                if XPData:
                    arenaUniqueID = XPData[0]
                    processedXP[arenaUniqueID] = _ControllableXPData(vehicleID, *XPData[1:])

        return result
