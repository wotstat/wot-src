import WWISE
from shared_utils import CONST_CONTAINER

class MarathonVideos(CONST_CONTAINER):
    VEHICLE = 1


def playSound(eventName):
    if eventName:
        WWISE.WW_eventGlobal(eventName)
    return


def onVideoStart(videoId, sourceID=b''):
    eventName = _MarathonVideoEvents.VIDEO_START.get(videoId)
    if eventName is not None:
        if videoId in (MarathonVideos.VEHICLE,):
            eventName = eventName.format(sourceID.replace(b'-', b'_'))
        WWISE.WW_eventGlobal(eventName)
        WWISE.WW_setState(_MarathonVideoStates.GROUP, _MarathonVideoStates.START)
    return


def onVideoDone():
    WWISE.WW_eventGlobal(_MarathonVideoEvents.VIDEO_DONE)
    WWISE.WW_setState(_MarathonVideoStates.GROUP, _MarathonVideoStates.DONE)
    return


class _MarathonVideoEvents(CONST_CONTAINER):
    VIDEO_START = {(MarathonVideos.VEHICLE): b'gui_marathon_video_tank_{}'}
    VIDEO_DONE = b'gui_marathon_video_stop'


class _MarathonVideoStates(CONST_CONTAINER):
    GROUP = b'STATE_video_overlay'
    START = b'STATE_video_overlay_on'
    DONE = b'STATE_video_overlay_off'
