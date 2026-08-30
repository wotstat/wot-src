from gui.limited_ui.lui_rules_storage import LuiRules
from helpers import dependency
from skeletons.gui.game_control import ILimitedUIController
_ALIAS_TO_RULE_ID = {b'blueprintsButton': (LuiRules.BLUEPRINTS_BUTTON), 
   b'DogTagHangarHint': (LuiRules.DOG_TAG_HINT), 
   b'PersonalReservesHangarHint': (LuiRules.PR_HANGAR_HINT), 
   b'sessionStats': (LuiRules.SESSION_STATS), 
   b'ModernizedSetupTabHint': (LuiRules.MODERNIZE_SETUP_HINT), 
   b'ModeSelectorWidgetsBtnHint': (LuiRules.MODE_SELECTOR_WIDGET_BTN_HINT), 
   b'AmmunitionPanelHintZoneHint': (LuiRules.AP_ZONE_HINT), 
   b'NewCampaignHint': (LuiRules.NEW_CAMPAIGN_HINT), 
   b'ParagonsEntryPoint': (LuiRules.PARAGONS_ENTRY_POINT), 
   b'ParagonsNotification': (LuiRules.PARAGONS_NOTIFICATION)}

class LimitedUIHintChecker(object):

    def check(self, aliasId):
        limitedUIController = dependency.instance(ILimitedUIController)
        ruleID = _ALIAS_TO_RULE_ID.get(aliasId)
        return ruleID is None or limitedUIController.isRuleCompleted(ruleID)
