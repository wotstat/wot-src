import typing, nations
from constants import IS_CLIENT
from debug_utils import LOG_CURRENT_EXCEPTION
from soft_exception import SoftException
from wotdecorators import singleton
from dossiers2.custom.cache import getCache as getHelperCache
_CONFIG_FILE = b'scripts/server_xml/blueprints.xml'

class BlueprintsException(SoftException):
    pass


def wipe(blueprints_cfg, pdata, leaveGold):
    pdata[b'blueprints'] = {}
    return


def makeDefaults():
    return {b'isEnabled': False, 
       b'useBlueprintsForUnlock': False, 
       b'allowBlueprintsConversion': False, 
       b'levels': {}}


def readConfig(verbose, **overrides):
    if IS_CLIENT:
        return makeDefaults()
    import XmlConfigReader
    reader = XmlConfigReader.makeReader(_CONFIG_FILE, b'', verbose)
    result = _readBlueprints(reader, b'blueprints')
    for k in result:
        if k not in overrides:
            continue
        if k in (b'isEnabled', b'useBlueprintsForUnlock', b'allowBlueprintsConversion'):
            result[k] &= overrides[k]
        else:
            result[k] = overrides[k]

    return result


def _readBlueprints(reader, subsectionName):
    section = reader.getSubsection(subsectionName)
    if section is None:
        return {}
    else:
        isEnabled = section.readBool(b'isEnabled', False)
        useBlueprintsForUnlock = section.readBool(b'useBlueprintsForUnlock', False)
        allowBlueprintsConversion = section.readBool(b'allowBlueprintsConversion', False)
        levels = {}
        levelsSubsection = reader.getSubsection(subsectionName + b'/levels')
        for lname, lsection in levelsSubsection.items():
            _, lvl = str(lname).split(b'_', 1)
            parts = lsection.readInt(b'parts', 0)
            progress = lsection.readFloat(b'progress', 0)
            requires = tuple(int(i) for i in lsection.readString(b'requires').split()) or (0, 0)
            decays = tuple(float(i) for i in lsection.readString(b'decays').split()) or (0, 0)
            allyConversionCoef = _readConversionCoefs(lsection, b'allyConversionCoefs')
            levels[int(lvl)] = (parts, progress, requires, decays, allyConversionCoef)

        return {b'isEnabled': isEnabled, 
           b'useBlueprintsForUnlock': useBlueprintsForUnlock, 
           b'allowBlueprintsConversion': allowBlueprintsConversion, 
           b'levels': levels}


def _readConversionCoefs(section, subsectionName):
    result = {}
    for allianceName, groupSection in section[subsectionName].items():
        result[nations.ALLIANCE_IDS[allianceName]] = group = dict()
        for nationName, _ in groupSection.items():
            group[nations.INDICES[nationName]] = groupSection.readFloat(nationName, 1)

    return result


@singleton
class g_cache(object):

    def __init__(self):
        self.__cfg = makeDefaults()
        return

    def __getattr__(self, attr):
        try:
            return self.__cfg[attr]
        except KeyError:
            raise AttributeError

        return

    def init(self, gameParams=None, nofail=True):
        cfg = self.__cfg
        try:
            if gameParams is not None:
                blueprints = gameParams[b'blueprints_config'].settings
            else:
                blueprints = readConfig(True)
            cfg.update(blueprints)
        except Exception:
            self.fini()
            if nofail:
                raise
            LOG_CURRENT_EXCEPTION()

        return

    def fini(self):
        self.__cfg.clear()
        return

    def __nonzero__(self):
        return bool(self.__cfg)


def init(gameParams=None, nofail=True):
    g_cache.init(gameParams=gameParams, nofail=nofail)
    return


def getAllResearchedVehicles(defaultUnlocks=frozenset()):
    return getHelperCache()[b'vehiclesInTrees'] - defaultUnlocks


def getResearchableVehiclesWithout1Lvl(unlocks=frozenset(), initialUnlocks=frozenset()):
    return getHelperCache()[b'vehiclesInTreesWithout1Lvl'] - unlocks - initialUnlocks


def getUnlockedVehicles(unlocks=frozenset(), initialUnlocks=frozenset()):
    return getHelperCache()[b'vehiclesInTrees'] & unlocks.union(initialUnlocks)


def isNationResearched(nationID, defaultUnlocks=frozenset(), unlocks=frozenset()):
    return not bool(getHelperCache()[b'vehiclesInTreesByNation'][nationID] - defaultUnlocks - unlocks)
