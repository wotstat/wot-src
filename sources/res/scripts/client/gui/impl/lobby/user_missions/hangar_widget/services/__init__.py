import Event
from gui.prb_control.entities.listener import IGlobalListener

class IBattlePassService(IGlobalListener):
    onBattlePassChanged = Event.Event()

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
    onEventsListChanged = Event.Event()

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
    onMissionsChanged = Event.Event()

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


class ICampaignService(IGlobalListener):
    onEventsListChanged = Event.Event()

    def startListening(self):
        raise NotImplementedError
        return

    def stopListening(self):
        raise NotImplementedError
        return

    def getEntries(self):
        raise NotImplementedError
        return

    def finalize(self):
        raise NotImplementedError
        return
