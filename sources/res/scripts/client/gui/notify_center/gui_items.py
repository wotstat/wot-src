from collections import namedtuple
from functools import partial
from debug_utils import LOG_WARNING, LOG_DEBUG
from gui.Scaleform.framework import ScopeTemplates
from gui.Scaleform.framework.managers.loaders import GuiImplViewLoadParams
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.poll.poll_view_model import PollViewType
from gui.promo.promo_logger import PromoLogSourceType
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from gui.shared.events import NotifyCenterShowItemEvent, LoadGuiImplViewEvent
from gui.shared.utils.decorators import ReprInjector
from gui.notify_center.client import ClosePollWindowFromPopUp, ClientLogic
from gui.notify_center.errors import ValidationError
from gui.notify_center.events import g_notifyCenterEvents
from gui.notify_center.settings import NOTIFY_CENTER_GUI_TYPE, NOTIFY_CENTER_GUI_INVALID_SEQS, convertToLocalIcon, convertToLocalBG
from helpers import dependency
from ids_generators import SequenceIDGenerator
from skeletons.gui.game_control import IPromoController
_ButtonData = namedtuple(b'_ButtonData', [
 b'label',
 b'action',
 b'visible',
 b'focused'])

@ReprInjector.simple((b'_name', b'name'), (b'_buttons', b'buttons'), (b'_hidden', b'hidden'))
class _GUIItem(object):
    __slots__ = (b'_name', b'_topic', b'_body', b'_note', b'_buttons', b'_hidden')

    def __init__(self, name, body, topic=u'', buttons=None, hidden=True):
        super(_GUIItem, self).__init__()
        self._name = name
        self._body = body
        self._topic = topic
        self._note = b''
        self._hidden = hidden
        self._buttons = []
        if buttons:
            for idx, (label, actions) in enumerate(buttons):
                self._buttons.append(_ButtonData(label, actions, True, idx == 0))

        return

    def getName(self):
        return self._name

    def getBody(self):
        return self._body

    def getTopic(self):
        return self._topic

    def getNote(self):
        return self._note

    def setNote(self, note):
        self._note = note
        return

    def getButtons(self):
        return self._buttons

    def getButtonsMap(self):
        return [b._asdict() for b in self.getButtons()]

    def getSubmitButton(self):
        if self._buttons:
            return self._buttons[0]
        else:
            return

    def getCancelButton(self):
        if len(self._buttons) > 1:
            return self._buttons[-1]
        else:
            return

    def hideButtons(self):
        return

    def isHidden(self):
        return self._hidden

    def setHidden(self, value):
        self._hidden = value
        return

    def getType(self):
        raise NotImplementedError
        return

    def getClientLogic(self):
        return

    def validate(self, actionsHolder):
        for idx, button in enumerate(self._buttons[:]):
            if not actionsHolder.hasAllActions(button.action):
                self._buttons[idx] = self._buttons[idx]._replace(visible=False)
                LOG_WARNING(b'Some actions are not defined for button', button)

        return

    def show(self, notID):
        g_notifyCenterEvents.onItemShowByDefault(notID, self)
        return

    def close(self, notID):
        return


_idGen = SequenceIDGenerator()

@ReprInjector.withParent((b'_priority', b'priority'), (b'_icon', b'icon'), (b'_bg', b'bg'), (b'_group', b'group'), (b'_isNotify', b'isNotify'))
class PopUpItem(_GUIItem):
    __slots__ = (b'_priority', b'_icon', b'_bg', b'_group', b'_isNotify')

    def __init__(self, body, topic, priority, buttons=None, icon=b'information', bg=b'', group=b'info', isNotify=True):
        super(PopUpItem, self).__init__((b'pop-up-{0}').format(_idGen.next()), body, topic, buttons, False)
        self._priority = priority
        self._icon = icon
        self._bg = bg
        self._group = group
        self._isNotify = isNotify
        return

    def hideButtons(self):
        self._buttons = [button._replace(visible=False) for button in self._buttons]
        return

    def getType(self):
        return NOTIFY_CENTER_GUI_TYPE.POP_UP

    def getPriority(self):
        return self._priority

    def getIcon(self):
        return self._icon

    def getLocalIcon(self):
        return convertToLocalIcon(self._icon)

    def getBG(self):
        return self._bg

    def getLocalBG(self):
        return convertToLocalBG(self._bg)

    def getGroup(self):
        return self._group

    def isNotify(self):
        return self._isNotify


@ReprInjector.withParent((b'_modal', b'modal'))
class WindowItem(_GUIItem):
    __slots__ = (b'_modal',)

    def __init__(self, name, body, topic=u'', buttons=None, modal=False, hidden=True):
        super(WindowItem, self).__init__(name, body, topic, buttons, hidden)
        self._modal = modal
        return

    def getType(self):
        return NOTIFY_CENTER_GUI_TYPE.BASIC_WINDOW

    def isModal(self):
        return self._modal

    def show(self, notID):
        LOG_DEBUG(b'WindowItem.show', notID, self._name)
        g_eventBus.handleEvent(NotifyCenterShowItemEvent(notID, self._name, NotifyCenterShowItemEvent.SHOW_BASIC_WINDOW), EVENT_BUS_SCOPE.LOBBY)
        return


@ReprInjector.withParent()
class PollItem(WindowItem):

    def getType(self):
        return NOTIFY_CENTER_GUI_TYPE.COMPLEX_WINDOW

    def getClientLogic(self):
        return ClosePollWindowFromPopUp(self._name)

    def show(self, notID):
        LOG_DEBUG(b'PollItem.show', notID, self._name)
        try:
            target = PollViewType(self._name)
        except ValueError:
            LOG_WARNING((b"View target is invalid, view can't be loaded, target={}").format(self._name))
            return

        from gui.impl.lobby.poll.poll_view import PollView
        layoutID = R.views.lobby.poll.PollView()
        g_eventBus.handleEvent(LoadGuiImplViewEvent(GuiImplViewLoadParams(layoutID=layoutID, viewClass=PollView, scope=ScopeTemplates.VIEW_SCOPE), ctx={b'notID': notID, 
           b'target': target}), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def close(self, notID):
        LOG_DEBUG(b'POllItem.close', notID, self._name)
        g_eventBus.handleEvent(NotifyCenterShowItemEvent(notID, self._name, NotifyCenterShowItemEvent.CLOSE_POLL_WINDOW), EVENT_BUS_SCOPE.LOBBY)
        return

    def validate(self, actionsHolder):
        if len(self._buttons) < 2:
            raise ValidationError((b'Poll item "{0}" must has two buttons.').format(self._name))
        super(PollItem, self).validate(actionsHolder)
        return


class BrowserItem(_GUIItem):
    __slots__ = (b'_handlers', b'__closeCallbacks')
    promoCtrl = dependency.descriptor(IPromoController)
    _CLOSE_CALLBACK_KEY = b'close_window'

    def __init__(self, name, body, topic=u'', handlers=None, buttons=None, hidden=True):
        super(BrowserItem, self).__init__(name, body, topic, buttons, hidden)
        self._handlers = handlers
        if handlers:
            handlersDict = dict(self._handlers)
            self.__closeCallbacks = handlersDict.get(self._CLOSE_CALLBACK_KEY, [])
        else:
            self.__closeCallbacks = []
        return

    def getHandlers(self):
        return self._handlers

    def getType(self):
        return NOTIFY_CENTER_GUI_TYPE.BROWSER

    def show(self, notID):
        LOG_DEBUG(b'BrowserItem.show', notID, self._name)
        url = self._body
        self.promoCtrl.showPromo(url, partial(self.__handleActions, notID), source=PromoLogSourceType.PRMP)
        return

    def __handleActions(self, notID):
        if self.__closeCallbacks:
            g_notifyCenterEvents.onItemActionFired(notID, self.__closeCallbacks, self.getName())
        return


@ReprInjector.simple((b'__items', b'items'))
class GUIHolder(object):
    __slots__ = (b'__items',)

    def __init__(self, items):
        super(GUIHolder, self).__init__()
        self.__items = {item.getType(): item for item in items}
        return

    def clear(self):
        self.__items.clear()
        return

    def all(self):
        return self.__items.itervalues()

    def hasItemType(self, itemType):
        return itemType in self.__items

    def getItemByType(self, itemType):
        item = None
        if self.hasItemType(itemType):
            item = self.__items[itemType]
        return item

    def getItemByName(self, name):
        for item in self.__items.itervalues():
            if item.getName() == name:
                return item

        return

    def getItemsNames(self):
        names = set()
        for item in self.__items.itervalues():
            if item.getType() == NOTIFY_CENTER_GUI_TYPE.POP_UP:
                continue
            names.add(item.getName())

        return names

    def getClientLogic(self):
        seq = []
        for item in self.__items.itervalues():
            itemLogic = item.getClientLogic()
            if itemLogic:
                seq.append(itemLogic)

        if seq:
            logic = ClientLogic(seq)
        else:
            logic = None
        return logic

    def showItem(self, notID, target):
        item = self.getItemByName(target)
        if item:
            item.show(notID)
        return

    def closeItem(self, notID, target):
        item = self.getItemByName(target)
        if item:
            item.close(notID)
        return

    def validate(self, actionsHolder=None):
        combination = sum(self.__items.keys())
        if combination in NOTIFY_CENTER_GUI_INVALID_SEQS:
            raise ValidationError((b'Combination of GUI items is not valid: {0}').format(combination))
        if not actionsHolder:
            return
        for _, item in self.__items.iteritems():
            item.validate(actionsHolder)

        return
