from messenger.m_constants import USER_ACTION_ID, USER_TAG, PROTO_TYPE, CLIENT_ACTION_ID
from messenger.proto.events import g_messengerEvents
from messenger.proto.xmpp import entities, errors
from messenger.proto.xmpp.contacts.note_tasks import RemoveNotesTask
from messenger.proto.xmpp.contacts.note_tasks import canNoteAutoDelete
from messenger.proto.xmpp.contacts.tasks import TaskResult, ContactTask, SeqTask
from messenger.proto.xmpp.find_criteria import ItemsFindCriteria
from messenger.proto.xmpp.gloox_constants import ROSTER_CONTEXT
from messenger.proto.xmpp.log_output import CLIENT_LOG_AREA, g_logOutput
from messenger.proto.xmpp.xmpp_constants import XMPP_ITEM_TYPE
from messenger.proto.xmpp.xmpp_items import RosterItem, ContactItem
from soft_exception import SoftException

def _syncRosterItem(storage, jid, name, groups, sub=None, clanInfo=None):
    dbID = jid.getDatabaseID()
    user = storage.getUser(dbID, PROTO_TYPE.XMPP)
    if user is not None:
        if user.isCurrentPlayer():
            return
        if user.getItemType() in XMPP_ITEM_TYPE.ROSTER_ITEMS:
            user.update(name=name, groups=groups, sub=sub, trusted=True, clanInfo=clanInfo)
        else:
            user.update(name=name, clanInfo=clanInfo, item=RosterItem(jid, groups, sub=sub, resources=user.getItem().getResources()))
    else:
        user = entities.XMPPUserEntity(dbID, name=name, clanInfo=clanInfo, item=RosterItem(jid, groups, sub=sub))
        storage.setUser(user)
    return user


def _syncEmptyGroups(storage, groups, woEvent=False):
    isGroupExists = storage.isGroupExists
    addEmptyGroup = storage.addEmptyGroup
    included = set()
    for group in groups:
        if not isGroupExists(group):
            addEmptyGroup(group)
            included.add(group)

    if included and not woEvent:
        g_messengerEvents.users.onEmptyGroupsChanged(included, set())
    return


class RosterResultTask(SeqTask):

    def run(self):
        return

    def _doRun(self, client):
        raise SoftException(b'This method should not be reached in this context')
        return

    def sync(self, seq):
        storage = self.usersStorage
        for jid, name, groups, sub, clanInfo in seq:
            _syncRosterItem(storage, jid, name, groups, sub, clanInfo)

        storage.removeTags({USER_TAG.CACHED}, ItemsFindCriteria(XMPP_ITEM_TYPE.ROSTER_ITEMS))
        return


class RosterItemTask(ContactTask):
    __slots__ = (b'_groups',)

    def __init__(self, jid, name=b'', groups=None):
        super(RosterItemTask, self).__init__(jid, name)
        self._groups = groups or set()
        return

    def clear(self):
        self._groups = set()
        super(RosterItemTask, self).clear()
        return

    def getContext(self):
        return ROSTER_CONTEXT.PUSH_ROSTER_ITEM

    def _doSync(self, name, groups=None, sub=None, clanInfo=None):
        return _syncRosterItem(self.usersStorage, self._jid, name, groups, sub, clanInfo)


class SyncSubscriptionTask(RosterItemTask):

    def _doSync(self, name, groups=None, sub=None, clanInfo=None):
        user = self._getUser()
        if user:
            prevSub = user.getSubscription()
            isOnline = user.isOnline()
        else:
            prevSub = None
            isOnline = False
        user = super(SyncSubscriptionTask, self)._doSync(name, groups, sub, clanInfo)
        nextSub = user.getSubscription()
        if prevSub and prevSub != nextSub:
            self._doNotify(USER_ACTION_ID.SUBSCRIPTION_CHANGED, user, nextRev=False)
            if isOnline != user.isOnline():
                g_messengerEvents.users.onUserStatusUpdated(user)
        return user

    def _doRun(self, client):
        user = self._getUser()
        if user:
            user.addTags({USER_TAG.SUB_IN_PROCESS})
        return


class AddRosterItemTask(RosterItemTask):

    def _doSync(self, name, groups=None, sub=None, clanInfo=None):
        user = super(AddRosterItemTask, self)._doSync(name, groups, sub, clanInfo)
        if user:
            g_logOutput.debug(CLIENT_LOG_AREA.ROSTER, b'Item is added to roster', user)
            self._doNotify(USER_ACTION_ID.FRIEND_ADDED, user)
        return

    def _doRun(self, client):
        client.setContactToRoster(self._jid, self._name, self._groups)
        return

    def _getError(self, pyGlooxTag):
        return errors.createServerActionIQError(CLIENT_ACTION_ID.ADD_FRIEND, pyGlooxTag)


class RemoveRosterItemTask(RosterItemTask):

    def _doSync(self, name, groups=None, sub=None, clanInfo=None):
        user = self._getUser()
        if not user or user.isCurrentPlayer():
            return user
        if user.getItemType() in XMPP_ITEM_TYPE.ROSTER_ITEMS:
            user.update(item=ContactItem(user.getJID()))
            _syncEmptyGroups(self.usersStorage, self._groups)
            g_logOutput.debug(CLIENT_LOG_AREA.ROSTER, b'Roster item is removed', user)
            self._doNotify(USER_ACTION_ID.FRIEND_REMOVED, user)
        elif user.getItemType() in XMPP_ITEM_TYPE.SUB_PENDING_ITEMS:
            user.update(item=ContactItem(user.getJID()))
            _syncEmptyGroups(self.usersStorage, self._groups)
            g_logOutput.debug(CLIENT_LOG_AREA.ROSTER, b'Friendship request is revoked by sender', user)
            g_messengerEvents.users.onFriendshipRequestsUpdated([user])
        return user

    def _doRun(self, client):
        client.removeContactFromRoster(self._jid)
        return

    def getContext(self):
        return ROSTER_CONTEXT.REMOVE_ROSTER_ITEM

    def _getError(self, pyGlooxTag):
        return errors.createServerActionIQError(CLIENT_ACTION_ID.REMOVE_FRIEND, pyGlooxTag)


class EmptyGroupsTask(RosterItemTask):

    def isInstantaneous(self):
        return True

    def _doRun(self, client):
        _syncEmptyGroups(self.usersStorage, self._groups)
        return


class ChangeRosterItemGroupsTask(RosterItemTask):
    __slots__ = (b'_exclude',)

    def __init__(self, jid, name=b'', groups=None, exclude=None):
        super(ChangeRosterItemGroupsTask, self).__init__(jid, name, groups)
        self._exclude = exclude or set()
        return

    def clear(self):
        self._exclude = None
        super(ChangeRosterItemGroupsTask, self).clear()
        return

    def sync(self, name, groups, sub=None, clanInfo=None):
        if self._groups != groups:
            return self._result
        self._result = TaskResult.REMOVE
        user = self._doSync(name, groups, sub, clanInfo)
        if user:
            _syncEmptyGroups(self.usersStorage, self._exclude, True)
            self._doNotify(USER_ACTION_ID.GROUPS_CHANGED, user)
        return self._result

    def _doSync(self, name, groups=None, sub=None, clanInfo=None):
        user = self._getUser()
        if user is not None and user.getItemType() in XMPP_ITEM_TYPE.ROSTER_ITEMS:
            sub = user.getSubscription()
        return super(ChangeRosterItemGroupsTask, self)._doSync(name, groups, sub, clanInfo)

    def _doRun(self, client):
        client.setContactToRoster(self._jid, self._name, self._groups)
        return

    def _getError(self, pyGlooxTag):
        return errors.createServerActionIQError(CLIENT_ACTION_ID.CHANGE_GROUP, pyGlooxTag)


class _RosterItemsGroupsChain(object):

    def next(self, chain):
        self._chain = chain
        return self._chain.pop(0)


class RemoveRosterItemsGroupsChain(RemoveRosterItemTask, _RosterItemsGroupsChain):

    def __init__(self, queue, removeNotes=None):
        jid, name, groups = self.next(queue)
        self._removeNotes = removeNotes or set()
        super(RemoveRosterItemsGroupsChain, self).__init__(jid, name, groups)
        return

    def sync(self, name, groups, sub=None, clanInfo=None):
        user = self._doSync(name, groups, sub, clanInfo)
        if user and user.getItemType() not in XMPP_ITEM_TYPE.ROSTER_ITEMS and canNoteAutoDelete(user):
            self._removeNotes.add(user.getID())
        self._result = TaskResult.REMOVE
        if self._chain:
            self._result |= TaskResult.CLONE
        elif self._removeNotes:
            self._result |= TaskResult.CREATE_SEQ
        return self._result

    def canShadowMode(self):
        return False

    def error(self, pyGlooxTag=None):
        super(RemoveRosterItemsGroupsChain, self).error(pyGlooxTag)
        if self._removeNotes:
            self._result |= TaskResult.CREATE_SEQ
        return

    def clone(self):
        if self._chain:
            tasks = [RemoveRosterItemsGroupsChain(self._chain, self._removeNotes)]
        else:
            tasks = []
        return tasks

    def createSeqTask(self):
        task = None
        if self._removeNotes:
            task = RemoveNotesTask(self._removeNotes)
        return task

    def getContext(self):
        if self._groups:
            context = ROSTER_CONTEXT.PUSH_ROSTER_ITEM
        else:
            context = ROSTER_CONTEXT.REMOVE_ROSTER_ITEM
        return context

    def _doRun(self, client):
        if self._groups:
            client.setContactToRoster(self._jid, self._name, self._groups)
        else:
            client.removeContactFromRoster(self._jid)
        return

    def _doSync(self, name, groups=None, sub=None, clanInfo=None):
        if self._groups:
            user = _syncRosterItem(self.usersStorage, self._jid, name, groups, sub, clanInfo)
            self._doNotify(USER_ACTION_ID.GROUPS_CHANGED, user)
        else:
            user = super(RemoveRosterItemsGroupsChain, self)._doSync(name, groups, sub, clanInfo)
        return user


class ChangeRosterItemsGroupsChain(ChangeRosterItemGroupsTask, _RosterItemsGroupsChain):

    def __init__(self, queue):
        jid, name, groups = self.next(queue)
        super(ChangeRosterItemsGroupsChain, self).__init__(jid, name, groups)
        return

    def sync(self, name, groups, sub=None, clanInfo=None):
        user = self._doSync(name, groups, sub, clanInfo)
        if user:
            self._doNotify(USER_ACTION_ID.GROUPS_CHANGED, user)
        self._result = TaskResult.CLONE | TaskResult.REMOVE
        return self._result

    def canShadowMode(self):
        return False

    def clone(self):
        if self._chain:
            tasks = [
             ChangeRosterItemsGroupsChain(self._chain)]
        else:
            tasks = []
        return tasks
