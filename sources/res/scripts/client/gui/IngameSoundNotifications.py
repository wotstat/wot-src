from __future__ import absolute_import
from collections import namedtuple
from random import randrange
from functools import partial
from future.utils import viewitems
import Math, BigWorld, ResMgr, BattleReplay, Event, SoundGroups, VSE, WWISE
from debug_utils import LOG_WARNING, LOG_DEBUG, LOG_ERROR
from helpers import isPlayerAvatar
from account_helpers import AccountSettings
from account_helpers.settings_core.settings_constants import SOUND
from helpers.CallbackDelayer import CallbackDelayer, TimeDeltaMeter
import importlib
_ENABLE_VO_LOGS = False
_SUBTITLE_PREFIX = b'#'
_SUBTITLES_END_MARKER = b'#end'

def LOG_VO(msg, *kargs, **kwargs):
    if _ENABLE_VO_LOGS:
        LOG_DEBUG((b'[SOUND][VO] {}').format(msg), *kargs, **kwargs)
    return


class IngameSoundNotifications(CallbackDelayer, TimeDeltaMeter):
    __EVENTS_PATH = b'gui/sound_notifications.xml'
    __CIRCUMSTANCES_PATH = b'gui/sound_circumstances.xml'
    __DEFAULT_LIFETIME = 3.0
    __TICK_DELAY = 0.5
    QueueItem = namedtuple(b'QueueItem', (b'eventName', b'priority', b'time', b'vehicleID', b'checkFn', b'position', b'boundVehicleID'))
    PlayingEvent = namedtuple(b'PlayingEvent', (b'eventName', b'vehicle', b'position', b'boundVehicle', b'is2D'))

    def __init__(self, arenaType):
        CallbackDelayer.__init__(self)
        TimeDeltaMeter.__init__(self)
        self.__isEnabled = False
        self.__enabledSoundCategories = set()
        self.__remappedNotifications = {}
        self.__events = {}
        self.__eventsPriorities = {}
        self.__eventsCooldowns = {}
        self.__fxCooldowns = {}
        self.__circumstances = {}
        self.__circumstancesWeights = {}
        self.__circumstancesGroupsWeights = {}
        self.__playingEvents = {}
        self.__queues = {}
        self._currentSubtitle = b''
        self.onPlayEvent = Event.Event()
        self.onAddEvent = Event.Event()
        self.onSubtitleShow = Event.Event()
        self.onSubtitleHide = Event.Event()
        planPath = arenaType.soundNotificationsPlan
        planContextPath = arenaType.soundNotificationsContext
        self.__vseContextClass = self.__importVSEContextClass(planContextPath)
        self.__readConfigs()
        self._vsePlan = VSE.Plan()
        self._vsePlan.load(planPath, b'', b'CLIENT')
        self.__soundNotificationsContext = None
        self.__delayedCallbacks = set()
        return

    def start(self):
        self.__enabledSoundCategories = set((b'fx', b'voice'))
        self.__isEnabled = True
        self.__soundNotificationsContext = self.__vseContextClass()
        WWISE.WW_addMarkerListener(self._soundMarkerHandler)
        self._vsePlan.setContext(self.__soundNotificationsContext)
        self._vsePlan.start()
        self.measureDeltaTime()
        self.delayCallback(self.__TICK_DELAY, self.__tick)
        BattleReplay.g_replayEvents.onTimeWarpStart += self.__onTimeWarpStart
        return

    def __onTimeWarpStart(self):
        self.__resetDelayedCallbacks()
        return

    def __resetDelayedCallbacks(self):
        for delayedCallbackID in self.__delayedCallbacks:
            BigWorld.cancelCallback(delayedCallbackID)

        self.__delayedCallbacks.clear()
        return

    def destroy(self):
        CallbackDelayer.destroy(self)
        self.__isEnabled = False
        self._vsePlan.stop()
        self._vsePlan = None
        WWISE.WW_removeMarkerListener(self._soundMarkerHandler)
        if self.__soundNotificationsContext is not None:
            self.__soundNotificationsContext.destroy()
            self.__soundNotificationsContext = None
        self.clear()
        self.__eventsPriorities = {}
        self.__eventsCooldowns = {}
        self.__fxCooldowns = {}
        self.__circumstancesWeights = {}
        self.__circumstancesGroupsWeights = {}
        self.__remappedNotifications = {}
        self.__resetDelayedCallbacks()
        BattleReplay.g_replayEvents.onTimeWarpStart -= self.__onTimeWarpStart
        return

    def isPlaying(self, eventName):
        for event in self.__playingEvents.values():
            if event and event.eventName == eventName:
                return True

        return False

    def setRemapping(self, remap):
        self.__remappedNotifications = remap
        return

    def play(self, vo, vehicleID=None, checkFn=None, position=None, boundVehicleID=None):
        LOG_VO((b'Request: "{}"').format(vo))
        if self.__checkPause():
            LOG_VO((b'Request "{}" is rejected. Reason: {}').format(vo, b'pause'))
            return
        else:
            eventName = self.__remappedNotifications.get(vo, vo)
            if eventName is None:
                LOG_VO((b'Request "{}" is rejected. Reason: {}').format(vo, b'remapping with empty'))
                return
            if vo in self.__remappedNotifications:
                LOG_VO((b'"{}" is overrode with "{}"').format(vo, eventName))
            event = self.__events.get(eventName, None)
            if event is None:
                LOG_WARNING(b"Couldn't find %s event" % eventName)
                LOG_VO((b'Request "{}" is rejected. Reason: {}').format(eventName, b'missed in sound_notifications.xml'))
                return
            if b'chance' in event and randrange(1, 100) > int(event[b'chance']):
                LOG_VO((b'Request "{}" is rejected. Reason: {}').format(eventName, b'chance'))
                return
            self.__playFX(eventName, vehicleID, position)
            isQueueSpecified = b'queue' not in event
            if isQueueSpecified or not self.isCategoryEnabled(b'voice'):
                if b'fxEvent' not in event:
                    LOG_VO((b'Request "{}" is rejected. Reason: {}').format(vo, b'queue is not specified' if isQueueSpecified else b'voices are disabled'))
                return
            predelay = float(event[b'predelay']) if b'predelay' in event else 0
            callbackIDHolder = []
            callbackID = BigWorld.callback(predelay, partial(self.__playDelayed, eventName, vehicleID, checkFn, position, boundVehicleID, callbackIDHolder))
            callbackIDHolder.append(callbackID)
            self.__delayedCallbacks.add(callbackID)
            return

    @staticmethod
    def __importVSEContextClass(contextPath):
        classPathParts = contextPath.split(b'.')
        class_name = classPathParts[-1]
        python_module_path = (b'.').join(classPathParts[:-1])
        try:
            python_module = importlib.import_module(python_module_path)
        except ImportError:
            LOG_ERROR(b'Failed to load Module ', contextPath)
            raise

        return getattr(python_module, class_name)

    def __playDelayed(self, eventName, vehicleID=None, checkFn=None, position=None, boundVehicleID=None, callbackIDHolder=None):
        self.__delayedCallbacks.discard(callbackIDHolder[0])
        event = self.__events.get(eventName, None)
        queueNum = int(event[b'queue'])
        priority = int(self.getEventInfo(eventName, b'priority'))
        queueItem = self.QueueItem(eventName, priority, BigWorld.time(), vehicleID, checkFn, position, boundVehicleID)
        index = 0
        for item in self.__queues[queueNum]:
            if item.priority < queueItem.priority:
                break
            index += 1

        self.__queues[queueNum].insert(index, queueItem)
        LOG_VO((b'Event "{}" added to queue "{}". {}').format(eventName, queueNum, [item.eventName for item in self.__queues[queueNum]]))
        if not self.__playingEvents[queueNum]:
            self.__playFirstFromQueue(queueNum)
        else:
            LOG_VO((b'"{}" is playing now').format(self.__playingEvents[queueNum].eventName))
            self.onAddEvent(eventName)
        return

    def __playFX(self, eventName, vehicleID, position):
        event = self.__events.get(eventName, {})
        isFX = b'fxEvent' in event
        if eventName in self.__fxCooldowns and self.__fxCooldowns[eventName]:
            if isFX:
                LOG_VO((b'Request "{}" is rejected. Reason: {}').format(eventName, b'FX cooldown'))
            return
        if not isFX or not self.isCategoryEnabled(b'fx'):
            if isFX:
                LOG_VO((b'Request "{}" is rejected. Reason: {}').format(eventName, b'FX sounds are disabled'))
            return
        if b'cooldownFx' in event and float(event[b'cooldownFx']) > 0:
            self.__fxCooldowns[eventName] = {b'time': (float(event[b'cooldownFx']))}
        fxEvent = event[b'fxEvent']
        LOG_VO((b'Play fx  "{}". fxEvent: "{}"').format(eventName, fxEvent))
        if vehicleID is not None:
            vehicle = BigWorld.entity(vehicleID)
            if vehicle:
                SoundGroups.g_instance.playSoundPos(fxEvent, vehicle.position)
        elif position is not None:
            SoundGroups.g_instance.playSoundPos(fxEvent, position)
        else:
            SoundGroups.g_instance.playSound2D(fxEvent)
        return

    def playNextQueueEvent(self, queueNum):
        if self.__checkPause():
            return
        else:
            self.__playingEvents[queueNum] = None
            self.__playFirstFromQueue(queueNum)
            return

    def replayLastQueueEvent(self, queueNum):
        if self.__checkPause():
            return
        if self.__playingEvents[queueNum]:
            self.onPlayEvent(self.__playingEvents[queueNum].eventName)
        return

    def getFirstQueueEvent(self, queueNum):
        if self.__queues[queueNum]:
            return self.__queues[queueNum][0].eventName
        return b''

    def clear(self):
        for queueNum, queue in viewitems(self.__queues):
            LOG_VO((b'Clear queue "{}". Removed events: {}').format(queueNum, [eventItem.eventName for eventItem in queue]))
            self.__queues[queueNum] = []

        for queueNum in self.__playingEvents:
            self.__playingEvents[queueNum] = None

        return

    def clearQueue(self, queueNum):
        LOG_VO((b'Clear queue "{}". Removed events: {}').format(queueNum, [eventItem.eventName for eventItem in self.__queues[queueNum]]))
        self.__queues[queueNum] = []
        return

    def enableFX(self, isEnabled):
        LOG_VO((b'fx sounds are {}').format(b'enabled' if isEnabled else b'disabled'))
        if isEnabled:
            self.__enabledSoundCategories.add(b'fx')
        else:
            self.__enabledSoundCategories.remove(b'fx')
        return

    def enableVoices(self, isEnabled, clearQueues=True):
        LOG_VO((b'voice sounds are {}').format(b'enabled' if isEnabled else b'disabled'))
        if isEnabled:
            self.__enabledSoundCategories.add(b'voice')
        else:
            self.__enabledSoundCategories.remove(b'voice')
            if clearQueues:
                self.clear()
        return

    def isCategoryEnabled(self, category):
        if category in self.__enabledSoundCategories:
            return True
        return False

    def getEventInfo(self, eventName, parameter):
        if parameter == b'priority' and eventName in self.__eventsPriorities and self.__eventsPriorities[eventName]:
            return self.__eventsPriorities[eventName][b'priority']
        if eventName in self.__events and parameter in self.__events[eventName]:
            return self.__events[eventName][parameter]
        return b''

    def getPlayingEventData(self, queueNum, parameter):
        playingEvent = self.__playingEvents[queueNum]
        if playingEvent and hasattr(playingEvent, parameter):
            return getattr(playingEvent, parameter)
        else:
            return

    def getCircumstanceInfo(self, circIndex, parameter):
        if parameter == b'weight':
            if circIndex in self.__circumstancesWeights and self.__circumstancesWeights[circIndex]:
                return self.__circumstancesWeights[circIndex][b'weight']
            if circIndex in self.__circumstances and b'group' in self.__circumstances[circIndex]:
                groupName = self.__circumstances[circIndex][b'group']
                if groupName in self.__circumstancesGroupsWeights and self.__circumstancesGroupsWeights[groupName]:
                    return self.__circumstancesGroupsWeights[groupName][b'weight']
        if circIndex in self.__circumstances and parameter in self.__circumstances[circIndex]:
            return self.__circumstances[circIndex][parameter]
        return b''

    def getCircumstanceIndex(self, circGroup, circName):
        for circ in self.__circumstances.values():
            if b'index' in circ and circ.get(b'group') == circGroup and circ.get(b'name') == circName:
                return circ[b'index']

        return b''

    def setEventCooldown(self, eventName, cooldown):
        if eventName in self.__events:
            self.__eventsCooldowns[eventName] = {b'time': cooldown}
        return

    def setEventPriority(self, eventName, priority, hold):
        if eventName in self.__events:
            self.__eventsPriorities[eventName] = {b'priority': priority, b'time': hold}
        return

    def setCircumstanceWeight(self, circIndex, weight, hold):
        if circIndex in self.__circumstances:
            self.__circumstancesWeights[circIndex] = {b'weight': weight, b'time': hold}
        return

    def setCircumstanceGroupWeight(self, groupName, weight, hold):
        self.__circumstancesGroupsWeights[groupName] = {b'weight': weight, b'time': hold}
        return

    def onNotificationBegins(self, eventName):
        LOG_VO((b'Play voice "{}"').format(eventName))
        self._hideSubtitle()
        return

    def log(self, msg):
        LOG_VO(msg)
        return

    def __checkPause(self):
        shouldPause = False
        if not self.__isEnabled or BigWorld.isWindowVisible() is False:
            shouldPause = True
        replayCtrl = BattleReplay.g_replayCtrl
        if replayCtrl.isPlaying:
            if replayCtrl.isTimeWarpInProgress or replayCtrl.isPaused:
                shouldPause = True
        if shouldPause:
            self.clear()
        return shouldPause

    def __playFirstFromQueue(self, queueNum):
        if not self.__queues[queueNum]:
            self.__playingEvents[queueNum] = None
            return
        else:
            queueItem = self.__queues[queueNum][0]
            del self.__queues[queueNum][0]
            checkCooldown = queueItem.eventName not in self.__eventsCooldowns or not self.__eventsCooldowns[queueItem.eventName]
            checkVehicle = queueItem.vehicleID is None or BigWorld.entity(queueItem.vehicleID) is not None
            checkFunction = queueItem.checkFn() if isPlayerAvatar() and queueItem.checkFn else True
            if checkFunction and checkVehicle and checkCooldown:
                LOG_VO((b'Try to play voice "{}". infEvent: "{}"').format(queueItem.eventName, self.__events[queueItem.eventName].get(b'infEvent')))
                vehicle = BigWorld.entity(queueItem.vehicleID) if queueItem.vehicleID is not None else None
                boundVehicle = BigWorld.entity(queueItem.boundVehicleID) if queueItem.boundVehicleID is not None else None
                position = vehicle.position if vehicle else queueItem.position
                self.__playingEvents[queueNum] = self.PlayingEvent(queueItem.eventName, vehicle, position, boundVehicle, position is None)
                self.onPlayEvent(queueItem.eventName)
            else:
                skipReason = b'cooldown' if checkCooldown else b"vehicle doesn't found" if checkVehicle else b'external'
                LOG_VO((b'Skip "{}". Reason: {}').format(queueItem.eventName, skipReason))
                self.__playFirstFromQueue(queueNum)
            return

    def __readConfigs(self):
        eventsSec = ResMgr.openSection(self.__EVENTS_PATH)
        self.__events = {}
        for eventSec in eventsSec.values():
            eventName = eventSec.readString(b'name')
            self.__events[eventName] = {}
            for infoSec in eventSec.values():
                self.__events[eventName][infoSec.name] = infoSec.asString
                if infoSec.name == b'queue' and infoSec.asInt not in self.__queues:
                    self.__queues[infoSec.asInt] = []
                    self.__playingEvents[infoSec.asInt] = None

        circsSec = ResMgr.openSection(self.__CIRCUMSTANCES_PATH)
        self.__circumstances = {}
        for circSec in circsSec.values():
            index = circSec.readString(b'index')
            self.__circumstances[index] = {}
            for infoSec in circSec.values():
                self.__circumstances[index][infoSec.name] = infoSec.asWideString

        return

    def __tick(self):
        delta = self.measureDeltaTime()
        self.__tickGroup(self.__eventsCooldowns, delta)
        self.__tickGroup(self.__fxCooldowns, delta)
        self.__tickGroup(self.__eventsPriorities, delta)
        self.__tickGroup(self.__circumstancesWeights, delta)
        self.__tickGroup(self.__circumstancesGroupsWeights, delta)
        for queueNum in self.__queues:
            self.__queues[queueNum] = [item for item in self.__queues[queueNum] if self.__checkLifetime(item)]

        if not BigWorld.isWindowVisible():
            self._hideSubtitle()
        return self.__TICK_DELAY

    def __checkLifetime(self, queueItem):
        event = self.__events[queueItem.eventName]
        lifetime = float(event[b'lifetime']) if b'lifetime' in event else self.__DEFAULT_LIFETIME
        result = queueItem.time + lifetime > BigWorld.time()
        if not result:
            LOG_VO((b'"{}" is removed from queue. Reason: lifetime').format(queueItem.eventName))
        return result

    @staticmethod
    def __tickGroup(group, delta):
        for name, info in group.items():
            if not info:
                continue
            info[b'time'] = info[b'time'] - delta
            if info[b'time'] < 0:
                group[name] = None

        return

    def _showSubtitle(self, subtitle):
        self._currentSubtitle = subtitle
        LOG_VO((b'Request subtitle: "{}"').format(subtitle))
        self.onSubtitleShow(subtitle)
        return

    def _hideSubtitle(self):
        if self._currentSubtitle:
            self._currentSubtitle = b''
            LOG_VO(b'Hide subtitle')
            self.onSubtitleHide()
        return

    def _soundMarkerHandler(self, marker):
        if not AccountSettings.getSettings(SOUND.SUBTITLES):
            return
        marker = marker.strip()
        if marker == _SUBTITLES_END_MARKER:
            self._hideSubtitle()
        elif marker.startswith(_SUBTITLE_PREFIX):
            self._showSubtitle(marker)
        return


class ComplexSoundNotifications(object):
    SPG_DISTANT_THREAT_SOUND = b'wpn_artillery_distant_threat'
    RTPC_EXT_SPG_SIGHT = b'RTPC_ext_artillery_sight'

    def __init__(self):
        self.__activeSounds = {}
        return

    def destroy(self):
        for sound in self.__activeSounds.values():
            sound.stop()

        self.__activeSounds.clear()
        return

    def notifyEnemySPGShotSound(self, distToTarget, shooterPosition):
        soundMatrix = Math.Matrix()
        soundMatrix.translation = shooterPosition
        sound = SoundGroups.g_instance.getSound3D(soundMatrix, ComplexSoundNotifications.SPG_DISTANT_THREAT_SOUND)
        if sound is not None:
            soundId = id(sound)
            self.__activeSounds[soundId] = sound
            sound.setRTPC(ComplexSoundNotifications.RTPC_EXT_SPG_SIGHT, distToTarget)
            sound.setCallback((lambda s: self.__endSoundCallback(soundId)))
            sound.play()
        return

    def __endSoundCallback(self, soundID):
        del self.__activeSounds[soundID]
        return
