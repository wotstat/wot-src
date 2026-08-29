import SoundGroups
from gui.impl.lobby.video.video_sound_manager import IVideoSoundManager, SoundManagerStates

class VideoRewardsSoundControl(IVideoSoundManager):
    __slots__ = (b'__state',)
    LOOTBOXES_REWARD_VIDEO_START = b'lootboxes_video_start'
    LOOTBOXES_REWARD_VIDEO_STOP = b'lootboxes_video_stop'
    LOOTBOXES_REWARD_VIDEO_PAUSE = b'lootboxes_video_pause'
    LOOTBOXES_REWARD_VIDEO_RESUME = b'lootboxes_video_resume'
    RTPC_VOLUME_CONTROL = b'RTPC_ext_video_volume'

    def __init__(self):
        self.__state = None
        return

    def start(self):
        self.setVolume()
        SoundGroups.g_instance.playSound2D(self.LOOTBOXES_REWARD_VIDEO_START)
        self.__state = SoundManagerStates.PLAYING
        return

    def stop(self):
        if self.__state != SoundManagerStates.STOPPED:
            SoundGroups.g_instance.playSound2D(self.LOOTBOXES_REWARD_VIDEO_STOP)
            self.__state = SoundManagerStates.STOPPED
        return

    def pause(self):
        SoundGroups.g_instance.playSound2D(self.LOOTBOXES_REWARD_VIDEO_PAUSE)
        self.__state = SoundManagerStates.PAUSE
        return

    def unpause(self):
        SoundGroups.g_instance.playSound2D(self.LOOTBOXES_REWARD_VIDEO_RESUME)
        self.__state = SoundManagerStates.PLAYING
        return

    def setVolume(self):
        maxVolumeCategoryName = SoundGroups.g_instance.getMaxVolumeFromCategories(SoundGroups.USER_SETTINGS_CATEGORY_NAMES)
        SoundGroups.g_instance.setRTPC(self.RTPC_VOLUME_CONTROL, maxVolumeCategoryName)
        return
