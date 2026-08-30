from __future__ import absolute_import
import logging, typing
from gui.Scaleform.genConsts.MISSIONS_ALIASES import MISSIONS_ALIASES
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.gen.view_models.common.missions.conditions.condition_group_model import ConditionGroupModel
from gui.impl.gen.view_models.common.missions.conditions.preformatted_condition_model import PreformattedConditionModel
from gui.server_events import formatters
from gui.server_events.cond_formatters import FORMATTER_IDS
from gui.server_events.cond_formatters import FormattableField
from gui.server_events.cond_formatters import prebattle, postbattle, vehicle
from gui.server_events.cond_formatters.bonus import BattlesCountFormatter
from gui.server_events.cond_formatters.bonus import MissionsBonusConditionsFormatter
from gui.server_events.cond_formatters.challenges.postbattle import ChallengePostBattleConditionsFormatter
from gui.server_events.formatters import PreFormattedCondition
from gui.shared.formatters.plain_text import PlainTextFormatter
from personal_missions_constants import CONDITION_ICON
from soft_exception import SoftException
if typing.TYPE_CHECKING:
    from typing import Optional, Union
    from gui.server_events.conditions import _Condition
    from gui.server_events.conditions import _ConditionsGroup
    from gui.server_events.event_items import ServerEventAbstract
    from gui.server_events.event_items import Quest
_logger = logging.getLogger(__name__)
CONDITION_GROUP_AND = b'and'
CONDITION_GROUP_OR = b'or'
CONDITION_GROUP_NOP = b'nop'
CONDITION_GROUP_NOT = b'not'
CONDITION_DEFAULT_NAME = b'play'
CONDITION_GROUP_TYPE_LIST = (
 CONDITION_GROUP_AND,
 CONDITION_GROUP_OR,
 CONDITION_GROUP_NOP,
 CONDITION_GROUP_NOT)
CONDITION_SPECIFIC_TYPE_LIST = (
 CONDITION_DEFAULT_NAME,)
CONDITION_TYPE_LIST = CONDITION_GROUP_TYPE_LIST + CONDITION_SPECIFIC_TYPE_LIST

class PreFormattedConditionModelPacker(object):

    @staticmethod
    def pack(preFormattedConditionTuple, conditionType):
        model = getDefaultPreformattedConditionModel()
        textFormatter = getDefaultPlainTextFormatter()
        if conditionType:
            model.setConditionType(conditionType)
        if preFormattedConditionTuple.titleData:
            model.setTitleData(textFormatter.getPlainTextFromFormattedField(preFormattedConditionTuple.titleData))
        if preFormattedConditionTuple.descrData:
            model.setDescrData(textFormatter.getPlainTextFromFormattedField(preFormattedConditionTuple.descrData))
        if preFormattedConditionTuple.iconKey:
            iconKey = preFormattedConditionTuple.iconKey
            model.setIconKey(iconKey)
        if preFormattedConditionTuple.current:
            current = preFormattedConditionTuple.current
            model.setCurrent(current)
        if preFormattedConditionTuple.earned:
            model.setEarned(max(preFormattedConditionTuple.earned, 0))
        if preFormattedConditionTuple.total:
            total = preFormattedConditionTuple.total
            model.setTotal(total)
        if preFormattedConditionTuple.progressID:
            progressID = preFormattedConditionTuple.progressID
            model.setProgressType(progressID)
        if preFormattedConditionTuple.sortKey:
            sortKey = preFormattedConditionTuple.sortKey
            model.setSortKey(sortKey)
        return model


class UIConditionPacker(object):

    def _packConditions(self, conditions, event):
        ctx = {b'data': conditions, b'event': event}
        classType = None
        try:
            classType = ctx[b'data'].classType
        except AttributeError:
            pass

        if classType != b'ConditionsGroup':
            return (self._travers(ctx), CONDITION_GROUP_NOP)
        else:
            booleanOperation = ctx[b'data'].getName()
            ctx[b'data'] = ctx[b'data'].items
            return (self._traversConditionItemsList(ctx), booleanOperation)

    def _convertConditionIntoPreFormattedCondition(self, ctx):
        raise SoftException(b'This method should not be reached in this context')
        return

    def pack(self, event, model):
        return self._pack(event, model)

    def _pack(self, event, model):
        raise SoftException(b'This method should not be reached in this context')
        return

    def _traversConditionItemsList(self, ctx):
        if not ctx[b'data']:
            return None
        else:
            result = []
            for condition in ctx[b'data']:
                ctx[b'data'] = condition
                result.append(self._travers(ctx))

            return result

    def _traversConditionGroup(self, ctx, operation):
        model = getDefaultConditionGroupModel()
        model.setConditionType(operation)
        for condition in self._traversConditionItemsList(ctx):
            if not condition:
                continue
            model.getItems().addViewModel(condition)

        return model

    def _traversCondition(self, ctx):
        condition = ctx[b'data']
        conditionName = condition.getName()
        preFormattedCondition = self._convertConditionIntoPreFormattedCondition(ctx)
        if not preFormattedCondition:
            if not ctx[b'event'].isGuiDisabled():
                _logger.error(b'Should not be reached: preFormattedConditionTuple was not received.')
            return None
        if len(preFormattedCondition) > 1:
            _logger.error(b'Should not be reached: More than one tuple was received.')
        preFmtCond = preFormattedCondition[0]
        return getDefaultPreFormattedConditionModelPacker().pack(preFmtCond, conditionName)

    def _travers(self, ctx):
        ctx[b'data'] = ctx.get(b'data', [])
        contextData = ctx[b'data']
        classType = None
        try:
            classType = contextData.classType
        except AttributeError:
            _logger.error(b'Type %s does not have attribute classType.', type(contextData))

        if classType == b'ConditionsGroup':
            booleanOperation = contextData.getName()
            ctx[b'data'] = contextData.items
            return self._traversConditionGroup(ctx, booleanOperation)
        else:
            if classType == b'Condition':
                if contextData.isHidden():
                    return
                return self._traversCondition(ctx)
            _logger.error(b'Condition packer for %s type is not implemented yet.', type(contextData))
            return


class BonusConditionPacker(UIConditionPacker):

    def __init__(self):
        super(BonusConditionPacker, self).__init__()
        self.isPostBattleConditionPresent = False
        return

    def _convertConditionIntoPreFormattedCondition(self, ctx):
        conditioName = ctx[b'data'].getName()
        groupFormatter = getDefaultMissionsBonusConditionsFormatter().getConditionFormatter(conditioName)
        if groupFormatter:
            return groupFormatter.format(ctx[b'data'], ctx[b'event'])
        if conditioName != b'battles':
            _logger.error(b'No formatter for conditioName %s.', conditioName)
        arePostBattleCondsPresent = self.isPostBattleConditionPresent
        battleFormatter = getDefaultBattlesCountFormatter(arePostBattleCondsPresent)
        return battleFormatter.format(ctx[b'data'], ctx[b'event'])

    def packWithPostBattleCondCheck(self, event, model, isPostBattleConditionPresent):
        self.isPostBattleConditionPresent = isPostBattleConditionPresent
        self.pack(event, model)
        return

    def _pack(self, event, model):
        bonusConditions = event.bonusCond.getConditions()
        bonusCondsModelList, typeOfBonusConditionGroup = self._packConditions(bonusConditions, event)
        isItemAddedToBonusCondModel = False
        if not bonusCondsModelList:
            _logger.debug(b'BonusConditions were not received for event %s.', event.getID())
            return
        else:
            for bonusCondModel in bonusCondsModelList:
                if not bonusCondModel:
                    continue
                model.getItems().addViewModel(bonusCondModel)
                isItemAddedToBonusCondModel = True

            if isItemAddedToBonusCondModel:
                model.setConditionType(typeOfBonusConditionGroup)
            return


class PostBattleConditionPacker(UIConditionPacker):

    def __init__(self):
        super(PostBattleConditionPacker, self).__init__()
        self.postBattleCondFormatter = getDefaultPostBattleCondFormatter()
        return

    def _convertConditionIntoPreFormattedCondition(self, ctx):
        conditionType = ctx[b'data'].getName()
        groupFormatter = self.postBattleCondFormatter.getConditionFormatter(conditionType)
        if not groupFormatter:
            _logger.error(b'Condition packer for type %s does not exists.', conditionType)
            return None
        else:
            return groupFormatter.format(ctx[b'data'], ctx[b'event'])

    def _pack(self, event, model):
        postBattleConditions = event.postBattleCond.getConditions()
        postBattleCondsModelList, typeOfPostBattleConditionGroup = self._packConditions(postBattleConditions, event)
        if not postBattleCondsModelList:
            _logger.debug(b'PostBattleConditions were not received for event %s.', event.getID())
            return
        else:
            for postBattleCondModel in postBattleCondsModelList:
                if not postBattleCondModel:
                    continue
                model.getItems().addViewModel(postBattleCondModel)

            model.setConditionType(typeOfPostBattleConditionGroup)
            return

    @classmethod
    def packDefaultCondition(cls, event, model):
        model.getItems().addViewModel(cls.getPlayBattleCondition(event))
        model.setConditionType(CONDITION_GROUP_AND)
        return

    @staticmethod
    def getPlayBattleCondition(event, packer=PreFormattedConditionModelPacker):
        if event.isGuiDisabled():
            icon = CONDITION_ICON.FOLDER
        else:
            icon = CONDITION_ICON.BATTLES
        titleArgs = (
         backport.text(R.strings.quests.details.conditions.playBattle.title()),)
        descrArgs = (backport.text(R.strings.quests.missionDetails.conditions.playBattle()),)
        playBattleCondition = formatters.packMissionIconCondition(FormattableField(FORMATTER_IDS.SIMPLE_TITLE, titleArgs), MISSIONS_ALIASES.NONE, FormattableField(FORMATTER_IDS.DESCRIPTION, descrArgs), icon)
        return packer.pack(playBattleCondition, CONDITION_DEFAULT_NAME)


class ChallengePostBattleConditionPacker(PostBattleConditionPacker):

    def __init__(self):
        super(ChallengePostBattleConditionPacker, self).__init__()
        self.postBattleCondFormatter = ChallengePostBattleConditionsFormatter()
        return


def getDefaultBonusCondPacker():
    return BonusConditionPacker()


def getDefaultPreBattleCondFormatter():
    return prebattle.MissionsPreBattleConditionsFormatter()


def getDefaultPostBattleCondFormatter():
    return postbattle.MissionsPostBattleConditionsFormatter()


def getDefaultVehicleCondFormatter():
    return vehicle.MissionsVehicleConditionsFormatter()


def getDefaultMissionsBonusConditionsFormatter():
    return MissionsBonusConditionsFormatter()


def getDefaultBattlesCountFormatter(hasPostBattleConditions):
    return BattlesCountFormatter(hasPostBattleConditions)


def getDefaultPreformattedConditionModel():
    return PreformattedConditionModel()


def getDefaultPlainTextFormatter():
    return PlainTextFormatter()


def getDefaultConditionGroupModel():
    return ConditionGroupModel()


def getDefaultPreFormattedConditionModelPacker():
    return PreFormattedConditionModelPacker()
