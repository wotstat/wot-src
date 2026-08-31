from __future__ import absolute_import
from items.artefacts import VisualScriptEquipment
from items import _xml
from items.components import component_constants
from items.artefacts import Repairkit

class WTEquipment(VisualScriptEquipment):
    __slots__ = (b'deploySeconds', b'consumeSeconds', b'soundPressedReady', b'soundPressedNotReady', b'soundPressedCancel')

    def __init__(self):
        super(WTEquipment, self).__init__()
        self.deploySeconds = component_constants.ZERO_INT
        self.consumeSeconds = component_constants.ZERO_INT
        self.soundPressedReady = None
        self.soundPressedNotReady = None
        self.soundPressedCancel = None
        return

    def _readBasicConfig(self, xmlCtx, section):
        super(WTEquipment, self)._readBasicConfig(xmlCtx, section)
        self.soundPressedReady = _xml.readStringOrNone(xmlCtx, section, b'soundPressedReady')
        self.soundPressedNotReady = _xml.readStringOrNone(xmlCtx, section, b'soundPressedNotReady')
        self.soundPressedCancel = _xml.readStringOrNone(xmlCtx, section, b'soundPressedCancel')
        scriptSection = section[b'script']
        if scriptSection:
            self.deploySeconds = _xml.readInt(xmlCtx, scriptSection, b'deploySeconds', minVal=0) if scriptSection.has_key(b'deploySeconds') else 0
            self.consumeSeconds = _xml.readInt(xmlCtx, scriptSection, b'consumeSeconds', minVal=0) if scriptSection.has_key(b'consumeSeconds') else 0
        return


class WTRepairkit(Repairkit):
    __slots__ = (b'soundPressedReady', b'soundPressedNotReady')

    def __init__(self):
        super(WTRepairkit, self).__init__()
        self.soundPressedReady = None
        self.soundPressedNotReady = None
        return

    def _readBasicConfig(self, xmlCtx, section):
        super(WTRepairkit, self)._readBasicConfig(xmlCtx, section)
        self.soundPressedReady = _xml.readStringOrNone(xmlCtx, section, b'soundPressedReady')
        self.soundPressedNotReady = _xml.readStringOrNone(xmlCtx, section, b'soundPressedNotReady')
        return
