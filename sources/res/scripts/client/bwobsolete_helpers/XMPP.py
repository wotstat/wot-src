import FantasyDemo, FDGUI, XMPPRoster

class AvatarRosterVisitor(XMPPRoster.XMPPRosterVisitor):

    def __init__(self):
        XMPPRoster.XMPPRosterVisitor.__init__(self)
        return

    def onFriendAdd(self, friend, transport):
        msg = b'Added %s to the friends list.' % friend
        FantasyDemo.addChatMsg(-1, msg, FDGUI.TEXT_COLOUR_SYSTEM)
        return

    def onFriendDelete(self, friend, transport):
        msg = b'Removed %s from the friends list.' % friend
        FantasyDemo.addChatMsg(-1, msg, FDGUI.TEXT_COLOUR_SYSTEM)
        return

    def onFriendPresenceChange(self, friend, transport, oldPresence, newPresence):
        state = None
        if oldPresence == b'available' and newPresence == b'unavailable':
            state = b'gone offline'
        elif oldPresence == b'unavailable' and newPresence == b'available':
            state = b'come online'
        if state:
            msg = b'%s has %s' % (friend, state)
            FantasyDemo.addChatMsg(-1, msg, FDGUI.TEXT_COLOUR_SYSTEM)
        return

    def onError(self, message):
        FantasyDemo.addChatMsg(-1, message, FDGUI.TEXT_COLOUR_SYSTEM)
        return
