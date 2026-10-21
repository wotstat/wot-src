import logging, ResMgr
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.battle_hints import BattleHintData
from gui.battle_control.controllers.battle_hints_ctrl import BattleHintsController
from portal.gui.shared.utils import getBossVehicleName
_logger = logging.getLogger(__name__)
_CONFIG_FILE = b'portal/gui/battle_hints.xml'
_BATTLE_HINT_DATA_MAPPING = {b'waveStarted': (
                  (
                   b'currentWave', int), (b'laneIndex', int)), 
   b'campBecameCapturable': (
                           (
                            b'frontier', str),), 
   b'campCaptured': (
                   (
                    b'frontier', str),), 
   b'almostBase': (
                 (
                  b'laneIndex', int),)}

def _mapBattleHintData(hintName, data):
    hintData = None
    mapping = _BATTLE_HINT_DATA_MAPPING.get(hintName)
    if mapping and data:
        hintData = {}
        for index, (k, t) in enumerate(mapping, start=1):
            value = t(data[(b'param{}').format(index)])
            hintData[k] = value

    elif mapping or data:
        _logger.error(b'Battle hint data mismatch')
    return hintData


class PortalBattleHintData(BattleHintData):

    def makeVO(self, data=None):
        hintData = _mapBattleHintData(self.name, data) or {}
        self.__processBattleHintData(hintData)
        vo = super(PortalBattleHintData, self).makeVO(hintData)
        if self.iconPath:
            vo[b'iconSource'] = self.__getIcon(hintData)
        return vo

    def __processBattleHintData(self, hintData):
        resource = R.strings.portal_battle.battle_hints.dyn(self.name)
        if b'laneIndex' in hintData:
            laneIndex = (b'c_{}').format(hintData[b'laneIndex'])
            hintData[b'lane'] = backport.text(resource.dyn(laneIndex)())
        if self.name == b'superBossFightStarted':
            hintData[b'bossName'] = getBossVehicleName()
        return

    def __getIcon(self, data):
        resource = R.images.portal.gui.maps.icons.battle_hints
        if b'frontier' in data:
            frontier = data[b'frontier'].lower()
            resource = resource.dyn(frontier)
        return backport.image(resource.dyn(self.iconPath)())


def makePortalHintsData():
    battleHintsConfig = ResMgr.openSection(_CONFIG_FILE)
    hints = []
    if battleHintsConfig:
        for hint in battleHintsConfig.values():
            hints.append(PortalBattleHintData(name=hint[b'name'].asString, componentAlias=hint[b'component'].asString, htmlTemplate=hint[b'htmlTemplate'].asString, iconPath=hint[b'iconPath'].asString if hint.has_key(b'iconPath') else None, duration=hint[b'duration'].asFloat if hint.has_key(b'duration') else None, maxWaitTime=hint[b'maxWaitTime'].asFloat if hint.has_key(b'maxWaitTime') else 10, priority=hint[b'priority'].asInt if hint.has_key(b'priority') else 0, soundFx=hint[b'soundFx'].asString if hint.has_key(b'soundFx') else None, soundNotification=hint[b'soundNotification'].asString if hint.has_key(b'soundNotification') else None, rawMessage=None))

    else:
        _logger.error(b'Failed to open: %s', _CONFIG_FILE)
    return hints


def createBattleHintsController():
    return BattleHintsController(makePortalHintsData())
