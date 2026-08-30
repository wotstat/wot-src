import logging
from debug_utils import LOG_ERROR, LOG_CURRENT_EXCEPTION
from gui.Scaleform.framework.entities.abstract.SoundManagerMeta import SoundManagerMeta
from gui.doc_loaders.GuiSoundsLoader import GuiSoundsLoader
import SoundGroups
_logger = logging.getLogger(__name__)

class SoundManager(SoundManagerMeta):

    def __init__(self):
        super(SoundManager, self).__init__()
        self.sounds = GuiSoundsLoader()
        return

    def _populate(self):
        super(SoundManager, self)._populate()
        try:
            self.sounds.load()
        except Exception:
            LOG_ERROR(b'There is error while loading sounds xml data')
            LOG_CURRENT_EXCEPTION()

        return

    def soundEventHandler(self, soundsTypeSection, state, eventType, eventID):
        self.playControlSound(state, eventType, eventID)
        return

    def playControlSound(self, state, eventType, eventID):
        sound, soundBankName = self.sounds.getControlSound(eventType, state, eventID)
        if sound is not None:
            SoundGroups.g_instance.playSound2D(sound, soundBankName)
        return

    def playEffectSound(self, effectName):
        sound = self.sounds.getEffectSound(effectName)
        if sound is not None:
            SoundGroups.g_instance.playSound2D(sound)
        else:
            _logger.warning(b'Sound effect "%s" not found', effectName)
        return
