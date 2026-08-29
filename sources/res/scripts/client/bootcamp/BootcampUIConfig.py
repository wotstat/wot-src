from copy import copy
import ResMgr
from soft_exception import SoftException
g_defaultBattleRibbonsSettings = {b'damage': False, 
   b'kill': False, 
   b'armor': False, 
   b'ram': False, 
   b'spotted': False, 
   b'capture': False, 
   b'crits': False}
XML_CONFIG_PATH = b'scripts/bootcamp_docs/battle_page_visibility.xml'

def readUISettingsFile(path):
    settingsConfig = ResMgr.openSection(path)
    if settingsConfig is None:
        raise SoftException(b"Can't open config file (%s)" % path)
    allPrebattleSettings = {}
    allRibbonsSettings = {}
    for name, section in settingsConfig.items():
        if name == b'lesson':
            lessonId = section[b'id'].asInt
            ribbonsSettings = copy(g_defaultBattleRibbonsSettings)
            ribString = section[b'ribbons'].asString
            ribbonNames = ribString.split()
            for ribName in ribbonNames:
                if ribName in ribbonsSettings:
                    ribbonsSettings[ribName] = True

            allRibbonsSettings[lessonId] = ribbonsSettings
            prebattleSettings = {}
            prebattleSection = section[b'prebattle']
            if prebattleSection.has_key(b'timeout'):
                prebattleSettings[b'timeout'] = prebattleSection[b'timeout'].asFloat
            allPrebattleSettings[lessonId] = prebattleSettings

    return (
     allPrebattleSettings, allRibbonsSettings)


g_prebattleSettings, g_battleRibbonsSettings = readUISettingsFile(XML_CONFIG_PATH)

def getBattleRibbonsSettings(lessonId):
    return g_battleRibbonsSettings[lessonId]


def getPrebattleSettings(lessonId):
    return g_prebattleSettings[lessonId]
