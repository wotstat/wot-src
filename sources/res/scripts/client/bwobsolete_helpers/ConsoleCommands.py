import BigWorld, FantasyDemo, Avatar, Math, FDGUI, re

def who(player, string):
    playerList = b'Players near you:\n'
    for i in BigWorld.entities.values():
        if i.__class__.__name__ == b'Avatar':
            playerList = playerList + i.playerName + b'\n'

    FantasyDemo.addChatMsg(-1, playerList)
    return


def help(player, string):
    if string:
        try:
            func = globals()[string]
            if callable(func) and func.__doc__:
                for s in func.__doc__.split(b'\n'):
                    FantasyDemo.addChatMsg(-1, s)

            else:
                raise b'Not callable'
        except:
            FantasyDemo.addChatMsg(-1, b'No help for ' + string)

    else:
        isCallable = lambda x: callable(globals()[x])
        ignoreList = (b'getV4FromString', b'help')
        notIgnored = lambda x: x not in ignoreList
        keys = filter(isCallable, globals().keys())
        keys = filter(notIgnored, keys)
        keys.sort()
        FantasyDemo.addChatMsg(-1, b'/help {command} for more info.')
        stripper = lambda c: c not in b'[]\'"'
        string = filter(stripper, str(keys))
        FantasyDemo.addChatMsg(-1, string)
    return


def target(player, string):
    t = BigWorld.target()
    if t:
        try:
            t.cell.directedChat(player.id, string)
            FantasyDemo.addChatMsg(player.id, b'[To ' + t.playerName + b'] ' + string)
        except:
            pass

    return


def pushUp(player, string):
    player.pushUpKey()
    return


def pullUp(player, string):
    player.pullUpKey()
    return


def follow(player, string):
    if BigWorld.target() != None:
        player.physics.chase(BigWorld.target(), 2.0, 0.5)
        player.physics.velocity = (0, 0, 6.0)
    return


def summon(player, string):
    if isinstance(BigWorld.connectedEntity(), Avatar.Avatar):
        BigWorld.connectedEntity().cell.summonEntity(str(string))
    else:
        FantasyDemo.addChatMsg(-1, b'Summon can only be called when connected to the server')
    return


def weather(player, string):
    import Weather
    Weather.weather().toggleRandomWeather(False)
    Weather.weather().summon(str(string))
    return


def rain(player, string):
    import Weather
    Weather.weather().rain(float(string))
    return


def getV4FromString(string):
    tokens = string.split(b' ')
    v = [1, 1, 1, 1]
    for i in tokens:
        try:
            v.append(float(i))
        except:
            pass

    return Math.Vector4(v[-4:])


def fog(player, string):
    import Weather
    Weather.weather().fog(getV4FromString(string))
    return


def ambient(player, string):
    import Weather
    Weather.weather().ambient(getV4FromString(string))
    return


def sunlight(player, string):
    import Weather
    Weather.weather().sun(getV4FromString(string))
    return


def wave(player, string):
    player.playGesture(1)
    return


def laugh(player, string):
    player.playGesture(16)
    return


def cry(player, string):
    player.playGesture(3)
    return


def point(player, string):
    player.playGesture(24)
    return


def shrug(player, string):
    player.playGesture(4)
    return


def yes(player, string):
    player.playGesture(19)
    return


def no(player, string):
    player.playGesture(20)
    return


def beckon(player, string):
    player.playGesture(21)
    return


def fat(player, string):
    player.playGesture(44)
    return


def skinny(player, string):
    player.playGesture(45)
    return


def addTransportAccount(player, string):
    string = string.encode(b'utf8').strip()
    m = re.match(b'(.+?)\\s+(.+?)\\s+(.+)', string)
    if not m:
        FantasyDemo.addChatMsg(-1, b'Invalid transport registration details.', FDGUI.TEXT_COLOUR_SYSTEM)
        return
    transport = m.group(1)
    username = m.group(2)
    password = m.group(3)
    registerMsg = b'Attempting to register %s account %s.' % (
     transport, username)
    FantasyDemo.addChatMsg(-1, registerMsg, FDGUI.TEXT_COLOUR_SYSTEM)
    player.base.xmppTransportAccountRegister(transport, username, password)
    return


def delTransportAccount(player, string):
    transport = string.encode(b'utf8').strip()
    wasFound = False
    for transportDetails in player.xmppTransportDetails:
        if not wasFound and transportDetails[b'transport'] == transport:
            wasFound = True

    if not wasFound:
        FantasyDemo.addChatMsg(-1, b'Transport not known.', FDGUI.TEXT_COLOUR_SYSTEM)
    else:
        player.base.xmppTransportAccountDeregister(transport)
    return


def addFriend(player, string):
    if string.find(b'@') >= 0:
        transport = b'xmpp'
        if string.startswith(b'@'):
            FantasyDemo.addChatMsg(-1, b'Invalid IM friend name.', FDGUI.TEXT_COLOUR_SYSTEM)
            return
        imContents = string.rsplit(b':', 1)
        friendID = imContents[0]
        if len(imContents) == 2:
            transport = imContents[1].encode(b'utf8').lower()
        if friendID.endswith(b'@'):
            friendID += b'eval.bigworldtech.com'
        friendsList = player.roster.findFriendsLike(friendID, transport)
        if len(friendsList):
            FantasyDemo.addChatMsg(-1, b'%s is already a friend.' % friendID, FDGUI.TEXT_COLOUR_SYSTEM)
            return
        player.base.xmppAddFriend(friendID, transport)
    else:
        player.addFriend(string.encode(b'utf8'))
    return


def delFriend(player, string):
    friendsList = player.roster.findFriendsLike(string)
    if not len(friendsList):
        player.delFriend(string.encode(b'utf8'))
    elif len(friendsList) > 1:
        FantasyDemo.addChatMsg(-1, b"Found multiple friends that match '%s'.", FDGUI.TEXT_COLOUR_SYSTEM)
        for friendItem in friendsList:
            FantasyDemo.addChatMsg(-1, friendItem[0], FDGUI.TEXT_COLOUR_SYSTEM)

    else:
        friend = friendsList[0]
        player.base.xmppDelFriend(friend[0], friend[1])
    return


def infoFriend(player, string):
    player.infoFriend(string)
    return


def listFriends(player, string):
    player.listFriends()
    return


def msgFriend(player, string):
    words = string.split(b':', 1)
    if len(words) < 2:
        FantasyDemo.addChatMsg(-1, b'Invalid format - /help msgFriend for details', FDGUI.TEXT_COLOUR_SYSTEM)
        return
    recipient = words[0].strip()
    message = words[1].strip()
    if not len(message):
        FantasyDemo.addChatMsg(-1, b'Invalid format - /help msgFriend for details', FDGUI.TEXT_COLOUR_SYSTEM)
        return
    friendsList = player.roster.findFriendsLike(recipient)
    if not len(friendsList):
        player.msgFriend(recipient.encode(b'utf8'), message)
    elif len(friendsList) > 1:
        FantasyDemo.addChatMsg(-1, b"Found multiple friends that match '%s'.", FDGUI.TEXT_COLOUR_SYSTEM)
        for friendItem in friendsList:
            FantasyDemo.addChatMsg(-1, friendItem[0], FDGUI.TEXT_COLOUR_SYSTEM)

    else:
        friend = friendsList[0]
        player.base.xmppMsgFriend(friend[0], friend[1], message)
        recipient = friend[0] + b' [IM]'
    FantasyDemo.addChatMsg(-1, b'You say to ' + recipient + b': ' + message, FDGUI.TEXT_COLOUR_YOU_SAY)
    return


tell = msgFriend
t = msgFriend

def teleport(player, dst):
    try:
        spaceName, pointName = str(dst).rsplit(b' ', 1)
    except ValueError:
        try:
            spaceName, pointName = str(dst).rsplit(b'/', 1)
        except ValueError:
            return

    BigWorld.player().tryToTeleport(spaceName, pointName)
    FantasyDemo.rds.fdgui.chatWindow.script.hideNow()
    return


def addNote(player, description):
    if description == None or len(description) == 0:
        FantasyDemo.addChatMsg(-1, b'Must provide a note description')
    else:
        print b'Adding a note:', description
        if isinstance(description, unicode):
            description = description.encode(b'utf8')
        player.base.addNote(description)
    return


def getNotes(player, arg):
    player.base.getNotes()
    return
