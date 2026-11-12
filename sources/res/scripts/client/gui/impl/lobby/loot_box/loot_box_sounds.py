import logging, Windowing, SoundGroups
from gui.impl.lobby.video.video_sound_manager import IVideoSoundManager
from shared_utils import CONST_CONTAINER
from sound_gui_manager import CommonSoundSpaceSettings
_logger = logging.getLogger(__name__)

class LootBoxViewEvents(CONST_CONTAINER):
    ENTRY_VIEW_ENTER = b'gui_lootbox_logistic_center_ambience_on'
    ENTRY_VIEW_EXIT = b'gui_lootbox_logistic_center_ambience_off'
    BENGAL_FIRE_OFF = b'gui_lootbox_logistic_center_bengal_fire_off'
    LOGISTIC_CENTER_SWITCH = b'gui_lootbox_logistic_center_switch'
    LOGISTIC_CENTER_NEXT = b'gui_lootbox_logistic_center_boxes_next'
    PREMIUM_MULTI_ENTER = b'gui_lootbox_reward_5_lootboxes'


class LootBoxSoundStates(CONST_CONTAINER):
    COMMON_SOUND_SPACE = b'LootBoxes'
    STATE_PLACE = b'STATE_hangar_place'
    STATE_PLACE_LOOTBOXES = b'STATE_hangar_place_lootboxes'
    STATE_PLACE_GARAGE = b'STATE_hangar_place_garage'


def playSound(eventName):
    if eventName:
        SoundGroups.g_instance.playSound2D(eventName)
    return


class LootBoxVideos(CONST_CONTAINER):
    DELIVERY = 0
    VEHICLE = 1
    STYLE = 2
    OPEN_BOX = 3


class LootBoxVideosSpecialRewardType(CONST_CONTAINER):
    GIFT = b'gift'
    COMMON = b'common'


class LootBoxVideoStartStopHandler(object):
    __slots__ = (b'__started', b'__checkPauseOnStart')

    def __init__(self, checkPauseOnStart=True):
        self.__checkPauseOnStart = checkPauseOnStart
        self.__started = False
        return

    @staticmethod
    def setVideoState(isOn):
        SoundGroups.g_instance.setState(_LootBoxVideoStates.GROUP, _LootBoxVideoStates.START if isOn else _LootBoxVideoStates.DONE)
        return

    def setIsNeedPause(self, isNeedPause):
        if not self.__started:
            return
        if isNeedPause:
            playSound(LootBoxVideoEvents.VIDEO_PAUSE)
        else:
            playSound(LootBoxVideoEvents.VIDEO_RESUME)
        return

    def onVideoStart(self, videoId, sourceID=b''):
        eventName = self.getEventName(videoId, sourceID)
        if eventName is not None:
            SoundGroups.g_instance.playSound2D(eventName)
            SoundGroups.g_instance.setState(_LootBoxVideoStates.GROUP, _LootBoxVideoStates.START)
            self.__started = True
            if self.__checkPauseOnStart and not Windowing.isWindowAccessible():
                playSound(LootBoxVideoEvents.VIDEO_PAUSE)
        return

    def getEventName(self, videoId, sourceID=b''):
        eventName = LootBoxVideoEvents.VIDEO_START.get(videoId)
        if eventName is not None:
            if videoId in (LootBoxVideos.VEHICLE, LootBoxVideos.STYLE):
                eventName = eventName.format(sourceID.replace(b'-', b'_'))
            elif videoId == LootBoxVideos.OPEN_BOX:
                eventName = eventName.format(sourceID)
        return eventName

    def onVideoDone(self):
        if self.__started:
            SoundGroups.g_instance.playSound2D(LootBoxVideoEvents.VIDEO_DONE)
            SoundGroups.g_instance.setState(_LootBoxVideoStates.GROUP, _LootBoxVideoStates.DONE)
            self.__started = False
        return


class PausedSoundManager(IVideoSoundManager):
    __slots__ = (b'__isPausable', b'__isOnPause')

    def __init__(self):
        self.__isPausable = self.__isOnPause = False
        return

    def start(self):
        self.__isPausable = True
        return

    def stop(self):
        self.__isPausable = False
        return

    def pause(self):
        if self.__isPausable and not self.__isOnPause:
            playSound(LootBoxVideoEvents.VIDEO_PAUSE)
            self.__isOnPause = True
        return

    def unpause(self):
        if self.__isPausable and self.__isOnPause:
            playSound(LootBoxVideoEvents.VIDEO_RESUME)
            self.__isOnPause = False
        return


class LootBoxVideoEvents(CONST_CONTAINER):
    VIDEO_START = {(LootBoxVideos.DELIVERY): b'gui_video_ny_delivery_lootbox', 
       (LootBoxVideos.VEHICLE): b'gui_lootbox_video_tank_{}', 
       (LootBoxVideos.STYLE): b'gui_lootbox_video_3dstyle_{}', 
       (LootBoxVideos.OPEN_BOX): b'gui_lootbox_video_open_lootbox_{}'}
    VIDEO_DONE = b'gui_lootbox_video_stop'
    VIDEO_PAUSE = b'gui_lootbox_video_pause'
    VIDEO_RESUME = b'gui_lootbox_video_resume'


class _LootBoxVideoStates(CONST_CONTAINER):
    GROUP = b'STATE_video_overlay'
    START = b'STATE_video_overlay_on'
    DONE = b'STATE_video_overlay_off'


LOOTBOXES_SOUND_SPACE = CommonSoundSpaceSettings(name=LootBoxSoundStates.COMMON_SOUND_SPACE, entranceStates={(LootBoxSoundStates.STATE_PLACE): (LootBoxSoundStates.STATE_PLACE_LOOTBOXES)}, exitStates={(LootBoxSoundStates.STATE_PLACE): (LootBoxSoundStates.STATE_PLACE_GARAGE)}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=LootBoxViewEvents.ENTRY_VIEW_ENTER, exitEvent=LootBoxViewEvents.ENTRY_VIEW_EXIT)
