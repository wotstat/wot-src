import logging
from gui.Scaleform.daapi import LobbySubView
from helpers import dependency
from skeletons.gui.game_control import IManualController
from skeletons.gui.lobby_context import ILobbyContext
from gui.sounds.filters import States, StatesGroup
from sound_gui_manager import CommonSoundSpaceSettings
_logger = logging.getLogger(__name__)

class ManualViewBase(LobbySubView):
    __background_alpha__ = 1
    lobbyContext = dependency.descriptor(ILobbyContext)
    manualController = dependency.descriptor(IManualController)
    SOUND_SPACE = b'manual'
    SOUND_STATE_PLACE = b'STATE_hangar_place'
    STATE_PLACE_MENU_GUIDE = b'STATE_hangar_place_menu_guide'
    BC_HANGAR_MUSIC_GUIDE_ENTER_SOUND_ID = b'bc_hangar_music_guide_enter'
    BC_HANGAR_MUSIC_GUIDE_EXIT_SOUND_ID = b'bc_hangar_music_guide_exit'
    _COMMON_SOUND_SPACE = CommonSoundSpaceSettings(name=SOUND_SPACE, entranceStates={SOUND_STATE_PLACE: STATE_PLACE_MENU_GUIDE, (StatesGroup.HANGAR_FILTERED): (States.HANGAR_FILTERED_OFF)}, exitStates={}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=BC_HANGAR_MUSIC_GUIDE_ENTER_SOUND_ID, exitEvent=BC_HANGAR_MUSIC_GUIDE_EXIT_SOUND_ID)

    def __init__(self, ctx=None):
        super(ManualViewBase, self).__init__()
        self._ctx = ctx
        self.lobbyContext.getServerSettings().onServerSettingsChange += self.__onServerSettingChanged
        self.chaptersUIData = self.manualController.getChaptersUIData()
        return

    def closeView(self):
        raise NotImplementedError
        return

    def _close(self):
        self.lobbyContext.getServerSettings().onServerSettingsChange -= self.__onServerSettingChanged
        self.destroy()
        return

    def __onServerSettingChanged(self, diff):
        if b'isManualEnabled' in diff:
            if not bool(diff[b'isManualEnabled']):
                self.closeView()
        if b'isBootcampEnabled' in diff:
            self.closeView()
        return
