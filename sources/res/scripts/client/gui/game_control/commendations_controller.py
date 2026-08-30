from __future__ import absolute_import
from enum import Enum
import Event
from gui.server_events import settings
from PlayerEvents import g_playerEvents
from commendations_schema import commendationsConfigSchema
from gui import SystemMessages
from gui.SystemMessages import SM_TYPE
from skeletons.gui.game_control import ICommendationsController

class NotificationTypeTemplate(Enum):
    MESSAGES = (b'#messenger:serviceChannelMessages/commendations/messages/enable', b'#messenger:serviceChannelMessages/commendations/messages/disable')
    LIVE_TAGS = (b'#messenger:serviceChannelMessages/commendations/liveTags/enable', b'#messenger:serviceChannelMessages/commendations/liveTags/disable')

    @property
    def getEnable(self):
        return self.value[0]

    @property
    def getDisable(self):
        return self.value[1]


class CommendationsController(ICommendationsController):

    def __init__(self):
        super(CommendationsController, self).__init__()
        self._modifiable = False
        self._isCommendationsEnabled = False
        self._isLiveTagsEnabled = False
        self.onSettingsChanged = Event.Event()
        return

    @property
    def isCommendationsEnabled(self):
        return self._isCommendationsEnabled

    @property
    def isLiveTagsEnabled(self):
        return self._isLiveTagsEnabled

    def init(self):
        g_playerEvents.onConfigModelUpdated += self._onConfigModelUpdated
        return

    def fini(self):
        g_playerEvents.onConfigModelUpdated -= self._onConfigModelUpdated
        return

    def onAccountBecomeNonPlayer(self):
        self._modifiable = False
        return

    def onAccountBecomePlayer(self):
        self._modifiable = True
        self._updateLocalCache()
        self._processSwitchNotifications()
        return

    def onAvatarBecomePlayer(self):
        self._updateLocalCache()
        return

    def _onConfigModelUpdated(self, gpKey):
        if commendationsConfigSchema.gpKey == gpKey and self._modifiable:
            self._updateLocalCache()
            self._processSwitchNotifications()
        return

    def _updateLocalCache(self):
        config = commendationsConfigSchema.getModel()
        if not config:
            return
        self._isCommendationsEnabled = config.isCommendationsEnabled
        self._isLiveTagsEnabled = config.isLiveTagsEnabled
        self.onSettingsChanged()
        return

    def _processSwitchNotifications(self):
        isCommsEnabled = self.isCommendationsEnabled
        isLiveTagsEnabled = self.isLiveTagsEnabled
        with settings.commendationsSettings() as commsSettings:
            wasCommsEnabled = commsSettings.isMessagesEnable
            wasLiveTagsEnabled = commsSettings.isLiveTagsEnable
            self._notifyClient(wasCommsEnabled, isCommsEnabled, NotificationTypeTemplate.MESSAGES)
            self._notifyClient(wasLiveTagsEnabled, isLiveTagsEnabled, NotificationTypeTemplate.LIVE_TAGS)
            commsSettings.setMessageEnable(isCommsEnabled)
            commsSettings.setLiveTagsEnable(isLiveTagsEnabled)
        return

    def _notifyClient(self, lastSeenStatus, currentStatus, notifications):
        if lastSeenStatus != currentStatus:
            notification = notifications.getEnable if currentStatus else notifications.getDisable
            smType = SM_TYPE.Information if currentStatus else SM_TYPE.Warning
            SystemMessages.pushI18nMessage(notification, type=smType)
        return
