from helpers import dependency
from notification.actions_handlers import NavigationDisabledActionHandler
from skeletons.gui.game_control import IWhiteTigerController
from gui.shop import showBuyLootboxOverlay
from notification.settings import NOTIFICATION_TYPE
from white_tiger.gui.shared import event_dispatcher
from gui.shared import event_dispatcher as shared_events
from white_tiger.gui.shared.event_dispatcher import showWTFairplayDialog

class _WTEventHandler(NavigationDisabledActionHandler):
    _wtController = dependency.descriptor(IWhiteTigerController)

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    def _canNavigate(self):
        result = super(_WTEventHandler, self)._canNavigate()
        return self._wtController.isEnabled() and result


class WTOpenPortalsHandler(_WTEventHandler):

    @classmethod
    def getActions(cls):
        return (b'wtOpenPortals',)

    def doAction(self, model, entityID, action):
        self._wtController.doSelectEventPrbAndCallback(shared_events.showEventStorageWindow)
        return


class WTOpenCollectionHandler(_WTEventHandler):

    @classmethod
    def getActions(cls):
        return (b'wtOpenCollection',)

    def doAction(self, model, entityID, action):
        self._wtController.doSelectEventPrbAndCallback(shared_events.showEventProgressionWindow)
        return


class WTOpenHandler(_WTEventHandler):

    @classmethod
    def getActions(cls):
        return (b'wtOpen',)

    def doAction(self, model, entityID, action):
        self._wtController.doSelectEventPrb()
        return


class WTOpenQuestsHandler(_WTEventHandler):

    @classmethod
    def getActions(cls):
        return (b'wtOpenQuests',)

    def doAction(self, model, entityID, action):
        self._wtController.doSelectEventPrbAndCallback(event_dispatcher.showEventProgressionWindow)
        return


class WTOpenTicketPurchasingHandler(_WTEventHandler):

    @classmethod
    def getActions(cls):
        return (b'wtOpenTicketPurchasing',)

    def doAction(self, model, entityID, action):
        self._wtController.doSelectEventPrbAndCallback(showBuyLootboxOverlay)
        return


class _WTFairPlayBase(_WTEventHandler):
    _PENALTY_TYPE = b''

    def doAction(self, model, entityID, action):
        notification = model.getNotification(self.getNotType(), entityID)
        showWTFairplayDialog(self._PENALTY_TYPE, data=notification.getSavedData())
        return

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE


class WTFairPlayActionHandler(_WTFairPlayBase):
    _PENALTY_TYPE = b'penalty'

    @classmethod
    def getActions(cls):
        return (b'WTFairPlayActionHandler',)


class WTWarningFairPlayActionHandler(_WTFairPlayBase):
    _PENALTY_TYPE = b'warning'

    @classmethod
    def getActions(cls):
        return (b'WTWarningFairPlayActionHandler',)
