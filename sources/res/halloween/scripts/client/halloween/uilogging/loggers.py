from __future__ import absolute_import
import logging
from typing import TYPE_CHECKING
from halloween.gui.sounds.halloween_sound_controller import getEventVoiceoverLanguage
from halloween.gui.sounds.sound_constants import SoundLanguage
from halloween.uilogging.logging_constants import FEATURE, HWLogActions, HWLogKeys, MIN_VO_TIME
from uilogging.base.logger import MetricsLogger, createPartnerID
if TYPE_CHECKING:
    pass
_logger = logging.getLogger(__name__)

class HWMetricsLogger(MetricsLogger):
    __slots__ = (b'_view', b'_partnerID')

    def __init__(self, view, partnerID=None):
        super(HWMetricsLogger, self).__init__(FEATURE)
        self._view = view
        self._partnerID = partnerID
        return

    def onStartView(self, action):
        self.startAction(action=action)
        return

    def onStopView(self, action, itemState=None, info=None, timeLimit=0):
        self.stopAction(action=action, item=self._view, partnerID=self._partnerID, timeLimit=timeLimit, itemState=itemState, info=info)
        return

    def onLog(self, action, item, itemState=None):
        self.log(action=action, item=item, parentScreen=self._view, itemState=itemState)
        return

    def onClick(self, item, itemState=None):
        self.onLog(HWLogActions.CLICK, item, itemState)
        return


VO_MAP = {(SoundLanguage.VOICEOVER_UA): b'UA', 
   (SoundLanguage.VOICEOVER_EN): b'EN', 
   (SoundLanguage.VOICEOVER_CN): b'CN', 
   (SoundLanguage.VOICEOVER_RU): b'RU'}

class DecryptionMetricsLogger(HWMetricsLogger):
    __slots__ = (b'_voLang',)

    def __init__(self):
        super(DecryptionMetricsLogger, self).__init__(HWLogKeys.DECRYPT_VIEW, createPartnerID())
        self._voLang = VO_MAP.get(getEventVoiceoverLanguage(), b'')
        return

    def onStartView(self, *_):
        super(DecryptionMetricsLogger, self).onStartView(HWLogActions.LIFETIME)
        return

    def onStopView(self, itemState=None, stopVO=False, *_):
        if stopVO:
            self.stopVO(itemState)
        super(DecryptionMetricsLogger, self).onStopView(HWLogActions.LIFETIME, itemState, self._voLang)
        return

    def startVO(self):
        self.startAction(HWLogActions.VO_LISTENED)
        return

    def stopVO(self, itemState):
        self.stopAction(action=HWLogActions.VO_LISTENED, item=self._view, partnerID=self._partnerID, timeLimit=MIN_VO_TIME, itemState=itemState, info=self._voLang)
        return
