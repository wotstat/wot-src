from __future__ import absolute_import
from gui.shared import events, EVENT_BUS_SCOPE
from gui.Scaleform.daapi.view.meta.EventBoardsDetailsContainerViewMeta import EventBoardsDetailsContainerViewMeta
from gui.Scaleform.genConsts.EVENTBOARDS_ALIASES import EVENTBOARDS_ALIASES
from gui.shared.formatters import text_styles
from helpers import dependency
from skeletons.gui.event_boards_controllers import IEventBoardController

class EventBoardsDetailsContainerView(EventBoardsDetailsContainerViewMeta):
    eventsController = dependency.descriptor(IEventBoardController)
    _linkage = None
    _extra = {}

    def __init__(self, ctx=None):
        super(EventBoardsDetailsContainerView, self).__init__()
        self.ctx = ctx
        eventID = ctx.get(b'eventID')
        self.eventData = self.eventsController.getEventsSettingsData().getEvent(eventID)
        return

    def closeView(self):
        self.destroy()
        return

    def _populate(self):
        super(EventBoardsDetailsContainerView, self)._populate()
        self.addListener(events.HideWindowEvent.HIDE_MISSION_DETAILS_VIEW, self.__handleDetailsClose, EVENT_BUS_SCOPE.LOBBY)
        data = {b'linkage': (self._linkage), 
           b'title': (text_styles.superPromoTitle(self.eventData.getName()))}
        data.update(self._extra)
        self.as_setInitDataS(data)
        return

    def _dispose(self):
        self.removeListener(events.HideWindowEvent.HIDE_MISSION_DETAILS_VIEW, self.__handleDetailsClose, EVENT_BUS_SCOPE.LOBBY)
        super(EventBoardsDetailsContainerView, self)._dispose()
        return

    def _onRegisterFlashComponent(self, viewPy, alias):
        super(EventBoardsDetailsContainerView, self)._onRegisterFlashComponent(viewPy, alias)
        viewPy.setOpener(self)
        return

    def __handleDetailsClose(self, _):
        self.destroy()
        return


class EventBoardsDetailsBrowserView(EventBoardsDetailsContainerView):
    _linkage = EVENTBOARDS_ALIASES.EVENTBOARDS_DETAILS_BROWSER_LINKAGE


class EventBoardsDetailsVehiclesView(EventBoardsDetailsContainerView):
    _linkage = EVENTBOARDS_ALIASES.EVENTBOARDS_DETAILS_VEHICLES_LINKAGE


class EventBoardsDetailsAwardsView(EventBoardsDetailsContainerView):
    _linkage = EVENTBOARDS_ALIASES.EVENTBOARDS_DETAILS_AWARDS_LINKAGE
    _extra = {b'bgWidth': 753, b'bgHeight': 509}


class EventBoardsDetailsBattleView(EventBoardsDetailsContainerView):
    _linkage = EVENTBOARDS_ALIASES.EVENTBOARDS_DETAILS_BATTLE_LINKAGE
    _extra = {b'bgWidth': 753, b'bgHeight': 549}
