from __future__ import absolute_import
from collections import namedtuple
import ResMgr
from constants import IS_CLIENT, IS_WEB, TTC_TOOLTIP_SECTIONS
from items import _xml
from items.components import component_constants, skills_constants
from items.components import skills_components
from items.components.skills_constants import ParamMeasureType, ParamSignType, SkillTypeName
SkillUISettings = namedtuple(b'SkillUISettings', (b'tooltipSection', b'typeName', b'kpi', b'params', b'descrArgs'))
SkillDescrsArg = namedtuple(b'SkillDescrsArg', (b'situational', b'name', b'measureType', b'sign', b'value', b'isKpiVisible'))
TTCParamsArg = namedtuple(b'TTCParamsArg', (b'name', b'situational', b'value'))

def _readSkillBasics(xmlCtx, section, subsectionName):
    section = _xml.getSubsection(xmlCtx, section, subsectionName)
    xmlCtx = (xmlCtx, subsectionName)
    vsePerk = _xml.readIntOrNone(xmlCtx, section, b'vsePerk')
    if IS_CLIENT or IS_WEB:
        uiSettings = _readUISettings(xmlCtx, section, b'UISettings')
        skill = skills_components.BasicSkill(subsectionName, vsePerk, uiSettings)
    else:
        skill = skills_components.BasicSkill(subsectionName, vsePerk=vsePerk)
    return (skill, xmlCtx, section)


def _readUISettings(xmlCtx, section, subsectionName):
    from items.artefacts_helpers import readKpi
    section = _xml.getSubsection(xmlCtx, section, subsectionName, throwIfMissing=False)
    if not section:
        return
    kpi = []
    if IS_CLIENT and section.has_key(b'kpi'):
        kpi = readKpi(xmlCtx, section[b'kpi'])
    return SkillUISettings(tooltipSection=_xml.readStringWithDefaultValue(xmlCtx, section, b'tooltipSection', TTC_TOOLTIP_SECTIONS.SKILLS), typeName=_xml.readStringWithDefaultValue(xmlCtx, section, b'typeName', SkillTypeName.MAIN), kpi=kpi, descrArgs=_readDescrArgs(xmlCtx, section, b'descr'), params=_readTTCParams(xmlCtx, section, b'params'))


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
    return skills_components.CommanderTutorSkill(skill, _xml.readNonNegativeFloat(xmlCtx, section, b'xpBonusFactorPerLevel'), _xml.readFraction(xmlCtx, section, b'efficiency'))


def _readCommanderSkillWithDelaySkill(xmlCtx, section, subsectionName):
    skill, xmlCtx, section = _readSkillBasics(xmlCtx, section, subsectionName)
    return skills_components.CommanderSkillWithDelay(skill, _xml.readNonNegativeFloat(xmlCtx, section, b'delay'))


def _readCommonSkill(xmlCtx, section, subsectionName):
    skill, xmlCtx, section = _readSkillBasics(xmlCtx, section, subsectionName)
    return skills_components.CommonSkill(skill)


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
   b'commander_coordination': _readCommonSkill, 
   b'commander_sixthSense': _readCommanderSkillWithDelaySkill, 
   b'commander_emergency': _readCrewMasterySkill, 
   b'commander_enemyShotPredictor': _readCommanderEnemyShotPredictorSkill, 
   b'commander_eagleEye': _readCommonSkill, 
   b'commander_practical': _readCommonSkill, 
   b'commander_holdLine': _readCrewMasterySkill, 
   b'commander_staySharp': _readCrewMasterySkill, 
   b'driver_smoothDriving': _readCommonSkill, 
   b'driver_virtuoso': _readCommonSkill, 
   b'driver_badRoadsKing': _readCommonSkill, 
   b'driver_rammingMaster': _readCommonSkill, 
   b'driver_motorExpert': _readCommonSkill, 
   b'driver_reliablePlacement': _readCommonSkill, 
   b'driver_suspensionRepair': _readCommonSkill, 
   b'driver_bulletproof': _readCrewMasterySkill, 
   b'gunner_smoothTurret': _readCommonSkill, 
   b'gunner_sniper': _readCommonSkill, 
   b'gunner_rancorous': _readCommonSkill, 
   b'gunner_armorer': _readCommonSkill, 
   b'gunner_focus': _readCommonSkill, 
   b'gunner_quickAiming': _readCommonSkill, 
   b'gunner_loneWolf': _readCommonSkill, 
   b'gunner_pointBlast': _readCommonSkill, 
   b'loader_pedant': _readCommonSkill, 
   b'loader_desperado': _readCommonSkill, 
   b'loader_intuition': _readCommonSkill, 
   b'loader_perfectCharge': _readCommonSkill, 
   b'loader_ammunitionImprove': _readCommonSkill, 
   b'loader_melee': _readCommonSkill, 
   b'loader_magMastery': _readCommonSkill, 
   b'loader_secondChance': _readCommonSkill, 
   b'radioman_finder': _readCommonSkill, 
   b'radioman_expert': _readCrewMasterySkill, 
   b'radioman_sideBySide': _readCrewMasterySkill, 
   b'fireFighting': _readCommonSkill, 
   b'radioman_interference': _readCommonSkill, 
   b'radioman_signalInterception': _readCommonSkill, 
   b'radioman_battleTempered': _readCommonSkill, 
   b'radioman_threatSearch': _readCommonSkill}

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


def readAutoFillConfig(xmlPath):
    cfg = {}
    xmlCtx = (
     None, xmlPath)
    section = ResMgr.openSection(xmlPath)
    if section is None:
        _xml.raiseWrongXml(None, xmlPath, b'can not open or read')
    autofillSection = _xml.getSubsection(xmlCtx, section, b'autofill')
    for roleName, roleSection in autofillSection.items():
        if roleName not in skills_constants.ROLES:
            _xml.raiseWrongXml(xmlCtx, roleName, b'wrong role name')
        skillsList = []
        for skillName in roleSection.keys():
            if skillName not in skills_constants.ACTIVE_SKILLS:
                _xml.raiseWrongXml(xmlCtx, skillName, b'wrong skill name')
            skillsList.append(skillName)

        cfg[roleName] = tuple(skillsList)

    return cfg
