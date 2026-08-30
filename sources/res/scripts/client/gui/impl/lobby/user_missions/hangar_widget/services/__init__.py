from __future__ import absolute_import
import typing
from gui.prb_control.entities.listener import IGlobalListener
if typing.TYPE_CHECKING:
    from typing import List
    from gui.impl.lobby.user_missions.hangar_widget.plugins import IUserMissionPlugin

class IBattlePassService(IGlobalListener):
    onBattlePassChanged = None

    def startListening(self):
        raise NotImplementedError
        return

    def stopListening(self):
        raise NotImplementedError
        return

    def isVisible(self):
        raise NotImplementedError
        return

    def finalize(self):
        raise NotImplementedError
        return


class IEventsService(IGlobalListener):
    onEventsListChanged = None

    def startListening(self):
        raise NotImplementedError
        return

    def stopListening(self):
        raise NotImplementedError
        return

    def getEntries(self):
        raise NotImplementedError
        return

    def getEntryData(self):
        raise NotImplementedError
        return

    def updateEntries(self):
        raise NotImplementedError
        return

    def finalize(self):
        raise NotImplementedError
        return

    @property
    def isAvailable(self):
        raise NotImplementedError
        return


class IMissionsService(IGlobalListener):
    onMissionsChanged = None

    def startListening(self):
        raise NotImplementedError
        return

    def stopListening(self):
        raise NotImplementedError
        return

    def isVisible(self):
        raise NotImplementedError
        return

    def finalize(self):
        raise NotImplementedError
        return


class IPersonalMissionsService(IMissionsService):
    onPersonalMissionsChanged = None
    onWidgetQuestIDMarkedAsNew = None
    onServicePMSyncCompleted = None

    def clearWidgetQuestIDMarkedAsNew(self):
        raise NotImplementedError
        return

    def setWidgetQuestIDMarkedAsNew(self, questID, doUpdateWidget=True):
        raise NotImplementedError
        return

    def getWidgetQuestIDMarkedAsNew(self):
        raise NotImplementedError
        return


class IMissionsContainerService(IGlobalListener):
    onShowPlugin = None
    onHidePlugin = None

    def showPlugin(self, viewAlias):
        raise NotImplementedError
        return

    def hidePlugin(self, viewAlias):
        raise NotImplementedError
        return

    def getVisiblePlugins(self):
        raise NotImplementedError
        return

    def isPluginVisible(self, viewAlias):
        raise NotImplementedError
        return

    def getSelectedSlide(self, sliderId):
        raise NotImplementedError
        return

    def onSlideChanged(self, selectedSlide):
        raise NotImplementedError
        return

    def finalize(self):
        raise NotImplementedError
        return


class IUserMissionWidgetService(object):
    onVisibleGroupsChanged = None

    def setGroupVisibility(self, groupName, isVisible):
        raise NotImplementedError
        return

    def getVisibleGroups(self):
        raise NotImplementedError
        return

    def isGroupVisible(self, groupName):
        raise NotImplementedError
        return

    def finalize(self):
        raise NotImplementedError
        return
