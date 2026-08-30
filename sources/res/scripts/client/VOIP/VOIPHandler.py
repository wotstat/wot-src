import logging
from wotdecorators import noexcept
_logger = logging.getLogger(__name__)
MESSAGE_IDS = {}
MSG_VOIP_INITED = 0
MESSAGE_IDS[MSG_VOIP_INITED] = b'MSG_VOIP_INITED'
MSG_VOIP_DESTROYED = 1
MESSAGE_IDS[MSG_VOIP_DESTROYED] = b'MSG_VOIP_DESTROYED'
MSG_CAPTURE_DEVICES = 10
MESSAGE_IDS[MSG_CAPTURE_DEVICES] = b'MSG_CAPTURE_DEVICES'
MSG_SET_CAPTURE_DEVICE = 11
MESSAGE_IDS[MSG_SET_CAPTURE_DEVICE] = b'MSG_SET_CAPTURE_DEVICE'
MSG_SET_LOCAL_SPEAKER_VOLUME = 20
MESSAGE_IDS[MSG_SET_LOCAL_SPEAKER_VOLUME] = b'MSG_SET_LOCAL_SPEAKER_VOLUME'
MSG_SET_LOCAL_MIC_VOLUME = 21
MESSAGE_IDS[MSG_SET_LOCAL_MIC_VOLUME] = b'MSG_SET_LOCAL_MIC_VOLUME'
MSG_MUTE_LOCAL_MIC = 22
MESSAGE_IDS[MSG_MUTE_LOCAL_MIC] = b'MSG_MUTE_LOCAL_MIC'
MSG_LOGIN_STATE_CHANGE = 30
MESSAGE_IDS[MSG_LOGIN_STATE_CHANGE] = b'MSG_LOGIN_STATE_CHANGE'
MSG_SESSION_ADDED = 42
MESSAGE_IDS[MSG_SESSION_ADDED] = b'MSG_SESSION_ADDED'
MSG_SESSION_REMOVED = 43
MESSAGE_IDS[MSG_SESSION_REMOVED] = b'MSG_SESSION_REMOVED'
MSG_NETWORK_TEST = 50
MESSAGE_IDS[MSG_NETWORK_TEST] = b'MSG_NETWORK_TEST'
MSG_PARTICIPANT_ADDED = 60
MESSAGE_IDS[MSG_PARTICIPANT_ADDED] = b'MSG_PARTICIPANT_ADDED'
MSG_PARTICIPANT_REMOVED = 61
MESSAGE_IDS[MSG_PARTICIPANT_REMOVED] = b'MSG_PARTICIPANT_REMOVED'
MSG_PARTICIPANT_UPDATED = 62
MESSAGE_IDS[MSG_PARTICIPANT_UPDATED] = b'MSG_PARTICIPANT_UPDATED'

class VOIPHandler(object):

    def __init__(self):
        return

    def onVoipInited(self, data):
        return

    def onVoipDestroyed(self, data):
        return

    def onCaptureDevicesArrived(self, data):
        return

    def onSetCaptureDevice(self, data):
        return

    def onSetLocalSpeakerVolume(self, data):
        return

    def onSetLocalMicVolume(self, data):
        return

    def onMuteLocalMic(self, data):
        return

    def onLoginStateChange(self, data):
        return

    def onSessionAdded(self, data):
        return

    def onSessionRemoved(self, data):
        return

    def onNetworkTest(self, data):
        return

    def onParticipantAdded(self, data):
        return

    def onParticipantRemoved(self, data):
        return

    def onParticipantUpdated(self, data):
        return

    @noexcept
    def __call__(self, message, data=None):
        if data is None:
            data = {}
        if message is not MSG_PARTICIPANT_UPDATED:
            _logger.debug(b'Message: %d [%s], Data: %s', message, MESSAGE_IDS[message], data)
        if message == MSG_VOIP_INITED:
            self.onVoipInited(data)
        elif message == MSG_VOIP_DESTROYED:
            self.onVoipDestroyed(data)
        elif message == MSG_CAPTURE_DEVICES:
            self.onCaptureDevicesArrived(data)
        elif message == MSG_SET_CAPTURE_DEVICE:
            self.onSetCaptureDevice(data)
        elif message == MSG_SET_LOCAL_SPEAKER_VOLUME:
            self.onSetLocalSpeakerVolume(data)
        elif message == MSG_SET_LOCAL_MIC_VOLUME:
            self.onSetLocalMicVolume(data)
        elif message == MSG_MUTE_LOCAL_MIC:
            self.onMuteLocalMic(data)
        elif message == MSG_LOGIN_STATE_CHANGE:
            self.onLoginStateChange(data)
        elif message == MSG_SESSION_ADDED:
            self.onSessionAdded(data)
        elif message == MSG_SESSION_REMOVED:
            self.onSessionRemoved(data)
        elif message == MSG_NETWORK_TEST:
            self.onNetworkTest(data)
        elif message == MSG_PARTICIPANT_ADDED:
            self.onParticipantAdded(data)
        elif message == MSG_PARTICIPANT_REMOVED:
            self.onParticipantRemoved(data)
        elif message == MSG_PARTICIPANT_UPDATED:
            self.onParticipantUpdated(data)
        return
