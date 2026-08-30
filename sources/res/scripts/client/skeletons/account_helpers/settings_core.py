from __future__ import absolute_import
import typing
if typing.TYPE_CHECKING:
    from account_helpers.settings_core.ServerSettingsManager import ServerSettingsManager

class ISettingsCache(object):
    onSyncStarted = None
    onSyncCompleted = None

    def init(self):
        raise NotImplementedError
        return

    def isSynced(self):
        raise NotImplementedError
        return

    def fini(self):
        raise NotImplementedError
        return

    def clear(self):
        raise NotImplementedError
        return

    @property
    def waitForSync(self):
        raise NotImplementedError
        return

    @property
    def settings(self):
        raise NotImplementedError
        return

    def update(self, callback=None):
        raise NotImplementedError
        return

    def getSectionSettings(self, section, defaultValue=0):
        raise NotImplementedError
        return

    def setSectionSettings(self, section, value):
        raise NotImplementedError
        return

    def setSettings(self, settings):
        raise NotImplementedError
        return

    def getSetting(self, key, defaultValue=0):
        raise NotImplementedError
        return

    def getVersion(self, defaultValue=0):
        raise NotImplementedError
        return

    def setVersion(self, value):
        raise NotImplementedError
        return

    def delSettings(self, settings):
        raise NotImplementedError
        return


class ISettingsCore(object):
    onOnceOnlyHintsChanged = None
    onSettingsChanged = None
    onSettingsApplied = None
    onSettingsReady = None
    isReady = property()

    def init(self):
        raise NotImplementedError
        return

    def fini(self):
        raise NotImplementedError
        return

    def clear(self):
        raise NotImplementedError
        return

    @isReady.getter
    def isReady(self):
        raise NotImplementedError
        return

    @property
    def options(self):
        raise NotImplementedError
        return

    @property
    def storages(self):
        raise NotImplementedError
        return

    @property
    def interfaceScale(self):
        raise NotImplementedError
        return

    @property
    def serverSettings(self):
        raise NotImplementedError
        return

    def packSettings(self, names):
        raise NotImplementedError
        return

    def getSetting(self, name):
        raise NotImplementedError
        return

    def getApplyMethod(self, diff):
        raise NotImplementedError
        return

    def applySetting(self, key, value):
        raise NotImplementedError
        return

    def previewSetting(self, name, value):
        raise NotImplementedError
        return

    def applySettings(self, diff):
        raise NotImplementedError
        return

    def revertSettings(self):
        raise NotImplementedError
        return

    def isSettingChanged(self, name, value):
        raise NotImplementedError
        return

    def applyStorages(self, restartApproved, force=False):
        raise NotImplementedError
        return

    def confirmChanges(self, confirmators):
        raise NotImplementedError
        return

    def clearStorages(self):
        raise NotImplementedError
        return

    def setOverrideSettings(self, overrideDict, disableStorages):
        raise NotImplementedError
        return

    def unsetOverrideSettings(self):
        raise NotImplementedError
        return


class IBattleCommunicationsSettings(object):
    onChanged = None

    @property
    def isEnabled(self):
        raise NotImplementedError
        return

    @property
    def showStickyMarkers(self):
        raise NotImplementedError
        return

    @property
    def showInPlayerList(self):
        raise NotImplementedError
        return

    @property
    def showCalloutMessages(self):
        raise NotImplementedError
        return

    @property
    def showLocationMarkers(self):
        raise NotImplementedError
        return

    @property
    def showBaseMarkers(self):
        raise NotImplementedError
        return

    @property
    def showCommendationsFeedbackOnReceive(self):
        raise NotImplementedError
        return

    def init(self):
        raise NotImplementedError
        return

    def fini(self):
        raise NotImplementedError
        return
