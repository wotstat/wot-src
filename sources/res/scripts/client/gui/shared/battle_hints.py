import logging
from collections import namedtuple
import ResMgr
from gui import makeHtmlString
from gui.impl import backport
from gui.impl.gen import R
_logger = logging.getLogger(__name__)
_CONFIG_FILE = b'gui/battle_hints.xml'

class BattleHintData(namedtuple(b'_HintData', (b'name', b'componentAlias', b'iconPath', b'duration', b'maxWaitTime', b'priority', b'soundFx', b'soundNotification', b'htmlTemplate', b'rawMessage'))):

    def makeVO(self, data=None):
        if data is None:
            data = {}
        message = self.rawMessage or makeHtmlString(b'html_templates:battleHints', self.htmlTemplate)
        message = self._applyDataParams(message, data)
        hasIcon = self.iconPath and b'battleHints' in R.images.gui.maps.icons.keys()
        return {b'message': message, 
           b'iconSource': (backport.image(R.images.gui.maps.icons.battleHints.event.dyn(self.iconPath)()) if hasIcon else None)}

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
            hints.append(BattleHintData(name=hint[b'name'].asString, componentAlias=hint[b'component'].asString, htmlTemplate=hint[b'htmlTemplate'].asString, iconPath=hint[b'iconPath'].asString if hint.has_key(b'iconPath') else None, duration=hint[b'duration'].asFloat if hint.has_key(b'duration') else None, maxWaitTime=hint[b'maxWaitTime'].asFloat if hint.has_key(b'maxWaitTime') else 10, priority=hint[b'priority'].asInt if hint.has_key(b'priority') else 0, soundFx=hint[b'soundFx'].asString if hint.has_key(b'soundFx') else None, soundNotification=hint[b'soundNotification'].asString if hint.has_key(b'soundNotification') else None, rawMessage=None))

    else:
        _logger.error(b'Failed to open: %s', _CONFIG_FILE)
    return hints
