from collections import namedtuple
import enum, typing
from lui_expression_parser import parseExpression
from ids_generators import SequenceIDGenerator
if typing.TYPE_CHECKING:
    from typing import Optional, Dict, Set, List, Tuple

class LuiRules(enum.Enum):
    LOBBY_HEADER_COUNTERS_STORE = b'store'
    LOBBY_HEADER_COUNTERS_PROFILE = b'profile'
    PROFILE_HOF = b'profileHof'
    PROFILE_TECHNIQUE_PAGE = b'profileTechniquePage'
    SESSION_STATS = b'sessionStats'
    BLUEPRINTS_BUTTON = b'blueprintsButton'
    LOBBY_HEADER_COUNTERS_MISSIONS = b'missions'
    MISSIONS_MARATHON_VIEW = b'MissionsMarathonView'
    LOBBY_HEADER_COUNTERS_PM_OPERATIONS = b'PersonalMissionOperations'
    AP_ZONE_HINT = b'AmmunitionPanelHintZoneHint'
    AP_BATTLE_ABILITIES_HINT = b'AmmunitionPanelBattleAbilitiesHint'
    TECH_TREE_EVENTS = b'TechTreeEvent'
    DOG_TAG_HINT = b'DogTagHangarHint'
    MODE_SELECTOR_WIDGET_BTN_HINT = b'ModeSelectorWidgetsBtnHint'
    PR_HANGAR_HINT = b'PersonalReservesHangarHint'
    MODERNIZE_SETUP_HINT = b'ModernizedSetupTabHint'
    OFFER_BANNER_WINDOW = b'OfferBannerWindow'
    COMP7_ENTRY_POINT = b'Comp7EntryPoint'
    BP_ENTRY = b'BattlePassEntry'
    PROGRESSIVE_ITEMS_REWARD = b'ProgressiveItemsReward'
    DAILY_MISSIONS = b'DailyMissions'
    CRAFT_MACHINE_ENTRY_POINT = b'CraftMachineEntryPoint'
    SHOP_SALES_ENTRY_POINT = b'ShopSalesEntryPoint'
    MAPBOX_ENTRY_POINT = b'MapboxEntryPoint'
    UNIVERSAL_FLAG_ENTRY_POINT = b'universalFlagEntryPoint'
    EPIC_BATTLES_ENTRY_POINT = b'EpicBattlesEntryPoint'
    BATTLE_MISSIONS = b'BattleMissions'
    HERO_TANK = b'HeroTank'
    BM_FLAG = b'BattleMattersFlag'
    PERSONAL_MISSIONS = b'PersonalMissions'
    SYS_MSG_COLLECTION_START_BP = b'sysMsgCollectionStartBattlePass'
    SYS_MSG_COLLECTIONS_UPDATED_ENTRY = b'sysMsgCollectionsUpdatedEntry'
    LOBBY_HEADER_COUNTERS_STORAGE = b'storage'
    PR_HANGAR_BUTTON = b'PersonalReservesHangarButton'
    STRONGHOLD_ENTRY_POINT = b'StrongholdEntryPoint'
    BR_ENTRY_POINT = b'BREntryPoint'
    ARMORY_YARD_ENTRY_POINT = b'ArmoryYardEntryPoint'
    BLACK_MARKET_ENTRY_POINT = b'BlackMarketEntryPoint'
    FUN_RANDOM_ENTRY_POINT = b'FunRandomEntryPoint'
    FUN_RANDOM_NOTIFICATIONS = b'FunRandomNotifications'
    GUI_LOOTBOXES_ENTRY_POINT = b'LootBoxesEntryPoint'
    RESOURCE_WELL = b'ResourceWellFlag'
    GUI_COSMIC_ENTRY_POINT = b'CosmicEntryPoint'
    SUBSCRIPTION_STATE = b'SubscriptionState'
    EARLY_ACCESS_ENTRY_POINT = b'EarlyAccessEntryPoint'
    PARAGONS_ENTRY_POINT = b'ParagonsEntryPoint'
    PARAGONS_TREE_BRANCHES = b'ParagonsTreeBranches'
    PARAGONS_NOTIFICATION = b'ParagonsNotification'
    PARAGONS_BUTTONS = b'ParagonsButtons'
    NEW_CAMPAIGN_HINT = b'NewCampaignHint'
    GUI_WHITE_TIGER_ENTRY_POINT = b'WhiteTigerEntryPoint'
    TEASER = b'Teaser'
    C7N_BUBBLE = b'CustomizationBubble'
    COMMON_CHAT = b'CommonChat'
    CHANNELS = b'Channels'
    PERSONAL_MISSIONS_CONTENT = b'PersonalMissionsContent'
    TOURNAMENTS_CONTENT = b'TournamentsContent'
    VERSUS_AI_CONTENT = b'VersusAIContent'
    STRONGHOLD_CONTENT = b'StrongholdContent'
    RANKED_CONTENT = b'RankedContent'
    SPEC_BATTLE_CONTENT = b'SpecBattleContent'
    COMP7_CONTENT = b'Comp7Content'
    ARCADE_CONTENT = b'ArcadeContent'
    FIELD_TRIALS_CONTENT = b'FieldTrialsContent'
    FRONTLINE_CONTENT = b'FrontlineContent'


class _LimitedUIRule(namedtuple(b'_LimitedUIRule', (b'idx', b'expression', b'expressionElements', b'tokens', b'message'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(idx=0, expression=None, expressionElements=[], tokens=set(), message=None)
        dataToUpdate = {k: v for k, v in kwargs.iteritems() if k in cls._fields}
        defaults.update(dataToUpdate)
        return super(_LimitedUIRule, cls).__new__(cls, **defaults)


class _LimitedUIRules(object):

    def __init__(self, rules):
        super(_LimitedUIRules, self).__init__()
        self.__rules = rules
        return

    def getRule(self, ruleID):
        return self.__rules.get(ruleID, None)

    def getRulesIDs(self):
        return set(self.__rules.keys())

    def hasRule(self, ruleID):
        return ruleID in self.__rules

    def getTokens(self, ruleID):
        if self.hasRule(ruleID):
            return self.getRule(ruleID).tokens
        return set()

    def getExpressionElements(self, ruleID):
        if self.hasRule(ruleID):
            return self.getRule(ruleID).expressionElements
        return []

    def getSysMessage(self, ruleID):
        if self.hasRule(ruleID):
            return self.getRule(ruleID).message
        return

    def clear(self):
        self.__rules.clear()
        return


class RulesStorageMaker(object):

    @classmethod
    def makeStorage(cls, rulesData):
        data = dict()
        idGen = SequenceIDGenerator(lowBound=-1)
        for ruleID, expressionStr, message in rulesData:
            expression, tokens, expressionElements = parseExpression(expressionStr)
            data[ruleID] = {b'idx': (idGen.next()), 
               b'expressionStr': expressionStr, 
               b'expression': expression, 
               b'expressionElements': expressionElements, 
               b'tokens': tokens, 
               b'message': message}

        rulesIDs = set(data.keys())
        for ruleID, item in data.items():
            cls.__normalizeRuleItem(data, rulesIDs, item)

        rules = {LuiRules(ruleID): _LimitedUIRule(**value) for ruleID, value in data.items()}
        return _LimitedUIRules(rules)

    @classmethod
    def __normalizeRuleItem(cls, data, rulesIDs, item):
        tokens = item[b'tokens']
        expressionStr = item[b'expressionStr']
        dependencies = tokens & rulesIDs
        if dependencies:
            while dependencies:
                dependency = dependencies.pop()
                dependsItem = data[dependency]
                dependencyExpression = cls.__normalizeRuleItem(data, rulesIDs, dependsItem)
                expressionStr = expressionStr.replace(dependency, (b'({})').format(dependencyExpression))

            expression, tokens, expressionElements = parseExpression(expressionStr)
            item[b'expressionStr'] = expressionStr
            item[b'expression'] = expression
            item[b'expressionElements'] = expressionElements
            item[b'tokens'] = tokens
        return expressionStr
