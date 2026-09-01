import typing, BigWorld
from CurrentVehicle import g_currentVehicle
from PlayerEvents import g_playerEvents
from constants import DEFAULT_HANGAR_SCENE
from debug_utils import LOG_ERROR
from frameworks.wulf import WindowLayer
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework.managers.containers import POP_UP_CRITERIA
from gui.Scaleform.locale.INVITES import INVITES
from gui.clans.formatters import ClanAppActionHtmlTextFormatter, ClanMultiNotificationsHtmlTextFormatter, ClanSingleNotificationHtmlTextFormatter
from gui.clans.settings import CLAN_APPLICATION_STATES, CLAN_INVITE_STATES
from gui.customization.shared import isVehicleCanBeCustomized
from gui.impl import backport
from gui.impl.gen import R
from gui.prb_control import prbInvitesProperty
from gui.prb_control.formatters.invites import getPrbInviteHtmlFormatter
from gui.server_events.recruit_helper import getNewRecruitsCounter
from gui.shared import EVENT_BUS_SCOPE, g_eventBus
from gui.shared.events import HangarSpacesSwitcherEvent, ViewEventType
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.notifications import NotificationGroup, NotificationGuiSettings, NotificationPriorityLevel
from gui.shared.system_factory import collectCustomizationHangarDecorator, collectC11nMessageLockAliases
from gui.shared.utils.functions import makeTooltip
from gui.wgnc.settings import WGNC_DEFAULT_ICON, WGNC_POP_UP_BUTTON_WIDTH
from helpers import dependency, time_utils
from helpers.events_handler import EventsHandler
from items import makeIntCompactDescrByID
from items.components.c11n_constants import CustomizationType
from messenger import g_settings
from messenger.formatters.service_channel_helpers import getPMAdvancedOperationAndQuest
from messenger.formatters.users_messages import makeFriendshipRequestText
from messenger.m_constants import PROTO_TYPE
from messenger.proto import proto_getter
from messenger.proto.xmpp.xmpp_constants import XMPP_ITEM_TYPE
from notification.settings import NOTIFICATION_BUTTON_STATE, NOTIFICATION_TYPE, makePathToIcon
from personal_missions import PM_BRANCH, PM_SWITCHES
from pet_system_common import pet_constants
from shared_utils import first
from skeletons.gui.battle_matters import IBattleMattersController
from skeletons.gui.challenges import IChallengesController
from skeletons.gui.game_control import IBattlePassController, ICollectionsSystemController, IHangarSpaceSwitchController, ILootBoxSystemController, IMapboxController, ISeniorityAwardsController
from skeletons.gui.app_loader import IAppLoader
from skeletons.gui.impl import IGuiLoader
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.pet_system import IPetSystemController
from skeletons.gui.shared import IItemsCache
from skeletons.gui.web import IWebController
if typing.TYPE_CHECKING:
    from gui.shared.events import LoadViewEvent

def _makeShowTime():
    return BigWorld.time()


_ICONS_FIELDS = (b'icon', b'defaultIcon', b'bgIcon')

def _getClanName(clanInfo):
    return (b'[{}] {}').format(clanInfo[1], clanInfo[0])


class _NotificationDecorator(EventsHandler):
    __slots__ = (b'_entityID', b'_entity', b'_settings', b'_vo', b'_isOrderChanged')

    def __init__(self, entityID, entity=None, settings=None):
        super(_NotificationDecorator, self).__init__()
        self._isOrderChanged = False
        self._entityID = entityID
        self._entity = entity
        self._settings = settings
        self._make(entity, settings)
        self._subscribe()
        return

    def __repr__(self):
        return (b'{0:>s}(typeID = {1:n}, entityID = {2:n})').format(self.__class__.__name__, self.getType(), self.getID())

    def __cmp__(self, other):
        if isinstance(other, _NotificationDecorator):
            return cmp(self.getOrder(), other.getOrder())
        return -1

    def __eq__(self, other):
        return isinstance(other, _NotificationDecorator) and self.getType() == other.getType() and self.getID() == other.getID()

    def clear(self):
        self._unsubscribe()
        self._entityID = 0
        self._entity = None
        self._vo.clear()
        self._settings = None
        return

    def getID(self):
        return self._entityID

    def getEntity(self):
        return self._entity

    def getSavedData(self):
        return

    def getType(self):
        return NOTIFICATION_TYPE.UNDEFINED

    @staticmethod
    def isPinned():
        return False

    def getGroup(self):
        return NotificationGroup.INFO

    def getSettings(self):
        return self._settings

    def getPriorityLevel(self):
        if self._settings:
            return self._settings.priorityLevel
        return NotificationPriorityLevel.MEDIUM

    def isAlert(self):
        result = False
        if self._settings:
            result = self._settings.isAlert
        return result

    def isNotify(self):
        result = False
        if self._settings:
            result = self._settings.isNotify
        return result

    def showAt(self):
        if self._settings:
            result = self._settings.showAt
        else:
            result = _makeShowTime()
        return result

    def isOrderChanged(self):
        return self._isOrderChanged

    def isShouldCountOnlyOnce(self):
        return False

    def update(self, entity):
        self._entity = entity
        return

    def getListVO(self, newId=None):
        vo = self._vo.copy()
        if newId is not None:
            vo[b'entityID'] = newId
        return vo

    def getPopUpVO(self, newId=None):
        vo = self.getListVO(newId)
        lifeTime = 0
        if self._settings is not None:
            lifeTime = vo[b'message'].get(b'lifeTime', 0) or self._settings.lifeTime or getattr(self._settings.auxData, b'timeoutMS', 0)
        settings = g_settings.lobby.serviceChannel
        if self.getPriorityLevel() == NotificationPriorityLevel.HIGH:
            vo[b'lifeTime'] = lifeTime or settings.highPriorityMsgLifeTime
            vo[b'hidingAnimationSpeed'] = settings.highPriorityMsgAlphaSpeed
        else:
            vo[b'lifeTime'] = lifeTime or settings.mediumPriorityMsgLifeTime
            vo[b'hidingAnimationSpeed'] = settings.mediumPriorityMsgAlphaSpeed
        return vo

    def getButtonLayout(self):
        return tuple()

    def getOrder(self):
        return (
         self.showAt(), 0)

    def _make(self, entity=None, settings=None):
        self._vo = {}
        self._settings = settings
        return

    def getCounterInfo(self):
        return (self.getGroup(), self.getType(), self.getID(), self.isShouldCountOnlyOnce())

    def decrementCounterOnHidden(self):
        return True


class SearchCriteria(_NotificationDecorator):
    __slots__ = (b'_typeID',)

    def __init__(self, typeID, itemID):
        super(SearchCriteria, self).__init__(itemID)
        self._typeID = typeID
        return

    def clear(self):
        super(SearchCriteria, self).clear()
        self._typeID = 0
        return

    def getType(self):
        return self._typeID


class MessageDecorator(_NotificationDecorator):

    def __init__(self, entityID, entity=None, settings=None, model=None):
        self._model = model
        super(MessageDecorator, self).__init__(entityID, entity, settings)
        return

    def getSavedData(self):
        return self._vo[b'message'].get(b'savedData')

    def getType(self):
        return NOTIFICATION_TYPE.MESSAGE

    def getGroup(self):
        return self._settings.groupID

    def update(self, formatted):
        super(MessageDecorator, self).update(formatted)
        self._make(formatted)
        return

    def getOrder(self):
        return (self.showAt(), self._entityID)

    def _make(self, formatted=None, settings=None):
        if settings:
            self._settings = settings
            if not self._settings.showAt:
                self._settings.showAt = _makeShowTime()
        message = formatted.copy() if formatted else {}
        for key in _ICONS_FIELDS:
            if key in message:
                message[key] = makePathToIcon(message[key])
            else:
                message[key] = b''

        self._vo = {b'typeID': (self.getType()), b'entityID': (self.getID()), 
           b'message': message, 
           b'notify': (self.isNotify())}
        return


class LowPriorityDecorator(MessageDecorator):

    def __init__(self, entityID, entity=None, settings=None, model=None):
        if settings is None:
            settings = NotificationGuiSettings(isNotify=True)
        settings.priorityLevel = NotificationPriorityLevel.LOW
        super(LowPriorityDecorator, self).__init__(entityID, entity, settings, model)
        return


class RecruitReminderMessageDecorator(MessageDecorator):

    def __init__(self, entityID, message, savedData, msgPrLevel=NotificationPriorityLevel.LOW):
        entity = g_settings.msgTemplates.format(b'RecruitReminder', ctx={b'text': message}, data={b'savedData': savedData})
        settings = NotificationGuiSettings(isNotify=getNewRecruitsCounter() > 0, priorityLevel=msgPrLevel)
        super(RecruitReminderMessageDecorator, self).__init__(entityID, entity, settings)
        return

    def isShouldCountOnlyOnce(self):
        return True

    def getType(self):
        return NOTIFICATION_TYPE.RECRUIT_REMINDER

    def getGroup(self):
        return NotificationGroup.OFFER

    def getSavedData(self):
        return self._vo[b'message'].get(b'savedData', {})

    def update(self, formatted):
        _NotificationDecorator.update(self, formatted)
        settings = NotificationGuiSettings(isNotify=getNewRecruitsCounter() > 0, priorityLevel=self.getPriorityLevel())
        super(RecruitReminderMessageDecorator, self)._make(formatted, settings)
        return


class EmailConfirmationReminderMessageDecorator(MessageDecorator):

    def __init__(self, entityID, message):
        entity = g_settings.msgTemplates.format(b'EmailConfirmationReminder', ctx={b'text': message})
        settings = NotificationGuiSettings(isNotify=True)
        super(EmailConfirmationReminderMessageDecorator, self).__init__(entityID, entity, settings)
        return

    def isShouldCountOnlyOnce(self):
        return True

    def getType(self):
        return NOTIFICATION_TYPE.EMAIL_CONFIRMATION_REMINDER

    def getGroup(self):
        return NotificationGroup.OFFER


class LockButtonMessageDecorator(MessageDecorator):

    def __init__(self, entityID, entity=None, settings=None, model=None):
        super(LockButtonMessageDecorator, self).__init__(entityID, entity, settings, model)
        g_eventBus.addListener(ViewEventType.LOAD_VIEW, self._viewLoaded, EVENT_BUS_SCOPE.LOBBY)
        g_eventBus.addListener(ViewEventType.LOAD_GUI_IMPL_VIEW, self._viewLoaded, EVENT_BUS_SCOPE.LOBBY)
        g_playerEvents.onEnqueued += self._onEqueued
        g_playerEvents.onDequeued += self._onDequeued
        return

    def clear(self):
        super(LockButtonMessageDecorator, self).clear()
        g_eventBus.removeListener(ViewEventType.LOAD_VIEW, self._viewLoaded, EVENT_BUS_SCOPE.LOBBY)
        g_eventBus.removeListener(ViewEventType.LOAD_GUI_IMPL_VIEW, self._viewLoaded, EVENT_BUS_SCOPE.LOBBY)
        g_playerEvents.onEnqueued -= self._onEqueued
        g_playerEvents.onDequeued -= self._onDequeued
        return

    def update(self, formatted):
        _NotificationDecorator.update(self, formatted)
        return

    def _onEqueued(self, _):
        self._updateButtonsState(lock=True)
        return

    def _onDequeued(self, _):
        self._updateButtonsState(lock=False)
        return

    def _make(self, formatted=None, settings=None):
        super(LockButtonMessageDecorator, self)._make(formatted, settings)
        self._updateButtons(None)
        return

    def _getLockAliases(self):
        return ()

    def _getButtonType(self):
        return b'submit'

    def _updateButtons(self, _):
        self._updateButtonsState(lock=False)
        return

    def _viewLoaded(self, event):
        if event.alias in self._getLockAliases():
            self._updateButtonsState(lock=True)
        else:
            from gui.lobby_state_machine.states import isInHangarState
            if isInHangarState():
                self._updateButtons(None)
        return

    def _updateButtonsState(self, lock=False):
        if self._entity is None or not self._entity.get(b'buttonsLayout'):
            return
        state = self._getBtnState(lock)
        btnType = self._getButtonType()
        self._entity.setdefault(b'buttonsStates', {}).update({btnType: state})
        if self._model is not None:
            self._model.updateNotification(self.getType(), self._entityID, self._entity, False)
        return

    def _getBtnState(self, lock):
        if lock:
            return NOTIFICATION_BUTTON_STATE.VISIBLE
        return NOTIFICATION_BUTTON_STATE.DEFAULT


class C11nMessageDecorator(LockButtonMessageDecorator):
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, entityID, entity=None, settings=None, model=None):
        super(C11nMessageDecorator, self).__init__(entityID, entity, settings, model)
        g_clientUpdateManager.addCallbacks({b'inventory': (self._updateButtons), 
           b'cache.vehsLock': (self._updateButtons)})
        g_eventBus.addListener(HangarSpacesSwitcherEvent.SWITCH_TO_HANGAR_SPACE, self._changeHangarSpace, EVENT_BUS_SCOPE.LOBBY)
        return

    def clear(self):
        super(C11nMessageDecorator, self).clear()
        g_clientUpdateManager.removeObjectCallbacks(self)
        g_eventBus.removeListener(HangarSpacesSwitcherEvent.SWITCH_TO_HANGAR_SPACE, self._changeHangarSpace, EVENT_BUS_SCOPE.LOBBY)
        return

    def _updateButtons(self, *_):
        self._updateButtonsState(lock=self._getIsLocked())
        return

    def _changeHangarSpace(self, *args, **kwargs):
        self._updateButtonsState(lock=self._getIsLocked())
        return

    def _onDequeued(self, _):
        self._updateButtonsState(lock=self._getIsLocked())
        return

    def _getLockAliases(self):
        return (VIEW_ALIAS.HERO_VEHICLE_PREVIEW,) + tuple(collectC11nMessageLockAliases()) + super(C11nMessageDecorator, self)._getLockAliases()

    def _getIsLocked(self):
        isLocked = True
        if any(handler() for handler in collectCustomizationHangarDecorator()):
            return isLocked
        else:
            vehicle = self._getVehicle()
            if vehicle is not None and vehicle.isCustomizationEnabled():
                isLocked = self._entity.get(b'savedData', {}).get(b'toStyle', False) and not isVehicleCanBeCustomized(vehicle, GUI_ITEM_TYPE.STYLE)
            return isLocked

    def _getVehicle(self):
        vehicle = None
        if self.itemsCache is not None and self.itemsCache.isSynced():
            savedData = self._entity.get(b'savedData')
            if savedData is not None:
                vehicleIntCD = savedData.get(b'vehicleIntCD')
                if vehicleIntCD is not None:
                    vehicle = self.itemsCache.items.getItemByCD(vehicleIntCD)
        return vehicle


class C11nProgressiveItemDecorator(C11nMessageDecorator):
    lockedButtonTooltip = makeTooltip(body=backport.text(R.strings.vehicle_customization.progressiveItemReward.gotoCustomizationButton.disabled.tooltip()))

    def _updateButtonsState(self, lock=False):
        super(C11nProgressiveItemDecorator, self)._updateButtonsState(lock)
        self.__setTooltip(lock)
        return

    def __setTooltip(self, isLocked):
        if self._entity is None:
            return
        else:
            buttonsLayout = self._entity.get(b'buttonsLayout')
            if isLocked and not buttonsLayout[0].get(b'tooltip'):
                tooltip = self.lockedButtonTooltip
                buttonsLayout[0][b'tooltip'] = tooltip
            if not isLocked and buttonsLayout[0].get(b'tooltip'):
                buttonsLayout[0][b'tooltip'] = b''
            return


class C2DProgressionStyleDecorator(C11nMessageDecorator):

    def __init__(self, entityID, entity=None, settings=None, model=None):
        super(C2DProgressionStyleDecorator, self).__init__(entityID, entity, settings, model)
        g_currentVehicle.onChanged += self._updateButtons
        return

    def clear(self):
        g_currentVehicle.onChanged -= self._updateButtons
        super(C2DProgressionStyleDecorator, self).clear()
        return

    def _getIsLocked(self):
        isLocked = super(C2DProgressionStyleDecorator, self)._getIsLocked()
        if isLocked:
            return isLocked
        style = self.itemsCache.items.getItemByCD(makeIntCompactDescrByID(b'customizationItem', CustomizationType.STYLE, self._entity[b'savedData'][b'styleID']))
        return not style.mayInstall(self._getVehicle())

    def _getVehicle(self):
        if self.itemsCache is not None and self.itemsCache.isSynced():
            return g_currentVehicle.item
        else:
            return


class PrbInviteDecorator(_NotificationDecorator):
    __slots__ = (b'_createdAt',)

    @prbInvitesProperty
    def prbInvites(self):
        return

    def __init__(self, invite):
        self._createdAt = invite.getCreateTime()
        super(PrbInviteDecorator, self).__init__(invite.clientID, invite)
        return

    def clear(self):
        self._createdAt = 0
        super(PrbInviteDecorator, self).clear()
        return

    def getSavedData(self):
        return self.getID()

    def getType(self):
        return NOTIFICATION_TYPE.INVITE

    def getGroup(self):
        return NotificationGroup.INVITE

    def update(self, entity):
        super(PrbInviteDecorator, self).update(entity)
        self._make(entity)
        return

    def getOrder(self):
        return (self.showAt(), self._createdAt)

    def _make(self, invite=None, settings=None):
        invite = invite or self.prbInvites.getInvite(self._entityID)
        if not invite:
            LOG_ERROR(b'Invite not found', self._entityID)
            self._vo = {}
            self._settings = NotificationGuiSettings(False, NotificationPriorityLevel.LOW, showAt=_makeShowTime())
            return
        if not invite.showAt or invite.isActive():
            if invite.showAt > 0:
                self._isOrderChanged = True
            invite.showAt = _makeShowTime()
        if invite.isActive():
            self._settings = NotificationGuiSettings(True, NotificationPriorityLevel.HIGH, showAt=invite.showAt)
        else:
            self._settings = NotificationGuiSettings(False, NotificationPriorityLevel.LOW, showAt=invite.showAt)
        formatter = getPrbInviteHtmlFormatter(invite)
        canAccept = formatter.canAcceptInvite(invite)
        canDecline = self.prbInvites.canDeclineInvite(invite)
        if canAccept or canDecline:
            submitState = cancelState = NOTIFICATION_BUTTON_STATE.VISIBLE
            if canAccept:
                submitState |= NOTIFICATION_BUTTON_STATE.ENABLED
            if canDecline:
                cancelState |= NOTIFICATION_BUTTON_STATE.ENABLED
        else:
            submitState = cancelState = 0
        message = g_settings.msgTemplates.format(b'invite', ctx={b'text': (formatter.getText(invite))}, data={b'timestamp': (invite.createTime), 
           b'icon': (formatter.getIconPath(invite, pathMaker=makePathToIcon)), 
           b'defaultIcon': (makePathToIcon(b'prebattleInviteIcon')), 
           b'buttonsStates': {b'submit': submitState, 
                              b'cancel': cancelState}})
        message = formatter.updateTooltips(invite, canAccept, message)
        self._vo = {b'typeID': (self.getType()), 
           b'entityID': (self.getID()), 
           b'message': message, 
           b'notify': (self.isNotify()), 
           b'auxData': []}
        return


class FriendshipRequestDecorator(_NotificationDecorator):
    __slots__ = (b'_receivedAt',)

    def __init__(self, user):
        self._receivedAt = None
        super(FriendshipRequestDecorator, self).__init__(user.getID(), entity=user, settings=NotificationGuiSettings(True, NotificationPriorityLevel.HIGH, showAt=_makeShowTime()))
        return

    @proto_getter(PROTO_TYPE.XMPP)
    def proto(self):
        return

    def getType(self):
        return NOTIFICATION_TYPE.FRIENDSHIP_RQ

    def getGroup(self):
        return NotificationGroup.INVITE

    def getOrder(self):
        return (
         self.showAt(), self._receivedAt)

    def update(self, user):
        super(FriendshipRequestDecorator, self).update(user)
        self._make(user=user, settings=NotificationGuiSettings(False, NotificationPriorityLevel.LOW, showAt=self.showAt()))
        return

    def _make(self, user=None, settings=None):
        if settings:
            self._settings = settings
        contacts = self.proto.contacts
        if user.getItemType() in XMPP_ITEM_TYPE.SUB_PENDING_ITEMS:
            self._receivedAt = user.getItem().receivedAt()
        canCancel, error = contacts.canCancelFriendship(user)
        if canCancel:
            canApprove, error = contacts.canApproveFriendship(user)
        else:
            canApprove = False
        if canApprove or canCancel:
            submitState = cancelState = NOTIFICATION_BUTTON_STATE.VISIBLE
            if canApprove:
                submitState |= NOTIFICATION_BUTTON_STATE.ENABLED
            if canCancel:
                cancelState |= NOTIFICATION_BUTTON_STATE.ENABLED
            self._settings.isNotify = True
            self._settings.priorityLevel = NotificationPriorityLevel.HIGH
        else:
            submitState = cancelState = NOTIFICATION_BUTTON_STATE.HIDDEN
        message = g_settings.msgTemplates.format(b'friendshipRequest', ctx={b'text': (makeFriendshipRequestText(user, error))}, data={b'timestamp': (self._receivedAt), 
           b'icon': (makePathToIcon(b'friendshipIcon')), 
           b'buttonsStates': {b'submit': submitState, 
                              b'cancel': cancelState}})
        self._vo = {b'typeID': (self.getType()), 
           b'entityID': (self.getID()), 
           b'message': message, 
           b'notify': (self.isNotify()), 
           b'auxData': []}
        return


class WGNCPopUpDecorator(_NotificationDecorator):
    __slots__ = (b'_itemName', b'__receivedAt')

    def __init__(self, entityID, item, offset=0, receivedAt=None):
        super(WGNCPopUpDecorator, self).__init__(entityID, item, NotificationGuiSettings(item.isNotify(), item.getPriority(), showAt=_makeShowTime() + offset))
        self.__receivedAt = receivedAt
        return

    def getType(self):
        return NOTIFICATION_TYPE.WGNC_POP_UP

    def getGroup(self):
        return self.getEntity().getGroup()

    def getOrder(self):
        timeCriteria = self.__receivedAt or self.showAt()
        return (timeCriteria, self._entityID)

    def getSavedData(self):
        return self._itemName

    def update(self, item):
        super(WGNCPopUpDecorator, self).update(item)
        self._make(item)
        return

    def _make(self, item=None, settings=None):
        self._itemName = item.getName()
        if settings:
            self._settings = settings
        layout, states = self._makeButtonsLayout(item)
        topic = item.getTopic()
        if topic:
            topic = g_settings.htmlTemplates.format(b'notificationsCenterTopic', ctx={b'topic': topic})
        body = item.getBody()
        note = item.getNote()
        if note:
            body += g_settings.htmlTemplates.format(b'notificationsCenterNote', ctx={b'note': note})
        bgSource, (_, bgHeight) = item.getLocalBG()
        message = g_settings.msgTemplates.format(b'wgncNotification_v2', ctx={b'topic': topic, 
           b'body': body}, data={b'icon': (makePathToIcon(item.getLocalIcon())), 
           b'defaultIcon': (makePathToIcon(WGNC_DEFAULT_ICON)), 
           b'bgIcon': {None: (makePathToIcon(bgSource))}, b'bgIconHeight': bgHeight, 
           b'buttonsLayout': layout, 
           b'buttonsStates': states})
        self._vo = {b'typeID': (self.getType()), 
           b'entityID': (self.getID()), 
           b'message': message, 
           b'notify': (self.isNotify()), 
           b'auxData': []}
        return

    def _makeButtonsLayout(self, item):
        layout = []
        states = {}
        seq = [
         b'submit', b'cancel']
        for _, button in enumerate(item.getButtons()):
            if not seq:
                LOG_ERROR(b'Button is ignored to display', button)
                continue
            buttonType = seq.pop(0)
            layout.append({b'label': (button.label), 
               b'type': buttonType, 
               b'action': (button.action), 
               b'width': WGNC_POP_UP_BUTTON_WIDTH})
            if button.visible:
                state = NOTIFICATION_BUTTON_STATE.ENABLED | NOTIFICATION_BUTTON_STATE.VISIBLE
            else:
                state = NOTIFICATION_BUTTON_STATE.HIDDEN
            states[buttonType] = state

        return (layout, states)


class _ClanBaseDecorator(_NotificationDecorator):
    __slots__ = (b'_createdAt',)

    def __init__(self, entityID, entity=None, settings=None):
        self._createdAt = time_utils.getCurrentTimestamp()
        super(_ClanBaseDecorator, self).__init__(entityID, entity, settings)
        return

    def clear(self):
        self._createdAt = 0
        super(_ClanBaseDecorator, self).clear()
        return

    def getOrder(self):
        return (self.showAt(), self._createdAt)

    def getSavedData(self):
        return self.getID()

    def getGroup(self):
        return NotificationGroup.INVITE


class _ClanDecorator(_ClanBaseDecorator):
    clanCtrl = dependency.descriptor(IWebController)

    def __init__(self, entityID, entity=None, settings=None):
        self._settings = None
        super(_ClanDecorator, self).__init__(entityID, entity, settings)
        return

    def update(self, entity):
        super(_ClanBaseDecorator, self).update(entity)
        self._make(entity)
        return

    def _make(self, entity=None, settings=None):
        if self._settings is None:
            self._settings = NotificationGuiSettings(True, NotificationPriorityLevel.MEDIUM, showAt=_makeShowTime())
        formatter = self._getFormatter()
        message = g_settings.msgTemplates.format(self._getTemplateId(), ctx={b'text': (self._getText(formatter, entity))}, data={b'timestamp': (self._createdAt), 
           b'icon': (makePathToIcon(b'clanInviteIcon')), 
           b'defaultIcon': (makePathToIcon(b'InformationIcon')), 
           b'buttonsStates': (self._getButtonsStates(entity))})
        self._vo = {b'typeID': (self.getType()), 
           b'entityID': (self.getID()), 
           b'message': message, 
           b'notify': (self.isNotify()), 
           b'auxData': []}
        return

    def _getFormatter(self):
        raise NotImplementedError
        return

    def _getText(self, formatter, entity):
        return formatter.getText(entity)

    def _getTemplateId(self):
        raise NotImplementedError
        return

    def _getButtonsStates(self, entity):
        raise NotImplementedError
        return


class _ClanSingleDecorator(_ClanDecorator):

    def __init__(self, entityID, entity=None, settings=None):
        self._state = self._getDefState()
        super(_ClanSingleDecorator, self).__init__(entityID, entity, settings)
        return

    def setState(self, value):
        self._state = value
        return

    def _getDefState(self):
        raise NotImplementedError
        return


class ClanSingleAppDecorator(_ClanSingleDecorator):

    def __init__(self, entityID, entity=None, settings=None, userName=None):
        self.__userName = userName
        self.__isInClanEnterCooldown = False
        super(ClanSingleAppDecorator, self).__init__(entityID, entity, settings)
        return

    def setUserName(self, value):
        self.__userName = value
        return

    def setClanEnterCooldown(self, value):
        self.__isInClanEnterCooldown = value
        return

    def getUserName(self):
        return self.__userName

    def getType(self):
        return NOTIFICATION_TYPE.CLAN_APP

    def getAccountID(self):
        return self._entity.getAccountID()

    def getApplicationID(self):
        return self._entity.getApplicationID()

    def _getTemplateId(self):
        return b'clanApp'

    def _getDefState(self):
        return CLAN_APPLICATION_STATES.ACTIVE

    def _getFormatter(self):
        return ClanSingleNotificationHtmlTextFormatter(b'appTitle', b'appComment', b'showUserProfileAction')

    def _getButtonsStates(self, entity):
        if self._state in (CLAN_APPLICATION_STATES.ACCEPTED, CLAN_APPLICATION_STATES.DECLINED) or not self.clanCtrl.getAccountProfile().getMyClanPermissions().canHandleClanInvites() or not self.clanCtrl.isEnabled() or self.__isInClanEnterCooldown:
            submit = cancel = NOTIFICATION_BUTTON_STATE.HIDDEN
        elif not self.clanCtrl.isAvailable():
            submit = cancel = NOTIFICATION_BUTTON_STATE.VISIBLE
        else:
            submit = cancel = NOTIFICATION_BUTTON_STATE.DEFAULT
        return {b'submit': submit, 
           b'cancel': cancel}

    def _getText(self, formatter, entity):
        if self.__isInClanEnterCooldown:
            stateStr = INVITES.CLANS_STATE_APP_ERROR_INCLANENTERCOOLDOWN
            isWarning = True
        else:
            stateStr = b'#invites:clans/state/app/%s' % self._state
            isWarning = False
        return formatter.getText((self.__userName, stateStr, isWarning))


class ClanSingleInviteDecorator(_ClanSingleDecorator):

    def getInviteID(self):
        return self._entity.getInviteId()

    def getClanID(self):
        return self._entity.getClanId()

    def getClanAbbrev(self):
        return self._entity.getClanTag()

    def getType(self):
        return NOTIFICATION_TYPE.CLAN_INVITE

    def _getTemplateId(self):
        return b'clanInvite'

    def _getDefState(self):
        return CLAN_INVITE_STATES.ACTIVE

    def _getFormatter(self):
        return ClanSingleNotificationHtmlTextFormatter(b'inviteTitle', b'inviteComment', b'showClanProfileAction')

    def _getButtonsStates(self, entity):
        if self._state in (CLAN_INVITE_STATES.ACCEPTED, CLAN_INVITE_STATES.DECLINED) or self.clanCtrl.getAccountProfile().isInClan() or not self.clanCtrl.isEnabled() or self.__isInClanEnterCooldown():
            submit = cancel = NOTIFICATION_BUTTON_STATE.HIDDEN
        elif not self.clanCtrl.isAvailable():
            submit = cancel = NOTIFICATION_BUTTON_STATE.VISIBLE
        else:
            submit = cancel = NOTIFICATION_BUTTON_STATE.DEFAULT
        return {b'submit': submit, 
           b'cancel': cancel}

    def _getText(self, formatter, entity):
        if self.__isInClanEnterCooldown():
            isWarning = True
            stateStr = INVITES.CLANS_STATE_INVITE_ERROR_INCLANENTERCOOLDOWN
        else:
            isWarning = False
            stateStr = b'#invites:clans/state/invite/%s' % self._state
        return formatter.getText((_getClanName((entity.getClanName(), entity.getClanTag())), stateStr, isWarning))

    def __isInClanEnterCooldown(self):
        profile = self.clanCtrl.getAccountProfile()
        return not profile.isInClan() and profile.isInClanEnterCooldown()


class _ClanMultiDecorator(_ClanDecorator):

    def _getButtonsStates(self, entity):
        if not self.clanCtrl.isEnabled():
            submit = NOTIFICATION_BUTTON_STATE.HIDDEN
        elif not self.clanCtrl.isAvailable():
            submit = NOTIFICATION_BUTTON_STATE.VISIBLE
        else:
            submit = NOTIFICATION_BUTTON_STATE.DEFAULT
        return {b'submit': submit}


class ClanAppsDecorator(_ClanMultiDecorator):

    def getType(self):
        return NOTIFICATION_TYPE.CLAN_APPS

    def _getTemplateId(self):
        return b'clanApps'

    def _getFormatter(self):
        return ClanMultiNotificationsHtmlTextFormatter(b'appsTitle', b'multiAppsCommon', b'showClanSettingsAction')


class ClanInvitesDecorator(_ClanMultiDecorator):

    def getType(self):
        return NOTIFICATION_TYPE.CLAN_INVITES

    def _getTemplateId(self):
        return b'clanPersonalInvites'

    def _getFormatter(self):
        return ClanMultiNotificationsHtmlTextFormatter(b'invitesTitle', b'multiAppsCommon', b'showClanSettingsAction')


class _ClassBaseActionDecorator(_ClanBaseDecorator):

    def __init__(self, entityID, actionType, userName=None, settings=None):
        self._actionType = actionType
        super(_ClassBaseActionDecorator, self).__init__(entityID, userName, settings)
        return

    def _getName(self, entity):
        raise NotImplementedError
        return

    def _make(self, entity=None, settings=None):
        self._settings = NotificationGuiSettings(True, NotificationPriorityLevel.MEDIUM, showAt=_makeShowTime())
        name = self._getName(entity)
        formatter = ClanAppActionHtmlTextFormatter(self._actionType)
        message = g_settings.msgTemplates.format(b'clanSimple', ctx={b'text': (formatter.getText(name))}, data={b'timestamp': (self._createdAt), 
           b'icon': (makePathToIcon(b'clanInviteIcon')), 
           b'defaultIcon': (makePathToIcon(b'InformationIcon'))})
        self._vo = {b'typeID': (self.getType()), 
           b'entityID': (self.getID()), 
           b'message': message, 
           b'notify': (self.isNotify()), 
           b'auxData': []}
        return


class ClanAppActionDecorator(_ClassBaseActionDecorator):

    def getType(self):
        return NOTIFICATION_TYPE.CLAN_APP_ACTION

    def _getName(self, clanInfo):
        return _getClanName(clanInfo)


class ClanInvitesActionDecorator(_ClassBaseActionDecorator):

    def setUserName(self, value):
        self._entity = value
        return

    def getType(self):
        return NOTIFICATION_TYPE.CLAN_INVITE_ACTION

    def update(self, formatted):
        super(ClanInvitesActionDecorator, self).update(formatted)
        self._make(formatted)
        return

    def _getName(self, entity):
        return entity


class ProgressiveRewardDecorator(_NotificationDecorator):
    ENTITY_ID = 0

    def __init__(self):
        super(ProgressiveRewardDecorator, self).__init__(self.ENTITY_ID)
        return

    def getType(self):
        return NOTIFICATION_TYPE.PROGRESSIVE_REWARD

    def getGroup(self):
        return NotificationGroup.OFFER

    def update(self, entity):
        super(ProgressiveRewardDecorator, self).update(entity)
        self._make(entity)
        return

    def decrementCounterOnHidden(self):
        return False

    def _make(self, entity=None, settings=None):
        self._settings = NotificationGuiSettings(isNotify=True, priorityLevel=NotificationPriorityLevel.MEDIUM)
        message = g_settings.msgTemplates.format(b'ProgressiveRewardNotification', data={b'icon': (makePathToIcon(b'InformationIcon'))})
        self._vo = {b'typeID': (self.getType()), 
           b'entityID': (self.getID()), 
           b'message': message, 
           b'notify': (self.isNotify()), 
           b'auxData': []}
        return


class MissingEventsDecorator(_NotificationDecorator):
    ENTITY_ID = 0

    def __init__(self, count):
        super(MissingEventsDecorator, self).__init__(self.ENTITY_ID, count)
        return

    def getType(self):
        return NOTIFICATION_TYPE.MISSING_EVENTS

    def getGroup(self):
        return NotificationGroup.OFFER

    @staticmethod
    def isPinned():
        return True

    def update(self, entity):
        super(MissingEventsDecorator, self).update(entity)
        self._make(entity)
        return

    def decrementCounterOnHidden(self):
        return False

    def _make(self, entity=None, settings=None):
        self._settings = NotificationGuiSettings(isNotify=True, priorityLevel=NotificationPriorityLevel.HIGH)
        message = g_settings.msgTemplates.format(b'MissingEventsNotification', ctx={b'count': entity})
        message[b'icon'] = makePathToIcon(message[b'icon'])
        self._vo = {b'typeID': (self.getType()), 
           b'entityID': (self.getID()), 
           b'message': message, 
           b'notify': (self.isNotify()), 
           b'auxData': []}
        return


class BattlePassSwitchChapterReminderDecorator(MessageDecorator):

    def __init__(self, entityID, message):
        super(BattlePassSwitchChapterReminderDecorator, self).__init__(entityID, self.__makeEntity(message), self.__makeSettings())
        return

    def isShouldCountOnlyOnce(self):
        return True

    def getGroup(self):
        return NotificationGroup.OFFER

    def getType(self):
        return NOTIFICATION_TYPE.BATTLE_PASS_SWITCH_CHAPTER_REMINDER

    def __makeEntity(self, message):
        return g_settings.msgTemplates.format(b'BattlePassSwitchChapterReminder', ctx={b'text': message})

    def __makeSettings(self):
        return NotificationGuiSettings(isNotify=True, priorityLevel=NotificationPriorityLevel.LOW)


class BattlePassLockButtonDecorator(MessageDecorator):
    __battlePassController = dependency.descriptor(IBattlePassController)

    def __init__(self, entityID, entity=None, settings=None, model=None):
        super(BattlePassLockButtonDecorator, self).__init__(entityID, entity, settings, model)
        self.__battlePassController.onBattlePassSettingsChange += self.__update
        self.__battlePassController.onSeasonStateChanged += self.__update
        return

    def clear(self):
        self.__battlePassController.onBattlePassSettingsChange -= self.__update
        self.__battlePassController.onSeasonStateChanged -= self.__update
        super(BattlePassLockButtonDecorator, self).clear()
        return

    def _make(self, formatted=None, settings=None):
        self.__updateEntityButtons()
        super(BattlePassLockButtonDecorator, self)._make(formatted, settings)
        return

    def __updateEntityButtons(self):
        if self._entity is None:
            return
        else:
            buttonsLayout = self._entity.get(b'buttonsLayout')
            if not buttonsLayout:
                return
            if self.__battlePassController.isActive():
                state, tooltip = NOTIFICATION_BUTTON_STATE.DEFAULT, b''
            else:
                state = NOTIFICATION_BUTTON_STATE.VISIBLE
                tooltip = makeTooltip(body=backport.text(R.strings.system_messages.battlePass.switch_pause.body()))
            buttonsStates = self._entity.get(b'buttonsStates')
            if buttonsStates is None:
                return
            buttonsStates[b'submit'] = state
            buttonsLayout[0][b'tooltip'] = tooltip
            return

    def __update(self, *_):
        self.__updateEntityButtons()
        if self._model is not None:
            self._model.updateNotification(self.getType(), self._entityID, self._entity, False)
        return


class MapboxButtonDecorator(MessageDecorator):
    __mapboxCtrl = dependency.descriptor(IMapboxController)

    def __init__(self, entityID, entity=None, settings=None, model=None):
        super(MapboxButtonDecorator, self).__init__(entityID, entity, settings, model)
        self.__mapboxCtrl.onPrimeTimeStatusUpdated += self.__update
        return

    def clear(self):
        self.__mapboxCtrl.onPrimeTimeStatusUpdated -= self.__update
        super(MapboxButtonDecorator, self).clear()
        return

    def _make(self, formatted=None, settings=None):
        self.__updateButtons()
        super(MapboxButtonDecorator, self)._make(formatted, settings)
        return

    def __updateButtons(self):
        if self._entity is None:
            return
        else:
            buttonsLayout = self._entity.get(b'buttonsLayout')
            buttonsStates = self._entity.get(b'buttonsStates')
            if not buttonsLayout or buttonsStates is None:
                return
            if self.__mapboxCtrl.isActive():
                state, tooltip = NOTIFICATION_BUTTON_STATE.DEFAULT, b''
            else:
                state = NOTIFICATION_BUTTON_STATE.VISIBLE
                tooltip = makeTooltip(body=backport.text(R.strings.mapbox.buttonDisable.tooltip()))
            buttonsStates[b'submit'] = state
            buttonsLayout[0][b'tooltip'] = tooltip
            return

    def __update(self, *_):
        self.__updateButtons()
        if self._model is not None:
            self._model.updateNotification(self.getType(), self._entityID, self._entity, False)
        return


class IntegratedAuctionDecorator(MessageDecorator):
    __OVERLAYS = (
     WindowLayer.FULLSCREEN_WINDOW, WindowLayer.OVERLAY, WindowLayer.TOP_WINDOW)
    __gui = dependency.descriptor(IGuiLoader)

    def __init__(self, entityID):
        super(IntegratedAuctionDecorator, self).__init__(entityID, self._makeEntity(), self._makeSettings())
        return

    def getGroup(self):
        return NotificationGroup.INFO

    def _makeEntity(self):
        raise NotImplementedError
        return

    def _makeSettings(self):
        return NotificationGuiSettings(isNotify=True, priorityLevel=self.__getPriority())

    def __getPriority(self):
        windows = self.__gui.windowsManager.findWindows((lambda w: w.layer in self.__OVERLAYS))
        if windows:
            return NotificationPriorityLevel.LOW
        return NotificationPriorityLevel.MEDIUM


class IntegratedAuctionStageStartDecorator(IntegratedAuctionDecorator):

    def getType(self):
        return NOTIFICATION_TYPE.AUCTION_STAGE_START

    def _makeEntity(self):
        title = backport.text(R.strings.messenger.serviceChannelMessages.integratedAuction.stageStart.title())
        text = backport.text(R.strings.messenger.serviceChannelMessages.integratedAuction.stageStart.text())
        return g_settings.msgTemplates.format(b'IntegratedAuctionStageStart', ctx={b'title': title, b'text': text})


class IntegratedAuctionStageFinishDecorator(IntegratedAuctionDecorator):

    def getType(self):
        return NOTIFICATION_TYPE.AUCTION_STAGE_FINISH

    def _makeEntity(self):
        title = backport.text(R.strings.messenger.serviceChannelMessages.integratedAuction.stageFinish.title())
        text = backport.text(R.strings.messenger.serviceChannelMessages.integratedAuction.stageFinish.text())
        return g_settings.msgTemplates.format(b'IntegratedAuctionStageFinish', ctx={b'title': title, b'text': text})


class SeniorityAwardsDecorator(MessageDecorator):
    __seniorityAwardCtrl = dependency.descriptor(ISeniorityAwardsController)

    def __init__(self, entityID, notificationType, savedData, model, template, priority, useCounterOnce=True, isNotify=True):
        self.__notificationType = notificationType
        self.__useCounterOnce = useCounterOnce
        entity = g_settings.msgTemplates.format(template, data={b'linkageData': savedData})
        settings = NotificationGuiSettings(isNotify=isNotify, priorityLevel=priority, groupID=self.getGroup())
        super(SeniorityAwardsDecorator, self).__init__(entityID, entity=entity, settings=settings, model=model)
        return

    def getType(self):
        return self.__notificationType

    def getGroup(self):
        return NotificationGroup.OFFER

    def getSavedData(self):
        return self._entity.get(b'linkageData')

    def isShouldCountOnlyOnce(self):
        return self.__useCounterOnce

    @staticmethod
    def isPinned():
        return True

    def decrementCounterOnHidden(self):
        return False

    def _make(self, entity=None, settings=None):
        self.__updateEntityButtons()
        super(SeniorityAwardsDecorator, self)._make(entity, settings)
        return

    def __updateEntityButtons(self):
        if self._entity is None:
            return
        else:
            buttonsLayout = self._entity.get(b'buttonsLayout')
            if not buttonsLayout:
                return
            buttonsStates = self._entity.get(b'buttonsStates')
            state = self._getButtonState()
            buttonsStates[b'submit'] = state
            return

    def _getButtonState(self):
        state = NOTIFICATION_BUTTON_STATE.VISIBLE
        if self.__seniorityAwardCtrl.timeLeft > 0:
            state |= NOTIFICATION_BUTTON_STATE.ENABLED
        return state


class LootBoxSystemDecorator(MessageDecorator):
    __lootBoxes = dependency.descriptor(ILootBoxSystemController)

    def __init__(self, entityID, message, savedData, model):
        super(LootBoxSystemDecorator, self).__init__(entityID, self.__makeEntity(message, savedData), self.__makeSettings(), model)
        return

    def getSavedData(self):
        return self._entity.get(b'savedData', {})

    def _getEvents(self):
        return (
         (
          self.__lootBoxes.onStatusChanged, self.__update),
         (
          self.__lootBoxes.onBoxesAvailabilityChanged, self.__update))

    def _make(self, formatted=None, settings=None):
        self.__updateEntityButtons()
        super(LootBoxSystemDecorator, self)._make(formatted, settings)
        return

    def __makeEntity(self, message, savedData):
        return g_settings.msgTemplates.format(b'LootBoxSystemStartSysMessage', ctx=message, data={b'savedData': savedData})

    def __makeSettings(self):
        return NotificationGuiSettings(isNotify=True, priorityLevel=NotificationPriorityLevel.MEDIUM)

    def __updateEntityButtons(self):
        if self._entity is None:
            return
        else:
            self._entity[b'buttonsStates'] = {b'submit': (NOTIFICATION_BUTTON_STATE.DEFAULT if self.__lootBoxes.isAvailable else NOTIFICATION_BUTTON_STATE.VISIBLE)}
            return

    def __update(self, *_):
        self.__updateEntityButtons()
        if self._model is not None:
            self._model.updateNotification(self.getType(), self._entityID, self._entity, False)
        return


class CollectionsLockButtonDecorator(MessageDecorator):
    __collectionsSystem = dependency.descriptor(ICollectionsSystemController)

    def __init__(self, entityID, entity=None, settings=None, model=None):
        super(CollectionsLockButtonDecorator, self).__init__(entityID, entity, settings, model)
        self.__collectionsSystem.onServerSettingsChanged += self.__update
        return

    def clear(self):
        self.__collectionsSystem.onServerSettingsChanged -= self.__update
        super(CollectionsLockButtonDecorator, self).clear()
        return

    def _make(self, formatted=None, settings=None):
        self.__updateEntityButtons()
        super(CollectionsLockButtonDecorator, self)._make(formatted, settings)
        return

    def __updateEntityButtons(self):
        if self._entity is None:
            return
        else:
            if self.__collectionsSystem.isEnabled():
                state = NOTIFICATION_BUTTON_STATE.DEFAULT
            else:
                state = NOTIFICATION_BUTTON_STATE.VISIBLE
            self._entity[b'buttonsStates'] = {b'submit': state}
            return

    def __update(self, *_):
        self.__updateEntityButtons()
        if self._model is not None:
            self._model.updateNotification(self.getType(), self._entityID, self._entity, False)
        return


class CollectionCustomMessageDecorator(CollectionsLockButtonDecorator):

    def __init__(self, entityID, message, messageType, notificationType, savedData, model):
        self.__notificationType = notificationType
        entity = self.__makeEntity(message, messageType, savedData)
        super(CollectionCustomMessageDecorator, self).__init__(entityID, entity, self.__makeSettings(), model=model)
        return

    def getType(self):
        return self.__notificationType

    def getGroup(self):
        return NotificationGroup.OFFER

    def __makeEntity(self, message, messageType, savedData):
        return g_settings.msgTemplates.format(messageType, ctx=message, data={b'savedData': savedData})

    def __makeSettings(self):
        return NotificationGuiSettings(isNotify=True, priorityLevel=NotificationPriorityLevel.MEDIUM)


class WinbackSelectableRewardReminderDecorator(MessageDecorator):

    def __init__(self, entityID):
        super(WinbackSelectableRewardReminderDecorator, self).__init__(entityID, self.__makeEntity(), self.__makeSettings())
        return

    def isShouldCountOnlyOnce(self):
        return True

    def getGroup(self):
        return NotificationGroup.OFFER

    def getType(self):
        return NOTIFICATION_TYPE.WINBACK_SELECTABLE_REWARD_AVAILABLE

    def __makeEntity(self):
        return g_settings.msgTemplates.format(b'WinbackSelectableRewardReminder')

    def __makeSettings(self):
        return NotificationGuiSettings(isNotify=True, priorityLevel=NotificationPriorityLevel.LOW)


class BattleMattersReminderDecorator(MessageDecorator):
    __battleMattersController = dependency.descriptor(IBattleMattersController)

    def __init__(self, entityID, notificationType, savedData, model, template, priority, useCounterOnce=True):
        self.__notificationType = notificationType
        self.__useCounterOnce = useCounterOnce
        entity = g_settings.msgTemplates.format(template, data={b'linkageData': savedData})
        settings = NotificationGuiSettings(isNotify=True, priorityLevel=priority, groupID=self.getGroup())
        super(BattleMattersReminderDecorator, self).__init__(entityID, entity=entity, settings=settings, model=model)
        self._subscribe()
        return

    def clear(self):
        self._unsubscribe()
        super(BattleMattersReminderDecorator, self).clear()
        return

    def getType(self):
        return self.__notificationType

    def getGroup(self):
        return NotificationGroup.OFFER

    def isShouldCountOnlyOnce(self):
        return self.__useCounterOnce

    def getSavedData(self):
        return self._entity.get(b'linkageData', {})

    @staticmethod
    def isPinned():
        return True

    def decrementCounterOnHidden(self):
        return True

    def _subscribe(self):
        events = self._getEvents()
        for event, handler in events:
            event += handler

        return

    def _unsubscribe(self):
        events = self._getEvents()
        for event, handler in events:
            event -= handler

        return

    def _getEvents(self):
        return ((self.__battleMattersController.onStateChanged, self.__onStateChanged),)

    def __onStateChanged(self):
        self.__update()
        return

    def __update(self):
        if not self.__battleMattersController.isEnabled() and self._model is not None:
            self._model.removeNotification(self.getType(), self._entityID)
            return
        else:
            self.__updateEntityButtons()
            if self._model is not None:
                self._model.updateNotification(self.getType(), self._entityID, self._entity, False)
            return

    def _make(self, entity=None, settings=None):
        self.__updateEntityButtons()
        super(BattleMattersReminderDecorator, self)._make(entity, settings)
        return

    def __updateEntityButtons(self):
        if self._entity is None:
            return
        else:
            buttonsLayout = self._entity.get(b'buttonsLayout')
            if not buttonsLayout:
                return
            buttonsStates = self._entity.get(b'buttonsStates', {})
            if buttonsStates is None:
                return
            state, tooltip = self._getButtonState()
            buttonsStates[b'submit'] = state
            buttonsLayout[0][b'tooltip'] = tooltip
            return

    def _getButtonState(self):
        state = NOTIFICATION_BUTTON_STATE.VISIBLE
        tooltip = b''
        if self.__battleMattersController.isActive() or self.__battleMattersController.hasDelayedRewards():
            state |= NOTIFICATION_BUTTON_STATE.ENABLED
        return (state, tooltip)


class PrestigeFirstEntryDecorator(LockButtonMessageDecorator):

    def __init__(self, entityID, message, linkageData, model):
        super(PrestigeFirstEntryDecorator, self).__init__(entityID, self.__makeEntity(message, linkageData), self.__makeSettings(), model)
        return

    def isShouldCountOnlyOnce(self):
        return True

    def getType(self):
        return NOTIFICATION_TYPE.PRESTIGE_FIRST_ENTRY

    def __makeEntity(self, message, linkageData):
        return g_settings.msgTemplates.format(b'PrestigeFirstEntryMessage', ctx=message, data={b'linkageData': linkageData})

    def __makeSettings(self):
        return NotificationGuiSettings(isNotify=True, priorityLevel=NotificationPriorityLevel.MEDIUM)


class PrestigeLvlUpDecorator(LockButtonMessageDecorator):
    __appLoader = dependency.descriptor(IAppLoader)
    __lobbyContext = dependency.descriptor(ILobbyContext)

    def __init__(self, entityID, entity=None, settings=None, model=None):
        super(PrestigeLvlUpDecorator, self).__init__(entityID, entity, settings, model)
        self.__lobbyContext.getServerSettings().onServerSettingsChange += self.__onServerSettingsChange
        return

    def clear(self):
        self.__lobbyContext.getServerSettings().onServerSettingsChange -= self.__onServerSettingsChange
        super(PrestigeLvlUpDecorator, self).clear()
        return

    def _make(self, formatted=None, settings=None):
        super(PrestigeLvlUpDecorator, self)._make(formatted, settings)
        isOnBattleQueueScreen = self.__appLoader.getApp().containerManager.getView(WindowLayer.SUB_VIEW, criteria={(POP_UP_CRITERIA.VIEW_ALIAS): (VIEW_ALIAS.BATTLE_QUEUE)}) is not None
        self._updateButtonsState(lock=isOnBattleQueueScreen)
        return

    def _updateButtonsState(self, lock=False):
        config = self.__lobbyContext.getServerSettings().prestigeConfig
        lock |= not config.isEnabled
        super(PrestigeLvlUpDecorator, self)._updateButtonsState(lock)
        return

    def __onServerSettingsChange(self, diff):
        prestigeChanged = diff.get(b'prestige_config')
        if not prestigeChanged:
            return
        config = self.__lobbyContext.getServerSettings().prestigeConfig
        if not config.isEnabled and self._model:
            self._updateButtonsState(lock=True)
        return


class ExchangeRateDiscountDecorator(MessageDecorator):

    def __init__(self, entityID, notificationType, savedData, model, template, priority, useCounterOnce=False, isNotify=True):
        self.__notificationType = notificationType
        self.__useCounterOnce = useCounterOnce
        entity = g_settings.msgTemplates.format(template, data={b'linkageData': savedData})
        settings = NotificationGuiSettings(isNotify=isNotify, priorityLevel=priority, groupID=self.getGroup())
        super(ExchangeRateDiscountDecorator, self).__init__(entityID, entity=entity, settings=settings, model=model)
        return

    def getType(self):
        return self.__notificationType

    def getGroup(self):
        return NotificationGroup.OFFER

    def getSavedData(self):
        return self._entity.get(b'linkageData')

    def isShouldCountOnlyOnce(self):
        return self.__useCounterOnce

    @staticmethod
    def isPinned():
        return True


class PostProgressionDecorator(LockButtonMessageDecorator):
    __appLoader = dependency.descriptor(IAppLoader)

    def _make(self, formatted=None, settings=None):
        super(PostProgressionDecorator, self)._make(formatted, settings)
        lobbyHangarWindow = self.__appLoader.getApp().containerManager.getView(WindowLayer.SUB_VIEW, criteria={(POP_UP_CRITERIA.VIEW_ALIAS): (VIEW_ALIAS.BATTLE_QUEUE)})
        self._updateButtonsState(lobbyHangarWindow is not None)
        return


class PM3QuestDecorator(LockButtonMessageDecorator):
    __lobbyContext = dependency.descriptor(ILobbyContext)
    _branchName = PM_BRANCH.PM3_NAME

    def __init__(self, entityID, entity=None, settings=None, model=None):
        super(PM3QuestDecorator, self).__init__(entityID, entity, settings, model)
        self.__lobbyContext.getServerSettings().onServerSettingsChange += self.__onServerSettingsChange
        return

    def clear(self):
        self.__lobbyContext.getServerSettings().onServerSettingsChange -= self.__onServerSettingsChange
        super(PM3QuestDecorator, self).clear()
        return

    def _getButtonType(self):
        return b'submitGhost'

    def isShouldCountOnlyOnce(self):
        return True

    def _updateButtonsState(self, lock=False):
        serverSettings = self.__lobbyContext.getServerSettings()
        isPMEnabled = serverSettings.isPersonalMissionsEnabled(self._branchName)
        disabledPMOperations = serverSettings.getDisabledPMOperations()
        savedData = self.getSavedData()
        operationID = savedData.get(b'operationID')
        lock |= not isPMEnabled or operationID in disabledPMOperations
        super(PM3QuestDecorator, self)._updateButtonsState(lock)
        return

    def _getBtnState(self, lock):
        savedData = self.getSavedData()
        operationID = savedData.get(b'operationID')
        chainID = savedData.get(b'chainID')
        questID = savedData.get(b'questID')
        _, quest = getPMAdvancedOperationAndQuest(operationID, chainID, questID)
        if not quest or not quest.isCompleted():
            return NOTIFICATION_BUTTON_STATE.HIDDEN
        return super(PM3QuestDecorator, self)._getBtnState(lock)

    def __onServerSettingsChange(self, diff):
        if PM_SWITCHES.MAP_BRANCH_NAME_TO_SWITCH_NAME.get(self._branchName) not in diff:
            return
        else:
            if self._model is not None:
                self._updateButtonsState()
                self._model.updateNotification(self.getType(), self._entityID, self._entity, False)
            return


class PM4QuestDecorator(PM3QuestDecorator):
    _branchName = PM_BRANCH.PM4_NAME


class VehSkillTreePerkAvailableDecorator(MessageDecorator):

    def __init__(self, entityID, savedData, model, template, priority):
        entity = g_settings.msgTemplates.format(template, data={b'linkageData': savedData})
        settings = NotificationGuiSettings(isNotify=True, priorityLevel=priority, groupID=self.getGroup())
        super(VehSkillTreePerkAvailableDecorator, self).__init__(entityID, entity=entity, settings=settings, model=model)
        return

    def getType(self):
        return NOTIFICATION_TYPE.VEH_SKILL_TREE_PERK_AVAILABLE

    def getGroup(self):
        return NotificationGroup.INFO

    def getSavedData(self):
        return self._entity.get(b'linkageData')

    def isShouldCountOnlyOnce(self):
        return True

    @staticmethod
    def isPinned():
        return True


class PetSystemDecorator(LockButtonMessageDecorator):
    __appLoader = dependency.descriptor(IAppLoader)
    __lobbyContext = dependency.descriptor(ILobbyContext)
    __petController = dependency.descriptor(IPetSystemController)
    __hangarSwitchController = dependency.descriptor(IHangarSpaceSwitchController)

    def __init__(self, entityID, entity=None, settings=None, model=None):
        super(PetSystemDecorator, self).__init__(entityID, entity, settings, model)
        self.__lobbyContext.getServerSettings().onServerSettingsChange += self.__onServerSettingsChange
        g_eventBus.addListener(HangarSpacesSwitcherEvent.SWITCH_TO_HANGAR_SPACE, self._changeHangarSpace, EVENT_BUS_SCOPE.LOBBY)
        return

    def clear(self):
        self.__lobbyContext.getServerSettings().onServerSettingsChange -= self.__onServerSettingsChange
        g_eventBus.removeListener(HangarSpacesSwitcherEvent.SWITCH_TO_HANGAR_SPACE, self._changeHangarSpace, EVENT_BUS_SCOPE.LOBBY)
        super(PetSystemDecorator, self).clear()
        return

    def _make(self, formatted=None, settings=None):
        super(PetSystemDecorator, self)._make(formatted, settings)
        isOnBattleQueueScreen = self.__appLoader.getApp().containerManager.getView(WindowLayer.SUB_VIEW, criteria={(POP_UP_CRITERIA.VIEW_ALIAS): (VIEW_ALIAS.BATTLE_QUEUE)}) is not None
        self._updateButtonsState(lock=isOnBattleQueueScreen)
        return

    def _updateButtonsState(self, lock=False):
        lock |= not self.__petController.isEnabled
        super(PetSystemDecorator, self)._updateButtonsState(lock)
        return

    def _changeHangarSpace(self, *args, **kwargs):
        isInDefaultHangar = self.__hangarSwitchController.currentSceneName == DEFAULT_HANGAR_SCENE
        self._updateButtonsState(lock=not isInDefaultHangar)
        return

    def __onServerSettingsChange(self, diff):
        if pet_constants.PETS_SYSTEM_CONFIG in diff:
            self._updateButtonsState()
        return


class ChallengesStartDecorator(MessageDecorator):
    __challenges = dependency.descriptor(IChallengesController)

    def __init__(self, entityID, notificationType, savedData, model, template, priority):
        self.__notificationType = notificationType
        entity = g_settings.msgTemplates.format(template, data={b'linkageData': savedData})
        settings = NotificationGuiSettings(isNotify=True, priorityLevel=priority, groupID=self.getGroup())
        super(ChallengesStartDecorator, self).__init__(entityID, entity=entity, settings=settings, model=model)
        return

    def getType(self):
        return self.__notificationType

    def getGroup(self):
        return NotificationGroup.INFO

    def getSavedData(self):
        return self._entity.get(b'linkageData')

    def isShouldCountOnlyOnce(self):
        return True

    def decrementCounterOnHidden(self):
        return True

    def _make(self, entity=None, settings=None):
        self.__updateEntityButtons()
        super(ChallengesStartDecorator, self)._make(entity, settings)
        return

    def _getButtonState(self):
        state = NOTIFICATION_BUTTON_STATE.VISIBLE
        if self.__challenges.isEnabled:
            state |= NOTIFICATION_BUTTON_STATE.ENABLED
        return state

    def __updateEntityButtons(self):
        if self._entity is None:
            return
        else:
            buttonsLayout = self._entity.get(b'buttonsLayout')
            if not buttonsLayout:
                return
            buttonsStates = self._entity.get(b'buttonsStates')
            state = self._getButtonState()
            buttonsStates[b'submit'] = state
            return


class ChallengesReminderDecorator(MessageDecorator):
    __challenges = dependency.descriptor(IChallengesController)
    ENTITY_ID = 0

    def __init__(self, model):
        super(ChallengesReminderDecorator, self).__init__(self.ENTITY_ID, self.__makeEntity(), self.__makeSettings(), model)
        return

    def getSavedData(self):
        return self._entity.get(b'savedData', {})

    def _getEvents(self):
        return (
         (
          self.__challenges.onChallengesSettingsChanged, self.__update),)

    def _make(self, formatted=None, settings=None):
        self.__updateEntityButtons()
        super(ChallengesReminderDecorator, self)._make(formatted, settings)
        return

    def __makeEntity(self):
        return g_settings.msgTemplates.format(b'ChallengesReminderSysMessage')

    def __makeSettings(self):
        return NotificationGuiSettings(isNotify=True, priorityLevel=g_settings.msgTemplates.priority(b'ChallengesReminderSysMessage'))

    def __updateEntityButtons(self):
        if self._entity is None:
            return
        else:
            state = NOTIFICATION_BUTTON_STATE.VISIBLE
            expiringChallenge = first(self.__challenges.getSoonEndingChallenges())
            if expiringChallenge is not None and expiringChallenge.isExpiringSoon:
                state |= NOTIFICATION_BUTTON_STATE.ENABLED
            self._entity[b'buttonsStates'] = {b'submit': state}
            return

    def __update(self, *_):
        self.__updateEntityButtons()
        if self._model is not None:
            self._model.updateNotification(self.getType(), self._entityID, self._entity, False)
        return

    def getType(self):
        return NOTIFICATION_TYPE.CHALLENGES_REMINDER
