import logging
from collections import namedtuple
import ResMgr
from gui import makeHtmlString
from gui.impl import backport
from gui.impl.gen import R
from items import _xml
from white_tiger.gui.battle_control.controllers.battle_hints_ctrl import WTBattleHintsController
_logger = logging.getLogger(__name__)
_CONFIG_FILE = b'white_tiger/gui/battle_hints.xml'
_XML_CTX = (None, _CONFIG_FILE)

class BattleHintData(namedtuple(b'_HintData', (b'name', b'componentAlias', b'iconPath', b'duration', b'maxWaitTime', b'priority', b'soundFx', b'soundNotification', b'htmlTemplate', b'rawMessage', b'backgroundColor', b'useCountdownTimer'))):

    def makeVO(self, data=None):
        if data is None:
            data = {}
        message = self.rawMessage or makeHtmlString(b'html_templates:battleHints', self.htmlTemplate)
        message = self._applyDataParams(message, data)
        hasIcon = self.iconPath and self.iconPath in R.images.white_tiger.gui.maps.icons.battleHints.keys()
        timer = self.duration
        if b'remainingTime' in data:
            timer = data[b'remainingTime']
        return {b'message': message, 
           b'iconSource': (backport.image(R.images.white_tiger.gui.maps.icons.battleHints.dyn(self.iconPath)()) if hasIcon else None), 
           b'timer': (timer * 1000), 
           b'useCountdownTimer': (self.useCountdownTimer), 
           b'backgroundColor': (self.backgroundColor)}

    def _applyDataParams(self, message, data):
        try:
            return message.format(**data)
        except KeyError:
            _logger.error(b'BattleHintData::_applyDataParams: Incorrect format for: %s', str(data))
            return message

        return


def makeHintsData():
    battleHintsConfig = ResMgr.openSection(_CONFIG_FILE)
    hints = []
    if battleHintsConfig:
        for hint in battleHintsConfig.values():
            hints.append(BattleHintData(name=hint[b'name'].asString, componentAlias=_xml.readTupleOfStrings(_XML_CTX, hint, b'component'), htmlTemplate=hint[b'htmlTemplate'].asString, iconPath=hint[b'iconPath'].asString if hint.has_key(b'iconPath') else None, duration=hint[b'duration'].asFloat if hint.has_key(b'duration') else None, maxWaitTime=hint[b'maxWaitTime'].asFloat if hint.has_key(b'maxWaitTime') else 10, priority=hint[b'priority'].asInt if hint.has_key(b'priority') else 0, soundFx=hint[b'soundFx'].asString if hint.has_key(b'soundFx') else None, useCountdownTimer=hint[b'useCountdownTimer'].asBool if hint.has_key(b'useCountdownTimer') else False, backgroundColor=hint[b'backgroundColor'].asString if hint.has_key(b'backgroundColor') else None, soundNotification=hint[b'soundNotification'].asString if hint.has_key(b'soundNotification') else None, rawMessage=None))

    else:
        _logger.error(b'Failed to open: %s', _CONFIG_FILE)
    return hints


def createWTBattleHintsController():
    return WTBattleHintsController(makeHintsData())
