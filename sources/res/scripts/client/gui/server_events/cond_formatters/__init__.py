from collections import namedtuple
import typing
from gui.Scaleform.locale.QUESTS import QUESTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.server_events.conditions import GROUP_TYPE
from gui.server_events.formatters import RELATIONS_SCHEME, RELATIONS
from gui.shared.formatters import text_styles
from helpers import i18n
from personal_missions_constants import CONDITION_ICON
from soft_exception import SoftException
if typing.TYPE_CHECKING:
    from gui.server_events.conditions import BattleResults
MAX_CONDITIONS_IN_OR_SECTION_SUPPORED = 2
TOP_RANGE_HIGHEST = 1
TOP_RANGE_LOWEST = 15

class CONDITION_SIZE(object):
    NORMAL = b'normal'
    MINIMIZED = b'minimized'


POSSIBLE_BATTLE_RESUTLS_KEYS = {b'damagedWhileMoving': (CONDITION_ICON.DAMAGE), 
   b'totalDamaged': (CONDITION_ICON.DAMAGE), 
   b'soloFlagCapture': (CONDITION_ICON.BASE_CAPTURE), 
   b'autoAimedShots': (CONDITION_ICON.HIT), 
   b'movingAvgDamage': (CONDITION_ICON.DAMAGE), 
   b'tdestroyedModules': (CONDITION_ICON.MODULE_CRIT)}
BATTLE_RESULTS_KEYS = {b'capturePoints': (CONDITION_ICON.BASE_CAPTURE), 
   b'critsCount': (CONDITION_ICON.MODULE_CRIT), 
   b'damageAssistedRadio': (CONDITION_ICON.ASSIST_RADIO), 
   b'damageAssistedRadioWhileInvisible': (CONDITION_ICON.ASSIST_RADIO), 
   b'damageAssistedStun': (CONDITION_ICON.ASSIST_STUN), 
   b'damageAssistedStunWhileInvisible': (CONDITION_ICON.ASSIST_STUN), 
   b'damageAssistedTrack': (CONDITION_ICON.ASSIST_TRACK), 
   b'damageAssistedTrackWhileInvisible': (CONDITION_ICON.ASSIST_TRACK), 
   b'damageBlockedByArmor': (CONDITION_ICON.DAMAGE_BLOCK), 
   b'damaged': (CONDITION_ICON.HURT_VEHICLES), 
   b'damagedHp': (CONDITION_ICON.HURT_VEHICLES), 
   b'damageDealt': (CONDITION_ICON.DAMAGE), 
   b'damagedVehicleCntAssistedRadio': (CONDITION_ICON.ASSIST_RADIO), 
   b'damagedVehicleCntAssistedStun': (CONDITION_ICON.ASSIST_STUN), 
   b'damagedVehicleCntAssistedTrack': (CONDITION_ICON.ASSIST_TRACK), 
   b'damagedWhileEnemyMoving': (CONDITION_ICON.DAMAGE), 
   b'damageReceived': (CONDITION_ICON.GET_DAMAGE), 
   b'directEnemyHits': (CONDITION_ICON.HIT), 
   b'directHits': (CONDITION_ICON.HIT), 
   b'directHitsReceived': (CONDITION_ICON.GET_HIT), 
   b'directTeamHits': (CONDITION_ICON.HIT), 
   b'droppedCapturePoints': (CONDITION_ICON.BASE_DEF), 
   b'explosionEnemyHits': (CONDITION_ICON.HIT), 
   b'explosionHits': (CONDITION_ICON.HIT), 
   b'explosionHitsReceived': (CONDITION_ICON.GET_HIT), 
   b'fortResource': (CONDITION_ICON.FOLDER), 
   b'freeXP': (CONDITION_ICON.EXPERIENCE), 
   b'subtotalXP': (CONDITION_ICON.EXPERIENCE), 
   b'factualXP': (CONDITION_ICON.EXPERIENCE), 
   b'health': (CONDITION_ICON.SAVE_HP), 
   b'inBattleMaxPiercingSeries': (CONDITION_ICON.HIT), 
   b'inBattleMaxSniperSeries': (CONDITION_ICON.HIT), 
   b'innerModuleCritCount': (CONDITION_ICON.MODULE_CRIT), 
   b'innerModuleDestrCount': (CONDITION_ICON.MODULE_CRIT), 
   b'killedAndDamagedByAllSquadmates': (CONDITION_ICON.KILL_VEHICLES), 
   b'kills': (CONDITION_ICON.KILL_VEHICLES), 
   b'killsAssistedRadio': (CONDITION_ICON.ASSIST_RADIO), 
   b'killsAssistedStun': (CONDITION_ICON.ASSIST_STUN), 
   b'killsAssistedTrack': (CONDITION_ICON.ASSIST_TRACK), 
   b'lifeTime': (CONDITION_ICON.SEC_ALIVE), 
   b'markOfMastery': (CONDITION_ICON.MASTER), 
   b'marksOnGun': (CONDITION_ICON.BARREL_MARK), 
   b'mileage': (CONDITION_ICON.METERS), 
   b'noDamageDirectHitsReceived': (CONDITION_ICON.DAMAGE_BLOCK), 
   b'originalCredits': (CONDITION_ICON.CREDITS), 
   b'originalXP': (CONDITION_ICON.EXPERIENCE), 
   b'percentFromTotalTeamDamage': (CONDITION_ICON.DAMAGE), 
   b'winAloneAgainstVehicleCount': (CONDITION_ICON.KILL_VEHICLES), 
   b'piercingEnemyHits': (CONDITION_ICON.DAMAGE), 
   b'piercings': (CONDITION_ICON.DAMAGE), 
   b'piercingsReceived': (CONDITION_ICON.TIMES_GET_DAMAGE), 
   b'potentialDamageDealt': (CONDITION_ICON.DAMAGE), 
   b'potentialDamageReceived': (CONDITION_ICON.GET_DAMAGE), 
   b'shots': (CONDITION_ICON.HIT), 
   b'sniperDamageDealt': (CONDITION_ICON.DAMAGE), 
   b'soloHitsAssisted': (CONDITION_ICON.ASSIST_RADIO), 
   b'spotted': (CONDITION_ICON.DISCOVER), 
   b'spottedAndDamagedSPG': (CONDITION_ICON.DISCOVER), 
   b'stunDuration': (CONDITION_ICON.ASSIST_STUN_DURATION), 
   b'stunned': (CONDITION_ICON.ASSIST_STUN), 
   b'stunNum': (CONDITION_ICON.ASSIST_STUN), 
   b'tdamageDealt': (CONDITION_ICON.DAMAGE), 
   b'tkills': (CONDITION_ICON.KILL_VEHICLES), 
   b'xp': (CONDITION_ICON.EXPERIENCE), 
   b'xp/attack': (CONDITION_ICON.EXPERIENCE), 
   b'xp/assist': (CONDITION_ICON.EXPERIENCE), 
   b'xp/other': (CONDITION_ICON.EXPERIENCE), 
   b'spottedBeforeWeBecameSpotted': (CONDITION_ICON.DISCOVER), 
   b'isEnemyBaseCaptured': (CONDITION_ICON.BASE_CAPTURE), 
   b'isAnyOurCrittedInnerModules': (CONDITION_ICON.SURVIVE), 
   b'isNotSpotted': (CONDITION_ICON.SURVIVE), 
   b'rankChange': (CONDITION_ICON.RANK_UP), 
   b'brPosInBattle': (CONDITION_ICON.TOP), 
   b'poiCapturedByOwnTeam': (CONDITION_ICON.BASE_CAPTURE), 
   b'comp7PrestigePoints': (CONDITION_ICON.PRESTIGE_POINTS), 
   b'win': (CONDITION_ICON.WIN), 
   b'credits': (CONDITION_ICON.CREDITS)}
BATTLE_RESULTS_AGGREGATED_KEYS = {(tuple(sorted([b'damagedVehicleCntAssistedTrack', b'damagedVehicleCntAssistedRadio']))): (CONDITION_ICON.ASSIST), 
   (tuple(sorted([b'killsAssistedTrack', b'killsAssistedRadio']))): (CONDITION_ICON.ASSIST), 
   (tuple(sorted([b'damageAssistedStun', b'damageAssistedTrack']))): (CONDITION_ICON.ASSIST), 
   (tuple(sorted([b'killsAssistedStun', b'killsAssistedTrack']))): (CONDITION_ICON.ASSIST), 
   (tuple(sorted([b'damagedVehicleCntAssistedStun', b'damagedVehicleCntAssistedTrack']))): (CONDITION_ICON.ASSIST)}
VEHICLE_TYPES = {b'heavyTank': b'#item_types:vehicle/tags/heavy_tank/name', 
   b'mediumTank': b'#item_types:vehicle/tags/medium_tank/name', 
   b'lightTank': b'#item_types:vehicle/tags/light_tank/name', 
   b'AT-SPG': b'#item_types:vehicle/tags/at-spg/name', 
   b'SPG': b'#item_types:vehicle/tags/spg/name'}

class FORMATTER_IDS(object):
    DESCRIPTION = b'descriptionFormatter'
    CUMULATIVE = b'cumulativeFormatter'
    COMPLEX = b'complex'
    RELATION = b'relationFormatter'
    COMPLEX_RELATION = b'complexRelationFormatter'
    SIMPLE_TITLE = b'simpleTitleFormatter'


class COMPLEX_CONDITION_BLOCK(object):
    ACHIEVEMENT = b'achievement'
    VEHICLES_LIST = b'vehicles_list'
    VEHICLES_FILTERS = b'vehicles_filters'


FormattableField = namedtuple(b'FormattableField', b'formatterID args')

def packDescriptionField(description):
    return FormattableField(FORMATTER_IDS.DESCRIPTION, (i18n.makeString(description),))


def packSimpleTitle(title):
    return FormattableField(FORMATTER_IDS.SIMPLE_TITLE, (i18n.makeString(title),))


def packText(text, styler=None):
    return {b'text': text, b'styler': styler}


def intersperse(sequence, item):
    result = []
    for element in sequence:
        result.append(element)
        result.append(item)

    if result:
        result.pop()
    return result


def getSeparator(groupType=GROUP_TYPE.AND):
    if groupType == GROUP_TYPE.OR:
        return i18n.makeString(b'#quests:details/groups/or')
    return b''


def getSeparatorBlock(groupType=GROUP_TYPE.AND):
    label = getSeparator(groupType)
    if label:
        item = packText(text=label, styler=text_styles.standard)
        item.update(isSeparator=True)
        return item
    else:
        return


def packTokenProgress(tokenId, questId, title, image, gotCount, needCount, isBigSize=False):
    if gotCount == needCount:
        tokensGot = text_styles.bonusAppliedText(gotCount)
    else:
        tokensGot = text_styles.stats(gotCount)
    tokensNeed = text_styles.standard(needCount)
    counterText = text_styles.disabled((b'{} / {}').format(tokensGot, tokensNeed))
    return {b'tokenId': tokenId, 
       b'questId': questId, 
       b'titleText': title, 
       b'isNormalSize': (not isBigSize), 
       b'imgSrc': image, 
       b'countText': counterText}


def getResultsData(condition):

    def _makeStr(i18nKey, *args, **kwargs):
        if condition.isNegative():
            i18nKey = b'%s/not' % i18nKey
        return i18n.makeString(i18nKey, *args, **kwargs)

    key = b''
    if condition.keyName:
        key = i18n.makeString(b'#quests:details/conditions/cumulative/%s' % condition.keyName)
    else:
        labels = [i18n.makeString(b'#quests:details/conditions/cumulative/%s' % key) for key in condition.getAggregatedKeys()]
        aggregated = (b'\n').join(labels)
        if aggregated:
            key = (b'\n').join([i18n.makeString(QUESTS.DETAILS_CONDITIONS_CUMULATIVE_AGGREGATED), aggregated])
    labelKey = b'#quests:details/conditions/results'
    topRangeUpper, topRangeLower = condition.getMaxRange()
    if topRangeLower < TOP_RANGE_LOWEST:
        if condition.keyName == b'brPosInBattle':
            teamKey = b'battleRoyale'
            key = b''
        elif condition.isTotal():
            teamKey = b'bothTeams'
        else:
            teamKey = b'halfTeam'
        labelKey = b'%s/%s/%s' % (labelKey, condition.localeKey, teamKey)
        if topRangeUpper == TOP_RANGE_HIGHEST:
            if topRangeLower == 1 and condition.isTotal():
                label = i18n.makeString(b'%s/top1' % labelKey, param=key)
            else:
                label = _makeStr(b'%s/top' % labelKey, param=key, count=topRangeLower)
        elif topRangeLower == topRangeUpper:
            label = _makeStr(b'%s/position' % labelKey, param=key, position=topRangeUpper)
        else:
            label = _makeStr(b'%s/range' % labelKey, param=key, high=topRangeUpper, low=topRangeLower)
    elif condition.isAvg():
        label = i18n.makeString(b'#quests:details/conditions/results/%s/avg' % condition.localeKey, param=key)
    else:
        label = i18n.makeString(b'#quests:details/conditions/results/%s/simple' % condition.localeKey, param=key)
    value, relation, relationI18nType = condition.relationValue, condition.relation, RELATIONS_SCHEME.DEFAULT
    if condition.keyName == b'markOfMastery':
        relationI18nType = RELATIONS_SCHEME.ALTERNATIVE
        if condition.relationValue == 0:
            if condition.relation in (RELATIONS.EQ, RELATIONS.LSQ):
                i18nLabelKey = b'#quests:details/conditions/cumulative/markOfMastery0'
            elif condition.relation in (RELATIONS.LS,):
                raise SoftException(b'Mark of mastery 0 can be used with greater or equal relation types')
            i18nLabelKey = b'#quests:details/conditions/cumulative/markOfMastery0/not'
            label, value, relation = i18n.makeString(i18nLabelKey), None, None
        else:
            i18nValueKey = b'#quests:details/conditions/cumulative/markOfMastery%d' % int(condition.relationValue)
            i18nLabel = i18n.makeString(b'#quests:details/conditions/cumulative/markOfMastery')
            label, value, relation = i18nLabel, i18n.makeString(i18nValueKey), condition.relation
    return (
     label, relation, relationI18nType, value)


def _get128CondIcon(iconKey):
    return RES_ICONS.get128ConditionIcon(iconKey)


def _get90CondIcon(iconKey):
    return RES_ICONS.get90ConditionIcon(iconKey)


def getCondIconBySize(size, iconKey):
    if size == CONDITION_SIZE.NORMAL:
        return _get128CondIcon(iconKey)
    return _get90CondIcon(iconKey)
