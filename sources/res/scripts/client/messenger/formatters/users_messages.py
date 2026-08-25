from gui import GUI_SETTINGS, makeHtmlString
from helpers import i18n
from messenger.m_constants import USER_ACTION_ID, MESSENGER_I18N_FILE
from messenger.proto.xmpp.xmpp_constants import CONTACT_LIMIT
_userTransferUserMsgKeys = {(USER_ACTION_ID.FRIEND_ADDED): (b'#%s:client/information/addToFriends/message' % MESSENGER_I18N_FILE), 
   (USER_ACTION_ID.IGNORED_ADDED): (b'#%s:client/information/addToIgnored/message' % MESSENGER_I18N_FILE), 
   (USER_ACTION_ID.TMP_IGNORED_ADDED): (b'#%s:client/information/addToTmpIgnored/message' % MESSENGER_I18N_FILE), 
   (USER_ACTION_ID.MUTE_SET): (b'#%s:client/information/setMuted/message' % MESSENGER_I18N_FILE), 
   (USER_ACTION_ID.MUTE_UNSET): (b'#%s:client/information/unsetMuted/message' % MESSENGER_I18N_FILE), 
   (USER_ACTION_ID.FRIEND_REMOVED): (b'#%s:client/information/removeFromFriends/message' % MESSENGER_I18N_FILE), 
   (USER_ACTION_ID.IGNORED_REMOVED): (b'#%s:client/information/removeFromIgnored/message' % MESSENGER_I18N_FILE), 
   (USER_ACTION_ID.TMP_IGNORED_REMOVED): (b'#%s:client/information/removeFromTmpIgnored/message' % MESSENGER_I18N_FILE)}

def getUserActionReceivedMessage(actionIndex, user):
    if not GUI_SETTINGS.voiceChat and actionIndex in [USER_ACTION_ID.MUTE_SET, USER_ACTION_ID.MUTE_UNSET]:
        return
    else:
        if actionIndex in _userTransferUserMsgKeys:
            message = i18n.makeString(_userTransferUserMsgKeys[actionIndex], user.getFullName())
        else:
            message = None
        return message


def getBroadcastIsInCoolDownMessage(coolDown):
    return i18n.makeString(b'#%s:client/error/broadcastInCooldown' % MESSENGER_I18N_FILE, coolDown)


def makeFriendshipRequestText(user, error):
    result = []
    text = makeHtmlString(b'html_templates:lobby/friendshipRequest', b'title', ctx={b'name': (user.getFullName())})
    result.append(text)
    if error:
        text = makeHtmlString(b'html_templates:lobby/friendshipRequest/note', error.getErrorName(), ctx={b'name': (user.getFullName()), 
           b'rosterMaxCount': (CONTACT_LIMIT.ROSTER_MAX_COUNT)})
        result.append(text)
    return (b'').join(result)
