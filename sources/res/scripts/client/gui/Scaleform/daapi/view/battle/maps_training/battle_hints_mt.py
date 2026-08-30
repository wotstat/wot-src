import logging
from collections import namedtuple
from enum import Enum
import ResMgr
from gui.battle_control.controllers.battle_hints_ctrl import BattleHintsController
from gui.impl import backport
from gui.impl.gen import R
from helpers.time_utils import ONE_MINUTE
_logger = logging.getLogger(__name__)
_CONFIG_FILE = b'gui/battle_hints_maps_training.xml'

class HintType(Enum):
    HINT = b'hint'
    GOAL = b'goal'
    TIMER_GREEN = b'timerGreen'
    TIMER_RED = b'timerRed'


class BattleHintData(namedtuple(b'_HintData', (b'name', b'componentAlias', b'duration', b'maxWaitTime', b'priority', b'hintType', b'soundFx', b'soundNotification', b'descriptionKey1', b'descriptionKey2', b'soundNotificationNewbie'))):

    def makeVO(self, data=None):
        vo = {b'hintType': (self.hintType)}
        if self.descriptionKey1 is not None:
            vo[b'description1'] = backport.text(R.strings.maps_training.hints.dyn(self.descriptionKey1)())
        if self.descriptionKey2 is not None:
            vo[b'description2'] = backport.text(R.strings.maps_training.hints.dyn(self.descriptionKey2)())
        if data is not None:
            self.__applyData(vo, data)
        return vo

    def __applyData(self, vo, data):
        if self.hintType is HintType.GOAL:
            vo[b'targetsCount'] = data[b'param1']
            vo[b'targetsTotal'] = data[b'param2']
        elif self.hintType in (HintType.TIMER_RED, HintType.TIMER_GREEN):
            minutes, seconds = divmod(int(data[b'param1']), ONE_MINUTE)
            minutesStr, secondsStr = (b'{}').format(minutes), (b'{:02d}').format(seconds)
            vo[b'description1'] = vo[b'description1'].format(minutes=minutesStr, seconds=secondsStr)
        return


def makeHintsData():
    battleHintsConfig = ResMgr.openSection(_CONFIG_FILE)
    hints = []
    if battleHintsConfig:
        for hint in battleHintsConfig.values():
            hints.append(BattleHintData(name=hint[b'name'].asString, componentAlias=hint[b'component'].asString, hintType=HintType(hint[b'hintType'].asString), descriptionKey1=hint[b'descriptionKey1'].asString if hint.has_key(b'descriptionKey1') else None, descriptionKey2=hint[b'descriptionKey2'].asString if hint.has_key(b'descriptionKey2') else None, duration=hint[b'duration'].asFloat if hint.has_key(b'duration') else None, maxWaitTime=hint[b'maxWaitTime'].asFloat if hint.has_key(b'maxWaitTime') else 10, priority=hint[b'priority'].asInt if hint.has_key(b'priority') else 0, soundFx=hint[b'soundFx'].asString if hint.has_key(b'soundFx') else None, soundNotification=hint[b'soundNotification'].asString if hint.has_key(b'soundNotification') else None, soundNotificationNewbie=hint[b'soundNotificationNewbie'].asString if hint.has_key(b'soundNotificationNewbie') else None))

    else:
        _logger.error(b'Failed to open: %s', _CONFIG_FILE)
    return hints


def createBattleHintsController():
    return BattleHintsController(makeHintsData())
