from __future__ import absolute_import
import resource_helper
from debug_utils import LOG_CURRENT_EXCEPTION
from constants import IS_WEB
from soft_exception import SoftException
BATTLE_HERO_TEXTS = {b'warrior': b'#achievements:warrior', 
   b'invader': b'#achievements:invader', 
   b'sniper': b'#achievements:sniper', 
   b'defender': b'#achievements:defender', 
   b'steelwall': b'#achievements:steelwall', 
   b'supporter': b'#achievements:supporter', 
   b'scout': b'#achievements:scout', 
   b'evileye': b'#achievements:evileye'}
BADGES_BLOCK = b'playerBadges'

class ACHIEVEMENT_BLOCK:
    CLIENT = b'client'
    TOTAL = b'achievements'
    TEAM_7X7 = b'achievements7x7'
    HISTORICAL = b'historicalAchievements'
    UNIQUE = b'uniqueAchievements'
    RARE = b'rareAchievements'
    FORT = b'fortAchievements'
    SINGLE = b'singleAchievements'
    SINGLE_7X7 = b'singleAchievementsRated7x7'
    CLAN = b'clanAchievements'
    RATED_7X7 = b'achievementsRated7x7'
    FALLOUT = b'falloutAchievements'
    EPIC_BATTLE = b'epicBattleAchievements'
    STEAM = b'steamAchievements'
    ALL = (
     CLIENT, TOTAL, TEAM_7X7, HISTORICAL, UNIQUE, RARE,
     FORT, SINGLE, CLAN, RATED_7X7, SINGLE_7X7, FALLOUT, EPIC_BATTLE, STEAM)


class ACHIEVEMENT_MODE:
    RANDOM = 1
    TEAM_7X7 = 2
    HISTORICAL = 4
    RATED_7X7 = 8
    RANKED = 22
    EPIC_BATTLE = 16
    ALL = RANDOM | TEAM_7X7 | HISTORICAL | RATED_7X7 | RANKED | EPIC_BATTLE


class ACHIEVEMENT_TYPE:
    REPEATABLE = b'repeatable'
    CLASS = b'class'
    CUSTOM = b'custom'
    SERIES = b'series'
    SINGLE = b'single'
    ALL = (
     REPEATABLE, CLASS, CUSTOM, SERIES, SINGLE)


class ACHIEVEMENT_SECTION:
    EPIC = b'epic'
    BATTLE = b'battle'
    SPECIAL = b'special'
    CLASS = b'class'
    ACTION = b'action'
    MEMORIAL = b'memorial'
    GROUP = b'group'
    ALL = (
     EPIC, BATTLE, SPECIAL, CLASS, ACTION, MEMORIAL, GROUP)


_AT, _AS, _AB, _AM = (
 ACHIEVEMENT_TYPE, ACHIEVEMENT_SECTION, ACHIEVEMENT_BLOCK,
 ACHIEVEMENT_MODE)
DEFAULT_WEIGHT = -1

def makeAchievesStorageName(block):
    return (
     block, b'')


MARK_OF_MASTERY = b'markOfMastery'
MARK_ON_GUN = b'marksOnGun'
RARE_STORAGE_RECORD = makeAchievesStorageName(_AB.RARE)
MARK_OF_MASTERY_RECORD = (_AB.TOTAL, MARK_OF_MASTERY)
MARK_ON_GUN_RECORD = (_AB.TOTAL, MARK_ON_GUN)
HONORED_RANK_RECORD = (_AB.CLIENT, b'honoredRank')
_MODE_CONVERTER = {b'random': (ACHIEVEMENT_MODE.RANDOM), 
   b'ranked': (ACHIEVEMENT_MODE.RANKED), 
   b'7x7': (ACHIEVEMENT_MODE.TEAM_7X7), 
   b'historical': (ACHIEVEMENT_MODE.HISTORICAL), 
   b'rated7x7': (ACHIEVEMENT_MODE.RATED_7X7), 
   b'epic_battle': (ACHIEVEMENT_MODE.EPIC_BATTLE), 
   b'all': (ACHIEVEMENT_MODE.ALL)}
ACHIEVEMENTS = {}
ACHIEVEMENT_SECTIONS_ORDER = (
 _AS.BATTLE, _AS.SPECIAL, _AS.EPIC, _AS.GROUP, _AS.MEMORIAL,
 _AS.CLASS, _AS.ACTION)
ACHIEVEMENT_SECTIONS_INDICES = dict((n, i) for i, n in enumerate(ACHIEVEMENT_SECTIONS_ORDER))
BATTLE_ACHIEVES_WITH_RIBBON = ()
BATTLE_ACHIEVES_RIGHT = ()
FORT_BATTLE_ACHIEVES_RIGHT = ()
BATTLE_APPROACHABLE_ACHIEVES = ()

def getType(record):
    global ACHIEVEMENTS
    if record in ACHIEVEMENTS:
        return ACHIEVEMENTS[record][b'type']
    else:
        return


def getSection(record):
    if record in ACHIEVEMENTS:
        return ACHIEVEMENTS[record][b'section']
    else:
        return


def getMode(record):
    if record in ACHIEVEMENTS:
        return ACHIEVEMENTS[record][b'mode']
    else:
        return


def getWeight(record):
    if record in ACHIEVEMENTS:
        return ACHIEVEMENTS[record][b'weight']
    else:
        return


def init(achievesMappingXmlPath):
    global BATTLE_ACHIEVES_RIGHT
    global BATTLE_ACHIEVES_WITH_RIBBON
    global BATTLE_APPROACHABLE_ACHIEVES
    global FORT_BATTLE_ACHIEVES_RIGHT
    if IS_WEB:
        return
    ctx, section = resource_helper.getRoot(achievesMappingXmlPath)
    for ctx, subSection in resource_helper.getIterator(ctx, section[b'achievements']):
        try:
            item = resource_helper.readItem(ctx, subSection, name=b'achievement')
            if not item.name:
                continue
            block, name = tuple(item.name.split(b':'))
            if block not in ACHIEVEMENT_BLOCK.ALL:
                raise SoftException(b'Unknown block name', (block, name))
            if b'type' not in item.value or item.value[b'type'] not in ACHIEVEMENT_TYPE.ALL:
                raise SoftException(b'Unknown achievement type', (block, name), item.value)
            if b'section' not in item.value or item.value[b'section'] not in ACHIEVEMENT_SECTION.ALL:
                raise SoftException(b'Unknown achievement section', (block, name), item.value)
            if b'mode' not in item.value or item.value[b'mode'] not in _MODE_CONVERTER:
                raise SoftException(b'Unknown achievement mode', (block, name), item.value)
            value = dict(item.value)
            value[b'mode'] = _MODE_CONVERTER[item.value[b'mode']]
            if b'weight' not in value:
                value[b'weight'] = -1.0
            ACHIEVEMENTS[(block, name)] = value
        except:
            LOG_CURRENT_EXCEPTION()

    BATTLE_ACHIEVES_WITH_RIBBON = tuple(resource_helper.readList(ctx, section[b'battleAchievesWithRibbon']).value)
    BATTLE_ACHIEVES_RIGHT = tuple(resource_helper.readList(ctx, section[b'battleResultsRight']).value)
    FORT_BATTLE_ACHIEVES_RIGHT = tuple(resource_helper.readList(ctx, section[b'fortBattleResultsRight']).value)
    BATTLE_APPROACHABLE_ACHIEVES = tuple(resource_helper.readList(ctx, section[b'approachableAchieves']).value)
    resource_helper.purgeResource(achievesMappingXmlPath)
    return
