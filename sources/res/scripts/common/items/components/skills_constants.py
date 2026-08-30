SKILL_NAMES = (b'reserved', b'commander', b'radioman', b'driver', b'gunner', b'loader', b'repair', b'fireFighting', b'camouflage', b'brotherhood', b'any', b'reserved', b'reserved', b'reserved', b'reserved', b'reserved', b'commander_tutor', b'commander_eagleEye', b'commander_sixthSense', b'commander_expert', b'commander_universalist', b'commander_enemyShotPredictor', b'reserved', b'reserved', b'reserved', b'reserved', b'reserved', b'reserved', b'driver_virtuoso', b'driver_smoothDriving', b'driver_badRoadsKing', b'driver_rammingMaster', b'driver_tidyPerson', b'reserved', b'reserved', b'reserved', b'reserved', b'gunner_gunsmith', b'gunner_sniper', b'gunner_smoothTurret', b'gunner_rancorous', b'reserved', b'reserved', b'reserved', b'reserved', b'reserved', b'loader_pedant', b'loader_desperado', b'loader_intuition', b'reserved', b'reserved', b'reserved', b'reserved', b'radioman_inventor', b'radioman_finder', b'radioman_retransmitter', b'radioman_lastEffort', b'reserved', b'reserved', b'reserved', b'reserved')
SKILL_INDICES = dict((x[1], x[0]) for x in enumerate(SKILL_NAMES) if not x[1].startswith(b'reserved'))
ORDERED_ROLES = (b'commander', b'gunner', b'driver', b'radioman', b'loader')
ROLES = frozenset((b'commander', b'radioman', b'driver', b'gunner', b'loader'))
ROLE_LIMITS = {b'commander': 1, b'driver': 1}
COMMON_SKILLS_ORDERED = (b'brotherhood', b'repair', b'camouflage', b'fireFighting')
COMMON_SKILLS = frozenset(COMMON_SKILLS_ORDERED)
SEPARATE_SKILLS = frozenset((b'radioman_lastEffort',))
ROLES_AND_COMMON_SKILLS = ROLES | COMMON_SKILLS
COMMANDER_SKILLS = (b'commander_eagleEye', b'commander_universalist', b'commander_tutor', b'commander_expert', b'commander_sixthSense', b'commander_enemyShotPredictor')
COMMON_ROLE = b'common'
SKILLS_BY_ROLES_ORDERED = {b'commander': (COMMON_SKILLS_ORDERED + COMMANDER_SKILLS), 
   b'driver': (COMMON_SKILLS_ORDERED + (b'driver_virtuoso', b'driver_smoothDriving', b'driver_badRoadsKing', b'driver_tidyPerson', b'driver_rammingMaster')), 
   b'gunner': (COMMON_SKILLS_ORDERED + (b'gunner_smoothTurret', b'gunner_sniper', b'gunner_rancorous', b'gunner_gunsmith')), 
   b'loader': (COMMON_SKILLS_ORDERED + (b'loader_desperado', b'loader_pedant', b'loader_intuition')), 
   b'radioman': (COMMON_SKILLS_ORDERED + (b'radioman_finder', b'radioman_retransmitter', b'radioman_lastEffort', b'radioman_inventor'))}
SKILLS_BY_ROLES = {}
for role, skills in SKILLS_BY_ROLES_ORDERED.iteritems():
    SKILLS_BY_ROLES.setdefault(role, frozenset(skills))

ROLES_BY_SKILLS = {}
for role, skills in SKILLS_BY_ROLES.iteritems():
    for skill in skills:
        ROLES_BY_SKILLS.setdefault(skill, set()).add(role)

ACTIVE_SKILLS = SKILLS_BY_ROLES[b'commander'] | SKILLS_BY_ROLES[b'radioman'] | SKILLS_BY_ROLES[b'driver'] | SKILLS_BY_ROLES[b'gunner'] | SKILLS_BY_ROLES[b'loader']
ACTIVE_FREE_SKILLS = ACTIVE_SKILLS | {b'any'}
UNLEARNABLE_SKILLS = (b'commander_sixthSense',)
LEARNABLE_ACTIVE_SKILLS = ACTIVE_SKILLS.difference(UNLEARNABLE_SKILLS)

class ParamMeasureType(object):
    PERCENTS = b'percents'
    SECONDS = b'seconds'
    PERCENT_GAP = b'percentGap'
    MPH = b'mph'
    METERS = b'meters'


class ParamSignType(object):
    PLUS = b'plus'
    MINUS = b'minus'
    SIGN_LESS = b'signLess'


class SkillTypeName(object):
    MAIN = b'main'
    SITUATIONAL = b'situational'
    COMMON = b'common'
    COMMANDER_SPECIAL = b'commanderSpecial'
