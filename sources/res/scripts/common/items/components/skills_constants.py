from __future__ import absolute_import
from collections import OrderedDict
from future.utils import iteritems
SKILL_NAMES = (b'reserved', b'commander', b'radioman', b'driver', b'gunner', b'loader', b'repair', b'fireFighting', b'camouflage', b'brotherhood', b'any', b'armorPatching', b'reserved', b'reserved', b'reserved', b'reserved', b'commander_tutor', b'commander_eagleEye', b'commander_sixthSense', b'commander_expert', b'commander_universalist', b'commander_enemyShotPredictor', b'commander_practical', b'commander_emergency', b'commander_coordination', b'commander_holdLine', b'commander_staySharp', b'reserved', b'driver_virtuoso', b'driver_smoothDriving', b'driver_badRoadsKing', b'driver_rammingMaster', b'driver_tidyPerson', b'driver_motorExpert', b'driver_reliablePlacement', b'driver_suspensionRepair', b'driver_bulletproof', b'gunner_gunsmith', b'gunner_sniper', b'gunner_smoothTurret', b'gunner_rancorous', b'gunner_focus', b'gunner_quickAiming', b'gunner_armorer', b'gunner_pointBlast', b'gunner_loneWolf', b'loader_pedant', b'loader_desperado', b'loader_intuition', b'loader_perfectCharge', b'loader_ammunitionImprove', b'loader_melee', b'loader_magMastery', b'radioman_inventor', b'radioman_finder', b'radioman_retransmitter', b'radioman_lastEffort', b'radioman_interference', b'radioman_signalInterception', b'radioman_sideBySide', b'radioman_expert', b'radioman_battleTempered', b'radioman_threatSearch', b'loader_secondChance')

class ROLE_NAMES(object):
    COMMANDER = b'commander'
    RADIOMAN = b'radioman'
    DRIVER = b'driver'
    GUNNER = b'gunner'
    LOADER = b'loader'


SKILL_INDICES = dict((x[1], x[0]) for x in enumerate(SKILL_NAMES) if not x[1].startswith(b'reserved'))
ORDERED_ROLES = (
 ROLE_NAMES.COMMANDER, ROLE_NAMES.GUNNER, ROLE_NAMES.DRIVER, ROLE_NAMES.RADIOMAN, ROLE_NAMES.LOADER)
ROLES = frozenset(ORDERED_ROLES)
COMMON_SKILL_ROLE_TYPE = b'common'
ROLE_LIMITS = {(ROLE_NAMES.COMMANDER): 1, (ROLE_NAMES.DRIVER): 1}
COMMON_SKILLS_ORDERED = (b'brotherhood', b'repair', b'camouflage')
COMMON_SKILLS = frozenset(COMMON_SKILLS_ORDERED)
ROLES_AND_COMMON_SKILLS = ROLES | COMMON_SKILLS
COMMANDER_SKILLS = (b'commander_eagleEye', b'commander_emergency', b'commander_tutor', b'commander_coordination', b'commander_enemyShotPredictor', b'commander_practical', b'commander_sixthSense', b'commander_holdLine', b'commander_staySharp')
GUNNER_SKILLS = (b'gunner_smoothTurret', b'gunner_sniper', b'gunner_rancorous', b'gunner_focus', b'gunner_quickAiming', b'gunner_armorer', b'gunner_pointBlast', b'gunner_loneWolf')
DRIVER_SKILLS = (b'driver_virtuoso', b'driver_smoothDriving', b'driver_badRoadsKing', b'driver_reliablePlacement', b'driver_rammingMaster', b'driver_motorExpert', b'driver_suspensionRepair', b'driver_bulletproof')
RADIOMAN_SKILLS = (b'radioman_finder', b'radioman_sideBySide', b'radioman_interference', b'radioman_signalInterception', b'radioman_expert', b'fireFighting', b'radioman_battleTempered', b'radioman_threatSearch')
LOADER_SKILLS = (b'loader_desperado', b'loader_pedant', b'loader_intuition', b'loader_perfectCharge', b'loader_melee', b'loader_ammunitionImprove', b'loader_secondChance', b'loader_magMastery')
COMMON_ROLE = b'common'
SKILLS_BY_ROLES_ORDERED = {(ROLE_NAMES.COMMANDER): (COMMON_SKILLS_ORDERED + COMMANDER_SKILLS), 
   (ROLE_NAMES.GUNNER): (COMMON_SKILLS_ORDERED + GUNNER_SKILLS), 
   (ROLE_NAMES.DRIVER): (COMMON_SKILLS_ORDERED + DRIVER_SKILLS), 
   (ROLE_NAMES.RADIOMAN): (COMMON_SKILLS_ORDERED + RADIOMAN_SKILLS), 
   (ROLE_NAMES.LOADER): (COMMON_SKILLS_ORDERED + LOADER_SKILLS)}
SKILL_NAMES_ORDERED = COMMON_SKILLS_ORDERED + COMMANDER_SKILLS + GUNNER_SKILLS + DRIVER_SKILLS + RADIOMAN_SKILLS + LOADER_SKILLS
SKILL_INDICES_ORDERED = dict((x[1], x[0]) for x in enumerate(SKILL_NAMES_ORDERED))
SKILLS_BY_ROLES = {}
for role, skills in iteritems(SKILLS_BY_ROLES_ORDERED):
    SKILLS_BY_ROLES.setdefault(role, frozenset(skills))

ROLES_BY_SKILLS = {}
for role, skills in iteritems(SKILLS_BY_ROLES):
    for skill in skills:
        ROLES_BY_SKILLS.setdefault(skill, set()).add(role)

ACTIVE_SKILLS = SKILLS_BY_ROLES[ROLE_NAMES.COMMANDER] | SKILLS_BY_ROLES[ROLE_NAMES.RADIOMAN] | SKILLS_BY_ROLES[ROLE_NAMES.DRIVER] | SKILLS_BY_ROLES[ROLE_NAMES.GUNNER] | SKILLS_BY_ROLES[ROLE_NAMES.LOADER]
ACTIVE_NOT_GROUP_SKILLS = frozenset(set(ACTIVE_SKILLS) - set(COMMON_SKILLS_ORDERED))
ACTIVE_FREE_SKILLS = ACTIVE_SKILLS | {b'any'}
UNLEARNABLE_SKILLS = (b'commander_sixthSense',)
LEARNABLE_ACTIVE_SKILLS = ACTIVE_SKILLS.difference(UNLEARNABLE_SKILLS)
LEARNABLE_COMMANDER_SKILLS = SKILLS_BY_ROLES[ROLE_NAMES.COMMANDER].difference(UNLEARNABLE_SKILLS)
ALL_SKILLS_BY_ROLE_TYPE = OrderedDict((
 (
  COMMON_ROLE, COMMON_SKILLS_ORDERED),
 (
  ROLE_NAMES.COMMANDER, tuple(skill for skill in COMMANDER_SKILLS if skill not in UNLEARNABLE_SKILLS)),
 (
  ROLE_NAMES.GUNNER, GUNNER_SKILLS),
 (
  ROLE_NAMES.DRIVER, DRIVER_SKILLS),
 (
  ROLE_NAMES.RADIOMAN, RADIOMAN_SKILLS),
 (
  ROLE_NAMES.LOADER, LOADER_SKILLS)))

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


class SkillUtilization(object):
    FREE_SKILL = 0
    MAJOR_SKILL = 1
    BONUS_SKILL = 2
