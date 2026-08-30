from debug_utils import LOG_ERROR
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.shared import g_eventBus, events, EVENT_BUS_SCOPE
from gui.shared.utils.functions import getViewName
from messenger.ext import channel_num_gen
from messenger.gui.Scaleform.view.lobby import MESSENGER_VIEW_ALIAS

def showLobbyChannelWindow(clientID):
    g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(MESSENGER_VIEW_ALIAS.LOBBY_CHANNEL_WINDOW), ctx={b'clientID': clientID}), scope=EVENT_BUS_SCOPE.LOBBY)
    return


def showLazyChannelWindow(clientID):
    g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(MESSENGER_VIEW_ALIAS.LAZY_CHANNEL_WINDOW), ctx={b'clientID': clientID}), scope=EVENT_BUS_SCOPE.LOBBY)
    return


def notifyCarousel(clientID, notify=True):
    g_eventBus.handleEvent(events.ChannelManagementEvent(clientID, events.ChannelManagementEvent.REQUEST_TO_CHANGE, {b'key': b'isNotified', 
       b'value': notify}), scope=EVENT_BUS_SCOPE.LOBBY)
    return


def showConnectToSecureChannelWindow(channel):
    g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(MESSENGER_VIEW_ALIAS.CONNECT_TO_SECURE_CHANNEL_WINDOW, getViewName(MESSENGER_VIEW_ALIAS.CONNECT_TO_SECURE_CHANNEL_WINDOW, channel.getClientID())), ctx={b'channel': channel}), scope=EVENT_BUS_SCOPE.LOBBY)
    return


def rqActivateChannel(clientID, component):
    g_eventBus.handleEvent(events.ChannelManagementEvent(clientID, events.ChannelManagementEvent.REQUEST_TO_ACTIVATE, {b'component': component}), scope=EVENT_BUS_SCOPE.LOBBY)
    return


def rqActivateLazyChannel(name, component):
    clientID = channel_num_gen.getClientID4LazyChannel(name)
    if not clientID:
        LOG_ERROR(b'Client ID is not found', name)
    else:
        rqActivateChannel(clientID, component)
    return


def rqDeactivateChannel(clientID):
    g_eventBus.handleEvent(events.ChannelManagementEvent(clientID, events.ChannelManagementEvent.REQUEST_TO_DEACTIVATE), scope=EVENT_BUS_SCOPE.LOBBY)
    return


def rqDeactivateLazyChannel(name):
    clientID = channel_num_gen.getClientID4LazyChannel(name)
    if not clientID:
        LOG_ERROR(b'Client ID is not found', name)
    else:
        rqDeactivateChannel(clientID)
    return


def rqExitFromChannel(clientID):
    g_eventBus.handleEvent(events.ChannelManagementEvent(clientID, events.ChannelManagementEvent.REQUEST_TO_EXIT), scope=EVENT_BUS_SCOPE.LOBBY)
    return


def rqExitFromLazyChannel(name):
    clientID = channel_num_gen.getClientID4LazyChannel(name)
    if not clientID:
        LOG_ERROR(b'Client ID is not found', name)
    else:
        rqExitFromChannel(clientID)
    return


def setMessageFadingEnabled(isEnabled):
    g_eventBus.handleEvent(events.ChannelManagementEvent(0, events.ChannelManagementEvent.MESSAGE_FADING_ENABLED, {b'isEnabled': isEnabled}), scope=EVENT_BUS_SCOPE.GLOBAL)
    return
