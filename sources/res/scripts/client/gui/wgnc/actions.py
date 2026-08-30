import BigWorld
from adisp import adisp_process
from debug_utils import LOG_CURRENT_EXCEPTION, LOG_ERROR, LOG_WARNING, LOG_DEBUG
from gui.game_control.links import URLMacros
from gui.promo.promo_logger import PromoLogSourceType
from gui.shared.event_dispatcher import showStrongholds
from gui.shared.utils.decorators import ReprInjector
from gui.wgnc.custom_actions_keeper import CustomActionsKeeper
from gui.wgnc.events import g_wgncEvents
from gui.wgnc.settings import WGNC_GUI_TYPE
from gui.wgnc.common import WebHandlersContainer
from gui.Scaleform.genConsts.RANKEDBATTLES_CONSTS import RANKEDBATTLES_CONSTS
from helpers import dependency
from skeletons.gui.game_control import IBrowserController, IPromoController, IRankedBattlesController
from web.web_client_api.sound import HangarSoundWebApi
from web.web_client_api import webApiCollection

@ReprInjector.simple((b'_name', b'name'))
class _Action(object):
    __slots__ = (b'_name',)

    def __init__(self, name):
        super(_Action, self).__init__()
        self._name = name
        return

    def getName(self):
        return self._name

    def validate(self, itemsHolder):
        return True

    def invoke(self, notID, actor=None):
        raise NotImplementedError
        return


@ReprInjector.withParent((b'_purge', b'purge'), (b'_isInvoked', b'isInvoked'))
class Callback(_Action):
    __slots__ = (b'_purge', b'_isInvoked')

    def __init__(self, name, purge=True):
        super(Callback, self).__init__(name)
        self._purge = purge
        self._isInvoked = False
        return

    def doPurge(self):
        return self._purge

    def invoke(self, notID, actor=None):
        if self._purge and self._isInvoked:
            LOG_DEBUG(b'Callback with purge=true has been invoked, it is skipped', self._name)
            return
        self._isInvoked = True
        try:
            BigWorld.player().sendNotificationReply(notID, self._purge, self._name)
        except (AttributeError, TypeError):
            LOG_CURRENT_EXCEPTION()

        return


@ReprInjector.withParent((b'_url', b'url'))
class _OpenBrowser(_Action):
    __slots__ = (b'_url',)

    def __init__(self, name, url):
        super(_OpenBrowser, self).__init__(name)
        self._url = url
        return

    def getURL(self):
        return self._url


@ReprInjector.withParent()
class OpenInternalBrowser(_OpenBrowser, WebHandlersContainer):
    __slots__ = (b'_browserID', b'_size', b'_showRefresh', b'_webHandlerName', b'_isSolidBorder')
    browserCtrl = dependency.descriptor(IBrowserController)

    def __init__(self, name, url, size=None, showRefresh=True, webHandlerName=None, isSolidBorder=False):
        super(OpenInternalBrowser, self).__init__(name, url)
        self._browserID = None
        self._size = size
        self._showRefresh = showRefresh
        self._webHandlerName = webHandlerName
        self._isSolidBorder = isSolidBorder
        return

    def invoke(self, _, actor=None):
        if actor:
            title = actor.getTopic()
        else:
            title = None
        self._doInvoke(title)
        return

    def _getHandlers(self):
        predefinedHandlers = self.getWebHandler(self._webHandlerName) or []
        return predefinedHandlers + webApiCollection(HangarSoundWebApi)

    @adisp_process
    def _doInvoke(self, title):
        self._browserID = yield self.browserCtrl.load(self._url, browserID=self._browserID, title=title, browserSize=self._size, showActionBtn=self._showRefresh, handlers=self._getHandlers(), isSolidBorder=self._isSolidBorder)
        browser = self.browserCtrl.getBrowser(self._browserID)
        if browser is not None:
            browser.setIsAudioMutable(True)
        return


@ReprInjector.withParent()
class OpenPromoBrowser(OpenInternalBrowser):
    __slots__ = ()
    promoCtrl = dependency.descriptor(IPromoController)

    def _doInvoke(self, _):
        self.promoCtrl.showPromo(self._url, source=PromoLogSourceType.PRMP)
        return


@ReprInjector.withParent()
class OpenStrongholdBrowser(OpenInternalBrowser):
    __slots__ = ()

    def _doInvoke(self, _):
        showStrongholds(self._url)
        return


@ReprInjector.withParent()
class OpenRankedBrowser(OpenInternalBrowser):
    __slots__ = ()
    __rankedController = dependency.descriptor(IRankedBattlesController)

    def _doInvoke(self, _):
        self.__rankedController.showRankedBattlePage(ctx={b'selectedItemID': (RANKEDBATTLES_CONSTS.RANKED_BATTLES_YEAR_RATING_ID)})
        return


@ReprInjector.withParent()
class OpenExternalBrowser(_OpenBrowser):

    @adisp_process
    def invoke(self, notID, actor=None):
        processedUrl = yield URLMacros().parse(self._url)
        try:
            BigWorld.wg_openWebBrowser(processedUrl)
        except (AttributeError, TypeError):
            LOG_CURRENT_EXCEPTION()

        return


@ReprInjector.withParent()
class CustomAction(_Action):

    def __init__(self, action_name, **kwargs):
        super(CustomAction, self).__init__(action_name)
        self.actionID = kwargs.get(b'id') or kwargs.get(b'action_id', -1)
        self.kwargs = kwargs
        return

    def invoke(self, notID, actor=None):
        actor, value = self.__getActor()
        if actor is not None:
            return CustomActionsKeeper.invoke(actor, **self.kwargs)
        else:
            LOG_ERROR(b"Can't find actor for ", str(value))
            return

    def __getActor(self):
        value = self.kwargs.get(b'value', None)
        if isinstance(value, dict):
            return (value.get(b'action_class', None), value)
        else:
            ac = self.kwargs.get(b'action_class', None)
            action = CustomActionsKeeper.getAction(ac or value) or (ac if value != ac else None)
            return (action, value)


@ReprInjector.withParent((b'_target', b'target'))
class OpenWindow(_Action):
    __slots__ = (b'_target',)

    def __init__(self, name, target):
        super(OpenWindow, self).__init__(name)
        self._target = target
        return

    def validate(self, itemsHolder):
        return itemsHolder.getItemByName(self._target) is not None

    def getTarget(self):
        return self._target

    def invoke(self, notID, actor=None):
        g_wgncEvents.onItemShowByAction(notID, self._target)
        return


@ReprInjector.withParent((b'_text', b'text'))
class ReplaceButtons(_Action):
    __slots__ = (b'_text',)

    def __init__(self, name, text):
        super(ReplaceButtons, self).__init__(name)
        self._text = text
        return

    def getTextToReplace(self):
        return self._text

    def invoke(self, notID, actor=None):
        if not actor:
            LOG_ERROR(b'GUI item is not found', self)
            return
        if actor.getType() != WGNC_GUI_TYPE.POP_UP:
            LOG_WARNING(b'Hiding buttons is allowed in pup up only', actor, self)
            return
        actor.hideButtons()
        actor.setNote(self._text)
        g_wgncEvents.onItemUpdatedByAction(notID, actor)
        return


def _getActions4String(value):
    seq = value.split(b',')
    for name in seq:
        yield name.strip()

    return


@ReprInjector.simple((b'__actions', b'actions'))
class ActionsHolder(object):
    __slots__ = (b'__actions',)

    def __init__(self, items):
        super(ActionsHolder, self).__init__()
        self.__actions = {item.getName(): item for item in items}
        return

    def clear(self):
        self.__actions.clear()
        return

    def hasAction(self, name):
        return name in self.__actions

    def hasAllActions(self, names):
        for name in _getActions4String(names):
            if not self.hasAction(name):
                return False

        return True

    def getAction(self, name):
        action = None
        if self.hasAction(name):
            action = self.__actions[name]
        return action

    def validate(self, itemsHolder):
        exclude = set()
        for name, action in self.__actions.iteritems():
            if not action.validate(itemsHolder):
                LOG_WARNING(b'Action is invalid', action)
                exclude.add(name)

        for name in exclude:
            self.__actions.pop(name, None)

        return

    def invoke(self, notID, names, actor=None):
        result = False
        if not notID:
            LOG_ERROR(b'ID of notification is not defined', notID)
            return result
        for name in _getActions4String(names):
            if self.hasAction(name):
                action = self.__actions[name]
                action.invoke(notID, actor)
                result = True
            else:
                LOG_ERROR(b'Action is not found', name)

        return result
