from __future__ import absolute_import
from collections import namedtuple
from debug_utils import LOG_DEBUG
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework import g_entitiesFactories
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.shared import g_eventBus
from gui.shared.event_bus import EVENT_BUS_SCOPE
from gui.shared.event_dispatcher import showPersonalMissionCampaignSelectorWindow
from gui.shared.events import OpenLinkEvent

def getFilters():
    return {
     _onShowInExternalBrowser,
     _onGoToHangar,
     _onGoToMissions,
     _onGoToPersonalMissions}


BrowserFilterResult = namedtuple(b'BrowserFilterResult', b'stopNavigation closeBrowser')
BrowserFilterResult.__new__.__defaults__ = (False, False)

def _onShowInExternalBrowser(url, tags):
    if b'external' in tags:
        LOG_DEBUG(b'Browser url has been processed', url)
        g_eventBus.handleEvent(OpenLinkEvent(OpenLinkEvent.SPECIFIED, url))
        return BrowserFilterResult(stopNavigation=True)
    return BrowserFilterResult()


def _onGoToHangar(url, tags):
    if b'go_to_hangar' in tags:
        LOG_DEBUG(b'Browser url has been processed: going to hangar. Url: ', url)
        from gui.shared.event_dispatcher import showHangar
        showHangar()
        return BrowserFilterResult(stopNavigation=True)
    return BrowserFilterResult()


def _onGoToMissions(url, tags):
    if b'go_to_missions' in tags:
        LOG_DEBUG(b'Browser url has been processed: going to missions. Url: ', url)
        g_eventBus.handleEvent(g_entitiesFactories.makeLoadEvent(SFViewLoadParams(VIEW_ALIAS.LOBBY_MISSIONS)), scope=EVENT_BUS_SCOPE.LOBBY)
        return BrowserFilterResult(stopNavigation=True, closeBrowser=True)
    return BrowserFilterResult()


def _onGoToPersonalMissions(url, tags):
    if b'go_to_campaigns' in tags:
        LOG_DEBUG(b'Browser url has been processed: going to personal missions. Url: ', url)
        showPersonalMissionCampaignSelectorWindow()
        return BrowserFilterResult(stopNavigation=True, closeBrowser=True)
    return BrowserFilterResult()
