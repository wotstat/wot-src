import json, logging
from collections import namedtuple
from functools import partial
import typing
from account_helpers import AccountSettings
from account_helpers.AccountSettings import GUI_LOOT_BOXES, LOOT_BOXES_INTRO_SHOWN
from gui.impl.gen import R
from gui_lootboxes.gui.shared.event_dispatcher import showLootBoxesWelcomeScreen
from helpers import dependency
from helpers.events_handler import EventsHandler
from helpers.time_utils import getTimestampByStrDate, getServerUTCTime
from skeletons.gui.game_control import IGameController, IEventsNotificationsController, IGuiLootBoxesIntroController
from soft_exception import SoftException
_logger = logging.getLogger(__name__)

class GuiLootBoxesIntroNotification(namedtuple(b'GuiLootBoxesIntroNotification', b'id startDate endDate view')):

    @classmethod
    def default(cls):
        return cls.__new__(cls, None, None, None, None)

    @classmethod
    def make(cls, data):
        if data[b'id'] == GuiLootboxesIntroController.DEFAULT_INTRO_ID:
            raise SoftException(b'Notificaiton id cannot be equal to default intro id')
        if data[b'view'] not in GuiLootboxesIntroController.VIEW_TO_HANDLER.keys():
            raise SoftException((b'Not registered view name {}').format(data[b'view']))
        return cls.__new__(cls, data[b'id'], getTimestampByStrDate(data[b'startDate']), getTimestampByStrDate(data[b'endDate']), data[b'view'])


class GuiLootboxesIntroController(IGuiLootBoxesIntroController, IGameController, EventsHandler):
    __slots__ = (b'__notifications',)
    __eventNotifications = dependency.descriptor(IEventsNotificationsController)
    INTRO_NOTIFICATION = b'lootboxIntroOverride'
    DEFAULT_INTRO_ID = 0
    VIEW_TO_HANDLER = {b'keysWelcomeScreen': (partial(showLootBoxesWelcomeScreen, layoutID=R.views.gui_lootboxes.lobby.gui_lootboxes.KeysWelcomeScreen()))}

    def __init__(self):
        self.__notifications = []
        return

    def onLobbyInited(self, _):
        self._subscribe()
        self.__tryParseNotifications(self.__getIntroNotifications())
        return

    def onAccountBecomeNonPlayer(self):
        self._unsubscribe()
        self.__notifications = []
        return

    def fini(self):
        self._unsubscribe()
        self.__notifications = []
        return

    def tryShowIntro(self):
        activeIntros = self.getActiveIntros()
        if not activeIntros:
            self.__tryShowDefaultIntro()
            return
        shownIntros = self.__getShownIntros()
        activeIntro = activeIntros[0]
        if activeIntro.id in shownIntros:
            _logger.debug(b'Intro already shown id=%s', activeIntro.id)
            return
        handler = self.VIEW_TO_HANDLER[activeIntro.view]
        handler(closeCallback=partial(self.__closeCallback, activeIntro.id))
        return

    def getActiveIntros(self):
        currentTime = getServerUTCTime()
        return [notification for notification in self.__notifications if notification.startDate <= currentTime <= notification.endDate]

    def _getEvents(self):
        return (
         (
          self.__eventNotifications.onEventNotificationsChanged, self.__onEventNotificationsChanged),)

    def __tryShowDefaultIntro(self):
        shownIntros = self.__getShownIntros()
        if self.DEFAULT_INTRO_ID in shownIntros:
            _logger.debug(b'Default intro already shown')
            return
        showLootBoxesWelcomeScreen(closeCallback=partial(self.__closeCallback, self.DEFAULT_INTRO_ID))
        return

    def __tryParseNotifications(self, notifications):
        if not notifications:
            return
        self.__notifications = []
        for notification in notifications:
            try:
                data = json.loads(notification.data)
                self.__notifications.append(GuiLootBoxesIntroNotification.make(data))
            except SoftException as e:
                _logger.error(e.message)
            except ValueError as e:
                _logger.error(b'Some error occured during parsing notification (type=%s): %s', notification.eventType, e)

        return

    def __getIntroNotifications(self):
        return self.__eventNotifications.getEventsNotifications((lambda notification: notification.eventType == self.INTRO_NOTIFICATION))

    def __onEventNotificationsChanged(self, *_):
        self.__tryParseNotifications(self.__getIntroNotifications())
        return

    def __closeCallback(self, introID):
        self.__setIntroShown(introID)
        return

    def __getShownIntros(self):
        return (AccountSettings.getSettings(GUI_LOOT_BOXES) or {}).get(LOOT_BOXES_INTRO_SHOWN, set())

    def __setIntroShown(self, introId):
        settings = AccountSettings.getSettings(GUI_LOOT_BOXES) or {}
        intros = settings.get(LOOT_BOXES_INTRO_SHOWN, set())
        if introId not in intros:
            intros.add(introId)
            settings[LOOT_BOXES_INTRO_SHOWN] = intros
            AccountSettings.setSettings(GUI_LOOT_BOXES, settings)
        return
