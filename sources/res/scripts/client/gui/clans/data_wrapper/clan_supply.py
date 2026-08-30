import logging
from typing import NamedTuple, Dict, Union, TYPE_CHECKING, List
from shared_utils import makeTupleByDict, CONST_CONTAINER
if TYPE_CHECKING:
    from typing import Optional
_logger = logging.getLogger(__name__)

class DataNames(CONST_CONTAINER):
    PROGRESSION_SETTINGS = b'PROGRESSION_SETTINGS'
    PROGRESSION_PROGRESS = b'PROGRESSION_PROGRESS'
    QUESTS_INFO = b'QUESTS_INFO'
    QUESTS_INFO_POST = b'QUESTS_INFO_POST'


class PointStatus(CONST_CONTAINER):
    PURCHASED = b'PURCHASED'
    AVAILABLE = b'AVAILABLE'


class ConditionRuleType(CONST_CONTAINER):
    FULL_DAMAGE = b'FULL_DAMAGE'
    FRAGS = b'FRAGS'
    WIN = b'WIN'
    EXP = b'EXP'


class ConditionSquadState(CONST_CONTAINER):
    SOLO = b'solo'
    PLATOON = b'platoon'
    DETACHMENT = b'detachment'


class QuestStatus(CONST_CONTAINER):
    INCOMPLETE = b'INCOMPLETE'
    REWARD_AVAILABLE = b'REWARD_AVAILABLE'
    REWARD_PENDING = b'REWARD_PENDING'
    COMPLETE = b'COMPLETE'


PointSettings = NamedTuple(b'PointSettings', [
 (
  b'is_elite', bool),
 (
  b'price', int),
 (
  b'rewards', Dict[str, Union[int, str, Dict, List[Dict]]])])
ProgressionSettings = NamedTuple(b'ProgressionSettings', [
 (
  b'enabled', bool),
 (
  b'points', Dict[str, PointSettings])])
PointProgress = NamedTuple(b'PointSettings', [
 (
  b'status', str)])
ProgressionProgress = NamedTuple(b'ProgressionProgress', [
 (
  b'last_purchased', str),
 (
  b'points', Dict[str, PointProgress])])
FragsCondition = NamedTuple(b'FragsCondition', [
 (
  b'type', str),
 (
  b'frags_count', str)])
FullDamageCondition = NamedTuple(b'FullDamageCondition', [
 (
  b'type', str),
 (
  b'full_damage', str)])
ExpCondition = NamedTuple(b'ExpCondition', [
 (
  b'type', str),
 (
  b'exp_earned', str)])
WinCondition = NamedTuple(b'WinCondition', [
 (
  b'type', str)])
CONDITIONS_TYPE = Union[FragsCondition, FullDamageCondition, ExpCondition, WinCondition]
SimpleCondition = NamedTuple(b'SimpleCondition', [
 (
  b'rule', CONDITIONS_TYPE),
 (
  b'squad_states', List[str])])
_RULE_TYPE_TO_CLAZZ = {(ConditionRuleType.FRAGS): FragsCondition, 
   (ConditionRuleType.WIN): WinCondition, 
   (ConditionRuleType.EXP): ExpCondition, 
   (ConditionRuleType.FULL_DAMAGE): FullDamageCondition}

def _makeSimpleCondition(conditionData):
    ruleData = conditionData.get(b'rule', {})
    ruleType = ruleData.get(b'type')
    if ruleType not in _RULE_TYPE_TO_CLAZZ:
        _logger.warning(b'Does not type class for the condition: %s', conditionData)
        return None
    else:
        conditionData.update({b'rule': (makeTupleByDict(_RULE_TYPE_TO_CLAZZ[ruleType], ruleData))})
        return makeTupleByDict(SimpleCondition, conditionData)


CommonCondition = NamedTuple(b'CommonCondition', [
 (
  b'level_from', int),
 (
  b'level_to', int)])
ConditionsInfo = NamedTuple(b'ConditionsInfo', [
 (
  b'main', SimpleCondition),
 (
  b'alternative', SimpleCondition),
 (
  b'common', CommonCondition)])
Quest = NamedTuple(b'Quest', [
 (
  b'name', str),
 (
  b'level', int),
 (
  b'current_progress', int),
 (
  b'required_progress', int),
 (
  b'status', str),
 (
  b'conditions', ConditionsInfo),
 (
  b'rewards', Dict[str, Union[int, str]])])
QuestsInfo = NamedTuple(b'QuestsInfo', [
 (
  b'enabled', bool),
 (
  b'cycle_end', int),
 (
  b'cycle_duration', int),
 (
  b'previous_rewards', Dict[str, Union[int, str]]),
 (
  b'quests', List[Quest])])

def makeQuestInfo(incomeData):
    incomeData = incomeData or {}
    questInfo = []
    incomeQuestInfoData = incomeData.get(b'quest_info', [])
    for rawQuest in sorted(incomeQuestInfoData, key=(lambda q: q.get(b'level'))):
        rawConditionsInfo = rawQuest.get(b'conditions', {})
        conditionsInfo = {b'main': (_makeSimpleCondition(rawConditionsInfo.get(b'main', {}))), 
           b'alternative': (_makeSimpleCondition(rawConditionsInfo.get(b'alternative', {}))), 
           b'common': (makeTupleByDict(CommonCondition, rawConditionsInfo.get(b'common', {})))}
        rawQuest.update({b'conditions': (makeTupleByDict(ConditionsInfo, conditionsInfo))})
        questInfo.append(makeTupleByDict(Quest, rawQuest))

    incomeData.update({b'quests': questInfo})
    incomeData.update({b'enabled': True})
    return makeTupleByDict(QuestsInfo, incomeData)
