import logging, Event
from VOIPHandler import VOIPHandler
from messenger.m_constants import PROTO_TYPE
from messenger.proto import proto_getter
from messenger.proto.events import g_messengerEvents
from messenger.storage import storage_getter
_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())
_logger.setLevel(logging.INFO)

class VOIPSingleton(VOIPHandler):

    def __init__(self):
        super(VOIPSingleton, self).__init__()
        from VOIPManagerWebRTC import VOIPManagerWebRTC
        self.__impl = VOIPManagerWebRTC()
        self.__settings = {}
        self.__profile = b'webrtc'
        self.__eventManager = em = Event.EventManager()
        self.onCaptureDevicesUpdated = Event.Event(em)
        self.onPlayerSpeaking = Event.Event(em)
        self.onInitialized = Event.Event(em)
        self.onFailedToConnect = Event.Event(em)
        self.onJoinedChannel = Event.Event(em)
        self.onLeftChannel = Event.Event(em)
        self.onChannelAvailable = Event.Event(em)
        self.onChannelLost = Event.Event(em)
        return

    @property
    def profile(self):
        return self.__profile

    def destroy(self):
        _logger.debug(b'destroy')
        self.onDisconnected()
        self.__unsubscribe()
        self.__impl.destroy()
        return

    def __subscribe(self):
        _logger.debug(b'subscribe')
        self.__impl.onCaptureDevicesUpdated += self.onCaptureDevicesUpdated
        self.__impl.onPlayerSpeaking += self.onPlayerSpeaking
        self.__impl.onInitialized += self.onInitialized
        self.__impl.onFailedToConnect += self.onFailedToConnect
        self.__impl.onJoinedChannel += self.onJoinedChannel
        self.__impl.onLeftChannel += self.onLeftChannel
        self.__impl.onChannelAvailable += self.onChannelAvailable
        self.__impl.onChannelLost += self.onChannelLost
        return

    def __unsubscribe(self):
        _logger.debug(b'unsubscribe')
        self.__impl.onCaptureDevicesUpdated -= self.onCaptureDevicesUpdated
        self.__impl.onPlayerSpeaking -= self.onPlayerSpeaking
        self.__impl.onInitialized -= self.onInitialized
        self.__impl.onFailedToConnect -= self.onFailedToConnect
        self.__impl.onJoinedChannel -= self.onJoinedChannel
        self.__impl.onLeftChannel -= self.onLeftChannel
        self.__impl.onChannelAvailable -= self.onChannelAvailable
        self.__impl.onChannelLost -= self.onChannelLost
        return

    @proto_getter(PROTO_TYPE.BW_CHAT2)
    def bwProto(self):
        return

    @storage_getter(b'users')
    def usersStorage(self):
        return

    @proto_getter(PROTO_TYPE.MIGRATION)
    def proto(self):
        return

    def isEnabled(self):
        return self.__impl.isEnabled()

    def isInitialized(self):
        return self.__impl.isInitialized()

    def isInTesting(self):
        return self.__impl.isInTesting()

    def getVOIPDomain(self):
        return self.__impl.getVOIPDomain()

    def getCurrentChannel(self):
        return self.__impl.getCurrentChannel()

    def isVoiceSupported(self):
        return self.__impl.isVoiceSupported()

    def isChannelAvailable(self):
        return self.__impl.isChannelAvailable()

    def getCaptureDevices(self):
        return self.__impl.getCaptureDevices()

    def getCurrentCaptureDevice(self):
        return self.__impl.getCurrentCaptureDevice()

    def getState(self):
        return self.__impl.getState()

    def getAPI(self):
        return self.__impl.getAPI()

    def isLoggedIn(self):
        return self.__impl.isLoggedIn()

    def onConnected(self):
        voipEvents = g_messengerEvents.voip
        voipEvents.onChannelAvailable += self.channelAvailable
        voipEvents.onChannelLost += self.channelLost
        voipEvents.onCredentialReceived += self.credentialReceived
        usersEvents = g_messengerEvents.users
        usersEvents.onUsersListReceived += self.usersListReceived
        usersEvents.onUserActionReceived += self.userActionReceived
        return

    def onDisconnected(self):
        voipEvents = g_messengerEvents.voip
        voipEvents.onChannelAvailable -= self.channelAvailable
        voipEvents.onChannelLost -= self.channelLost
        voipEvents.onCredentialReceived -= self.credentialReceived
        usersEvents = g_messengerEvents.users
        usersEvents.onUsersListReceived -= self.usersListReceived
        usersEvents.onUserActionReceived -= self.userActionReceived
        return

    def channelAvailable(self, channel, token, isRejoin, isEchoChannel):
        self.__impl.channelAvailable(channel, token, isRejoin, isEchoChannel)
        return

    def channelLost(self):
        self.__impl.channelLost()
        return

    def credentialReceived(self, name, pwd):
        self.__impl.credentialReceived(name, pwd)
        return

    def usersListReceived(self, tags):
        self.__impl.usersListReceived(tags)
        return

    def userActionReceived(self, actionID, user, shadowMode):
        self.__impl.userActionReceived(actionID, user, shadowMode)
        return

    def enable(self, enabled, isInitFromPrefs=False):
        self.__impl.enable(enabled, isInitFromPrefs)
        return

    def applyChannelSetting(self, isEnabled, channelID):
        self.__impl.applyChannelSetting(isEnabled, channelID)
        return

    def enableCurrentChannel(self, isEnabled=True, autoEnableVOIP=True):
        self.__impl.enableCurrentChannel(isEnabled, autoEnableVOIP)
        return

    def isCurrentChannelEnabled(self):
        return self.__impl.isCurrentChannelEnabled()

    def initialize(self, voipSettings):
        _logger.debug(b'initialize')
        if b'profile' not in voipSettings:
            return
        profile = voipSettings[b'profile']
        if self.__profile != profile:
            self.__profile = profile
            self.__impl.destroy()
            if voipSettings[b'profile'] == b'vivox':
                from VOIPManager import VOIPManager
                self.__impl = VOIPManager()
            elif voipSettings[b'profile'] == b'webrtc':
                from VOIPManagerWebRTC import VOIPManagerWebRTC
                self.__impl = VOIPManagerWebRTC()
        self.onConnected()
        self.__subscribe()
        self.__impl.initialize(voipSettings)
        return

    def logout(self):
        self.__impl.logout()
        return

    def enterTestChannel(self):
        self.__impl.enterTestChannel()
        return

    def leaveTestChannel(self):
        self.__impl.leaveTestChannel()
        return

    def setMasterVolume(self, attenuation):
        self.__impl.setMasterVolume(attenuation)
        return

    def setMicrophoneVolume(self, attenuation):
        self.__impl.setMicrophoneVolume(attenuation)
        return

    def setVoiceActivation(self, enabled):
        self.__impl.setVoiceActivation(enabled)
        return

    def setMicMute(self, muted=True):
        self.__impl.setMicMute(muted)
        return

    def requestCaptureDevices(self):
        self.__impl.requestCaptureDevices()
        return

    def setCaptureDevice(self, deviceName):
        self.__impl.setCaptureDevice(deviceName)
        return

    def isParticipantTalking(self, dbid):
        return self.__impl.isParticipantTalking(dbid)

    def onVoipInited(self, data):
        self.__impl.onVoipInited(data)
        return

    def onVoipDestroyed(self, data):
        self.__impl.onVoipDestroyed(data)
        return

    def onCaptureDevicesArrived(self, data):
        self.__impl.onCaptureDevicesArrived(data)
        return

    def onSetCaptureDevice(self, data):
        self.__impl.onSetCaptureDevice(data)
        return

    def onSetLocalSpeakerVolume(self, data):
        self.__impl.onSetLocalSpeakerVolume(data)
        return

    def onSetLocalMicVolume(self, data):
        self.__impl.onSetLocalMicVolume(data)
        return

    def onMuteLocalMic(self, data):
        self.__impl.onMuteLocalMic(data)
        return

    def onLoginStateChange(self, data):
        self.__impl.onLoginStateChange(data)
        return

    def onSessionAdded(self, data):
        self.__impl.onSessionAdded(data)
        return

    def onSessionRemoved(self, data):
        self.__impl.onSessionRemoved(data)
        return

    def onNetworkTest(self, data):
        self.__impl.onNetworkTest(data)
        return

    def onParticipantAdded(self, data):
        self.__impl.onParticipantAdded(data)
        return

    def onParticipantRemoved(self, data):
        self.__impl.onParticipantRemoved(data)
        return

    def onParticipantUpdated(self, data):
        self.__impl.onParticipantUpdated(data)
        return
