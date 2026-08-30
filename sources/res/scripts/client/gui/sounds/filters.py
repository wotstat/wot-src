import WWISE
from gui.sounds.sound_constants import SoundFilters
from shared_utils import CONST_CONTAINER

class StatesGroup(CONST_CONTAINER):
    HANGAR_FILTERED = b'STATE_hangar_filtered'
    BOOTCAMP_ARENA_FILTERED = b'STATE_bootcamp_arena_filtered'
    HANGAR_PLACE_BATTLE_PASS = b'STATE_hangar_place_battle_pass'
    OVERLAY_HANGAR_GENERAL = b'STATE_overlay_hangar_general'
    VIDEO_OVERLAY = b'STATE_video_overlay'
    HANGAR_PLACE_TASKS = b'STATE_hangar_place_tasks'


_ON_PATTERN = b'{}_on'
_OFF_PATTERN = b'{}_off'

class States(CONST_CONTAINER):
    OVERLAY_HANGAR_GENERAL_ON = _ON_PATTERN.format(StatesGroup.OVERLAY_HANGAR_GENERAL)
    OVERLAY_HANGAR_GENERAL_OFF = _OFF_PATTERN.format(StatesGroup.OVERLAY_HANGAR_GENERAL)
    HANGAR_FILTERED_ON = _ON_PATTERN.format(StatesGroup.HANGAR_FILTERED)
    HANGAR_FILTERED_OFF = _OFF_PATTERN.format(StatesGroup.HANGAR_FILTERED)
    VIDEO_OVERLAY_ON = _ON_PATTERN.format(StatesGroup.VIDEO_OVERLAY)
    VIDEO_OVERLAY_OFF = _OFF_PATTERN.format(StatesGroup.VIDEO_OVERLAY)
    HANGAR_PLACE_TASKS_DAILY = b'STATE_hangar_place_tasks_daily'
    HANGAR_PLACE_TASKS_MISSIONS = b'STATE_hangar_place_tasks_missions'
    HANGAR_PLACE_TASKS_BATTLE_PASS = b'STATE_hangar_place_tasks_battle_pass'
    HANGAR_PLACE_TASKS_EVENTS = b'STATE_hangar_place_tasks_events'
    HANGAR_PLACE_TASKS_BATTLE_MATTERS = b'STATE_hangar_place_tasks_battle_matters'


class Events(CONST_CONTAINER):
    BOB_ENTER = b'gui_bb_bloggers_progress_page_ambient_Entrance'
    BOB_EXIT = b'gui_bb_bloggers_progress_page_ambient_Exit'
    MARATHON_ENTER = b'ev_hangar_marathon_enter'
    MARATHON_EXIT = b'ev_hangar_marathon_exit'
    BATTLE_MATTERS_ENTER = b'bm_enter'
    BATTLE_MATTERS_EXIT = b'bm_exit'


def switchHangarFilteredFilter(on=True):
    _setState(StatesGroup.HANGAR_FILTERED, States.HANGAR_FILTERED_ON if on else States.HANGAR_FILTERED_OFF)
    return


def switchHangarOverlaySoundFilter(on=True):
    _switchOverlaySoundFilter(StatesGroup.OVERLAY_HANGAR_GENERAL, States.OVERLAY_HANGAR_GENERAL_ON, States.OVERLAY_HANGAR_GENERAL_OFF, on)
    return


def switchVideoOverlaySoundFilter(on=True):
    _switchOverlaySoundFilter(StatesGroup.VIDEO_OVERLAY, States.VIDEO_OVERLAY_ON, States.VIDEO_OVERLAY_OFF, on)
    return


class _StateKeeper(object):
    __stateHoldersCounts = {}

    @classmethod
    def checkinHolder(cls, stateName):
        prevCount = cls.__stateHoldersCounts.get(stateName, 0)
        cls.__stateHoldersCounts[stateName] = prevCount + 1
        return prevCount

    @classmethod
    def checkoutHolder(cls, stateName):
        count = cls.__stateHoldersCounts.get(stateName, 0)
        if count > 0:
            count -= 1
        cls.__stateHoldersCounts[stateName] = count
        return count


class _SoundFilterAbstract(object):

    def start(self):
        return

    def stop(self):
        return

    def stopView(self, view):
        return


class EmptySoundFilter(_SoundFilterAbstract):

    def __repr__(self):
        return b'EmptyFilter'


class _WWISEStateAmbient(_SoundFilterAbstract):

    def __init__(self, stateID):
        self._stateID = stateID
        return

    def start(self):
        startState = self._getStartState()
        if startState:
            _setState(self._stateID, startState)
        return

    def stop(self):
        stopState = self._getStopState()
        if stopState:
            _setState(self._stateID, stopState)
        return

    def _getStartState(self):
        return b'%s_on' % self._stateID

    def _getStopState(self):
        return b'%s_off' % self._stateID

    def __repr__(self):
        return b'WWISE(%s)' % self._stateID


class WWISEFilteredHangarFilter(_WWISEStateAmbient):

    def __init__(self):
        _WWISEStateAmbient.__init__(self, StatesGroup.HANGAR_FILTERED)
        return

    def stopView(self, view):
        view.soundManager.clear(stopPersistent=True)
        return


class WWISEHangarOverlayFilter(_WWISEStateAmbient):

    def __init__(self):
        _WWISEStateAmbient.__init__(self, StatesGroup.OVERLAY_HANGAR_GENERAL)
        return


class WWISEFilteredBootcampArenaFilter(_WWISEStateAmbient):

    def __init__(self):
        _WWISEStateAmbient.__init__(self, StatesGroup.BOOTCAMP_ARENA_FILTERED)
        return


class WWISEBattlePassFilter(_WWISEStateAmbient):

    def __init__(self):
        super(WWISEBattlePassFilter, self).__init__(StatesGroup.HANGAR_PLACE_BATTLE_PASS)
        return


class WWISEHangarTasksFilter(_WWISEStateAmbient):

    def __init__(self):
        _WWISEStateAmbient.__init__(self, StatesGroup.HANGAR_PLACE_TASKS)
        return

    def _getStopState(self):
        return b''


class WWISEHangarTasksBPFilter(WWISEHangarTasksFilter):

    def _getStartState(self):
        return States.HANGAR_PLACE_TASKS_BATTLE_PASS


class WWISEHangarTasksDailyFilter(WWISEHangarTasksFilter):

    def _getStartState(self):
        return States.HANGAR_PLACE_TASKS_DAILY


class WWISEHangarTasksMissionsFilter(WWISEHangarTasksFilter):

    def _getStartState(self):
        return States.HANGAR_PLACE_TASKS_MISSIONS


class WWISEMarathonPageFilter(WWISEHangarTasksFilter):

    def start(self):
        super(WWISEMarathonPageFilter, self).start()
        WWISE.WW_eventGlobal(Events.MARATHON_ENTER)
        return

    def stop(self):
        super(WWISEMarathonPageFilter, self).stop()
        WWISE.WW_eventGlobal(Events.MARATHON_EXIT)
        return

    def _getStartState(self):
        return States.HANGAR_PLACE_TASKS_EVENTS


class WWISEEventPageFilter(WWISEHangarTasksFilter):

    def _getStartState(self):
        return States.HANGAR_PLACE_TASKS_EVENTS


class WWISEBattleMattersFilter(WWISEHangarTasksFilter):

    def _getStartState(self):
        return States.HANGAR_PLACE_TASKS_BATTLE_MATTERS


def getEmptyFilter():
    return EmptySoundFilter()


def get(filterID):
    if filterID in _filters:
        return _filters[filterID]
    return EmptySoundFilter()


def _selectFilter(wwise):
    if WWISE.enabled:
        return wwise
    return EmptySoundFilter()


_filters = {(SoundFilters.FILTERED_HANGAR): (_selectFilter(WWISEFilteredHangarFilter())), 
   (SoundFilters.BATTLE_PASS_FILTER): (_selectFilter(WWISEBattlePassFilter())), 
   (SoundFilters.HANGAR_OVERLAY): (_selectFilter(WWISEHangarOverlayFilter())), 
   (SoundFilters.HANGAR_PLACE_TASKS_DAILY): (_selectFilter(WWISEHangarTasksDailyFilter())), 
   (SoundFilters.HANGAR_PLACE_TASKS_MISSIONS): (_selectFilter(WWISEHangarTasksMissionsFilter())), 
   (SoundFilters.HANGAR_PLACE_TASKS_BATTLE_PASS): (_selectFilter(WWISEHangarTasksBPFilter())), 
   (SoundFilters.HANGAR_PLACE_TASKS_EVENTS): (_selectFilter(WWISEEventPageFilter())), 
   (SoundFilters.HANGAR_PLACE_TASKS_BATTLE_MATTERS): (_selectFilter(WWISEBattleMattersFilter()))}

def _setState(stateGroup, stateName):
    WWISE.WW_setState(stateGroup, stateName)
    return


def _switchOverlaySoundFilter(group, stateOn, stateOff, on=True):
    if on:
        prevHolders = _StateKeeper.checkinHolder(group)
        if not prevHolders:
            _setState(group, stateOn)
    else:
        currHolders = _StateKeeper.checkoutHolder(group)
        if not currHolders:
            _setState(group, stateOff)
    return
