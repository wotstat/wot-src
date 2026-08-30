from collections import namedtuple
import ResMgr
from constants import IS_CLIENT, IS_WEB, TTC_TOOLTIP_SECTIONS
from items import _xml
from items.components import component_constants, skills_constants
from items.components import skills_components
from items.components.component_constants import EMPTY_STRING
from items.components.skills_constants import ParamMeasureType, ParamSignType, SkillTypeName
if IS_CLIENT or IS_WEB:
    from gui.impl import backport
    from gui.impl.gen import R
SkillUISettings = namedtuple(b'SkillUISettings', (b'tooltipSection', b'typeName', b'kpi', b'params', b'descrArgs'))
SkillDescrsArg = namedtuple(b'SkillDescrsArg', (b'situational', b'name', b'measureType', b'sign', b'value', b'isKpiVisible'))
TTCParamsArg = namedtuple(b'TTCParamsArg', (b'name', b'situational', b'value'))

def _readSkillBasics(xmlCtx, section, subsectionName):
    section = _xml.getSubsection(xmlCtx, section, subsectionName)
    xmlCtx = (xmlCtx, subsectionName)
    vsePerk = _xml.readIntOrNone(xmlCtx, section, b'vsePerk')
    if IS_CLIENT or IS_WEB:
        uiSettings = _readUISettings(xmlCtx, section, b'UISettings')
        tags = _readTags(xmlCtx, section, b'tags')
        skillLocales = _readLocales(subsectionName, section)
        skill = skills_components.BasicSkill(subsectionName, i18n=skillLocales, icon=_xml.readStringWithDefaultValue(xmlCtx, section, b'icon', (b'{}.png').format(subsectionName)), vsePerk=vsePerk, uiSettings=uiSettings, tags=tags)
    else:
        skill = skills_components.BasicSkill(subsectionName, vsePerk=vsePerk)
    return (skill, xmlCtx, section)


def _readLocales(skillName, section):

    def localeText(locRoot, dynName):
        if locRoot.isValid():
            dynStr = locRoot.dyn(dynName)
            if dynStr.isValid():
                return backport.text(dynStr())
        return EMPTY_STRING

    localeRoot = R.strings.crew_perks.dyn(skillName)
    altRoot = localeRoot.dyn(b'alt')
    return skills_components.SkillLocales(section.readString(b'userString', localeText(localeRoot, b'name')), section.readString(b'shortDescription', localeText(localeRoot, b'shortDescription')), section.readString(b'maxLvlDescription', localeText(localeRoot, b'maxLvlDescription')), section.readString(b'currentLvlDescription', localeText(localeRoot, b'currentLvlDescription')), section.readString(b'altDescription', localeText(altRoot, b'description')), section.readString(b'altInfo', localeText(altRoot, b'info')), section.readString(b'alertDescription', localeText(localeRoot, b'alertDescription')))


def _readUISettings(xmlCtx, section, subsectionName):
    from items.artefacts_helpers import readKpi
    section = _xml.getSubsection(xmlCtx, section, subsectionName, throwIfMissing=False)
    if not section:
        return
    kpi = []
    if IS_CLIENT and section.has_key(b'kpi'):
        kpi = readKpi(xmlCtx, section[b'kpi'])
    return SkillUISettings(tooltipSection=_xml.readStringWithDefaultValue(xmlCtx, section, b'tooltipSection', TTC_TOOLTIP_SECTIONS.SKILLS).split(), typeName=_xml.readStringWithDefaultValue(xmlCtx, section, b'typeName', SkillTypeName.MAIN), kpi=kpi, descrArgs=_readDescrArgs(xmlCtx, section, b'descr'), params=_readTTCParams(xmlCtx, section, b'params'))


def _readTags(xmlCtx, section, subsectionName):
    tagNames = _xml.readStringOrNone(xmlCtx, section, subsectionName)
    if tagNames is None:
        return frozenset()
    else:
        res = set()
        for tagName in tagNames.split():
            res.add(intern(tagName))

        return frozenset(res)


def _readDescrArgs(xmlCtx, section, subsectionName):
    section = _xml.getSubsection(xmlCtx, section, subsectionName, throwIfMissing=False)
    if not section:
        return {}
    settings = []
    for _, argSection in section.items():
        name = _xml.readNonEmptyString(xmlCtx, argSection, b'paramName')
        value = _xml.readFloat(xmlCtx, argSection, b'value')
        sign = ParamSignType.SIGN_LESS
        if value > 0:
            sign = ParamSignType.PLUS
        elif value < 0:
            sign = ParamSignType.MINUS
        settings.append((name,
         SkillDescrsArg(situational=_xml.readBool(xmlCtx, argSection, b'situationalParam', False), isKpiVisible=_xml.readBool(xmlCtx, argSection, b'isKpiVisible', True), name=name, measureType=_xml.readStringWithDefaultValue(xmlCtx, argSection, b'measureType', ParamMeasureType.PERCENTS), sign=_xml.readStringWithDefaultValue(xmlCtx, argSection, b'sign', sign), value=value)))

    return settings


def _readTTCParams(xmlCtx, section, subsectionName):
    section = _xml.getSubsection(xmlCtx, section, subsectionName, throwIfMissing=False)
    if not section:
        return {}
    params = {}
    for _, param in section.items():
        name = _xml.readNonEmptyString(xmlCtx, param, b'name')
        params[name] = TTCParamsArg(name=name, situational=_xml.readBool(xmlCtx, param, b'situationalParam', False), value=_xml.readFloat(xmlCtx, param, b'value'))

    return params


def _readRole(xmlCtx, section, subsectionName):
    skill, _, __ = _readSkillBasics(xmlCtx, section, subsectionName)
    return skill


def _readBrotherhoodSkill(xmlCtx, section, subsectionName):
    skill, xmlCtx, section = _readSkillBasics(xmlCtx, section, subsectionName)
    return skills_components.BrotherhoodSkill(skill, _xml.readFloat(xmlCtx, section, b'crewLevelIncrease', component_constants.ZERO_FLOAT))


def _readCommanderTutorSkill(xmlCtx, section, subsectionName):
    skill, xmlCtx, section = _readSkillBasics(xmlCtx, section, subsectionName)
    return skills_components.CommanderTutorSkill(skill, _xml.readNonNegativeFloat(xmlCtx, section, b'xpBonusFactorPerLevel'))


def _readCommanderUniversalistSkill(xmlCtx, section, subsectionName):
    skill, xmlCtx, section = _readSkillBasics(xmlCtx, section, subsectionName)
    return skills_components.CommanderUniversalistSkill(skill, _xml.readFraction(xmlCtx, section, b'efficiency'))


def _readCommanderSkillWithDelaySkill(xmlCtx, section, subsectionName):
    skill, xmlCtx, section = _readSkillBasics(xmlCtx, section, subsectionName)
    return skills_components.CommanderSkillWithDelay(skill, _xml.readNonNegativeFloat(xmlCtx, section, b'turnOnDelay'), _xml.readNonNegativeFloat(xmlCtx, section, b'turnOffDelay'))


def _readCommonSkill(xmlCtx, section, subsectionName):
    skill, xmlCtx, section = _readSkillBasics(xmlCtx, section, subsectionName)
    return skills_components.CommonSkill(skill)


def _readRadiomanLastEffortSkill(xmlCtx, section, subsectionName):
    skill, xmlCtx, section = _readSkillBasics(xmlCtx, section, subsectionName)
    return skills_components.RadiomanLastEffortSkill(skill, _xml.readFloat(xmlCtx, section, b'durationPerLevel'))


def _readCrewMasterySkill(xmlCtx, section, subsectionName):
    skill, xmlCtx, section = _readSkillBasics(xmlCtx, section, subsectionName)
    return skills_components.CrewMasterySkill(skill, _xml.readFloat(xmlCtx, section, b'crewLevelIncrease'))


def _readCommanderEnemyShotPredictorSkill(xmlCtx, section, subsectionName):
    skill, xmlCtx, section = _readSkillBasics(xmlCtx, section, subsectionName)
    return skills_components.CommanderEnemyShotPredictor(skill, _xml.readNonNegativeFloat(xmlCtx, section, b'minExplosionRadius'), _xml.readNonNegativeFloat(xmlCtx, section, b'explosionMultiplier'), _xml.readNonNegativeFloat(xmlCtx, section, b'recalculatingHeight'), _xml.readNonNegativeFloat(xmlCtx, section, b'targetRadius'))


_g_skillConfigReaders = {b'repair': _readRole, 
   b'camouflage': _readRole, 
   b'brotherhood': _readBrotherhoodSkill, 
   b'commander_tutor': _readCommanderTutorSkill, 
   b'commander_universalist': _readCommanderUniversalistSkill, 
   b'commander_expert': _readCommonSkill, 
   b'commander_sixthSense': _readCommanderSkillWithDelaySkill, 
   b'commander_enemyShotPredictor': _readCommanderEnemyShotPredictorSkill, 
   b'commander_eagleEye': _readCommonSkill, 
   b'driver_tidyPerson': _readCommonSkill, 
   b'driver_smoothDriving': _readCommonSkill, 
   b'driver_virtuoso': _readCommonSkill, 
   b'driver_badRoadsKing': _readCommonSkill, 
   b'driver_rammingMaster': _readCommonSkill, 
   b'gunner_smoothTurret': _readCommonSkill, 
   b'gunner_sniper': _readCommonSkill, 
   b'gunner_rancorous': _readCommonSkill, 
   b'gunner_gunsmith': _readCommonSkill, 
   b'loader_pedant': _readCommonSkill, 
   b'loader_desperado': _readCommonSkill, 
   b'loader_intuition': _readCommonSkill, 
   b'radioman_finder': _readCommonSkill, 
   b'radioman_inventor': _readCommonSkill, 
   b'radioman_lastEffort': _readRadiomanLastEffortSkill, 
   b'radioman_retransmitter': _readCommonSkill, 
   b'fireFighting': _readRole}

def readSkillsConfig(xmlPath):
    xmlCtx = (
     None, xmlPath)
    section = ResMgr.openSection(xmlPath)
    if section is None:
        _xml.raiseWrongXml(None, xmlPath, b'can not open or read')
    config = skills_components.SkillsConfig()
    for skillName in skills_constants.ROLES:
        skillConfig = _readRole(xmlCtx, section, b'roles/' + skillName)
        config.addSkill(skillName, skillConfig)

    section = _xml.getSubsection(xmlCtx, section, b'skills')
    xmlCtx = (xmlCtx, b'skills')
    for skillName in skills_constants.ACTIVE_SKILLS:
        skillConfig = _g_skillConfigReaders[skillName](xmlCtx, section, skillName)
        config.addSkill(skillName, skillConfig)

    ResMgr.purge(xmlPath, True)
    return config
