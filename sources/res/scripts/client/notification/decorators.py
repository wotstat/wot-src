import typing, BigWorld
from CurrentVehicle import g_currentVehicle
from debug_utils import LOG_ERROR
from frameworks.wulf import WindowLayer
from PlayerEvents import g_playerEvents
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.common.battle_royale.br_helpers import currentHangarIsBattleRoyale
from gui.Scaleform.framework.managers.loaders import g_viewOverrider
from gui.Scaleform.locale.INVITES import INVITES
from gui.clans.formatters import ClanSingleNotificationHtmlTextFormatter, ClanMultiNotificationsHtmlTextFormatter, ClanAppActionHtmlTextFormatter
from gui.clans.settings import CLAN_APPLICATION_STATES, CLAN_INVITE_STATES
from gui.customization.shared import isVehicleCanBeCustomized
from gui.impl import backport
from gui.impl.gen import R
from gui.prb_control import prbInvitesProperty, prbEntityProperty
from gui.prb_control.formatters.invites import getPrbInviteHtmlFormatter
from gui.server_events.events_helpers import getIdxFromQuestID
from gui.shared import EVENT_BUS_SCOPE, g_eventBus
from gui.shared.events import HangarSpacesSwitcherEvent, ViewEventType
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.notifications import NotificationGroup, NotificationGuiSettings, NotificationPriorityLevel
from gui.shared.utils.functions import makeTooltip
from gui.paragons.paragons_constants import MESSAGE_ICONS
from gui.notify_center.settings import NOTIFY_CENTER_DEFAULT_ICON, NOTIFY_CENTER_POP_UP_BUTTON_WIDTH
from helpers import dependency, time_utils
from items import makeIntCompactDescrByID
from items.components.c11n_constants import CustomizationType
from messenger import g_settings
from messenger.formatters.users_messages import makeFriendshipRequestText
from messenger.m_constants import PROTO_TYPE
from messenger.proto import proto_getter
from messenger.proto.xmpp.xmpp_constants import XMPP_ITEM_TYPE
from notification.settings import NOTIFICATION_BUTTON_STATE, NOTIFICATION_TYPE, makePathToIcon
from skeletons.gui.battle_matters import IBattleMattersController
from skeletons.gui.game_control import IBattlePassController, ICollectionsSystemController, IMapboxController, IResourceWellController, ISeniorityAwardsController, IEarlyAccessController, IParagonsController
from skeletons.gui.impl import IGuiLoader
from skeletons.gui.shared import IItemsCache
from skeletons.gui.web import IWebController
if typing.TYPE_CHECKING:
    from gui.shared.events import LoadViewEvent

def _makeShowTime():
    return BigWorld.time()


_ICONS_FIELDS = (b'icon', b'defaultIcon', b'bgIcon')

def _getClanName(clanInfo):
    return (b'[{}] {}').format(clanInfo[1], clanInfo[0])


class _NotificationDecorator(object):
    __slots__ = (b'_entityID', b'_entity', b'_settings', b'_vo', b'_isOrderChanged')

    def __init__(self, entityID, entity=None, settings=None):
        super(_NotificationDecorator, self).__init__()
        self._isOrderChanged = False
        self._entityID = entityID
        self._entity = entity
        self._make(entity, settings)
        return

    def __repr__(self):
        return (b'{0:>s}(typeID = {1:n}, entityID = {2:n})').format(self.__class__.__name__, self.getType(), self.getID())

    def __cmp__(self, other):
        return cmp(self.getOrder(), other.getOrder())

    def __eq__(self, other):
        return self.getType() == other.getType() and self.getID() == other.getID()

    def clear(self):
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
        result = NotificationPriorityLevel.MEDIUM
        if self._settings:
            result = self._settings.priorityLevel
        return result

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
            if key in formatted:
                message[key] = makePathToIcon(message[key])
            else:
                message[key] = b''

        self._vo = {b'typeID': (self.getType()), b'entityID': (self.getID()), 
           b'message': message, 
           b'notify': (self.isNotify())}
        return


class RecruitReminderMessageDecorator(MessageDecorator):

    def __init__(self, entityID, message, savedData, msgPrLevel=NotificationPriorityLevel.LOW):
        entity = g_settings.msgTemplates.format(b'RecruitReminder', ctx={b'text': message}, data={b'savedData': savedData})
        settings = NotificationGuiSettings(isNotify=True, priorityLevel=msgPrLevel)
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
        g_playerEvents.onEnqueued += self._onEqueued
        g_playerEvents.onDequeued += self._onDequeued
        g_viewOverrider.onViewOverriden += self._onViewOverriden
        self._updateButtonsState(self.prbEntity and self.prbEntity.isInQueue())
        return

    def clear(self):
        super(LockButtonMessageDecorator, self).clear()
        g_eventBus.removeListener(ViewEventType.LOAD_VIEW, self._viewLoaded, EVENT_BUS_SCOPE.LOBBY)
        g_playerEvents.onEnqueued -= self._onEqueued
        g_playerEvents.onDequeued -= self._onDequeued
        g_viewOverrider.onViewOverriden -= self._onViewOverriden
        return

    def update(self, formatted):
        _NotificationDecorator.update(self, formatted)
        return

    @prbEntityProperty
    def prbEntity(self):
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

    def _updateButtons(self, _):
        self._updateButtonsState(lock=False)
        return

    def _viewLoaded(self, event):
        if event.alias in self._getLockAliases():
            self._updateButtonsState(lock=True)
        elif VIEW_ALIAS.LOBBY_HANGAR == event.alias:
            self._updateButtons(event)
        return

    def _onViewOverriden(self, alias, *_):
        if VIEW_ALIAS.LOBBY_HANGAR == alias:
            self._updateButtons(None)
        return

    def _updateButtonsState(self, lock=False):
        if self._entity is None or not self._entity.get(b'buttonsLayout'):
            return
        state = NOTIFICATION_BUTTON_STATE.VISIBLE if lock else NOTIFICATION_BUTTON_STATE.DEFAULT
        self._entity.setdefault(b'buttonsStates', {}).update({b'submit': state})
        if self._model is not None:
            self._model.updateNotification(self.getType(), self._entityID, self._entity, False)
        return


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

    def _getLockAliases(self):
        return (VIEW_ALIAS.HERO_VEHICLE_PREVIEW,) + super(C11nMessageDecorator, self)._getLockAliases()

    def _getIsLocked(self):
        isLocked = True
        vehicle = self._getVehicle()
        if not currentHangarIsBattleRoyale() and vehicle is not None and vehicle.isCustomizationEnabled():
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


class NotifyCenterPopUpDecorator(_NotificationDecorator):
    __slots__ = (b'_itemName', b'__receivedAt')

    def __init__(self, entityID, item, offset=0, receivedAt=None):
        super(NotifyCenterPopUpDecorator, self).__init__(entityID, item, NotificationGuiSettings(item.isNotify(), item.getPriority(), showAt=_makeShowTime() + offset))
        self.__receivedAt = receivedAt
        return

    def getType(self):
        return NOTIFICATION_TYPE.NOTIFY_CENTER_POP_UP

    def getGroup(self):
        return self.getEntity().getGroup()

    def getOrder(self):
        timeCriteria = self.__receivedAt or self.showAt()
        return (timeCriteria, self._entityID)

    def getSavedData(self):
        return self._itemName

    def update(self, item):
        super(NotifyCenterPopUpDecorator, self).update(item)
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
        message = g_settings.msgTemplates.format(b'notifyCenterNotification_v2', ctx={b'topic': topic, 
           b'body': body}, data={b'icon': (makePathToIcon(item.getLocalIcon())), 
           b'defaultIcon': (makePathToIcon(NOTIFY_CENTER_DEFAULT_ICON)), 
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
               b'width': NOTIFY_CENTER_POP_UP_BUTTON_WIDTH})
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


class ResourceWellLockButtonDecorator(MessageDecorator):
    __resourceWell = dependency.descriptor(IResourceWellController)

    def __init__(self, entityID, entity=None, settings=None, model=None):
        super(ResourceWellLockButtonDecorator, self).__init__(entityID, entity, settings, model)
        self.__resourceWell.onEventUpdated += self.__update
        return

    def clear(self):
        self.__resourceWell.onEventUpdated -= self.__update
        return

    def _make(self, formatted=None, settings=None):
        self.__updateEntityButtons()
        super(ResourceWellLockButtonDecorator, self)._make(formatted, settings)
        return

    def __updateEntityButtons(self):
        if self._entity is None:
            return
        else:
            if self.__resourceWell.isActive():
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


class ResourceWellStartDecorator(ResourceWellLockButtonDecorator):

    def __init__(self, entityID, message, model):
        super(ResourceWellStartDecorator, self).__init__(entityID, self.__makeEntity(message), self.__makeSettings(), model)
        return

    def getType(self):
        return NOTIFICATION_TYPE.RESOURCE_WELL_START

    def __makeEntity(self, message):
        return g_settings.msgTemplates.format(b'ResourceWellStartSysMessage', ctx=message)

    def __makeSettings(self):
        return NotificationGuiSettings(isNotify=True, priorityLevel=NotificationPriorityLevel.HIGH)


class TradingCaravanDecorator(MessageDecorator):
    __OVERLAYS = (
     WindowLayer.FULLSCREEN_WINDOW, WindowLayer.OVERLAY, WindowLayer.TOP_WINDOW)
    __gui = dependency.descriptor(IGuiLoader)

    def getGroup(self):
        return NotificationGroup.INFO

    def _makeSettings(self):
        return NotificationGuiSettings(isNotify=True, priorityLevel=self.__getPriority())

    def __getPriority(self):
        windows = self.__gui.windowsManager.findWindows((lambda w: w.layer in self.__OVERLAYS))
        if windows:
            return NotificationPriorityLevel.LOW
        return NotificationPriorityLevel.MEDIUM


class TradingCaravanRefillDecorator(TradingCaravanDecorator):

    def __init__(self, entityID, message):
        super(TradingCaravanRefillDecorator, self).__init__(entityID, self.__makeEntity(message), self._makeSettings())
        return

    def getType(self):
        return NOTIFICATION_TYPE.TRADING_CARAVAN_REFILL

    def __makeEntity(self, message):
        return g_settings.msgTemplates.format(b'TradingCaravanRefillSysMessage', ctx=message)


class CustomNotificationsDecorator(MessageDecorator):
    __OVERLAYS = (
     WindowLayer.FULLSCREEN_WINDOW, WindowLayer.OVERLAY, WindowLayer.TOP_WINDOW)
    __gui = dependency.descriptor(IGuiLoader)

    def getGroup(self):
        return NotificationGroup.INFO

    def _makeSettings(self):
        return NotificationGuiSettings(isNotify=True, priorityLevel=self.__getPriority())

    def __getPriority(self):
        windows = self.__gui.windowsManager.findWindows((lambda w: w.layer in self.__OVERLAYS))
        if windows:
            return NotificationPriorityLevel.LOW
        return NotificationPriorityLevel.MEDIUM


class CustomNotificationsStartDecorator(CustomNotificationsDecorator):

    def __init__(self, entityID, message):
        super(CustomNotificationsStartDecorator, self).__init__(entityID, self.__makeEntity(message), self._makeSettings())
        return

    def getType(self):
        return NOTIFICATION_TYPE.CUSTOM_NOTIFICATIONS

    def __makeEntity(self, message):
        return g_settings.msgTemplates.format(b'CustomNotificationSysMessage', ctx=message)


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


class BlackMarketAuctionDecorator(MessageDecorator):
    __OVERLAYS = (
     WindowLayer.FULLSCREEN_WINDOW, WindowLayer.OVERLAY, WindowLayer.TOP_WINDOW)
    __gui = dependency.descriptor(IGuiLoader)

    def __init__(self, entityID):
        super(BlackMarketAuctionDecorator, self).__init__(entityID, self._makeEntity(), self._makeSettings())
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


class BlackMarketVehicleAuctionStageStartDecorator(BlackMarketAuctionDecorator):

    def getType(self):
        return NOTIFICATION_TYPE.BLACK_MARKET_STAGE_START

    def _makeEntity(self):
        title = backport.text(R.strings.messenger.serviceChannelMessages.integratedAuction.stageStart.title())
        text = backport.text(R.strings.messenger.serviceChannelMessages.integratedAuction.stageStart.text())
        return g_settings.msgTemplates.format(b'BlackMarketVehicleAuctionStageStart', ctx={b'title': title, b'text': text})


class BlackMarketVehicleAuctionStageFinishDecorator(BlackMarketAuctionDecorator):

    def getType(self):
        return NOTIFICATION_TYPE.BLACK_MARKET_STAGE_FINISH

    def _makeEntity(self):
        title = backport.text(R.strings.messenger.serviceChannelMessages.integratedAuction.stageFinish.title())
        text = backport.text(R.strings.messenger.serviceChannelMessages.integratedAuction.stageFinish.text())
        return g_settings.msgTemplates.format(b'BlackMarketVehicleAuctionStageFinish', ctx={b'title': title, b'text': text})


class BlackMarketAuctionStageStartDecorator(BlackMarketAuctionDecorator):

    def getType(self):
        return NOTIFICATION_TYPE.BLACK_MARKET_STAGE_START

    def _makeEntity(self):
        title = backport.text(R.strings.messenger.serviceChannelMessages.integratedAuction.stageStart.title())
        text = backport.text(R.strings.messenger.serviceChannelMessages.integratedAuction.stageStart.text())
        return g_settings.msgTemplates.format(b'BlackMarketAuctionStageStart', ctx={b'title': title, b'text': text})


class BlackMarketAuctionStageFinishDecorator(BlackMarketAuctionDecorator):

    def getType(self):
        return NOTIFICATION_TYPE.BLACK_MARKET_STAGE_FINISH

    def _makeEntity(self):
        title = backport.text(R.strings.messenger.serviceChannelMessages.integratedAuction.stageFinish.title())
        text = backport.text(R.strings.messenger.serviceChannelMessages.integratedAuction.stageFinish.text())
        return g_settings.msgTemplates.format(b'BlackMarketAuctionStageFinish', ctx={b'title': title, b'text': text})


class SeniorityAwardsDecorator(MessageDecorator):
    __seniorityAwardCtrl = dependency.descriptor(ISeniorityAwardsController)

    def __init__(self, entityID, notificationType, savedData, model, template, priority, useCounterOnce=True):
        self.__notificationType = notificationType
        self.__useCounterOnce = useCounterOnce
        entity = g_settings.msgTemplates.format(template, data={b'linkageData': savedData})
        settings = NotificationGuiSettings(isNotify=True, priorityLevel=priority, groupID=self.getGroup())
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


class WotPlusIntroViewMessageDecorator(MessageDecorator):
    ENTITY_ID = 0

    def __init__(self):
        entity = g_settings.msgTemplates.format(b'WotPlusIntroAnnouncement')
        settings = NotificationGuiSettings(isNotify=True, priorityLevel=NotificationPriorityLevel.LOW)
        super(WotPlusIntroViewMessageDecorator, self).__init__(self.ENTITY_ID, entity, settings)
        return

    def getType(self):
        return NOTIFICATION_TYPE.WOT_PLUS_INTRO

    def getGroup(self):
        return NotificationGroup.OFFER


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
        if self.__battleMattersController.isActive():
            state |= NOTIFICATION_BUTTON_STATE.ENABLED
        return (state, tooltip)


class EarlyAccessDecorator(MessageDecorator):
    __earlyAccessController = dependency.descriptor(IEarlyAccessController)

    def __init__(self, entityID, entity=None, settings=None, model=None):
        super(EarlyAccessDecorator, self).__init__(entityID, entity, settings, model)
        self.__earlyAccessController.onFeatureStateChanged += self.__update
        self.__earlyAccessController.onUpdated += self.__update
        return

    def _make(self, entity=None, settings=None):
        self.__updateEntityButtons()
        super(EarlyAccessDecorator, self)._make(entity, settings)
        return

    def clear(self):
        self.__earlyAccessController.onFeatureStateChanged -= self.__update
        self.__earlyAccessController.onUpdated -= self.__update
        return

    def __update(self, *args):
        if not self.__earlyAccessController.isEnabled() and self._model is not None:
            self._model.removeNotification(self.getType(), self._entityID)
            return
        else:
            self.__updateEntityButtons()
            if self._model is not None:
                self._model.updateNotification(self.getType(), self._entityID, self._entity, False)
            return

    def __updateEntityButtons(self):
        if self._entity is None:
            return
        else:
            buttonsLayout = self._entity.get(b'buttonsLayout')
            buttonsStates = self._entity.get(b'buttonsStates')
            if not buttonsLayout or buttonsStates is None:
                return
            if not self.__earlyAccessController.isQuestActive():
                state = NOTIFICATION_BUTTON_STATE.VISIBLE
            else:
                state = NOTIFICATION_BUTTON_STATE.DEFAULT
            buttonsStates[b'submit'] = state
            return


class ParagonsMessageDecorator(MessageDecorator):
    __ctrl = dependency.descriptor(IParagonsController)
    _chapter = None
    _level = None
    _isVehicleReceived = False

    @property
    def featureIsInactive(self):
        return not self.__ctrl.isEnabled or self.__ctrl.isPaused

    def __init__(self, entityID, entity=None, settings=None, model=None):
        super(ParagonsMessageDecorator, self).__init__(entityID, entity, settings, model)
        auxData = settings.auxData
        if auxData:
            self._chapter = auxData.get(b'chapter')
            self._level = auxData.get(b'level')
            self._isVehicleReceived = False
        self.__ctrl.onSelectedRewardMarked += self.__onSelectedRewardMarked
        self.__ctrl.onSettingsChanged += self.__onSettingsChanged
        return

    def clear(self):
        self.__ctrl.onSelectedRewardMarked -= self.__onSelectedRewardMarked
        self.__ctrl.onSettingsChanged -= self.__onSettingsChanged
        super(ParagonsMessageDecorator, self).clear()
        return

    def _make(self, formatted=None, settings=None):
        self.__updateButtons()
        super(ParagonsMessageDecorator, self)._make(formatted, settings)
        return

    def __updateButtons(self):
        if self._entity is None or not self._entity.get(b'buttonsLayout'):
            return
        state = NOTIFICATION_BUTTON_STATE.DEFAULT | NOTIFICATION_BUTTON_STATE.VISIBLE
        if self._isVehicleReceived or self.featureIsInactive:
            state = NOTIFICATION_BUTTON_STATE.HIDDEN
        buttonsStates = self._entity.get(b'buttonsStates')
        if buttonsStates is None:
            self._entity.setdefault(b'buttonsStates', {}).update({b'submit': state})
        else:
            buttonsStates[b'submit'] = state
        return

    def __onSelectedRewardMarked(self, chapter, level, _):
        self.__update(chapter, level, True)
        return

    def __onSettingsChanged(self, _):
        self.__update(self._chapter, self._level, False)
        return

    def __update(self, chapter, level, isVehicleReceived):
        if self._chapter != chapter or self._level != level:
            return
        self._isVehicleReceived = isVehicleReceived
        if self._model is not None:
            self._model.updateNotification(self.getType(), self._entityID, self._entity, False)
        return


class ParagonsAchievementDecorator(MessageDecorator):

    def _make(self, formatted=None, settings=None):
        self._settings = NotificationGuiSettings(isNotify=True, priorityLevel=NotificationPriorityLevel.HIGH)
        iconGetter = MESSAGE_ICONS.get(settings.messageType)
        if iconGetter is not None:
            pathToIcon = backport.image(iconGetter())
            formatted[b'icon'] = pathToIcon
        self._vo = {b'typeID': (self.getType()), 
           b'entityID': (self.getID()), 
           b'message': formatted, 
           b'notify': (self.isNotify())}
        return


class BattleMattersAwardsDecorator(MessageDecorator):
    __battleMattersController = dependency.descriptor(IBattleMattersController)

    def __init__(self, entityID, entity=None, settings=None, model=None):
        self.__questIdx = settings.auxData.get(b'questIdx') if settings else None
        super(BattleMattersAwardsDecorator, self).__init__(entityID, entity, settings, model)
        self.__battleMattersController.onFinish += self.__update
        return

    def clear(self):
        self.__battleMattersController.onFinish -= self.__update
        super(BattleMattersAwardsDecorator, self).clear()
        return

    def _make(self, formatted=None, settings=None):
        self.__updateEntityButtons()
        super(BattleMattersAwardsDecorator, self)._make(formatted, settings)
        return

    def __update(self):
        self.__updateEntityButtons()
        if self._model is not None:
            self._model.updateNotification(self.getType(), self._entityID, self._entity, False)
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
        finalQuest = self.__battleMattersController.getFinalQuest()
        if finalQuest and getIdxFromQuestID(finalQuest.getID()) == self.__questIdx:
            return NOTIFICATION_BUTTON_STATE.HIDDEN
        if not self.__battleMattersController.isFinished():
            return NOTIFICATION_BUTTON_STATE.DEFAULT
        return NOTIFICATION_BUTTON_STATE.VISIBLE
