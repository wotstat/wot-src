from __future__ import absolute_import
import typing, itertools
from collections import namedtuple
from adisp import adisp_async
import Event, nations
from gui import GUI_NATIONS
from gui.ClientUpdateManager import g_clientUpdateManager
from gui import SystemMessages
from gui.impl import backport
from gui.prb_control.entities.listener import IGlobalListener
from gui.prb_control.events_dispatcher import g_eventDispatcher
from gui.shared.utils import decorators
from constants import EVENT_CLIENT_DATA, PREMIUM_ENTITLEMENTS
from gui.server_events.bonuses import getNonQuestBonuses, VehiclesBonus, mergeBonuses, CustomizationsBonus, NationalBlueprintBonus, IntelligenceBlueprintBonus
from gui.shared.gui_items.Vehicle import Vehicle
from gui.shared.gui_items import GUI_ITEM_TYPE
from halloween.gui.halloween_gui_constants import FUNCTIONAL_FLAG
from halloween.gui.shared.gui_items.processors.processors import OpenArtefactProcessor
from halloween.skeletons.halloween_controller import IHalloweenController
from halloween.skeletons.halloween_artefacts_controller import IHalloweenArtefactsController
from halloween.skeletons.halloween_twitch_con_controller import IHalloweenTwitchConController
from halloween_common.halloween_constants import ArtefactsSettings, ArtefactType, RENT_VEHICLE_PREFIX, ARTEFACT_ID_MASK, HWStoryChoiceSettings
from halloween.gui.server_events.bonuses import CerfTokenBonus
from helpers import dependency
from items.components.c11n_constants import Rarity
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.customization import ICustomizationService
from skeletons.gui.server_events import IEventsCache
from skeletons.gui.shared import IItemsCache
from shared_utils import first
from gui.shared.money import Currency
from gui.shared.utils.requesters.blueprints_requester import getFragmentNationID
if typing.TYPE_CHECKING:
    from gui.server_events.bonuses import TokensBonus, SimpleBonus
QuestConditions = namedtuple(b'QuestConditions', (b'name', b'description', b'totalValue', b'progress'))
QuestConditions.__new__.__defaults__ = (b'', b'', 0, 0)
ArtefactPrice = namedtuple(b'ArtefactPrice', (b'currency', b'amount'))
ArtefactPrice.__new__.__defaults__ = (None, 0)
QUEST_BONUS_CONDITIONS = (b'cumulative', b'cumulativeExt', b'cumulativeSum', b'vehicleKillsCumulative', b'vehicleDamageCumulative', b'vehicleStunCumulative', b'battles')
PHASE_COMPLETION_QUEST_BR_CONDITION = (b'halloween_phase', b'greater')
TOTAL_PHASE_COUNT = 4
_blueprints_national_order = [str(b'blueprint_national_' + nation) for nation in GUI_NATIONS]
BONUS_ORDER = [
 b'lootBox', b'dossier', HWStoryChoiceSettings.FAKE_MEDAL, b'vehicles', b'slots', b'cerfToken', b'tmanToken', b'tankmen', b'crewSkins', ArtefactsSettings.CREW_100, b'berths', b'customizations', b'crewBooks', PREMIUM_ENTITLEMENTS.VIP, PREMIUM_ENTITLEMENTS.PLUS, PREMIUM_ENTITLEMENTS.BASIC, Currency.BPCOIN, b'battlePassPoints', ArtefactsSettings.KEY_TOKEN, Currency.CRYSTAL, Currency.GOLD, Currency.CREDITS, b'xp', Currency.FREE_XP, Currency.EQUIP_COIN, b'battle_bonus_x5', b'crew_bonus_x3', b'battlePassQuestChainToken', b'tokens', b'battleToken', b'vehicleXP', b'tankmenXP', b'goodies', b'items', b'blueprints_universal'] + _blueprints_national_order + [b'blueprints', b'blueprintsAny']

class Artefact(namedtuple(b'Artefact', (b'artefactID', b'decodePrice', b'skipPrice', b'bonusRewards', b'questConditions', b'artefactTypes'))):

    def getCtx(self):
        return dict(self._asdict())


def getTokenValue(bonus):
    token = first(bonus.getTokens().keys(), b'')
    if token.startswith(b'xpx5') or token.startswith(b'Expx5'):
        return b'battle_bonus_x5'
    return token


def getBlueprintsValue(bonus):
    fragmentCD = bonus.getValue()[0]
    if isinstance(bonus, NationalBlueprintBonus):
        blueprintNation = nations.MAP.get(getFragmentNationID(fragmentCD), nations.NONE_INDEX)
        return str(b'blueprint_national_' + blueprintNation)
    if isinstance(bonus, IntelligenceBlueprintBonus):
        return b'blueprints_universal'
    return b'blueprints'


_VALUE_GETTER_MAP = {b'tokens': getTokenValue, 
   b'battleToken': getTokenValue, 
   b'blueprints': getBlueprintsValue}

def getBonusPriority(bonus):
    bonusType = bonus.getName()
    _getter = _VALUE_GETTER_MAP.get(bonusType)
    bonusValue = _getter(bonus) if _getter else None
    if bonusValue in BONUS_ORDER:
        position = BONUS_ORDER.index(bonusValue)
    elif bonusType in BONUS_ORDER:
        position = BONUS_ORDER.index(bonusType)
    else:
        position = len(BONUS_ORDER) + 1
    return position


def isArtefactQuest(qID):
    return qID.startswith(ArtefactsSettings.QUEST_PREFIX)


class HalloweenArtefactsController(IHalloweenArtefactsController, IGlobalListener):
    itemsCache = dependency.descriptor(IItemsCache)
    eventsCache = dependency.descriptor(IEventsCache)
    settingsCore = dependency.descriptor(ISettingsCore)
    halloweenCtrl = dependency.descriptor(IHalloweenController)
    c11n = dependency.descriptor(ICustomizationService)
    twitchConCtrl = dependency.descriptor(IHalloweenTwitchConController)

    def __init__(self):
        super(HalloweenArtefactsController, self).__init__()
        self.onArtefactStatusUpdated = Event.Event()
        self.onArtefactKeyUpdated = Event.Event()
        self.onArtefactSettingsUpdated = Event.Event()
        self._artefacts = {}
        self._selectedArtefactID = None
        self._needSelectNextSlide = False
        self._choiceID = None
        return

    def fini(self):
        self.stopGlobalListening()
        g_clientUpdateManager.removeObjectCallbacks(self)
        self.halloweenCtrl.onSettingsUpdate -= self.__updateSettings
        self.onArtefactStatusUpdated.clear()
        self.onArtefactKeyUpdated.clear()
        self.onArtefactSettingsUpdated.clear()
        self._artefacts = {}
        self._selectedArtefactID = None
        self._needSelectNextSlide = False
        return

    def isEnabled(self):
        return self._getConfig().get(b'enabled', False)

    def onDisconnected(self):
        super(HalloweenArtefactsController, self).onDisconnected()
        self._selectedArtefactID = None
        self._needSelectNextSlide = False
        self.stopGlobalListening()
        return

    def onAvatarBecomePlayer(self):
        super(HalloweenArtefactsController, self).onAvatarBecomePlayer()
        self._needSelectNextSlide = False
        self.stopGlobalListening()
        return

    def onLobbyInited(self, event):
        super(HalloweenArtefactsController, self).onLobbyInited(event)
        self.startGlobalListening()
        g_clientUpdateManager.addCallbacks({b'tokens': (self.__handleTokensUpdate), 
           (b'eventsData.' + str(EVENT_CLIENT_DATA.QUEST)): (self.__onQuestsUpdated)})
        self.halloweenCtrl.onSettingsUpdate += self.__updateSettings
        return

    def onLobbyStarted(self, ctx):
        super(HalloweenArtefactsController, self).onLobbyStarted(ctx)
        self._needSelectNextSlide = False
        self._initArtefacts()
        return

    def onPrbEntitySwitched(self):
        if self.prbEntity.getModeFlags() & FUNCTIONAL_FLAG.HALLOWEEN:
            return
        self._needSelectNextSlide = False
        return

    @property
    def needSelectNextSlide(self):
        return self._needSelectNextSlide

    @needSelectNextSlide.setter
    def needSelectNextSlide(self, value):
        self._needSelectNextSlide = value
        return

    @property
    def selectedArtefactID(self):
        if self._selectedArtefactID in self._artefacts:
            return self._selectedArtefactID
        else:
            return

    @selectedArtefactID.setter
    def selectedArtefactID(self, artefactID):
        self._selectedArtefactID = artefactID
        return

    def artefactsSorted(self):
        return sorted(self._artefacts.values(), key=(lambda artefact: self.getIndex(artefact.artefactID)))

    def regularArtefacts(self):
        return self.artefactsSorted()[:-1]

    def getFinalArtefact(self):
        return next((x for x in self._artefacts.values() if ArtefactType.FINAL in x.artefactTypes), None)

    def getOpenedArtefactToken(self, artefactID):
        return artefactID + self._getConfig().get(b'openedSuffix', b'')

    def geArtefactIDFromOpenToken(self, token):
        return token.replace(self._getConfig().get(b'openedSuffix', b''), b'')

    def isFinalArtefact(self, artefect):
        return ArtefactType.FINAL in artefect.artefactTypes

    def getArtefact(self, artefactID):
        return self._artefacts.get(artefactID)

    def isArtefactOpened(self, artefactID):
        openedTokenID = self.getOpenedArtefactToken(artefactID)
        return self.eventsCache.questsProgress.getTokenCount(openedTokenID) > 0

    def isArtefactReceived(self, artefactID):
        return self.eventsCache.questsProgress.getTokenCount(artefactID) > 0

    def setChoice(self, choiceID):
        self._choiceID = choiceID
        return

    def getChoiceID(self):
        return self._choiceID

    def getArtefactKeyQuantity(self):
        return self.eventsCache.questsProgress.getTokenCount(ArtefactsSettings.KEY_TOKEN)

    def getCurrentArtefactProgress(self):
        return sum(list(int(self.isArtefactOpened(artefactID)) for artefactID in self._artefacts))

    def getAvailableArtefactProgress(self):
        return sum(list(int(self.isArtefactReceived(artefactID)) for artefactID in self._artefacts))

    def getMaxArtefactsProgress(self):
        return len(self._artefacts) - 1

    def getArtefactsCount(self):
        return len(self._artefacts)

    def getMainGiftVehicle(self):
        finalArtefact = self.getFinalArtefact()
        if not finalArtefact:
            return
        else:
            for bonus in finalArtefact.bonusRewards:
                if not isinstance(bonus, VehiclesBonus):
                    continue
                vehiclesBonuses = bonus.getVehicles()
                mainVehicleBonus = vehiclesBonuses[0] if vehiclesBonuses else []
                return next((b for b in mainVehicleBonus if isinstance(b, Vehicle)), None)

            return

    def getMainGiftStyle(self):
        finalArtefact = self.getFinalArtefact()
        if not finalArtefact:
            return
        else:
            for bonus in finalArtefact.bonusRewards:
                if not isinstance(bonus, CustomizationsBonus):
                    continue
                bonuses = bonus.getList()
                for item in bonuses:
                    customization = self.itemsCache.items.getItemByCD(item.get(b'intCD', 0))
                    if customization and customization.itemTypeID == GUI_ITEM_TYPE.STYLE:
                        return customization

            return

    def getRareAttachmentsFromArtefact(self, artefactID):
        artefact = self.getArtefact(artefactID)
        if not artefact:
            return []
        attachments = []
        for bonus in artefact.bonusRewards:
            if not isinstance(bonus, CustomizationsBonus):
                continue
            bonuses = bonus.getList()
            for item in bonuses:
                c11nItem = self.c11n.getItemByCD(item.get(b'intCD', 0))
                if c11nItem and c11nItem.itemTypeID == GUI_ITEM_TYPE.ATTACHMENT and c11nItem.rarity in Rarity.UI_EFFECT:
                    attachments.append(c11nItem)

        return attachments

    def isArtefactHasTwitchConCertificate(self, artefactID):
        artefact = self.getArtefact(artefactID)
        if not artefact:
            return False
        for bonus in artefact.bonusRewards:
            if not isinstance(bonus, CerfTokenBonus):
                continue
            return self.twitchConCtrl.getCertificateTokenName() in bonus.getTokens()

        return False

    def isExistUnreceivedTwitchConCertificate(self):
        return any(not self.isArtefactOpened(artefactID) and self.isArtefactHasTwitchConCertificate(artefactID) for artefactID in self._artefacts)

    def getArtefactIDForAccessToVehicle(self, vehTypeCD):
        for artefactID, artefact in self._getArtefacts().items():
            accessToVehicle = artefact.get(b'accessToVehicle')
            if accessToVehicle == vehTypeCD:
                return artefactID

        return

    def getLackOfKeysForArtefact(self, artefactID):
        return max(0, self.__getArtefactKeyCost(artefactID) - self.getArtefactKeyQuantity())

    def getLackOfKeysForArtefacts(self):
        keysCount = 0
        for artefactID in self._artefacts:
            keysCount += self.__getArtefactKeyCost(artefactID)

        return max(0, keysCount - self.getArtefactKeyQuantity())

    def getQuest(self, questID):
        return self.eventsCache.getHiddenQuests((lambda q: q.getID() in [questID])).get(questID)

    @adisp_async
    @decorators.adisp_process(b'updating')
    def openArtefact(self, artefactID, isSkipQuest, callback):
        result = yield OpenArtefactProcessor(self, artefactID, isSkipQuest).request()
        if result.userMsg:
            SystemMessages.pushMessage(result.userMsg, type=result.sysMsgType)
        callback(result.success)
        return

    def isProgressCompleted(self):
        return self.getCurrentArtefactProgress() >= self.getMaxArtefactsProgress()

    def getArtefactIDByIndex(self, index):
        return ARTEFACT_ID_MASK.format(index=index)

    def getIndex(self, artefactID):
        _, index, __ = artefactID.split(b':')
        return int(index)

    def resetSelectedArtefactID(self):
        self._selectedArtefactID = None
        return

    def _initArtefacts(self):
        quests = self.eventsCache.getAllQuests((lambda q: isArtefactQuest(q.getID())))
        self._artefacts = dict((artefactID, Artefact(artefactID, ArtefactPrice(*self._getArtefactPrice(artefactID)), ArtefactPrice(*self._getArtefactQuestSkipPrice(artefactID)), self._getArtefactBonuses(artefactID, quests), self._getArtefactQuestConditions(artefactID, quests), self._getArtefactTypes(artefactID))) for artefactID in self._getArtefacts().keys())
        return

    def _getArtefactTypes(self, artefactID):
        return self._getArtefacts().get(artefactID, {}).get(b'type', [])

    def _getArtefactQuestSkipPrice(self, artefactID):
        return self._getArtefacts().get(artefactID, {}).get(b'questSkipCost', (None, 0))

    def _getArtefactPrice(self, artefactID):
        return self._getArtefacts().get(artefactID, {}).get(b'cost', (None, 0))

    @classmethod
    def _formatter(cls, value):
        return backport.getNiceNumberFormat(value)

    def _getArtefactQuestConditions(self, artefactID, quests):
        quest = quests.get(artefactID)
        if quest is not None:
            curProgress, totalValue = self.__getFirstQuestProgress(quest)
            description = quest.getDescription()
            if totalValue is not None:
                curProgressStr, totalValueStr = self._formatter(int(curProgress)), self._formatter(int(totalValue))
                description = description.format(total=totalValueStr, current=curProgressStr if not self.isArtefactOpened(artefactID) else totalValueStr)
            return QuestConditions(quest.getUserName(), description, totalValue, curProgress)
        else:
            return QuestConditions()

    def _getArtefactBonuses(self, artefactID, quests):
        if ArtefactType.FINAL in self._getArtefactTypes(artefactID):
            quest = quests.get(artefactID)
            if quest:
                return sorted(quest.getBonuses(), key=getBonusPriority)
            return []
        rewards = []
        artefactConfig = self._getArtefacts().get(artefactID, {})
        bonusesConfig = artefactConfig.get(b'bonus', {})
        accessToVehicle = artefactConfig.get(b'accessToVehicle')
        if accessToVehicle:
            rentTime = self._getRentConfig().get(b'time', 0)
            opendSuffix = self._getRentConfig().get(b'openedSuffix')
            shopSuffix = self._getRentConfig().get(b'shopSuffix')
            vehiclesConfig = self._getRentConfig().get(b'vehicles', {})
            accessShopToken = vehiclesConfig.get(accessToVehicle, {}).get(shopSuffix, b'hw25_unknown')
            accessOpenToken = vehiclesConfig.get(accessToVehicle, {}).get(opendSuffix)
            if not self.eventsCache.questsProgress.getTokenCount(accessShopToken) > 0 or self.eventsCache.questsProgress.getTokenCount(accessOpenToken) > 0:
                rewards.extend(getNonQuestBonuses(VehiclesBonus.VEHICLES_BONUS, {accessToVehicle: {b'rent': {b'time': rentTime}}}))
        for bonusType, bonusValue in bonusesConfig.items():
            rewards.extend(getNonQuestBonuses(bonusType, bonusValue))

        questsToRun = artefactConfig.get(b'questsToRun')
        if questsToRun:
            quests = self.eventsCache.getHiddenQuests((lambda q: q.getID() in questsToRun))
            if quests:
                rewards.extend(itertools.chain.from_iterable(q.getBonuses() for q in quests.values()))
        sortedBonuses = sorted(mergeBonuses(rewards), key=getBonusPriority)
        return sortedBonuses

    def _getConfig(self):
        return self.halloweenCtrl.getModeSettings().artefactsSettings

    def _getRentConfig(self):
        return self.halloweenCtrl.getModeSettings().rent

    def _getArtefacts(self):
        return self._getConfig().get(b'artefacts', {})

    def __getFirstQuestProgress(self, quest):
        for condName in QUEST_BONUS_CONDITIONS:
            cond = quest.bonusCond.getConditions().find(condName)
            if not cond:
                continue
            curProgressData = quest.bonusCond.getProgress().get(None, {})
            totalValue = cond.getTotalValue()
            curProggres = (quest.isCompleted() or curProgressData.get)(cond.getKey(), 0) if 1 else totalValue
            return (curProggres, totalValue)

        return (0, 1)

    def __handleTokensUpdate(self, diff):
        for token in diff:
            if token.startswith(ArtefactsSettings.KEY_TOKEN):
                self.onArtefactKeyUpdated()
                continue
            if token.startswith(ArtefactsSettings.TOKEN_PREFIX):
                self.onArtefactStatusUpdated(token)
            if token.startswith(RENT_VEHICLE_PREFIX):
                self._initArtefacts()
                self.onArtefactSettingsUpdated()
                g_eventDispatcher.updateUI()

        return

    def __onQuestsUpdated(self, _):
        self._initArtefacts()
        self.onArtefactSettingsUpdated()
        return

    def __updateSettings(self):
        self._initArtefacts()
        self.onArtefactSettingsUpdated()
        return

    def __getArtefactKeyCost(self, artefactID):
        artefact = self.getArtefact(artefactID)
        if not artefact:
            return 0
        else:
            if self.isArtefactOpened(artefactID):
                return 0
            if artefact.skipPrice.currency is not None and not self.isArtefactReceived(artefactID):
                amount = artefact.skipPrice.amount
            else:
                amount = artefact.decodePrice.amount
            return amount
