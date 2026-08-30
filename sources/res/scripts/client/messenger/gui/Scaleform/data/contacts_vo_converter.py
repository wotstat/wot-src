from constants import WG_GAMES
from gui import makeHtmlString
from gui.Scaleform.genConsts.CONTACTS_ALIASES import CONTACTS_ALIASES
from gui.Scaleform.locale.MESSENGER import MESSENGER as I18N_MESSENGER
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.impl import backport
from gui.impl.gen import R
from helpers import dependency
from helpers import i18n
from helpers.html import escape
from messenger import g_settings
from messenger.m_constants import USER_TAG
from messenger.storage import MessengerStorageDescriptor, UsersStorage
from predefined_hosts import g_preDefinedHosts
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.lobby_context import ILobbyContext
_CATEGORY_I18N_KEY = {(CONTACTS_ALIASES.GROUP_FRIENDS_CATEGORY_ID): (I18N_MESSENGER.MESSENGER_CONTACTS_MAINGROPS_FRIENDS), 
   (CONTACTS_ALIASES.GROUP_FORMATIONS_CATEGORY_ID): (I18N_MESSENGER.MESSENGER_CONTACTS_MAINGROPS_FORMATIONS), 
   (CONTACTS_ALIASES.GROUP_OTHER_CATEGORY_ID): (I18N_MESSENGER.MESSENGER_CONTACTS_MAINGROPS_OTHER)}
_DEF_RULES = CONTACTS_ALIASES.GROUP_IS_RESIZABLE
_MUTABLE_RULE = CONTACTS_ALIASES.GROUP_CAN_BE_MANAGED
_FRIENDS_RULES = CONTACTS_ALIASES.GROUP_IS_DROP_ALLOWED | CONTACTS_ALIASES.GROUP_IS_RESIZABLE
_IGNORED_RULES = CONTACTS_ALIASES.GROUP_IS_DROP_ALLOWED | CONTACTS_ALIASES.GROUP_IS_RESIZABLE

class _WOT_GAME_RESOURCE(object):
    ONLINE = b'user_is_online'
    UNKNOWN = b'unknown'
    BUSY = b'user_is_busy'
    BUSY_BLIND = b'user_is_busy_violet'


def makeClanFullName(clanAbbrev):
    formatted = b''
    if clanAbbrev:
        formatted = (u'{0} [{1}]').format(i18n.makeString(I18N_MESSENGER.DIALOGS_CONTACTS_TREE_CLAN), clanAbbrev)
    return formatted


def makeContactStatusDescription(isOnline, tags, clientInfo=None):
    name, description = (b'', b'')
    if isOnline:
        if clientInfo:
            gameHost = clientInfo.gameHost
            arenaLabel = clientInfo.arenaLabel
        else:
            gameHost, arenaLabel = (b'', b'')
        if gameHost:
            item = g_preDefinedHosts.byUrl(gameHost)
            name = item.shortName or item.name
        if USER_TAG.PRESENCE_DND in tags:
            descRes = R.strings.tooltips.Contact.status.inBattle.dyn(arenaLabel)
            if descRes.exists():
                description = backport.text(descRes())
            else:
                description = backport.text(R.strings.tooltips.Contact.status.inBattle.unknown())
        else:
            description = backport.text(R.strings.tooltips.Contact.status.online())
        if name:
            description = (b'{0}, {1}').format(description, name)
    else:
        description = backport.text(R.strings.tooltips.Contact.status.offline())
    return description


def _setMutableRule(rules, flag):
    if flag:
        if not rules & _MUTABLE_RULE:
            rules |= _MUTABLE_RULE
    elif rules & _MUTABLE_RULE > 0:
        rules |= _MUTABLE_RULE
    return rules


class CategoryConverter(object):
    __slots__ = (b'_categoryID', b'_userString', b'_rules')

    def __init__(self, categoryID, rules=_DEF_RULES):
        super(CategoryConverter, self).__init__()
        self._categoryID = categoryID
        self._userString = i18n.makeString(_CATEGORY_I18N_KEY[categoryID])
        self._rules = rules
        return

    def getCategoryID(self):
        return self._categoryID

    def setMutable(self, value):
        self._rules = _setMutableRule(self._rules, value)
        return

    def makeVO(self, children=None):
        baseVo = self.makeBaseVO()
        baseVo[b'isOpened'] = True
        baseVo[b'data'][b'title'] = self._userString
        baseVo[b'children'] = children
        return baseVo

    def makeBaseVO(self):
        return {b'gui': {b'id': (self._categoryID)}, b'data': {b'rules': (self._rules)}}


class ContactConverter(object):
    _colors = {}
    settingsCore = dependency.descriptor(ISettingsCore)
    lobbyContext = dependency.descriptor(ILobbyContext)

    @classmethod
    def getIcons(cls, tags, note):
        icons = []
        if USER_TAG.IGR_BASE in tags:
            icons.append(RES_ICONS.MAPS_ICONS_LIBRARY_BASIC_SMALL)
        elif USER_TAG.IGR_PREMIUM in tags:
            if USER_TAG.SUB_TO not in tags:
                icons.append(RES_ICONS.MAPS_ICONS_LIBRARY_PREMIUM_SMALL)
        if USER_TAG.IGNORED in tags:
            icons.append(RES_ICONS.MAPS_ICONS_MESSENGER_CONTACTIGNORED)
        elif USER_TAG.FRIEND in tags and USER_TAG.SUB_TO not in tags and USER_TAG.SUB_FROM not in tags:
            icons.append(RES_ICONS.MAPS_ICONS_MESSENGER_CONTACTCONFIRMNEEDED)
        if USER_TAG.BAN_CHAT in tags:
            icons.append(RES_ICONS.MAPS_ICONS_MESSENGER_CONTACTMSGSOFF)
        if note:
            icons.append(RES_ICONS.MAPS_ICONS_MESSENGER_CONTACTNOTE)
        return icons

    @classmethod
    def getColor(cls, tags, isOnline):
        if USER_TAG.CURRENT in tags:
            colors = cls._getColors(b'currentUser')
        elif {
         USER_TAG.FRIEND, USER_TAG.SUB_TO}.issubset(tags):
            colors = cls._getColors(b'friend')
        elif {
         USER_TAG.CLAN_MEMBER, USER_TAG.OTHER_CLAN_MEMBER}.issubset(tags):
            colors = cls._getColors(b'clanMember')
        else:
            colors = cls._getColors(b'others')
        if isOnline:
            color = colors[0]
        else:
            color = colors[1]
        return color

    @classmethod
    def makeVO(cls, contact, useBigIcons=False):
        dbID = contact.getID()
        tags = contact.getTags()
        note = contact.getNote()
        isOnline = contact.isOnline()
        if USER_TAG.CLAN_MEMBER in tags:
            pass
        elif contact.getClanAbbrev():
            tags.add(USER_TAG.OTHER_CLAN_MEMBER)
        baseUserProps = cls.makeBaseUserProps(contact)
        baseUserProps[b'rgb'] = cls.getColor(tags, isOnline)
        baseUserProps[b'icons'] = cls.getIcons(tags, note)
        baseUserProps[b'tags'] = list(tags)
        resourceIconId = cls.getGuiResourceID(contact)
        isColorBlind = cls.settingsCore.getSetting(b'isColorBlind')
        if resourceIconId == WG_GAMES.TANKS:
            if contact.isOnline():
                if USER_TAG.PRESENCE_DND in tags:
                    resourceIconId = _WOT_GAME_RESOURCE.BUSY_BLIND if isColorBlind else _WOT_GAME_RESOURCE.BUSY
                else:
                    resourceIconId = _WOT_GAME_RESOURCE.ONLINE
            else:
                resourceIconId = _WOT_GAME_RESOURCE.UNKNOWN
        return {b'userProps': baseUserProps, b'dbID': dbID, 
           b'note': (escape(note)), 
           b'resource': (RES_ICONS.getContactStatusIcon(b'48x48' if useBigIcons else b'24x24', resourceIconId))}

    @classmethod
    def makeBaseUserProps(cls, contact):
        return {b'userName': (contact.getName()), 
           b'tags': (list(contact.getTags())), 
           b'region': (cls.lobbyContext.getRegionCode(contact.getID())), 
           b'clanAbbrev': (contact.getClanAbbrev())}

    @classmethod
    def makeIconTag(cls, key=b'imgTag', iconPath=b''):
        if iconPath:
            ctx = {b'iconName': iconPath}
        else:
            ctx = None
        return makeHtmlString(b'html_templates:contacts/contact', key, ctx=ctx)

    @classmethod
    def getGuiResourceID(cls, contact):
        resourceId = contact.getResourceID()
        if resourceId:
            for prefix in WG_GAMES.ALL:
                if prefix != WG_GAMES.TANKS:
                    if prefix in resourceId:
                        resourceId = prefix
                        break

        if not resourceId:
            resourceId = WG_GAMES.TANKS
        return resourceId

    @classmethod
    def _getColors(cls, name):
        if not cls._colors:
            scheme = g_settings.getColorScheme(b'contacts')
            cls._colors = {b'friend': (scheme.getColors(b'friend')), 
               b'clanMember': (scheme.getColors(b'clanMember')), 
               b'others': (scheme.getColors(b'others')), 
               b'currentUser': (scheme.getColors(b'currentUser'))}
        return cls._colors[name]


_CACHED_ICONS_TAGS = {b'ignored': (ContactConverter.makeIconTag(iconPath=b'contactIgnored.png')), 
   b'pending': (ContactConverter.makeIconTag(iconPath=b'contactConfirmNeeded.png')), 
   b'note': (ContactConverter.makeIconTag(iconPath=b'contactNote.png'))}

class _GroupCondition(object):
    __slots__ = (b'_htmlString', b'_allIDs')

    def __init__(self):
        super(_GroupCondition, self).__init__()
        self._htmlString = b''
        self._allIDs = set()
        return

    def clear(self):
        self._allIDs.clear()
        return

    def set(self, contact):
        self._allIDs.add(contact.getID())
        self._htmlString = self._makeHtmlString()
        return True

    def validate(self, contact):
        return True

    def exists(self, dbID):
        return dbID in self._allIDs

    def empty(self):
        return not self._allIDs

    def remove(self, dbID):
        result = dbID in self._allIDs
        if result:
            self._allIDs.remove(dbID)
            self._htmlString = self._makeHtmlString()
        return result

    def getHtmlString(self):
        return self._htmlString

    def _makeHtmlString(self):
        return b''


class TotalCondition(_GroupCondition):

    def _makeHtmlString(self):
        total = len(self._allIDs)
        if total:
            result = makeHtmlString(b'html_templates:contacts/group', b'totalUsersCounter', ctx={b'totalCount': total})
        else:
            result = b''
        return result


class OnlineTotalCondition(TotalCondition):
    __slots__ = (b'_online',)

    def __init__(self):
        super(OnlineTotalCondition, self).__init__()
        self._online = {}
        return

    def clear(self):
        self._online.clear()
        super(OnlineTotalCondition, self).clear()
        return

    def set(self, contact):
        self._online[contact.getID()] = 1 if contact.isOnline() else 0
        super(OnlineTotalCondition, self).set(contact)
        return True

    def validate(self, contact):
        self._online[contact.getID()] = 1 if contact.isOnline() else 0
        return True

    def remove(self, dbID):
        result = self._online.pop(dbID, None) is not None
        super(OnlineTotalCondition, self).remove(dbID)
        return result

    def _makeHtmlString(self):
        total = len(self._allIDs)
        if total:
            result = makeHtmlString(b'html_templates:contacts/group', b'onlineUsersCounter', ctx={b'onlineCount': (sum(self._online.values())), 
               b'totalCount': total})
        else:
            result = b''
        return result


class OnlineOnlyCondition(OnlineTotalCondition):

    def set(self, contact):
        return super(OnlineOnlyCondition, self).set(contact) and contact.isOnline()

    def validate(self, contact):
        return super(OnlineOnlyCondition, self).validate(contact) and contact.isOnline()


class IContactsConverter(object):
    __slots__ = ()

    def clear(self, full=False):
        raise NotImplementedError
        return

    def getContacts(self):
        raise NotImplementedError
        return

    def hasContacts(self):
        return False

    def hasContact(self, dbID):
        raise NotImplementedError
        return

    def setContact(self, contact):
        raise NotImplementedError
        return

    def removeContact(self, dbID):
        raise NotImplementedError
        return

    def makeVO(self, pattern=None):
        raise NotImplementedError
        return


class _ContactsConverter(IContactsConverter):
    __slots__ = (b'_contacts', b'_condition', b'_converter', b'_showEmptyItem', b'_parent')

    def __init__(self, parent, condition=None, showEmptyItem=False):
        super(_ContactsConverter, self).__init__()
        self._contacts = {}
        self._condition = condition or _GroupCondition()
        self._converter = ContactConverter()
        self._showEmptyItem = showEmptyItem
        self._parent = parent
        return

    def getContacts(self):
        return self._contacts.copy()

    def hasContacts(self):
        return len(self._contacts) > 0

    def clear(self, full=False):
        self._contacts.clear()
        self._condition.clear()
        if full:
            self._parent = None
        return

    def isEmpty(self):
        return not self._contacts

    def showEmptyItem(self, value):
        self._showEmptyItem = value
        return

    def setConditionClass(self, clazz):
        self._condition = clazz()
        return

    def hasContact(self, dbID):
        return self._condition.exists(dbID)

    def setContact(self, contact):
        result = self._condition.set(contact)
        dbID = contact.getID()
        if result:
            self._contacts[dbID] = self._makeContactVO(contact)
        elif not self._condition.validate(contact):
            result = self._contacts.pop(dbID, None) is not None
        return result

    def removeContact(self, dbID):
        result = self._condition.remove(dbID)
        self._contacts.pop(dbID, None)
        return result

    def makeVO(self, pattern=None):
        if pattern:
            contacts = self._matchPattern(pattern, self._contacts.itervalues())
        elif not self._contacts and self._showEmptyItem:
            return [self.makeEmptyRow(self._parent)]
        contacts = self._contacts.itervalues()
        return sorted(contacts, key=(lambda item: item[b'criteria']))

    def _makeContactVO(self, contact):
        dbID = contact.getID()
        return {b'data': (self._converter.makeVO(contact)), 
           b'criteria': (
                       0 if contact.isOnline() else 1,
                       contact.getName().lower()), 
           b'gui': {b'id': dbID}, b'parentItemData': (self._parent)}

    @classmethod
    def makeEmptyRow(cls, parent, isVisible=True, isActive=True):
        return {b'gui': {b'id': None}, b'parentItemData': parent, 
           b'data': {b'isActive': isActive, 
                     b'isVisible': isVisible}}

    def _matchPattern(self, pattern, contacts):
        return [vo for vo in contacts if pattern.match(vo[b'criteria'][1])]


class GroupConverter(_ContactsConverter):
    __slots__ = (b'_name', b'_criteria', b'_isOpened', b'_rules', b'_parentCategory')

    def __init__(self, name, parentCategory, condition=None, rules=_DEF_RULES, showEmptyItem=False, isOpened=False):
        self._name = name
        self._criteria = name.lower()
        self._isOpened = isOpened
        self._rules = rules
        self._parentCategory = parentCategory
        super(GroupConverter, self).__init__(self.__makeBaseVO(parentCategory), condition, showEmptyItem)
        return

    def clear(self, full=False):
        super(GroupConverter, self).clear()
        if full:
            self._parentCategory = None
        return

    def getName(self):
        return self._name

    def getCriteria(self):
        return self._criteria

    def getGuiID(self):
        return self._name

    def setMutable(self, value):
        self._rules = _setMutableRule(self._rules, value)
        return

    def setOpened(self, value):
        self._isOpened = value
        return

    def toggle(self):
        self._isOpened = not self._isOpened
        return

    def makeVO(self, pattern=None):
        contacts = super(GroupConverter, self).makeVO(pattern)
        if pattern:
            isOpened = True
            if not contacts:
                return None
        else:
            isOpened = self._isOpened
        vo = self.__makeBaseVO(self._parentCategory)
        vo[b'isOpened'] = isOpened
        vo[b'children'] = contacts
        vo[b'data'][b'isOpened'] = isOpened
        vo[b'data'][b'headerDisplayTitle'] = escape(self._name)
        vo[b'data'][b'headerHtmlPart'] = self._condition.getHtmlString()
        return vo

    def __makeBaseVO(self, parent):
        return {b'gui': {b'id': (self.getGuiID())}, b'parentItemData': parent, 
           b'data': {b'headerTitle': (self._name), 
                     b'rules': (self._rules)}}


class ClanConverter(GroupConverter):

    def __init__(self, parentCategory, clanAbbrev=b'', condition=None):
        super(ClanConverter, self).__init__(makeClanFullName(clanAbbrev), parentCategory, condition)
        return

    def isEmpty(self):
        return not self._name or self._condition.empty()

    def getGuiID(self):
        return CONTACTS_ALIASES.CLAN_GROUP_RESERVED_ID

    def setClanAbbrev(self, clanAbbrev):
        self._name = makeClanFullName(clanAbbrev)
        return


class IgnoredConverter(GroupConverter):

    def __init__(self, parentCategory):
        super(IgnoredConverter, self).__init__(i18n.makeString(I18N_MESSENGER.MESSENGER_CONTACTS_MAINGROPS_OTHER_IGNORED), parentCategory, TotalCondition(), _IGNORED_RULES)
        return

    def getGuiID(self):
        return CONTACTS_ALIASES.IGNORED_GROUP_RESERVED_ID


class RqFriendshipConverter(GroupConverter):

    def __init__(self, parentCategory):
        super(RqFriendshipConverter, self).__init__(i18n.makeString(I18N_MESSENGER.MESSENGER_CONTACTS_MAINGROPS_OTHER_FRIENDSHIPREQUEST), parentCategory, TotalCondition())
        return

    def getGuiID(self):
        return CONTACTS_ALIASES.PENDING_FRIENDS_GROUP_RESERVED_ID


class FriendsWoGroupConverter(_ContactsConverter):
    pass


class FriendsGroupsConverter(IContactsConverter):
    usersStorage = MessengerStorageDescriptor(UsersStorage)
    __slots__ = (b'_groups', b'_mapping', b'_rules', b'_showEmptyItem', b'_conditionClass', b'__parentCategory')

    def __init__(self, parent):
        super(FriendsGroupsConverter, self).__init__()
        self._mapping = {}
        self._groups = {}
        self._rules = _FRIENDS_RULES
        self._showEmptyItem = False
        self._conditionClass = OnlineTotalCondition
        self.__parentCategory = parent
        return

    def getContacts(self):
        result = {}
        for frGroupConverter in self._groups.itervalues():
            result.update(frGroupConverter.getContacts())

        return result

    def hasContacts(self):
        for frGroupConverter in self._groups.itervalues():
            if frGroupConverter.getContacts():
                return True

        return False

    def clear(self, full=False):
        while self._groups:
            _, group = self._groups.popitem()
            group.clear()

        self._mapping.clear()
        if full:
            self.__parentCategory = None
        return

    def isEmpty(self):
        return not self._groups

    def showEmptyItem(self, value):
        for group in self._groups.itervalues():
            group.showEmptyItem(value)

        self._showEmptyItem = value
        return

    def setConditionClass(self, clazz):
        for group in self._groups.itervalues():
            group.setConditionClass(clazz)

        self._conditionClass = clazz
        return

    def hasContact(self, dbID):
        return dbID in self._mapping

    def setContact(self, contact):
        groups = contact.getGroups()
        self._mapping[contact.getID()] = groups
        for group in groups:
            if group not in self._groups:
                self._groups[group] = GroupConverter(group, self.__parentCategory, self._conditionClass(), self._rules, self._showEmptyItem)
            self._groups[group].setContact(contact)

        return

    def removeContact(self, dbID):
        groups = self._mapping.pop(dbID, set())
        isExists = self.usersStorage.isGroupExists
        for group in groups:
            if group in self._groups:
                converter = self._groups[group]
                if converter.removeContact(dbID) and converter.isEmpty() and not isExists(group):
                    self._groups.pop(group)

        return

    def setMutable(self, value):
        for group in self._groups.itervalues():
            group.setMutable(value)

        self._rules = _setMutableRule(self._rules, value)
        return

    def getGroup(self, name):
        group = None
        if name in self._groups:
            group = self._groups[name]
        return group

    def removeGroups(self, groups):
        for group in groups:
            self._groups.pop(group, None)

        return

    def setGroups(self, groups, isOpened=False):
        self._groups.update([(group, GroupConverter(group, self.__parentCategory, self._conditionClass(), self._rules, self._showEmptyItem, isOpened)) for group in groups])
        return

    def makeVO(self, pattern=None):
        vos = []
        for group in sorted(self._groups.itervalues(), key=(lambda group: group.getCriteria())):
            vo = group.makeVO(pattern)
            if vo:
                vos.append(vo)

        return vos
