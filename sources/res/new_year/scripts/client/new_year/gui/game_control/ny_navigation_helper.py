from skeletons.gui.shared.utils import IHangarSpace
from helpers import dependency
from new_year.gui.impl.new_year.navigation import NewYearNavigation
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from new_year.gui.shared.event_dispatcher import showLootBoxEntry
from gui.shared.events import LobbySimpleEvent

def switchNewYearView(anchorName, aliasName=None):
    kwargs = {b'forceShowMainView': True}
    ctx = {b'anchorName': anchorName, 
       b'viewAlias': aliasName, 
       b'instantly': True, 
       b'kwargs': kwargs}
    g_eventBus.handleEvent(LobbySimpleEvent(LobbySimpleEvent.SWITCH_NEW_YEAR_VIEW, ctx), EVENT_BUS_SCOPE.LOBBY)
    return


def showLootBox(lootBoxType, category=b''):
    ctx = {b'lootBoxType': lootBoxType, 
       b'category': category}
    g_eventBus.handleEvent(LobbySimpleEvent(LobbySimpleEvent.SHOW_LOOT_BOX_VIEW, ctx), EVENT_BUS_SCOPE.LOBBY)
    return


def _externalSwitchToViewWithCtx(ctx, *args, **kwargs):
    ctx.update({b'anchordAsObject': True, 
       b'instantly': True, 
       b'args': args, 
       b'kwargs': kwargs})
    g_eventBus.handleEvent(LobbySimpleEvent(LobbySimpleEvent.SWITCH_NEW_YEAR_VIEW, ctx), EVENT_BUS_SCOPE.LOBBY)
    return


class NewYearNavigationHelper(object):
    __hangarSpace = dependency.descriptor(IHangarSpace)

    def onLobbyInited(self):
        g_eventBus.addListener(LobbySimpleEvent.SWITCH_NEW_YEAR_VIEW, self.__onSwitchEvent, EVENT_BUS_SCOPE.LOBBY)
        g_eventBus.addListener(LobbySimpleEvent.SHOW_LOOT_BOX_VIEW, self.__onShowLootBox, EVENT_BUS_SCOPE.LOBBY)
        self.__hangarSpace.onHeroTankReady += self.__onHeroTankReady
        return

    def clear(self):
        g_eventBus.removeListener(LobbySimpleEvent.SWITCH_NEW_YEAR_VIEW, self.__onSwitchEvent, EVENT_BUS_SCOPE.LOBBY)
        g_eventBus.removeListener(LobbySimpleEvent.SHOW_LOOT_BOX_VIEW, self.__onShowLootBox, EVENT_BUS_SCOPE.LOBBY)
        self.__hangarSpace.onHeroTankReady -= self.__onHeroTankReady
        NewYearNavigation.clear()
        return

    @staticmethod
    def __onSwitchEvent(event):
        ctx = event.ctx
        anchorName = ctx.get(b'anchorName')
        aliasName = ctx.get(b'viewAlias')
        anchordAsObject = ctx.get(b'anchordAsObject', False)
        if anchorName:
            if anchordAsObject:
                instantly = ctx.get(b'instantly', False)
                args = ctx.get(b'args')
                kwargs = ctx.get(b'kwargs')
                NewYearNavigation.showMainView(anchorName, viewAlias=aliasName, instantly=instantly, *args, **kwargs)
            else:
                NewYearNavigation.switchByAnchorName(anchorName)
        return

    @staticmethod
    def __onShowLootBox(event):
        category = event.ctx.get(b'category')
        lootBoxType = event.ctx.get(b'lootBoxType')
        if lootBoxType:
            showLootBoxEntry(lootBoxType=lootBoxType, category=category)
        return

    def __onHeroTankReady(self):
        NewYearNavigation.onHeroTankReady()
        return
