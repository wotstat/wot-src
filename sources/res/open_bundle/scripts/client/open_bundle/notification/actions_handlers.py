from __future__ import absolute_import
from notification.actions_handlers import NavigationDisabledActionHandler
from notification.settings import NOTIFICATION_TYPE
from open_bundle.gui.shared.event_dispatcher import showOpenBundleMainView

class OpenBundleReminderHandler(NavigationDisabledActionHandler):

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return (b'openBundle',)

    def doAction(self, model, entityID, action):
        notification = model.getNotification(self.getNotType(), entityID)
        savedData = notification.getSavedData()
        if savedData and b'bundleID' in savedData and savedData[b'bundleID']:
            showOpenBundleMainView(savedData[b'bundleID'])
        return
