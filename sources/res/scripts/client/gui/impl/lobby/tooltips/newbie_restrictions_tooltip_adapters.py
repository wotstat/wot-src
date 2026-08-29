import logging
from frameworks.wulf import Array
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.tooltips.condition_group import ConditionGroup
from gui.impl.gen.view_models.views.lobby.tooltips.newbie_restrictions_tooltip_model import NewbieRestrictionsTooltipModel
from gui.limited_ui.lui_rules_storage import LuiRules
from helpers import dependency, int2roman
from skeletons.gui.game_control import ILimitedUIController
from skeletons.gui.lobby_context import ILobbyContext
_logger = logging.getLogger(__name__)

def _getFooterResource(resourceBranchName, resourceName):
    if resourceBranchName is None:
        return R.invalid()
    else:
        return R.strings.tooltips.newbie_restrictions.footer.dyn(resourceBranchName).dyn(resourceName)()


class NewbieRestrictionsTooltipAdapter(object):

    def fillConditionGroups(self, conditionGroups):
        raise NotImplementedError()
        return

    def fillFooter(self, model):
        raise NotImplementedError()
        return

    def _fillFooter(self, model, resourceBranchName):
        model.setFooterTitleText(_getFooterResource(resourceBranchName, b'title'))
        model.setFooterText(_getFooterResource(resourceBranchName, b'desc'))
        return


class LimitedUINewbieRestrictionsTooltipAdapter(NewbieRestrictionsTooltipAdapter):
    __limitedUIController = dependency.descriptor(ILimitedUIController)
    __LUI_RULE_TO_RESOURCE_BRANCH_NAME = {(LuiRules.PERSONAL_MISSIONS_CONTENT): b'personal_missions', 
       (LuiRules.TOURNAMENTS_CONTENT): b'tournaments', 
       (LuiRules.VERSUS_AI_CONTENT): b'versus_ai', 
       (LuiRules.STRONGHOLD_CONTENT): b'stronghold', 
       (LuiRules.RANKED_CONTENT): b'ranked', 
       (LuiRules.SPEC_BATTLE_CONTENT): b'spec_battles', 
       (LuiRules.COMP7_CONTENT): b'comp7', 
       (LuiRules.ARCADE_CONTENT): b'arcade', 
       (LuiRules.FIELD_TRIALS_CONTENT): b'field_trials', 
       (LuiRules.FRONTLINE_CONTENT): b'frontline'}

    def __init__(self, luiRuleID):
        self.__luiRuleID = luiRuleID
        return

    def fillConditionGroups(self, conditionGroups):
        conditionRepresentation = self.__limitedUIController.getRuleConditionRepresentation(self.__luiRuleID)
        for conditionGroup in conditionRepresentation:
            conditionGroupModel = ConditionGroup()
            conditions = conditionGroupModel.getConditions()
            for condition in conditionGroup:
                conditions.addString(backport.text(R.strings.tooltips.newbie_restrictions.condition.dyn(condition.resourceName)(), **condition.kwargs))

            conditionGroups.addViewModel(conditionGroupModel)

        return

    def fillFooter(self, model):
        resourceBranchName = self.__LUI_RULE_TO_RESOURCE_BRANCH_NAME.get(self.__luiRuleID)
        if resourceBranchName is None:
            _logger.warning(b'There is no resource branch name for limited ui rule %s', self.__luiRuleID)
        self._fillFooter(model, resourceBranchName)
        return


class ChatLockNewbieRestrictionsTooltipAdapter(NewbieRestrictionsTooltipAdapter):
    __lobbyContext = dependency.descriptor(ILobbyContext)

    def fillConditionGroups(self, conditionGroups):
        conditionGroupModel = ConditionGroup()
        conditions = conditionGroupModel.getConditions()
        serverSettings = self.__lobbyContext.getServerSettings()
        conditions.addString(backport.text(R.strings.tooltips.newbie_restrictions.condition.battlesCountThreshold(), battlesCount=serverSettings.newbieChatLockConfig.battlesCountThreshold))
        conditions.addString(backport.text(R.strings.tooltips.newbie_restrictions.condition.vehicleLevelThreshold(), level=int2roman(serverSettings.newbieChatLockConfig.vehicleLevelThreshold)))
        conditionGroups.addViewModel(conditionGroupModel)
        return

    def fillFooter(self, model):
        self._fillFooter(model, b'chats')
        return
