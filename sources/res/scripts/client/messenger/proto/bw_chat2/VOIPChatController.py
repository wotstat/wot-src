import BigWorld, BattleReplay, VOIP, CommandMapping
from VOIP.voip_constants import VOIP_SUPPORTED_API
from constants import ARENA_BONUS_TYPE_IDS, ARENA_BONUS_TYPE
from debug_utils import LOG_WARNING
from adisp import adisp_async, adisp_process
from gui import GUI_SETTINGS
from gui.impl import backport
from gui.impl.gen import R
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from gui.shared.events import GameEvent
from gui.shared.utils.key_mapping import getReadableKey
from helpers import dependency
from messenger.proto.events import g_messengerEvents
from messenger.proto.interfaces import IVOIPChatController
from account_helpers.settings_core.settings_constants import SOUND
from messenger.proto.shared_messages import ACTION_MESSAGE_TYPE, ClientActionMessage
from skeletons.account_helpers.settings_core import ISettingsCore

class VOIPChatController(IVOIPChatController):
    __slots__ = (b'__callbacks', b'__captureDevicesCallbacks')
    settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self):
        self.__callbacks = []
        self.__captureDevicesCallbacks = []
        return

    def start(self):
        voipMgr = VOIP.getVOIPManager()
        voipMgr.onInitialized += self.__initResponse
        voipMgr.onFailedToConnect += self.__failedResponse
        voipMgr.onCaptureDevicesUpdated += self.__captureDevicesResponse
        voipMgr.onPlayerSpeaking += self.__onPlayerSpeaking
        voipMgr.onJoinedChannel += self.__onJoinedChannel
        voipMgr.onLeftChannel += self.__onLeftChannel
        g_eventBus.addListener(GameEvent.TOGGLE_VOIP_CHANNEL_ENABLED, self.__onToggleChannelEnabled, scope=EVENT_BUS_SCOPE.BATTLE)
        self.__initialize()
        return

    def stop(self):
        voipMgr = VOIP.getVOIPManager()
        voipMgr.onInitialized -= self.__initResponse
        voipMgr.onFailedToConnect -= self.__failedResponse
        voipMgr.onCaptureDevicesUpdated -= self.__captureDevicesResponse
        voipMgr.onPlayerSpeaking -= self.__onPlayerSpeaking
        voipMgr.onJoinedChannel -= self.__onJoinedChannel
        voipMgr.onLeftChannel -= self.__onLeftChannel
        g_eventBus.removeListener(GameEvent.TOGGLE_VOIP_CHANNEL_ENABLED, self.__onToggleChannelEnabled, scope=EVENT_BUS_SCOPE.BATTLE)
        self.__callbacks = []
        self.__captureDevicesCallbacks = []
        return

    def isReady(self):
        return VOIP.getVOIPManager().isInitialized()

    def isPlayerSpeaking(self, accountDBID):
        if self.isVOIPEnabled():
            return bool(VOIP.getVOIPManager().isParticipantTalking(accountDBID))
        return False

    def isVOIPEnabled(self):
        return GUI_SETTINGS.voiceChat

    def isVivox(self):
        return VOIP.getVOIPManager().getAPI() == VOIP_SUPPORTED_API.VIVOX

    def isYY(self):
        return VOIP.getVOIPManager().getAPI() == VOIP_SUPPORTED_API.YY

    def invalidateInitialization(self):
        if self.isVOIPEnabled() and not BattleReplay.isPlaying() and not self.isReady():
            g_messengerEvents.voip.onVoiceChatInitFailed()
        return

    def setMicrophoneMute(self, isMuted, force=False):
        voipMgr = VOIP.getVOIPManager()
        if voipMgr is not None:
            if force or voipMgr.getCurrentChannel() and not voipMgr.isInTesting():
                voipMgr.setMicMute(muted=isMuted)
        return

    def invalidateMicrophoneMute(self):
        keyCode = CommandMapping.g_instance.get(b'CMD_VOICECHAT_MUTE')
        if not BigWorld.isKeyDown(keyCode):
            self.setMicrophoneMute(isMuted=True, force=True)
        return

    @adisp_async
    def requestCaptureDevices(self, firstTime=False, callback=None):
        voipMgr = VOIP.getVOIPManager()
        if voipMgr.getVOIPDomain() == b'':
            LOG_WARNING(b'RequestCaptureDevices. Vivox is not supported')
            callback([])
            return
        if not self.isReady():
            LOG_WARNING(b'RequestCaptureDevices. Vivox has not been initialized')
            callback([])
            return
        options = self.settingsCore.options

        def resetCapturedDevice(devices, firstTime=firstTime):
            if firstTime:
                option = options.getSetting(SOUND.CAPTURE_DEVICES)
                option.apply(option.get(), firstTime)
            callback(devices)
            return

        self.__captureDevicesCallbacks.append(resetCapturedDevice)
        voipMgr.requestCaptureDevices()
        return

    def isCurrentChannelEnabled(self):
        return VOIP.getVOIPManager().isCurrentChannelEnabled()

    def enableCurrentChannel(self, isEnableChannel):
        VOIP.getVOIPManager().enableCurrentChannel(isEnableChannel)
        return

    @adisp_process
    def __initialize(self):
        serverSettings = getattr(BigWorld.player(), b'serverSettings', {})
        if serverSettings and b'voipDomain' in serverSettings:
            domain = serverSettings[b'voipUserDomain']
            server = serverSettings[b'voipDomain']
        else:
            domain = b''
            server = b''
        yield self.__initializeSettings(domain, server)
        yield self.requestCaptureDevices(True)
        return

    @adisp_async
    def __initializeSettings(self, domain, server, callback):
        if self.isReady():
            self.__applyUserSettings()
            callback(True)
            return
        if domain == b'':
            LOG_WARNING(b'Initialize. Vivox is not supported')
            return
        self.__callbacks.append(callback)
        voipMgr = VOIP.getVOIPManager()
        if voipMgr.isNotInitialized():
            voipMgr.initialize(domain, server)
        self.__applyUserSettings()
        return

    def __applyUserSettings(self):
        options = self.settingsCore.options
        vOIPSetting = options.getSetting(b'enableVoIP')
        vOIPSetting.initFromPref()
        channelSettings = options.getSetting(SOUND.VOIP_ENABLE_CHANNEL)
        channelSettings.initFromPref()
        return

    def __initResponse(self, _):
        if self.isVOIPEnabled() and self.isReady():
            g_messengerEvents.voip.onVoiceChatInitSucceeded()
        while self.__callbacks:
            self.__callbacks.pop(0)(self.isReady())

        return

    def __failedResponse(self):
        self.invalidateInitialization()
        return

    def __captureDevicesResponse(self):
        devices = VOIP.getVOIPManager().getCaptureDevices()
        while self.__captureDevicesCallbacks:
            self.__captureDevicesCallbacks.pop(0)(devices)

        return

    def __onPlayerSpeaking(self, accountDBID, isSpeak):
        if self.isVOIPEnabled():
            g_messengerEvents.voip.onPlayerSpeaking(accountDBID, bool(isSpeak))
        return

    def __onJoinedChannel(self, channel, isTestChannel, isRejoin):
        if self.isVOIPEnabled():
            keyCode = CommandMapping.g_instance.get(b'CMD_VOICECHAT_MUTE')
            if BigWorld.isKeyDown(keyCode):
                VOIP.getVOIPManager().setMicMute(False)
            g_messengerEvents.voip.onChannelEntered(channel, isTestChannel, isRejoin)
        return

    def __onLeftChannel(self, channel, wasTestChannel):
        if self.isVOIPEnabled():
            g_messengerEvents.voip.onChannelLeft(channel, wasTestChannel)
        return

    def __onToggleChannelEnabled(self, event):
        voipMgr = VOIP.getVOIPManager()
        isEnabled = not voipMgr.isCurrentChannelEnabled()
        voipMgr.enableCurrentChannel(isEnabled)
        self.__showMessage(isEnabled, event.ctx.get(b'arenaBonusType'))
        return

    @classmethod
    def __showMessage(cls, enable, arenaBonusType):
        if arenaBonusType == ARENA_BONUS_TYPE.COMP7:
            cls.__showComp7Message(enable)
            return
        if arenaBonusType == ARENA_BONUS_TYPE.RANKED:
            cls.__showRankedMessage(enable)
            return
        if enable:
            msg = backport.text(R.strings.messenger.client.dynSquad.enableVOIP())
        else:
            customResource = R.strings.messenger.client.dyn(ARENA_BONUS_TYPE_IDS.get(arenaBonusType))
            if customResource.isValid():
                messageRId = customResource.disableVOIP()
            else:
                messageRId = R.strings.messenger.client.dynSquad.disableVOIP()
            msg = backport.text(messageRId, keyName=getReadableKey(CommandMapping.CMD_VOICECHAT_ENABLE))
        g_messengerEvents.onWarningReceived(ClientActionMessage(msg=msg, type_=ACTION_MESSAGE_TYPE.ERROR))
        return

    @staticmethod
    def __showComp7Message(enable):
        if enable:
            msg = backport.text(R.strings.messenger.client.dynSquad.enableVOIP())
        else:
            msg = backport.text(R.strings.messenger.client.COMP7.disableVOIP(), keyName=getReadableKey(CommandMapping.CMD_VOICECHAT_ENABLE))
        g_messengerEvents.onComp7VOIPNotificationReceived(ClientActionMessage(msg=msg, type_=ACTION_MESSAGE_TYPE.PLAYER if enable else ACTION_MESSAGE_TYPE.WARNING))
        return

    @staticmethod
    def __showRankedMessage(enable):
        if enable:
            msg = backport.text(R.strings.messenger.client.dynSquad.enableVOIP())
        else:
            msg = backport.text(R.strings.messenger.client.COMP7.disableVOIP(), keyName=getReadableKey(CommandMapping.CMD_VOICECHAT_ENABLE))
        g_messengerEvents.onRankedVOIPNotificationReceived(ClientActionMessage(msg=msg, type_=ACTION_MESSAGE_TYPE.PLAYER if enable else ACTION_MESSAGE_TYPE.WARNING))
        return
