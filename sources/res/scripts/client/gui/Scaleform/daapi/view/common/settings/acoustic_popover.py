from debug_utils import LOG_ERROR
from gui.Scaleform.daapi.view.common.settings import acoustic_presets
from gui.Scaleform.daapi.view.meta.AcousticPopoverMeta import AcousticPopoverMeta
from gui.Scaleform.genConsts.ACOUSTICS import ACOUSTICS
from gui.Scaleform.locale.SETTINGS import SETTINGS
from helpers.i18n import makeString

class AcousticPopover(AcousticPopoverMeta):

    def __init__(self, ctx=None):
        super(AcousticPopover, self).__init__(ctx)
        if ctx is None:
            raise UserWarning(b'Context is required')
        self.__acousticType = ctx.get(b'data', ACOUSTICS.TYPE_ACOUSTIC_20)
        self.__player = acoustic_presets.createPlayer(self, self.__acousticType)
        return

    def setEnabled(self, isEnabled):
        self.as_setEnableS(isEnabled)
        return

    def setItemsSelected(self, speakerIDs):
        self.as_onItemSelectS(speakerIDs)
        return

    def setItemsPlay(self, speakerIDs):
        self.as_onItemPlayS(speakerIDs)
        return

    def setPauseEnabled(self, isEnabled):
        self.as_updateBtnEnabledS(ACOUSTICS.ACTION_PAUSE, isEnabled)
        return

    def setPlayEnabled(self, isEnabled):
        self.as_updateBtnEnabledS(ACOUSTICS.ACTION_PLAY, isEnabled)
        return

    def onActionStart(self, actionID):
        if self.__player is not None:
            if actionID == ACOUSTICS.ACTION_PLAY:
                self.__player.play()
            elif actionID == ACOUSTICS.ACTION_PAUSE:
                self.__player.pause()
            elif actionID == ACOUSTICS.ACTION_REPEAT:
                self.__player.reset()
            else:
                LOG_ERROR(b'Action is not found', actionID)
        else:
            LOG_ERROR(b'Player is not created')
        return

    def onSpeakerClick(self, speakerID):
        if self.__player is not None:
            self.__player.click(speakerID)
        else:
            LOG_ERROR(b'Player is not created')
        return

    def _populate(self):
        super(AcousticPopover, self)._populate()
        self.as_setDataS({b'title': (b'%s %s' % (
                    makeString(SETTINGS.SOUNDS_ACOUSTICTYPE_POPOVER_TITLE),
                    makeString(SETTINGS.sounds_acoustictype((b'popover/{}').format(self.__acousticType))))), 
           b'sndType': (self.__acousticType)})
        if self.__player is not None:
            self.__player.setupInitState()
        return

    def as_disposeS(self):
        if self.__player is not None:
            self.__player.clear()
        super(AcousticPopover, self).as_disposeS()
        return
