from messenger.gui.Scaleform import FILL_COLORS

class IGUIEntry(object):

    def init(self):
        return

    def clear(self):
        return

    def show(self):
        return

    def close(self, nextScope):
        return

    @property
    def channelsCtrl(self):
        return

    def invoke(self, method, *args, **kwargs):
        return

    def isFocused(self):
        return False

    def handleKey(self, event):
        return False

    def addClientMessage(self, message, isCurrentPlayer=False):
        return


class IGUIEntryDecorator(IGUIEntry):

    def getEntry(self, scope):
        return

    def setEntry(self, scope, entry):
        return

    def switch(self, scope):
        return


class IControllerFactory(object):

    def init(self):
        return []

    def clear(self):
        return

    def factory(self, entity):
        return


class IControllersCollection(IControllerFactory):

    def getController(self, clientID):
        return

    def hasController(self, controller):
        return False

    def getControllerByCriteria(self, criteria):
        return

    def getControllersIterator(self):
        return

    def removeControllers(self):
        return


class IEntityController(object):

    def setView(self, view):
        return

    def removeView(self):
        return

    def clear(self):
        return


class IChannelController(IEntityController):

    def getChannel(self):
        return

    def join(self):
        return

    def exit(self):
        return

    def activate(self):
        return

    def deactivate(self, entryClosing=False):
        return

    def isJoined(self):
        return False

    def setHistory(self, history):
        return

    def getHistory(self):
        return []

    def hasUnreadMessages(self):
        return len(self.getHistory()) > 0

    def setMembersDP(self, membersDP):
        return

    def removeMembersDP(self):
        return

    def canSendMessage(self):
        return (
         False, b'N/A')

    def sendMessage(self, message):
        return

    def sendCommand(self, command):
        return

    def addMessage(self, message, doFormatting=True):
        return False

    def addCommand(self, command):
        return b''

    def isEnabled(self):
        return True

    def hasUntrustedMembers(self):
        return False


class IBattleChannelView(object):

    def addController(self, ctrl):
        return

    def removeController(self, ctrl):
        return

    def addMessage(self, text, fillColor=FILL_COLORS.BLACK, accountDBID=0):
        return
